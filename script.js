// Caulderon Interactive — shared site script

// Footer year
document.querySelectorAll('#year, #cyear').forEach(function(el){
  el.textContent = new Date().getFullYear();
});

// Mobile nav toggle
document.querySelectorAll('.nav-toggle').forEach(function(btn){
  btn.addEventListener('click', function(){
    var inner = btn.closest('.nav-inner');
    var links = inner && inner.querySelector('.nav-links');
    if(!links) return;
    var open = links.classList.toggle('is-open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  var inner = btn.closest('.nav-inner');
  var links = inner && inner.querySelector('.nav-links');
  if(links){
    links.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click', function(){
        links.classList.remove('is-open');
        btn.setAttribute('aria-expanded', 'false');
      });
    });
  }
});


// MeritNiti — Government Jobs & Exam Updates
(function(){
  var host = document.getElementById('meritniti-jobs-feed');
  var allLinks = document.querySelectorAll('[data-meritniti-jobs-link]');
  if(!host && !allLinks.length) return;

  function jobsBasePath(){
    var name = (window.location.hostname || '').toLowerCase();
    var onMeritNitiDomain = name === 'meritniti.com' || name.endsWith('.meritniti.com');
    return onMeritNitiDomain ? '/jobs/' : '/meritniti/jobs/';
  }

  var basePath = jobsBasePath();
  allLinks.forEach(function(a){ a.setAttribute('href', basePath); });
  if(!host) return;

  function text(value){
    return value === null || value === undefined ? '' : String(value);
  }

  function safeInternalHref(value){
    try{
      var u = new URL(text(value), window.location.origin);
      if(u.protocol !== 'https:' && u.protocol !== 'http:') return basePath;
      // Feed cards should point to MeritNiti pages. If a malformed feed row tries
      // to point elsewhere, fall back to the verified-updates index.
      if(u.origin !== window.location.origin) return basePath;
      return u.href;
    }catch(_){
      return basePath;
    }
  }

  function formatDate(value){
    if(!value) return '';
    var d = new Date(String(value).slice(0,10) + 'T00:00:00');
    if(Number.isNaN(d.getTime())) return text(value);
    return d.toLocaleDateString('en-IN', { day:'2-digit', month:'short', year:'numeric' });
  }

  function statusLabel(row){
    if(row.latest_event && row.latest_event !== 'Recruitment') return row.latest_event;
    var map = {
      closing_soon: 'Closing soon',
      open: 'Applications open',
      upcoming: 'Applications upcoming',
      open_unknown: 'Applications open',
      recent_unknown: 'Recent notification'
    };
    return map[row.application_status] || 'Recruitment';
  }

  function isActive(row){
    return ['open','closing_soon','upcoming','open_unknown'].indexOf(row.application_status) !== -1;
  }

  function byLatestEvent(a,b){
    return text(b.latest_event_date).localeCompare(text(a.latest_event_date));
  }

  function chooseRows(rows){
    var active = rows.filter(isActive);
    var followups = rows
      .filter(function(x){ return x.latest_event && x.latest_event !== 'Recruitment'; })
      .sort(byLatestEvent);

    var selected = active.slice(0,4);
    followups.forEach(function(row){
      if(selected.length >= 6) return;
      if(!selected.some(function(x){ return x.exam_key === row.exam_key; })) selected.push(row);
    });
    return selected.slice(0,6);
  }

  function makeCard(row){
    var a = document.createElement('a');
    a.className = 'mn-update-card';
    a.href = safeInternalHref(row.url);

    var top = document.createElement('div');
    top.className = 'mn-update-top';

    var kind = document.createElement('span');
    kind.className = 'mn-update-kind';
    kind.textContent = statusLabel(row);

    var verified = document.createElement('span');
    verified.className = 'mn-update-verified';
    verified.textContent = row.verification_status === 'verified' ? 'Official-source verified' : 'Source checked';

    top.appendChild(kind);
    top.appendChild(verified);

    var h3 = document.createElement('h3');
    h3.textContent = text(row.title) || 'Government recruitment update';

    var org = document.createElement('div');
    org.className = 'mn-update-org';
    org.textContent = text(row.organisation) || 'Recruiting authority';

    var meta = document.createElement('div');
    meta.className = 'mn-update-meta';

    if(row.vacancies){
      var v = document.createElement('span');
      v.innerHTML = '<strong>' + Number(row.vacancies).toLocaleString('en-IN') + '</strong> posts';
      meta.appendChild(v);
    }
    if(row.deadline){
      var d = document.createElement('span');
      d.textContent = 'Last date: ' + formatDate(row.deadline);
      meta.appendChild(d);
    }
    if(!row.deadline && row.latest_event_date){
      var u = document.createElement('span');
      u.textContent = 'Update: ' + formatDate(row.latest_event_date);
      meta.appendChild(u);
    }

    a.appendChild(top);
    a.appendChild(h3);
    a.appendChild(org);
    a.appendChild(meta);
    return a;
  }

  function setMessage(className, title, body, includeLink){
    host.replaceChildren();
    var box = document.createElement('div');
    box.className = className;
    var b = document.createElement('b');
    b.textContent = title;
    var span = document.createElement('span');
    span.textContent = body;
    box.appendChild(b);
    box.appendChild(span);
    if(includeLink){
      var link = document.createElement('a');
      link.href = basePath;
      link.textContent = 'Open the full updates page →';
      box.appendChild(link);
    }
    host.appendChild(box);
  }

  fetch(basePath + 'feed.json', {
    cache:'no-store',
    credentials:'same-origin',
    headers:{ 'Accept':'application/json' }
  })
  .then(function(response){
    if(!response.ok) throw new Error('HTTP ' + response.status);
    return response.json();
  })
  .then(function(rows){
    if(!Array.isArray(rows)) throw new Error('Invalid feed');
    var selected = chooseRows(rows);
    host.replaceChildren();
    if(!selected.length){
      setMessage(
        'mn-update-empty',
        'No prominent verified update is active right now.',
        'The scanner will add vacancies and important follow-ups here when a qualifying official notice is verified.',
        true
      );
      return;
    }
    selected.forEach(function(row){ host.appendChild(makeCard(row)); });
  })
  .catch(function(){
    setMessage(
      'mn-update-error',
      'Verified updates are temporarily unavailable.',
      'The feed may not have been generated or deployed yet. MeritNiti will not substitute unverified information.',
      true
    );
  })
  .finally(function(){
    host.setAttribute('aria-busy','false');
  });
})();
