MERITNITI CDN UPLOAD — caulderoninteractive.com

IMPORTANT: Keep the .json.gz files compressed. Do not extract them individually.

Your website root already contains files such as index.html / meritniti.html and the meritniti/jobs/ folder.
Copy this archive's meritniti/content/ folder into the WEBSITE ROOT so that content becomes a sibling of jobs:

<website-root>/
  index.html
  meritniti.html
  meritniti/
    jobs/
    content/
      manifest.json
      manifest_additions_02.json
      packs/
        practice_comprehension_01.json.gz
        practice_comprehension_02.json.gz
        practice_reasoning_01.json.gz
        practice_reasoning_02.json.gz
        practice_quantitative_01.json.gz
        practice_quantitative_02.json.gz
        practice_general_knowledge_01.json.gz
        practice_general_knowledge_02.json.gz
        practice_english_01.json.gz
        practice_english_02.json.gz
        practice_hindi_01.json.gz
        practice_hindi_02.json.gz

If the site is Git-connected, commit and push these files with the rest of the static site. Cloudflare will redeploy automatically from the repository.

After deployment, these must return HTTP 200:
https://caulderoninteractive.com/meritniti/content/manifest.json
https://caulderoninteractive.com/meritniti/content/packs/practice_quantitative_02.json.gz
https://caulderoninteractive.com/meritniti/content/packs/practice_reasoning_02.json.gz

The Android app should use this catalogue URL:
https://caulderoninteractive.com/meritniti/content/manifest.json

There is no HTML link required. The Android ContentPackService fetches manifest.json directly over HTTPS; manifest.json then supplies the URLs of the .json.gz pack files.
