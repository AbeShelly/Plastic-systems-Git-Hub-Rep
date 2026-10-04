# Lane: dealer-lists (round 2) - working log, started 2026-10-04

Tasks: (1) recover oldindiandealers.com (Mike Dunn) from Common Crawl; (2) CAIMAG 'Sidecar' dealer thread + other online
old-dealer lists / Hatfield snippets; (3) post-1947 Erie Indian dealer check (1948-1955), any East 10th address in any decade;
(4) eBay / WorthPoint leads via WebSearch.
Read first: ACCESS.md, FINDINGS_SO_FAR.md, critic1.json, lanes/local-history.md, trade-press.md, gap-1923-1934.md (skim others).
Scratch: lanes/dealer-lists/

## Log
### 1. oldindiandealers.com via Common Crawl (in progress)
- index.commoncrawl.org: collinfo.json -> curl (35) connection reset x2; CC-MAIN-2014-10-index query -> (52) empty reply.
  => index server BLOCKED here (2 fails). WORKAROUND (same public data, no index server): data.commoncrawl.org works
  (HTTP 206 range). Wrote lanes/dealer-lists/ccsearch.py = binary search of cc-index/collections/<CRAWL>/indexes/cluster.idx
  by HTTP Range (2.5 s between requests), then fetch+gunzip the cdx-NNNNN.gz block(s). Validated on CC-MAIN-2014-10 with
  'org,antiquemotorcycle)' -> 564 captures (works). Results per crawl in lanes/dealer-lists/cc/<CRAWL>.txt.
- 'com,oldindiandealers)' (SURT key, covers www. and any path): 0 captures in ALL 36 crawls checked:
  CC-MAIN-2008-2009, 2009-2010, 2012, 2013-20, 2013-48, 2014-10, 2014-15, 2014-23, 2014-35, 2014-41, 2014-49, 2014-52, 2015-06,
  2015-11, 2015-18, 2015-22, 2015-32, 2015-40, 2015-48, 2016-07, 2016-18, 2016-26, 2016-36, 2016-44, 2017-04, 2017-13, 2017-22
  (1 block gunzip error, retried OK), 2017-30, 2017-43, 2018-05 (same, retried OK), 2018-13, 2018-26, 2018-47, 2019-13, 2019-35,
  2020-05. Old ARC-era index format validated: 'org,antiquemotorcycle)' -> 276 captures in 2009-2010, 53 in 2012.
  => oldindiandealers.com was never captured by Common Crawl. NOT RECOVERABLE here. Only remaining copy = Wayback (manual).
- AMCA thread context (local-history amca/p3-p5.html, re-read): Mike ("mdunn") built the site 2009 from forum contributions
  (dealer names/addresses with Google-maps links); by p5 (later years) users report "I can't locate the website that was set up".
  The forum-posted entries (pp.1-5) contain no Erie, Pa. dealer (round 1).

### 2. Other dealer lists / forums
- indianmotorcycles.net "List of Indian Dealerships in the United States and Canada" (thread 2610): curl -> 202 proof-of-work
  bot challenge (headless check); WebFetch -> 307 to tollbit.indianmotorcycles.net (pay-per-crawl gateway) => BLOCKED (not
  pursued: payment/bot wall). WebSearch snippets show it is a MODERN (Polaris-era) dealer list (Arizona/California/Michigan
  current dealers) => irrelevant anyway.
- CAIMAG forum (www.caimag.com/forum/..., Buzz Kanter's Classic American Iron): HTTP 522 x2 (forum.php and archive t-3198)
  => BLOCKED (site offline). AMCA thread 23629 "CAIMAG website" (curl 200): posters say CAIMAG went offline in 2020; last
  Wayback copy Feb 2020 (web.archive.org blocked here). Thread ID of Sidecar's 42-page dealer thread NOT found by WebSearch.
  -> manual step (Wayback) / possible CC search once a thread id is known.

### 3. POST-1947 CHECK - NEW PRIMARY FINDING (LOC Erie phone books 1948-1957, not used in round 1)
- New LOC reels found (WebFetch item JSON): usteledirec07591 = "Pennsylvania - White pages and Yellow Pages - Erie - 8/1948
  thru Fall/1951" (848 files); usteledirec07592 = "... Erie - 7/1952 thru 7/1957" (1020 files). OCR JSON downloaded from
  https://tile.loc.gov/storage-services/public/gdcmassbookdig/<R>/<R>.text.json -> lanes/dealer-lists/<R>.text.json
- Editions (reel 07591): A = "Directory corrected to May 28, 1948 / Approximate delivery date, next issue, July 1949", copyright
  stamp "AUG 18 1948" (seq24, viewed); white seq21-113, yellow 114-205. B = cover "JULY 1949" (seq208), "corrected to April 29,
  1949 / next issue, July 1950", stamp "JUN 28 1949" (seq211, viewed); white 207-304, yellow 305-392. C = corrected to May 12,
  1950 (seq400, OCR); yellow 510-610. D = corrected to September 28, 1951 (seq619, OCR); yellow 741-840.
  Reel 07592: July 1952 (seq25 "corrected to May 9, 1952"), July 1953 (seq263), July 1955 (seq510/514 "corrected to April 29,
  1955"), July 1957 (seq763). (OCR for the 1952-57 dates; covers.)
- VERIFIED ON IMAGE:
  * 1948 ed. (Aug 1948) yellow p.116, seq173: "Motorcycles / Harley-Davidson Motorcycle Agency / 114 E 11 st ....5-2140 /
    INDIAN MOTORCYCLE SALES & SERVICE / Headquarters for new and used motorcycles. Authorized Indian service. Genuine Indian
    parts. Specially designed accessories, sports equipment and apparel. [Indian MOTORCYCLES logo] / "WHERE TO BUY THEM" /
    STRAUS A LOUIS 1315 Peach st.......2-3495"
    Evidence: evidence/1948-08_loc-erie-phonebook-yellow_reel07591_seq173_p116_indian-motorcycle-sales-service-straus-1315-peach_composite.png
    Date evidence: evidence/1948-08_loc-erie-phonebook_reel07591_seq24_p2-3_directory-corrected-may-28-1948-stamp-aug-18-1948_composite.png
  * 1949 ed. (July 1949) yellow p.113, seq362: identical block "INDIAN MOTORCYCLE SALES & SERVICE ... STRAUS A LOUIS 1315 Peach
    st.......2-3495" under Motorcycles, after Harley-Davidson 114 E 11 st 5-2140.
    Evidence: evidence/1949-07_loc-erie-phonebook-yellow_reel07591_seq362_p113_indian-motorcycle-sales-service-straus-1315-peach_composite.png
  * 1949 ed. white p.80 (Humphries-Irene's), seq250: "Indian Motorcycle Agency 1315 Peach st..2-3495"
    Evidence: evidence/1949-07_loc-erie-phonebook-white_reel07591_seq250_p80_indian-motorcycle-agency-1315-peach-2-3495_composite.png
    Date evidence: evidence/1949-07_loc-erie-phonebook_reel07591_seq211_p2-3_directory-corrected-april-29-1949-stamp-jun-28-1949_composite.png
  * 1950 ed. (corrected May 12, 1950) yellow p.126, seq576: Motorcycles = ONLY "HARLEY DAVIDSON MOTORCYCLE AGENCY / SALES and
    SERVICE / GENUINE PARTS and ACCESSORIES / FACTORY TRAINED MECHANICS / LOCATIONS, ERIE and BUFFALO / 29 Years in Business /
    114 E 11 st....5-2140". No Indian.
    Evidence: evidence/1950-07_loc-erie-phonebook-yellow_reel07591_seq576_p126_motorcycles-harley-only-no-indian_composite.png
  * Viewed at 15% (no crop saved): 1951 ed. yellow p.123 seq804 Motorcycles = Harley only ("30 Years in Business", 114 E 11 st
    4-3161); 1952 ed. (reel 07592) p.130 seq219 = Harley only "John Menzel Prop 114 E 11 st 4-3161" (Motor Scooters: Cushman ->
    Gravely Tractor Sales & Service 5553 W Ridge rd); 1953 ed. p.122 seq464 = Harley only (John Menzel Prop); 1955 ed. p.125
    seq716 = Harley only (John Menzel Prop). => No Indian dealer listed in Erie phone books 1950-1955. 1957 (seq973) OCR only.
- OCR-ONLY context for A. Louis Straus (to image-check if needed):
  * 1935-40 (reel 07589 seq306/392/480): "Straus A Louis r 822 Weschler av 73-302" (residential). 1941-46 (reel 07590 seq65,
    178, 295, 412): "Straus A Louis r 3403 Erie st". July 1947 (reel 07590 seq818 yellow): "STRAUS A LOUIS autos 1315 Peach st
    23-495"; seq834 "Big Lot The 1315 Peach Erie-23-495"; seq835 "Straus Louis A 1315 Peach........ Erie-23-495".
  * 1948 ed.: white seq99 "Straus A Louis autos 1315 Peach st"; seq41 "Cushman Motor Scooters 1315 Peach st...2-3495"; seq28
    "Austin of England Motor Cars / 1315 Peach st"; yellow seq119 "AUSTIN OF ENGLAND MOTOR CARS ... DEALER / STRAUS A LOUIS
    1315 Peach st...Erie-2-3495". 1949 ed.: yellow seq361 "Motor Scooters / CUSHMAN MOTOR SCOOTERS ... DEALER / STRAUS A LOUIS
    1315 Peach st"; seq229 Cushman Motor Scooters 1315 Peach. 1950 ed.: white seq493 "Straus A Louis autos 1315 Peach st",
    Austin dealer seq517; 1951 ed.: seq722 autos 1315 Peach; seq750 "STRAUS A LOUIS / Distributor of Imported Cars / 1315
    Peach st". 1953 ed. (reel 07592 seq381): "Straus A Louis autos 127 E 12 st"; 1955 seq632/660-664 STRAUS A LOUIS 127 E 12 st
    2-3495. 1315 Peach later = "Warren Radio Inc 1315 Peach st" (1955-57, seq642/691/728).
  => Erie's Indian agency 1948-49 = A. Louis Straus, an imported-car (Austin of England) and Cushman scooter dealer, 1315 Peach
     St (phone 2-3495). Listing gone by the 1950 edition. Not on East 10th.
- East 10th in 1948-57 books: no cycle/motorcycle/scooter business with an E 10th address (OCR grep). Bicycle trade 1948-57:
  West Side Cycle Works 362 W 8th; Hoffman Joseph J bicycles 405 W 8th; Adams A R Cycle Shop 744 E 21st; Gabbel's Bicycle &
  Locksmith Shop; Hayes Bicycle Shop 1207 Powell av; Schneider M C bicycles 11 W 17th; Russ Bicycle Repair 2210 Buffalo rd (OCR).
- Bayhurst 1948-57 (OCR): "Bayhurst Charles 847 E 7 st" (residential, no business) every edition; 1955 "...27-0232".
- A. Louis Straus in July 1947 book (reel 07590, edition "corrected to May 1, 1947", OCR only): white seq818 "STRAUS A LOUIS autos
  1315 Peach st 23-495"; yellow seq834 "Big Lot The 1315 Peach Erie-23-495" (Automobile Dealers); seq835 "CUSHMAN MOTOR SCOOTERS
  ... A. LOUIS STRAUS 1315 Peach St. ERIE 23-495". No Indian in July 1947 (round-1 image check of the 1947 Motorcycles block:
  Harley only). => Straus took the Indian line between May 1947 and May 1948; dropped it before May 1950.
- 1958-1960 (new reel usteledirec07593 "Erie - 7/1958 thru 7/1960", OCR only; editions corrected to Apr 18 1958, Apr 17 1959,
  Apr 22 1960): Motorcycles = Harley-Davidson Motorcycle Agency 3001 Glenwood Pk av; STARVAGGI'S GARAGE "BSA - AJS / ARIEL -
  MATCHLESS - SUNBEAM / SALES and SERVICE / 3417 Peach st" (seq235 1958, seq500 1959). No Indian; no cycle business on E 10th.
  Straus A Louis 127 E 12 st (still autos). Bayhurst Charles 847 E 7 st (residential).

### 4. eBay / WorthPoint / web (WebSearch only; no direct site searches - WorthPoint needs login)
- Queries: '"Erie, Pa" Indian motorcycle dealer vintage advertising worthpoint'; '"Bayhurst" Indian motorcycle Erie';
  '"LeJeal" Erie Indian motorcycle OR "Le Jeal Cycle"'; '"Indian Motorcycle Agency" "Erie" ebay OR worthpoint'; 'worthpoint
  "Erie, Pa." motorcycle dealer decal OR "license plate" OR "dealer plate" Indian'; 'Beckman Indian motorcycle "Erie, Pa" 1920s
  "Parade"'; '"Straus" Indian motorcycle Erie 1948 OR 1949 "Peach"'; 'ebay "Erie Pa" Indian motorcycle dealer vintage ... tank
  decal OR sign OR photo'; '"Indian Motorcycle Sales & Service" "Erie"'; '"Erie" Pennsylvania 1930s "Indian" motorcycle shop
  "11th Street" OR "Tenth Street" ...'; '"A. Louis Straus" OR "Louis Straus" Erie ... Austin'.
  RESULT: MISS - only modern dealers (Indian Motorcycle of Erie / Off-Road Express, 10320 Wattsburg Rd), generic Indian
  memorabilia, a generic 1938 Indian dealer brochure on WorthPoint (worthpoint.com/worthopedia/1938-indian-motorcycle-co-dealer-
  1923128030, not Erie-specific). No Erie-dealer-marked item (decal, plate frame, photo, letterhead) for LeJeal, Beckman,
  Bayhurst, "Indian Motorcycle Agency" or Straus surfaced.
- chiefmotorcycleforum.com topic 5526 "Indian Motorcycle of Erie Pa." : curl 202 PoW bot challenge; WebFetch -> tollbit
  pay-per-crawl redirect => BLOCKED (title suggests the modern dealer).
- Journal of Erie Studies "The Early Automobile and its Influence on Erie, Pennsylvania, 1896-1920"
  (journals.psu.edu/eriestudies/article/download/74/74/146, PDF 200): LeJeal/Hagenlocher 1895 car, Roth bicycles; NO motorcycle
  dealer content. MISS.
- AMCA forum guest search: "Straus Erie" 0 results; "Erie Indian dealer" 0 results.
- Hatfield, "Indian Chief motorcycles, 1922-1953" (archive.org indianchiefmotor00hatf): lending-only, djvu.txt 401 (BLOCKED);
  IA FTS hit for "Indian dealer" Erie in it = "Indian News road tester Erie "Red" Armstrong" (a person named Erie, not Erie PA).
- Google Books feed: worked for the first ~10 queries (American Motorcyclist 1955-63 lists: Erie = Harley-Davidson only, "Erie
  H-D Sales" 114 E 11th 1955, 3001 Glenwood Park Ave by 1959); then "Internal error - please retry later" on 5 consecutive tries
  ('"Louis Straus" Erie', '"Straus" "1315 Peach"', '"Erie, Pa." Indian "Straus"') => PARTIAL/BLOCKED for the rest of the lane.
- archive.org: American Motorcycling issues on IA = only 1955 (AmericanMotorcyclingV09n01195501, bub_gb_-PsDAAAAMBAJ) and 1967+.
- CAIMAG via Common Crawl (ccsearch.py 'com,caimag)'): captures exist (2015-48: 610, 2016-44: 713, 2017-30: 331, 2018-26: 1029,
  2019-13: 352, 2019-35: 2793, 2020-05: 2103) but only scattered pages: 1,123 distinct thread URLs, none dealer-history related
  (only "dealer-in-united-kingdom" t12123). Indian Motorcycle forum f27 listing (2019-03-22 capture) page 1: no dealer thread.
  Member "SIDECAR" = member.php?5409-sidecar; blog.php?5409-SIDECAR capture (2019-08-22) = "SIDECAR does not have a blog yet."
  => Sidecar's 42-page dealer thread NOT recoverable from CC. -> manual (Wayback: web.archive.org/web/2020*/caimag.com/forum/*,
  look in forums 27 Indian Motorcycle, 31 Collectibles & Literature, 22 General Motorcycle Discussion; search posts by member 5409).

## CONCLUSIONS (dealer-lists lane)
1. NEW, IMAGE-VERIFIED: Erie had an Indian dealer after WWII: A. Louis Straus, 1315 Peach St, phone 2-3495.
   Aug 1948 book (corrected May 28, 1948) yellow p.116 and July 1949 book (corrected Apr 29, 1949) yellow p.113: "INDIAN MOTORCYCLE
   SALES & SERVICE / Headquarters for new and used motorcycles. Authorized Indian service. Genuine Indian parts. ... "WHERE TO BUY
   THEM" / STRAUS A LOUIS 1315 Peach st.......2-3495"; July 1949 white p.80: "Indian Motorcycle Agency 1315 Peach st..2-3495".
   Gone by the 1950 book (image: Motorcycles = Harley only). 1951, 1952, 1953, 1955 Motorcycles headings (viewed at 15%) = Harley
   only (114 E 11th, John Menzel Prop from 1952). 1957-60 OCR = Harley (+ Starvaggi's Garage BSA/AJS/Ariel/Matchless 3417 Peach,
   1958-59). Straus was an auto dealer (Austin of England; Cushman scooters 1947-49; "Distributor of Imported Cars" 1951; 127 E
   12th by 1953) - OCR context. => In 1948-1955 the only Indian dealer was Straus, 1315 Peach St, 1948-49. NOT East 10th.
2. oldindiandealers.com: never captured by Common Crawl (36 crawls 2008-2020, 0 captures; method validated). Not recoverable here.
3. CAIMAG 'Sidecar' thread: site offline (522), not in CC captures, Wayback blocked -> manual.
4. No other online old-dealer list reachable (indianmotorcycles.net list = modern + paywalled; Hatfield books lending-only; GB feed
   failing after ~10 queries). No Erie-specific Indian collectible on eBay/WorthPoint via WebSearch.
5. "East 10th": no motorcycle/bicycle/scooter business with an E 10th address in any Erie phone book 1948-1960 (OCR grep), and
   no dealer list or collectible mentions one. (Side note, not evidence: the Pennsylvania Telephone Corporation's general offices
   were at "20 East Tenth Street" - printed on p.3 of the 1948 and 1949 books.)
6. Harley agency 114 E 11th advertised "29 Years in Business" (1950 book, image) and "30 Years in Business" (1951 book, viewed) ->
   counts back to c.1921 (interpretation; continuity of the 114 E 11th Harley shop 1934-1955 is image-verified in phone books).

### Viewer links for Abe (LOC; sp = seq)
- 1948 yellow p.116: https://www.loc.gov/resource/gdcmassbookdig.usteledirec07591/?sp=173  (date page sp=24)
- 1949 yellow p.113: https://www.loc.gov/resource/gdcmassbookdig.usteledirec07591/?sp=362  (date page sp=211, cover sp=208)
- 1949 white p.80:  https://www.loc.gov/resource/gdcmassbookdig.usteledirec07591/?sp=250
- 1950 yellow p.126: ...07591/?sp=576 ; 1951 yellow p.123: ...07591/?sp=804
- 1952 p.130: https://www.loc.gov/resource/gdcmassbookdig.usteledirec07592/?sp=219 ; 1953 p.122 sp=464 ; 1955 p.125 sp=716
- Item records: https://www.loc.gov/item/usteledirec07591/ , /usteledirec07592/ , /usteledirec07593/ (1958-60)
