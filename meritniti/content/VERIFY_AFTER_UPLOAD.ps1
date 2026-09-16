$urls = @(
  "https://caulderoninteractive.com/meritniti/content/manifest.json",
  "https://caulderoninteractive.com/meritniti/content/packs/practice_comprehension_02.json.gz",
  "https://caulderoninteractive.com/meritniti/content/packs/practice_reasoning_02.json.gz",
  "https://caulderoninteractive.com/meritniti/content/packs/practice_quantitative_02.json.gz",
  "https://caulderoninteractive.com/meritniti/content/packs/practice_general_knowledge_02.json.gz",
  "https://caulderoninteractive.com/meritniti/content/packs/practice_english_02.json.gz",
  "https://caulderoninteractive.com/meritniti/content/packs/practice_hindi_02.json.gz"
)
foreach ($u in $urls) {
  try {
    $r = Invoke-WebRequest -Uri $u -Method Head -UseBasicParsing
    Write-Host ("OK {0} {1}" -f $r.StatusCode, $u)
  } catch {
    Write-Host ("FAIL {0}" -f $u) -ForegroundColor Red
  }
}
