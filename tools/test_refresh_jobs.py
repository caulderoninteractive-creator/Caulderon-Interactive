"""Offline checks for the scheduled discovery-only job."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import refresh_jobs as jobs


class DiscoveryTests(unittest.TestCase):
    def test_first_party_careers_are_explored_without_publishing(self):
        class Response:
            def __init__(self, url, content):
                self.url, self.content = url, content
            def __enter__(self): return self
            def __exit__(self, *_): pass
            def read(self, size): return self.content[:size]
        pages = {
            'https://example.gov.in/': b'<a href="/careers">Careers</a><a href="https://other.gov.in/vacancies">Other</a>',
            'https://example.gov.in/careers': b'<a href="/careers/technician-notice.pdf">Technician recruitment</a>',
        }
        def open_page(request, timeout):
            return Response(request.full_url, pages[request.full_url])
        with tempfile.TemporaryDirectory() as tmp, patch.object(jobs,'ROOT',Path(tmp)), \
             patch.object(jobs,'SOURCES',{'Test':'https://example.gov.in/'}), \
             patch.object(jobs,'urlopen',side_effect=open_page):
            (Path(tmp)/'tools').mkdir()
            jobs.discover()
            report=json.loads((Path(tmp)/'tools/discovery_report.json').read_text())
        urls={lead['url'] for lead in report['leads']}
        self.assertIn('https://example.gov.in/careers/technician-notice.pdf',urls)
        self.assertFalse(any('other.gov.in' in url for url in urls))
        self.assertFalse(report['failures'])


if __name__ == '__main__': unittest.main()
