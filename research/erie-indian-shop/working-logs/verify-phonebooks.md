# Lane: verify-phonebooks (adversarial re-check of round-1 phone-book claims)
Started 2026-10-04. Method: re-fetch each LOC page from tile.loc.gov IIIF (own helper lanes/verify-phonebooks/f.sh, sleeps 3.5 s
after every request), overview at pct 12.5, then full-res REGION crops chosen from my own overview (not from round-1 coordinates).
Saved evidence crops opened only AFTER my own reading. Scratch images: lanes/verify-phonebooks/.

## Step 0: seq -> image-file mapping
WebFetch https://www.loc.gov/resource/gdcmassbookdig.usteledirec07589/?sp=293&fo=json -> "index": 293, image file
usteledirec07589_0292 => viewer sp=N = IIIF file _(N-1). The locimg.sh convention (SEQ-1) is correct.

## Per-claim readings
(Reel usteledirec07589 unless stated. "IMG" = read by me on a freshly fetched tile.loc.gov image; crops in lanes/verify-phonebooks/cNNN.jpg)
- C1 seq293: right page header "ERIE ... JOHNSTON 39" (h293.jpg). Col 1 under Hanley funeral ad: "Independent Wall Paper Co 1210 State st.......24-500" /
  "Indian Motorcycle Agency 120 E 11th st....69-312" / "Indich Cafeteria 1123 State st...55-297" (c293.jpg, full res). IMG.
- C2 seq345: left page header "24 Marine  ERIE CLASSIFIED BUSINESS DIRECTORY  Motors" (overview). Col 3: "Morticians -See Funeral Directors" /
  "Motorcycles" / "Harley-Davidson Motorcycle Agency" / "114 E 11th.Erie-52-140" / "Indian Motorcycle Agency 120 E 11th.Erie-69-312" / "Motors—Electric". IMG.
- C3 seq379: left page "38 HOLMAN  ERIE", col 3: "Independent Iron & Metal Co 235 E 20th st...55-273" / "Independent Wall Paper Co 1210 State st.......24-500" /
  "Indian Motorcycle Agency 120 E 11th st.....69-312" / "Industrial Loan Society Inc 202 Palace Hdw bl..52-184". IMG (c379a.jpg pct50).
- C4 seq431: left page "24 Marine  ERIE CLASSIFIED BUSINESS DIRECTORY  Multigraph", col 3: "Motorcycles" / "Harley-Davidson Motorcycle Agency" /
  "114 E 11th.Erie-52-140" / "Indian Motorcycle Agency 120 E 11th.Erie-69-312". IMG.
- C5 seq466: right page "ERIE ... JELL 39", col 2: "Independent Wall Paper Co 1116 State st....24-500" / "Indian Motorcycle Agency 120 E 11th st.....69-312" /
  "INDUSTRIAL LOAN SOCIETY INC 202 Palace Hdw bl 52-184". IMG.
- C6 seq499: right page "Manufacturers  ERIE CLASSIFIED BUSINESS DIRECTORY  Movers 25", col 3: "Morticians -See Funeral Directors" / "Motorcycles" /
  "Harley-Davidson Motorcycle Agency" / "114 E 11th.Erie-52-140" / "Indian Motorcycle Agency 120 E 11th.Erie-69-312" / "Motor Trucks". IMG.
- C7/C50 seq542: left page "16 BARBER  ERIE", col 3: "Bayer W K r 724 West 10th st...58-235" / "BAYERSON OIL WORKS 848 E 12th st.23-765" /
  "Bayhurst Charles motorcycles 302 E 11th st..48-385" / "Bayton Albert r 2808 Greely av.....W94-306" / "Beach Forest r 2021 Victory av Wesleyville....82-383". IMG.
- C8 seq554: right page "ERIE ... JAMESON 41", col 2: "Independent Order Foresters 19 W 12th st.....76-276" / "Independent Wall Paper Co 1116 State st...24-500" /
  "Indian Motorcycle Agency 302 E 11th st.....48-385" / "Indich Chas Mrs r 336 W 4th st.....71-137". IMG.
  OCR grep of whole reel 07589 for 48-385 or "302 E 11th": only seq542, 554, 595. "Same business" is an inference from shared line/address, not printed.
- C9 seq595: left page "34 Memorial  ERIE CLASSIFIED BUSINESS DIRECTORY  Motors", col 3: "Moth Destroyers BUYER'S GUIDE INFORMATION SERVICE.Erie-22-790" /
  "Motorcycles" / "Harley-Davidson Motorcycle Agency" / "114 E 11th.Erie-52-140" / "Indian Motorcycle Agency 302 E 11th.Erie-48-385" / "Motor Trucks". IMG.
- C10 seq158: right page "Monuments  ERIE CLASSIFIED BUSINESS DIRECTORY  Oils 19", col 1 (of right page): "Motor Bus Lines -See Bus Lines" / "Motorcycles" /
  "Harley-Davidson Motorcycle Agency" / "114 East 11th st.52-140" / "Motors—Electric". Only one entry. IMG.
- C11 seq259: right page "Mailing  ERIE CLASSIFIED BUSINESS DIRECTORY  Motors 23", col 3: "Morticians" / "Motorcycles" / "Harley-Davidson Motorcycle Agency" /
  "114 E 11th.Erie-52-140" / "Motors—Electric". Only one entry. IMG.
- C12 seq704: left page "50 MON-MOV  CLASSIFIED BUSINESS DIRECTORY", col 3: "Motor Trucks -See Truck Dealers" / "Motorcycles." / "Harley-Davidson Motorcycle Agency" /
  "114 E 11th.Erie-52-140" / "Motors—Electric". Only one entry. IMG.
- C13 seq808: left page "48 MOR-MOV  CLASSIFIED BUSINESS DIRECTORY", col 3: "Motor Trucks" / "Motorcycles." / "Harley-Davidson Motorcycle Agency" /
  "114 E 11th.Erie-52-140" / "Motors—Electric". Only one entry. IMG.
- C14 seq911: left page "40 MON-MOV  CLASSIFIED BUSINESS DIRECTORY", col 3: "Motor Trucks -See Truck Dealers" / "Motorcycles." / "Harley-Davidson Motorcycle Agency" /
  "114 E 11th.Erie-52-140" / "Motors—Electric". Only one entry. IMG.

## Edition attribution (reel 07589), all viewed by me on fresh images (m_cards.jpg, m_cov1.jpg, m_cov2.jpg)
Target cards: seq103 "JULY 1934", 188 "JANUARY 1935", 269 "JULY 1935", 355 "JANUARY 1936", 441 "JULY 1936", 529 "JULY 1937",
629 "JULY 1938", 737 "JANUARY 1939", 841 "JULY 1940".
Covers: seq105 "ERIE AND NEARBY POINTS TELEPHONE DIRECTORY JULY, 1934 ... PENNSYLVANIA TELEPHONE CORPORATION"; seq190 "... JANUARY, 1935";
seq271 "... JULY, 1935"; seq357 "... JANUARY, 1936"; seq443 "... JULY, 1936"; seq531 "... JULY, 1937"; seq632 "ERIE AND NEARBY POINTS TELEPHONE
DIRECTORY ... JULY 1938 ... PENNSYLVANIA TELEPHONE CORPORATION" (Copyright Deposit bookplate on left); seq740 "ERIE AND NEARBY COMMUNITIES TELEPHONE
DIRECTORY JANUARY 1939"; seq845 "ERIE AND NEARBY COMMUNITIES TELEPHONE DIRECTORY JULY 1940". OCR scan for any other month-year cover page found none
in between. So seq293/345 = Jul 1935; 379/431 = Jan 1936; 466/499 = Jul 1936; 542/554/595 = Jul 1937; 158 = Jul 1934; 259 = Jan 1935;
704 = Jul 1938; 808 = Jan 1939; 911 = Jul 1940. Attributions in claims 1-14 correct.
- C15 white-page negative (all IMG, full-res crops c126/c211/c655/c761/c868):
  seq126 (Jul 1934, left p.38 "HORNIK", col 3): "Independent Wall Paper Co 1021 State st.....24-500" / "Indich Cafeteria 1123 State st....55-297" / "Indich Inc cafeteria 630 Peach st...43-142"
  seq211 (Jan 1935, right p.39 "JOHNSTON", col 1): "Independent Wall Paper Co 1021 State st.....24-500" / "Indich Cafeteria 1123 State st....55-297"
  seq655 (Jul 1938, left p.40 "HUT-JOH", col 1): "Independent Wall Paper Co 1116 State st....24-500" / "Indich Chas Mrs r 336 W 4th st....71-137"
  seq761 (Jan 1939, right p.39 "HUF-JER", col 2): "Independent Wall Paper Co 1116 State st....24-500" / "Indich Chas Mrs r 336 W 4th st....71-137"
  seq868 (Jul 1940, left p.42 "HUM-JER", col 1): "Independent Wall Paper Co 1116 State st......49-348" / "Indich Chas Mrs r 336 W 4th st....71-137"
  No "Indian ..." line at the slot in any of the five. Confirmed.
- C16 Bayhurst slot 1934-36 (all IMG, full-res c115/c200/c282/c368/c455):
  seq115 (Jul 1934, left p.16 "BARBER", col 2): "Bayer W K r 724 West 10th st...58-235" / "BAYERSON OIL WORKS 848 E 12th st.....23-765" / "Beamish H C r 622 W 9th st....24-563"
  seq200 (Jan 1935, left p.16 "BARRETT", col 2): "BAYERSON OIL WORKS 848 E 12th st.....23-765" / "Beamish H C r 622 W 9th st....24-563"
  seq282 (Jul 1935, left p.16 "BARTLETT", col 2): "BAYERSON OIL WORKS 848 E 12th st.....23-765" / "Beamer Jas R Rev r 1451 Mapleleaf dr.....W95-128"
  seq368 (Jan 1936, left p.16 "BAUBLITZ", col 1): "BAYERSON OIL WORKS 848 E 12th st.....23-765" / "Beamer Chas A r 351 W 20th st....76-250"
  seq455 (Jul 1936, left p.16 "BARRY", col 2): "BAYERSON OIL WORKS 848 E 12th st.....23-765" / "Beach Forest r 2021 Victory av Wesleyville....82-383"
  No Bayhurst at the slot in any. Confirmed (slot check only; a misfiled/variant spelling elsewhere is not excluded).
- C17 seq642 (Jul 1938, left p.14 "BAR-BEC", col 3) IMG: "Bayer W K r 1576 W 6th st....33-240" / "BAYERSON OIL WORKS 848 E 12th st.23-765" /
  "Bayhurst Frank W r 2314 Kilpatrick av.....54-274" / "Bayle R L r 2509 German st.....09-514" / "Bayton Albert r 2808 Greely av....W94-306". Confirmed.
  Extra (claim 17 note, now IMG): seq749 (Jan 1939, left p.14 "BAR-BEL", col 2): "BAYERSON OIL WORKS 848 E 12th st.23-765" / "Bayhurst Frank W r 2314 Kilpatrick av.....54-274" /
  "Bayle R L r 2509 German st....09-514". seq854 (Jul 1940, right p.15 "BAX-BEN", col 1): same three lines (Frank W 54-274). No Charles in 1938, Jan 1939, Jul 1940.
- Reel 07590 mapping: WebFetch https://www.loc.gov/resource/gdcmassbookdig.usteledirec07590/?sp=256&fo=json -> index 256, file usteledirec07590_0255 (same SEQ-1 rule).
- Reel 07590 edition cards (IMG, m_r90cards.jpg): seq19 "JULY 1941", 128 "JULY 1942", 243 "JULY 1943", 360 "JANUARY 1944", 478 "JULY 1945",
  606 "JULY 1946", 762 "JULY 1947". Cover seq246 (IMG): "ERIE AND NEARBY COMMUNITIES TELEPHONE DIRECTORY JULY 1943 ... PENNSYLVANIA TELEPHONE CORPORATION".
- C18/C51 reel 07590 seq256 (Jul 1943, left p.16 "BAU-BEN", col 1) IMG: "BAYERSON OIL WORKS 848 E 12th st.23-765" / "Bayhurst Charles r 847 E 7th st.....50-232" /
  "Bayhurst Edna Miss r 530 Shunpike rd.......92-544" / "Bayhurst Frank W r 2214 Kilpatrick av.....54-274" / "Bayle Mike r 2716 Pear st...46-271". Confirmed.
  C51 other editions now IMG (half-res crops r90c373/489/616/772): seq373 (Jan 1944, left p.14 "BAU-BEM", col 1), seq489 (Jul 1945, left p.14 "BAR-BED", col 2),
  seq616 (Jul 1946, left p.12 "BAU-BEN", col 1), seq772 (Jul 1947, left p.12 "BAU-BEL", col 2): each "Bayhurst Charles r 847 E 7th st.....50-232"
  followed by "Bayhurst Edna Miss r 530 Shunpike rd...92-544" / "Bayhurst Frank W r 2214 Kilpatrick av...54-274". Confirmed for all five 1943-47 editions.
- C19 reel 07590 yellow pages, all IMG full-res (y93/y205/y322/y440/y560/y702/y865.jpg):
  seq93 (Jul 1941, left p.40 "MOR-MOV CLASSIFIED BUSINESS DIRECTORY", col 3), seq205 (Jul 1942, right p.39 "MON-MOV", col 1), seq322 (Jul 1943, left p.36 "MIL-MOT", col 2),
  seq440 (Jan 1944, right p.37 "MOR-MOV", col 1), seq560 (Jul 1945, left p.38 "MOR-MOV", col 3), seq702 (Jul 1946, right p.65 "MIL-MOT", col 3),
  seq865 (Jul 1947, left p.68 "MON-MOT", col 3): each "Motorcycles." / "Harley-Davidson Motorcycle Agency" / "114 E 11th.Erie-52-140" then "Motors—Electric". Harley only.
  Line reading CONFIRMED; but "No Indian dealer in Erie" is an inference from absence of a classified listing (Bayhurst still had a motorcycle
  business in 1939-40 per other lanes while the phone books carried nothing) -> wording should be "no Indian listing under Motorcycles".
- C20 Harley 114 E 11th 52-140: seen by me on images in all 16 LOC-held editions (reel 07589 seq158, 259, 345, 431, 499, 595, 704, 808, 911;
  reel 07590 seq93, 205, 322, 440, 560, 702, 865). Variant: Jul 1934 prints "114 East 11th st.52-140" (no "Erie-" prefix). LOC reels do not hold
  every edition (e.g. no Jan 1937/Jan 1938/Jul 1939/Jan 1940/Jan 1941-43 books on film), so "every edition" = every LOC-held edition.
- 1911/1914 attribution (IMG, m_e_cov.jpg): seq21 cover "ERIE COUNTY TELEPHONE DIRECTORY ... Erie, Corry, Union City and Nearby Places SEPTEMBER 15, 1911" (Bell System);
  seq56 = LOC card "TELEPHONE DIRECTORIES WHITE PAGES SEE INDEX OF LOCALITIES AT BEGINNING OF REEL"; seq57 cover "TELEPHONE DIRECTORY WINTER ISSUE
  ... THE BELL TELEPHONE COMPANY OF PENNSYLVANIA ... OCTOBER 5, 1914 ... ERIE COUNTY Erie, Albion, Corry, North East, North Girard, Union City and Nearby Towns".
- C21 seq32 (1911, right page header "19 ... ERIE L", col 1) IMG: "LeJeal Cycle & Mobile Wks., 1721-3 Sassafras  1761- J" / "LeJeal, C. H., Cycle Works, 1721-3 Sassafras..  1761- J"
  (between "Leiplein, E. F., Res., 808 E. 8th 1192- J" and "Lemmon, A. H. & Sons, Coal & Builders' Supplies, 801 E. 6th 541-W"). Confirmed.
- C22 seq72 (1914, left page "L Erie (26) Bell Telephone", col 2) IMG: "1761J LeJeal Cycle & Mobile Wks..1721 Sassafras" / "1761J LeJeal C H, Cycle Wks.....1721 Sassafras". Confirmed.
- C23 seq69 (1914, right page "Bell Telephone (21) G Erie", col 1) IMG: "804J Gas Engine & Cycle Co, C H Retcher," / "Prop..........25 W 7th" (wrapped over two lines). Confirmed.
- C24 seq60 (1914 front matter, right page "(3)"; left page "Classified Index to Advertisers, Continued" stamped "OCT 27 1914") IMG:
  "Erie Rubber Company / Rain Coats  Golf Goods / Mechanical Rubber Goods / Automobile, Motorcycle and Bicycle Supplies / DISTRIBUTORS OF /
  Goodyear Automobile Tires / ERIE RUBBER COMPANY, ERIE, PA. / Odd Fellows Bldg., 28-30 W. 11th St. / MAIL AND TELEPHONE ORDERS GIVEN PROMPT ATTENTION /
  Telephone No. 165-J". Confirmed.
- C25 Bicycles headings (IMG): seq337 (Jul 1935, left p.8 "Beauty ... Brushes", col 2): "Bicycle Repairing" / "Hoffman Joseph J 362 W 8th.......Erie-76-289" /
  "Bicycles" / "Hoffman Joseph J 362 W 8th.......Erie-76-289" / "Billiard Parlors". Line CONFIRMED.
  seq152 (Jul 1934, left p.6 "Batteries ... Brass", col 2): "Bicycle Repairing" / "Hoffman Joseph J 362 W 8th st........76-289" / "Bicycles" / same.
  reel 07590 seq426 (Jan 1944, right p.9 "BEE-BOA", col 1): "Bicycles." / "Gabbel's Bicycle & Locksmith Shop 34 S Main.Union City-33-W" / "Hoffman Joseph J 362 W 8th.......Erie-76-289".
  reel 07590 seq545 (Jul 1945, right p.9 "BEE-BON", col 3): "Bicycle Repairing" / "Hoffman Joseph J 405 W 8th.......Erie-76-289" / "Bicycles." /
  "Gabbel's Bicycle & Locksmith Shop 34 S Main.Union City-33-W" / "Hoffman Joseph J 405 W 8th.......Erie-76-289".
  => CORRECTION: Hoffman is at 405 W 8th already in July 1945 (not "by 1946"); 362 W 8th holds 1934 - Jan 1944. So "362 W 8th ... 1934-1945" is wrong for 1945.
  Also reel 07590 seq87 (Jul 1941 classified p.29, Hardware) carries a display ad "SALSBURY & NASH HARDWARE 3406 W. LAKE RD. Dial Erie 41-240" whose
  product list includes "BICYCLES" — not under the Bicycles heading, and W Lake Rd is probably outside the city, but "only bicycle listing in the classified pages"
  should be narrowed to "only Erie listing under the Bicycles / Bicycle Repairing headings". Other editions (seq251, 422, 491, 582, 685, 790, 896; 07590 seq78, 191, 308) OCR only.
  (seq415/485 "Bicycles / Marsh Hardware Co 416 Lake ... Erie-12-345" = sample listings on a "YOU Can use any of these features profitably" promo page — not real.)
- tile.loc.gov returned HTTP 503 twice during this lane (seq545, seq426); each succeeded on a single retry after 20-30 s. Not blocked.
- Extra for C18 note (now IMG): reel 07590 seq32 (Jul 1941, right p.15, col 3): "BAYERSON OIL WORKS 848 E 12th st.23-765" / "Bayhurst Edna Miss r 536 Shunpike rd...92-544" /
  "Bayhurst Frank W r 2314 Kilpatrick av....54-274" / "Bayhurst Lewis r 129 W 25th st....23-313". seq141 (Jul 1942, right p.15, col 3): BAYERSON / "Bayhurst Edna Miss r 536 Shunpike rd...92-544" /
  "Bayhurst Frank W r 2314 Kilpatrick av....54-274" / "Bayle Mike r 2716 Pear st". No Charles in 1941 or 1942. Confirmed.
- OCR sweep reel 07589 for bayh|motorcyc|indian mot: no other Bayhurst or motorcycle line besides those above (white-page Harley lines seq124, 209, 291, 377, 465, 552, 653, 759, 866).

## Saved evidence crops (opened only after my own readings)
All 24 files exist, are <=1800 px and legibly show the claimed lines. Labelling issues (not legibility):
- The single-page crops for seq293, 345, 379, 431, 466, 499, 542, 554, 595, 158, 259, 704, 808, 911 are two stitched strips (page-header strip pasted above a
  full-res body crop; visible seam). The multi-panel files 1934-1940_..._no-indian_..., 1934-1936_..._no-bayhurst_..., and 1941-1947_..._motorcycles-blocks
  are also stitched. None carry the required "_composite" suffix -> rename.
- 1938-07_..._seq642, 1943-07_..._reel07590_seq256, 1911-09_..._seq32, 1914-10_..._seq69/seq72, 1935-07_..._seq337 have no page-heading context in the crop.
- Panels for seq211 and seq761 in the no-indian composite are at pct25: small but legible.

## Verdicts
CONFIRMED: 1, 2, 3, 4, 5, 6, 7, 9, 15, 16, 17, 18, 21, 22, 23, 24, 50, 51.
CORRECTED: 8 (line exact; "same business / Bayhurst operated the agency" is inference from shared address+phone, not printed),
 10, 11, 12, 13, 14, 19 (lines exact; "No Indian dealer" overreaches -> "no Indian listing under the classified Motorcycles heading"),
 20 ("every edition" -> every LOC-filmed edition, 16 of them; Jul 1934 prints "114 East 11th st.52-140"),
 25 (Jul 1945 classified shows Hoffman at 405 W 8th, not 362; Gabbel's (Union City) also under Bicycles 1943-45; Salsbury & Nash Hardware
     3406 W Lake Rd ad lists BICYCLES in Jul 1941 classified p.29).
REFUTED: none. COULD-NOT-CHECK: none.
Requests: ~150 tile.loc.gov image requests, >=3.5 s apart; 2 transient HTTP 503s, each recovered on one retry after 20-30 s. 2 WebFetch calls to loc.gov JSON.
