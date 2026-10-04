# Access map for this container (tested 2026-10-04) — READ BEFORE SEARCHING

This is a cloud container, NOT Abe's NUC. There is no agent-desktop Chrome, no /home/abe/stack,
no /mnt/nas, no Flight Recorder, no logged-in accounts. Do not pretend otherwise.

## WORKS
- tile.loc.gov (LOC images + OCR). Erie phone-book OCR is already downloaded:
    work/loc/usteledirec07589.text.json  (Erie 9/1911-7/1940; per-page OCR keyed by 1-based seq)
    work/loc/usteledirec07590.text.json  (Erie 7/1941-7/1947)
  Grep:   python3 work/tools/grep_loc.py work/loc/usteledirec07589.text.json 'REGEX'
  Image:  work/tools/locimg.sh REEL SEQ PCT OUT.jpg   (REGION="x,y,w,h" env var for full-res crop)
  Viewer URL for Abe: https://www.loc.gov/resource/gdcmassbookdig.REEL/?sp=SEQ
- www.loc.gov item/search JSON: blocked to curl (Cloudflare) BUT the WebFetch tool gets through
  (e.g. https://www.loc.gov/item/XXXX/?fo=json). Use WebFetch for loc.gov JSON, then curl tile.loc.gov.
  Pattern: storage-services/public/<collection>/<id>/<id>.text.txt / .pdf ; image-services/iiif/public:...
- Google Books FULL-TEXT search with snippets (old GData feed, whole corpus):
    python3 work/tools/gbfeed.py 'QUERY' [N]       (prints title|date|ids|snippet)
  books.google.com/books?id=..&q=.. and googleapis.com return 429 (rate-limited) — do not hammer.
  www.google.com/books/edition/_/ID pages load but search-inside is JS-only.
  Space requests >= 3 s apart. Snippets are LEADS until confirmed on a page image.
- archive.org: metadata search (advancedsearch.php), FULL-TEXT search:
    python3 work/tools/iafts.py 'QUERY' [hits] [page]
  full text: https://archive.org/download/ID/ID_djvu.txt ; page images via
  https://archive.org/download/ID/page/n{LEAF}.jpg  or BookReader IIIF
  (https://iiif.archive.org/iiif/3/ID%24{LEAF}/full/max/0/default.jpg — leaf is 0-based).
  archive.org page URL for Abe: https://archive.org/details/ID/page/nLEAF
- forum.antiquemotorcycle.org pages (curl works, 200).
- WebSearch tool (US web search), WebFetch tool (summarised by a small model — never trust it for
  verbatim quotes; use it only to locate, then confirm with curl or page images).
- Headless Chromium (Playwright at /opt/node-tools/node_modules/playwright, exe /opt/pw-browsers/chromium,
  proxy = $HTTPS_PROXY, proxy CA now trusted in NSS). Cloudflare "Verify you are human" pages remain:
  DO NOT try to solve or click CAPTCHAs. Treat as blocked -> manual list for Abe.

## BLOCKED (log as blocked, add to manual list; do not retry more than twice)
- HathiTrust babel.hathitrust.org — hard IP block ("Blocked from HathiTrust"), also Cloudflare.
  catalog.hathitrust.org/api/volumes/... JSON works (metadata only).
- web.archive.org — connection reset at the proxy; WebFetch also refuses it.
- findagrave.com — 403 (Cloudflare), WebFetch also 403.
- erielibrary.org — 503 / timeout.
- oldindiandealers.com — no response.
- books.google.com classic search — 429.

## Rules
- Human pace: >= 2-3 s between page loads to the same host. No bulk scraping.
- A source fails twice: log it, skip it.
- Every fact: source URL + page/seq + exact line as printed. Else label UNVERIFIED.
- Max 1800 px on any image you Read. Resize with: convert in.jpg -resize 1800x1800\> out.jpg
- No payments, sign-ups, posts, emails.
