# Lane: loc-phonebooks — working log
Started 2026-10-04. Sources: LOC reels usteledirec07589 (Erie 1911-1940), usteledirec07590 (Erie 1941-1947).
Image fetch: tools/locimg.sh (tile.loc.gov IIIF). Scratch: lanes/loc-phonebooks/. Evidence: ../evidence/.

## Step 0: OCR re-grep of key lines

## Step 1a: Edition covers / target cards (viewed at pct 12.5, all on reel usteledirec07589)
Target cards (seq103, 269, 441, 529, 629, 841) read on image: "JULY 1934", "JULY 1935", "JULY 1936", "JULY 1937", "JULY 1938", "JULY 1940".
(Jan cards seq188 "JANUARY 1935", seq355 "JANUARY 1936", seq737 "JANUARY 1939" per OCR.)
Covers viewed on image:
- seq105: "ERIE AND NEARBY POINTS TELEPHONE DIRECTORY JULY, 1934 ... PENNSYLVANIA TELEPHONE CORPORATION" (Ecoma Milk ad top)
- seq190: "ERIE AND NEARBY POINTS TELEPHONE DIRECTORY JANUARY, 1935 ... PENNSYLVANIA TELEPHONE CORPORATION" (date stamp "DEC 29 1934"; Gebhardt Coal ad)
- seq271: "... TELEPHONE DIRECTORY JULY, 1935 ... PENNSYLVANIA TELEPHONE CORPORATION"
- seq357: "... TELEPHONE DIRECTORY JANUARY, 1936 ... PENNSYLVANIA TELEPHONE CORPORATION"
- seq443: "... TELEPHONE DIRECTORY JULY, 1936 ... PENNSYLVANIA TELEPHONE CORPORATION"
- seq531: "... TELEPHONE DIRECTORY JULY, 1937 ... PENNSYLVANIA TELEPHONE CORPORATION"
- seq632: "ERIE AND NEARBY POINTS TELEPHONE DIRECTORY ... JULY 1938 ... PENNSYLVANIA TELEPHONE CORPORATION" (LC Copyright Deposit bookplate)
- seq740: "ERIE AND NEARBY COMMUNITIES TELEPHONE DIRECTORY JANUARY 1939 ... PENNSYLVANIA TELEPHONE CORPORATION"
- seq845: "ERIE AND NEARBY COMMUNITIES TELEPHONE DIRECTORY JULY 1940 ... PENNSYLVANIA TELEPHONE CORPORATION"
NOTE: publisher is Pennsylvania Telephone Corporation (not Bell) for all 1934-1940 Erie editions.

## Step 1b: Listing verification on page images
- seq293 (July 1935 white, spread pp.38-39, right page "JOHNSTON 39", col 1 near top), viewed REGION 5050,100,2500,1500 pct50:
  "Indian Motorcycle Agency 120 E 11th st.....69-312"  (between "Independent Wall Paper Co 1210 State st" and "Indich Cafeteria 1123 State st")
  evidence: evidence/1935-07_loc-erie-phonebook-white_seq293.png
- seq345 (July 1935 yellow; left page header "24 Marine  ERIE CLASSIFIED BUSINESS DIRECTORY  Motors"), col 3, REGION 3350,4950,1750,900 pct100:
  "Motorcycles" / "Harley-Davidson Motorcycle Agency" / "114 E 11th.Erie-52-140" / "Indian Motorcycle Agency 120 E 11th.Erie-69-312"
  (between "Morticians —See Funeral Directors" and "Motors—Electric"). evidence/1935-07_loc-erie-phonebook-yellow_seq345.png
- seq293 header confirmed: "Designates Private Branch Exchange ... ERIE ... JOHNSTON 39" (page 39).
- seq379 (Jan 1936 white, left page "38 HOLMAN ERIE"), col 3, REGION 3300,3700,1800,1300 pct100:
  "Indian Motorcycle Agency 120 E 11th st....69-312" (between "Independent Wall Paper Co 1210 State st...24-500" and "Industrial Loan Society Inc 202 Palace Hdw bl..52-184")
  evidence/1936-01_loc-erie-phonebook-white_seq379.png
- seq431 (Jan 1936 yellow; left page "24 Marine  ERIE CLASSIFIED BUSINESS DIRECTORY  Multigraph"), col 3, REGION 3350,2350,1750,1000:
  "Motorcycles" / "Harley-Davidson Motorcycle Agency" / "114 E 11th.Erie-52-140" / "Indian Motorcycle Agency 120 E 11th.Erie-69-312"
  evidence/1936-01_loc-erie-phonebook-yellow_seq431.png
- seq466 (July 1936 white; right page header "ERIE ... JELL 39"), col 2, REGION 6200,2500,1800,1000:
  "Indian Motorcycle Agency 120 E 11th st.....69-312" (between "Independent Wall Paper Co 1116 State st...24-500" and "INDUSTRIAL LOAN SOCIETY INC")
  evidence/1936-07_loc-erie-phonebook-white_seq466.png
- seq499 (July 1936 yellow; right page "Manufacturers  ERIE CLASSIFIED BUSINESS DIRECTORY  Movers 25"), col 3, REGION 7650,1350,1750,1050:
  "Motorcycles" / "Harley-Davidson Motorcycle Agency" / "114 E 11th.Erie-52-140" / "Indian Motorcycle Agency 120 E 11th.Erie-69-312"
  evidence/1936-07_loc-erie-phonebook-yellow_seq499.png
- seq542 (July 1937 white; left page "16 BARBER  ERIE"), col 3, REGION 3050,2450,1800,800:
  "Bayhurst Charles motorcycles 302 E 11th st..48-385" (between "BAYERSON OIL WORKS 848 E 12th st.23-765" and "Bayton Albert r 2808 Greely av...W94-306")
  evidence/1937-07_loc-erie-phonebook-white_seq542.png
- seq554 (July 1937 white; right page "ERIE ... JAMESON 41"), col 2, REGION 6800,4050,1850,800:
  "Indian Motorcycle Agency 302 E 11th st.....48-385" (between "Independent Wall Paper Co 1116 State st...24-500" and "Indich Chas Mrs r 336 W 4th st...71-137")
  evidence/1937-07_loc-erie-phonebook-white_seq554.png
  NOTE: phone 48-385 identical to Bayhurst Charles motorcycles line (seq542) => same business; Indian agency operated by Charles Bayhurst in 1937.
- seq595 (July 1937 yellow; left page "34 Memorial  ERIE CLASSIFIED BUSINESS DIRECTORY  Motors"), col 3, REGION 3350,1250,1750,1100:
  "Motorcycles" / "Harley-Davidson Motorcycle Agency" / "114 E 11th.Erie-52-140" / "Indian Motorcycle Agency 302 E 11th.Erie-48-385"
  evidence/1937-07_loc-erie-phonebook-yellow_seq595.png
- seq158 (July 1934 yellow; right page "Monuments  ERIE CLASSIFIED BUSINESS DIRECTORY  Oils 19"), col 1, REGION 4950,2250,1750,1150:
  "Motorcycles" / "Harley-Davidson Motorcycle Agency" / "114 East 11th st.52-140"  -- ONLY entry; NO Indian (negative evidence)
  evidence/1934-07_loc-erie-phonebook-yellow_seq158.png
- seq259 (Jan 1935 yellow; right page "Mailing  ERIE CLASSIFIED BUSINESS DIRECTORY  Motors 23"), col 3, REGION 8050,2400,1800,1100:
  "Motorcycles" / "Harley-Davidson Motorcycle Agency" / "114 E 11th.Erie-52-140" -- ONLY entry; NO Indian (negative evidence)
  evidence/1935-01_loc-erie-phonebook-yellow_seq259.png
- seq704 (July 1938 yellow; left page "50 MON-MOV  CLASSIFIED BUSINESS DIRECTORY"), col 3, REGION 3350,2900,1750,1000:
  "Motorcycles." / "Harley-Davidson Motorcycle Agency" / "114 E 11th.Erie-52-140" -- ONLY entry; NO Indian (negative evidence)
  evidence/1938-07_loc-erie-phonebook-yellow_seq704.png
- seq808 (Jan 1939 yellow; left page "48 MOR-MOV  CLASSIFIED BUSINESS DIRECTORY"), col 3, REGION 3200,1250,1750,1000:
  "Motorcycles." / "Harley-Davidson Motorcycle Agency" / "114 E 11th.Erie-52-140" -- ONLY entry; NO Indian. (OCR of this page is garbled; image read.)
  evidence/1939-01_loc-erie-phonebook-yellow_seq808.png
- seq911 (July 1940 yellow; left page "40 MON-MOV  CLASSIFIED BUSINESS DIRECTORY"), col 3, REGION 3250,2100,1750,1000:
  "Motorcycles." / "Harley-Davidson Motorcycle Agency" / "114 E 11th.Erie-52-140" -- ONLY entry; NO Indian (negative evidence)
  evidence/1940-07_loc-erie-phonebook-yellow_seq911.png

## Step 2: Reel usteledirec07590 edition map (target cards viewed on image; covers viewed for 1945, 1947; OCR for others)
Target cards: seq19 "JULY 1941", seq128 "JULY 1942", seq243 "JULY 1943", seq360 "JANUARY 1944", seq478 "JULY 1945", seq606 "JULY 1946", seq762 "JULY 1947".
Covers: seq23 (OCR "TELEPHONE DIRECTORY JULY 194]"), seq132 (OCR "JULY 1942"), seq246 (OCR "JULY 1943"), seq364 (OCR "JANUARY 1944"),
 seq480 image "ERIE AND NEARBY COMMUNITIES TELEPHONE DIRECTORY JULY 1945 ... PENNSYLVANIA TELEPHONE CORPORATION",
 seq608 (OCR "JULY 1946"), seq764 image "... TELEPHONE DIRECTORY ... JULY 1947 ... PENNSYLVANIA TELEPHONE CORPORATION".
Yellow-page target cards: seq72, 185, 303, 421, 540, 669, 830.
Reel contents card seq8: "LOCALITY: ERIE (Includes Albion to West Springfield) July 1941 THROUGH ERIE ... July 1947".

## Step 2b: 1941-47 "Motorcycles." classified blocks (reel 07590), viewed on image (REGION crops at pct50)
- July 1941 seq93 (left p.40 "MOR-MOV CLASSIFIED BUSINESS DIRECTORY"), REGION 3250,1500,1650,800: "Motorcycles." / "Harley-Davidson Motorcycle Agency" / "114 E 11th.Erie-52-140" only
- July 1942 seq205 (right p.39 "MON-MOV"), REGION 5100,3250,1650,800: same, Harley only
- July 1943 seq322 (left p.36 "MIL-MOT"), REGION 1800,5100,1700,800: same, Harley only
- Jan 1944 seq440 (right p.37 "MOR-MOV"), REGION 5300,1400,1650,800: same, Harley only
- July 1945 seq560 (left p.38 "MOR-MOV"), REGION 3250,3100,1650,800: same, Harley only
- July 1946 seq702 (right p.65 "MIL-MOT"), REGION 7750,2350,1700,800: same, Harley only
- July 1947 seq865 (left p.68 "MON-MOT"), REGION 3250,2300,1650,800: same, Harley only
=> NO Indian dealer listed in Erie classified 1941-1947. evidence/1941-1947_loc-erie-phonebook-yellow_reel07590_motorcycles-blocks.png
White pages 1941-47: no "Indian Motorcycle" line in OCR. Charles Bayhurst listed only as residence "Bayhurst Charles r 847 E 7th st 50-232" (1943-1947 editions).

## Step 1c: Bayhurst absence check, white pages 1934-36 (image-verified)
Viewed the alphabetical position (BAYERSON OIL WORKS -> next entry) on images:
- Jul 1934 seq115: "BAYERSON OIL WORKS 848 E 12th st....23-765" / next "Beamish H C r 622 W 9th st" -> no Bayhurst
- Jan 1935 seq200: BAYERSON -> "Beamish H C r 622 W 9th st" -> no Bayhurst
- Jul 1935 seq282: BAYERSON -> "Beamer Jas R Rev r 1451 Mapleleaf dr" -> no Bayhurst
- Jan 1936 seq368: BAYERSON -> "Beamer Chas A r 351 W 20th st" -> no Bayhurst
- Jul 1936 seq455: BAYERSON -> "Beach Forest r 2021 Victory av Wesleyville" -> no Bayhurst
evidence/1934-1936_loc-erie-phonebook-white_no-bayhurst_seq115-200-282-368-455.png
So Charles Bayhurst has NO own phone listing while the "Indian Motorcycle Agency" was at 120 E 11th (69-312).
The 1935-36 agency operator is NOT named in these directories. Link Bayhurst<->Indian is proven only for July 1937 (shared phone 48-385, 302 E 11th).
OCR (not image-checked): Jul 1938 seq642, Jan 1939 seq749, Jul 1940 seq854: only "Bayhurst Frank W r 2314 Kilpatrick av"; no Charles.
1941 seq32: Edna Miss, Frank W, Lewis r 129 W 25th. 1942 seq141: Edna, Frank W. 1943-47: Charles r 847 E 7th st 50-232.
- seq642 (July 1938 white, p.14 "BAR-BEC"), REGION 3400,2850,1750,700 pct50 (image): "BAYERSON OIL WORKS 848 E 12th st.23-765" / "Bayhurst Frank W r 2314 Kilpatrick av....54-274" / "Bayle R L r 2509 German st" -> no Charles Bayhurst, no motorcycle line in 1938.
  evidence/1938-07_loc-erie-phonebook-white_seq642.png
- reel 07590 seq256 (July 1943 white), REGION 550,4650,1750,700 pct50 (image): "Bayhurst Charles r 847 E 7th st.....50-232" / "Bayhurst Edna Miss r 530 Shunpike rd.......92-544" / "Bayhurst Frank W r 2214 Kilpatrick av......54-274"
  evidence/1943-07_loc-erie-phonebook-white_reel07590_seq256.png

## Step 4: 1911 / 1914 editions
- Sep 1911 seq32 (p.19, right page, col 1), REGION 4650,4400,2200,700 pct50 (image):
  "LeJeal Cycle & Mobile Wks., 1721-3 Sassafras ..... 1761- J" / "LeJeal, C. H., Cycle Works, 1721-3 Sassafras.. 1761- J"
  evidence/1911-09_loc-erie-phonebook_seq32.png
- Oct 1914 seq72 (p.(26) "L Erie ... Bell Telephone", col 2), REGION 1850,2050,1800,700 pct50 (image):
  "1761J LeJeal Cycle & Mobile Wks..1721 Sassafras" / "1761J LeJeal C H, Cycle Wks.....1721 Sassafras"
  evidence/1914-10_loc-erie-phonebook_seq72.png
- Oct 1914 seq69 (p.(21) "Bell Telephone ... G Erie", right page col 1), REGION 4000,1450,1900,650 pct50 (image):
  "804J Gas Engine & Cycle Co, C H Retcher, Prop..........25 W 7th"  evidence/1914-10_loc-erie-phonebook_seq69.png
- Oct 1914 seq60 (front-matter "Classified Index to Advertisers, Continued", ad on p.(3)), REGION 4150,2900,3200,2200 pct50 (image):
  "Erie Rubber Company / Rain Coats Golf Goods / Mechanical Rubber Goods / Automobile, Motorcycle and Bicycle Supplies /
   DISTRIBUTORS OF Goodyear Automobile Tires / ERIE RUBBER COMPANY, ERIE, PA. / Odd Fellows Bldg., 28-30 W. 11th St. / Telephone No. 165-J"
  evidence/1914-10_loc-erie-phonebook_seq60_erie-rubber-ad.png ; left page stamped "OCT 27 1914".
- 1914 seq94 (Girard/North Girard section): "Hilliker H E & Sons, Bicycles & Rprs. Depot" (OCR only; Girard, not Erie city).
- The 1911 and 1914 books have NO classified "Motorcycles" heading (only an advertiser index, seq58-60). No "Indian" agency, no Harley, no other motorcycle dealer by name in OCR of seq19-101.

## Step 1d: White-page negative check (no "Indian Motorcycle Agency" in alphabetical slot), image-verified
- Jul 1934 seq126: "Independent Wall Paper Co 1021 State st.....24-500" -> "Indich Cafeteria 1123 State st....55-297" (no Indian)
- Jan 1935 seq211: "Independent Wall Paper Co 1021 State st...24-500" -> "Indich Cafeteria 1123 State st...55-297" (no Indian)
- Jul 1938 seq655: "Independent Wall Paper Co 1116 State st....24-500" -> "Indich Chas Mrs r 336 W 4th st....71-137" (no Indian)
- Jan 1939 seq761: "Independent Wall Paper Co 1116 State st...24-500" -> "Indich Chas Mrs r 336 W 4th st...71-137" (no Indian)
- Jul 1940 seq868: "Independent Wall Paper Co 1116 State st......49-348" -> "Indich Chas Mrs r 336 W 4th st....71-137" (no Indian)
evidence/1934-1940_loc-erie-phonebook-white_no-indian_seq126-211-655-761-868.png
=> Indian agency appears in exactly four editions: Jul 1935, Jan 1936, Jul 1936 (120 E 11th, 69-312) and Jul 1937 (302 E 11th, 48-385).

## Step 3: East 10th Street test (OCR grep, both reels)
Regex: (E|East|Ea).? (10th|1Oth|l0th|10tb|lOth|IOth|I0th|Tenth) AND motor|cycle|garage|auto|repair|tire|vulcan|machin|bicycl|indian|sales|harley|service|supply|accessor|battery|welding|radio|electric
Raw hits: lanes/loc-phonebooks/e10_hits.txt (346 lines). Summary by business: lanes/loc-phonebooks/e10_summary.txt.
Also grep for any line with 10th AND (cycl|indian|harley|motorc): ZERO motorcycle/bicycle businesses on E 10th (or W 10th) in any edition 1911-1947.
(Only artefact: 07590 seq545 "Martha's Beauty Shoppe 108 E 10th ... Bicycle Repairing" = OCR merge of two columns in July 1945 yellow pages; not a bicycle shop.)
E 10th WAS Erie's auto row in 1934-47 (OCR, not image-checked): Birkland C O Motor Co 201 E 10th 23-031 (1934-47; Willys/Hudson/Graham),
Goodyear Tire & Rubber Co / Prest-O-Lite Battery Service 163 E 10th 23-633, Horan Mike tire shop & Perry Tire & Repair Co 145 East 10th 22-948,
Erie Brake Service 160 E 10th (1934-37), Hart Tressa Auto Laundry 150 E 10th (1936-40), Everett R L Garage 113/118 E 10th (1935),
Erie Buick Co / Buick Sales & Service 117 E 10th 25-671 (1939-44), Litzel's Garage 420 E 10th 59-175 (1935-43), Milliken & Book Garage 420 E 10th (1934-35),
Daylight Service Co 126 E 10th (1937-39), Avenue Service Station 963 E 10th (1936-47), Erie Motors Inc / Kloss Motors (Nash) 134 E 10th (1941-47), Jones Motor Sales 162 E 10th (1943-44).
Verdict: "East 10th Street" is NOT supported for any motorcycle business in these directories. The Indian agency was on East 11th (120 E 11th, then 302 E 11th),
one block south of the E 10th auto row; the Harley agency was at 114 E 11th. Plausible memory conflation (10th vs 11th) but that is interpretation.

### Neighbours on East 11th (OCR)
114 E 11th: Harley-Davidson Motorcycle Agency 52-140 (every edition Jul 1934 - Jul 1947).
118 E 11th: Brown & Kelly garage 24-130 (1934-35); May's Auto Exchange (Jan 1936); East Eleventh St Garage 69-412 (Jul 1936); Barnhart Al M garage / Black Carl R garage (1940-41); Erie Motor Service / GMC Sales & Service 22-590 (1940-47). Moorhouse Motor Co 118 E 11th 22-487 (Jan 1939 yellow, OCR).
120 E 11th: only "Indian Motorcycle Agency 69-312" (Jul 1935, Jan 1936, Jul 1936). No other occupant found in OCR for any edition.
124 E 11th: Fuessler Motor Sales 69-113 (1934-36); Erie Brake Service 40-230 (1938); Haft's Garage 40-230 (1939-41); Firch Supply 23-891 (1945-47).
302 E 11th: only Indian Motorcycle Agency / Bayhurst Charles motorcycles 48-385 (Jul 1937); later "Cioccio J r 302 E 11th st" (residence, 1943-47).
304 E 11th: Lewis J W r (1935-39). 306 E 11th: Dayton Scale / Hobart Mfg / McCray Refrigerator 24-979 (all years). 308 E 11th: Knoll Bros grocers (1914); 63-207/C6-282 (1934-35).
151 E 11th: Johnson/Johnston David r (1911, 1914); Purdy C J Mrs r 43-235 (1936). NO Bayhurst listed at 151 E 11th in any edition (the "L. J. Bayhurst, 151 East 11th" of American Rifleman 1926-27 had no phone in 1934-47 books).

## Step 5: Per-edition table of motorcycle businesses (LOC Erie phone books)
(IMG = read on page image; OCR = OCR text only)
| Edition | Seq (white / yellow) | Motorcycle businesses listed |
|---|---|---|
| Sep 1911 | seq19-53 | No motorcycle heading. Cycle trade: "LeJeal Cycle & Mobile Wks., 1721-3 Sassafras 1761-J"; "LeJeal, C. H., Cycle Works, 1721-3 Sassafras 1761-J" (seq32 IMG) |
| Oct 1914 | seq56-101 | No motorcycle heading. "LeJeal Cycle & Mobile Wks..1721 Sassafras 1761J", "LeJeal C H, Cycle Wks 1721 Sassafras 1761J" (seq72 IMG); "Gas Engine & Cycle Co, C H Retcher, Prop 25 W 7th 804J" (seq69 IMG); Erie Rubber Company ad "Automobile, Motorcycle and Bicycle Supplies ... 28-30 W. 11th St. Telephone No. 165-J" (seq60 IMG) |
| Jul 1934 | 124 / 158 | Harley-Davidson Motorcycle Agency 114 East 11th st 52-140 (IMG yellow). No Indian (IMG white seq126 + yellow seq158) |
| Jan 1935 | 209 / 259 | Harley-Davidson 114 E 11th 52-140 (IMG). No Indian (IMG white seq211 + yellow) |
| Jul 1935 | 291,293 / 345 | Harley 114 E 11th 52-140; Indian Motorcycle Agency 120 E 11th 69-312 (IMG both) |
| Jan 1936 | 377,379 / 431 | Harley 114 E 11th 52-140; Indian Motorcycle Agency 120 E 11th 69-312 (IMG both) |
| Jul 1936 | 465,466 / 499 | Harley 114 E 11th 52-140; Indian Motorcycle Agency 120 E 11th 69-312 (IMG both) |
| Jul 1937 | 542,552,554 / 595 | Harley 114 E 11th 52-140; Indian Motorcycle Agency 302 E 11th 48-385 (IMG white+yellow); Bayhurst Charles motorcycles 302 E 11th st 48-385 (IMG) |
| Jul 1938 | 653 / 704 | Harley only (IMG yellow; IMG white no Indian seq655; Bayhurst Frank W only seq642 IMG) |
| Jan 1939 | 759 / 808 | Harley only (IMG yellow; IMG white no Indian seq761) |
| Jul 1940 | 866 / 911 | Harley only (IMG yellow; IMG white no Indian seq868) |
| Jul 1941 - Jul 1947 (reel 07590) | yellow seq93,205,322,440,560,702,865 | Harley only (IMG all seven) |
Bicycle trade 1934-47: Hoffman Joseph J (bicycles; "West Side Cycle Works") 362 W 8th 76-289 (1934-45; 405 W 8th in 1946-47) (IMG Jul 1935 seq337; OCR others);
Gabbel's Bicycle & Locksmith Shop 34 S Main, Union City (1943-47 OCR); Lewis W C bicycles Main st N Girard (1941-47 OCR); Schneider M C 11 W 17th (1946-47 OCR);
Horton George C 3160 Highland av (1946 OCR); Blickle Supply 1405 E Lake rd (1947 OCR). 1947 yellow seq835 ad: "CUSHMAN MOTOR SCOOTERS ... A. LOUIS STRAUS 1315 Peach St. ERIE 23-495" (OCR).

## Conclusions
1. The only Indian dealer in the LOC Erie phone books is "Indian Motorcycle Agency": 120 E 11th st, phone 69-312, in Jul 1935, Jan 1936, Jul 1936; then 302 E 11th st, phone 48-385, in Jul 1937.
2. In Jul 1937 the white pages also list "Bayhurst Charles motorcycles 302 E 11th st..48-385" — identical address and phone -> Charles Bayhurst ran the Indian agency in 1937.
   For 1935-36 the operator is not named (Bayhurst has no listing at all 1934-36, image-verified).
3. Absent Jul 1934 & Jan 1935 (so it started between Jan and Jul 1935 in phone-book terms, or had no phone before) and absent from Jul 1938 onward through Jul 1947.
4. No East 10th Street motorcycle business in any edition 1911-1947. E 10th was the auto row one block north.
5. Harley-Davidson Motorcycle Agency 114 E 11th 52-140 was the only other motorcycle listing, continuously 1934-1947.
6. LOC has NO Erie editions 1915-1933, so 1920s locations cannot be tested from this source.

## Sources checked (this lane)
- tile.loc.gov IIIF images reel usteledirec07589 — HIT (all crops above). ~110 image requests, >=3 s apart.
- work/loc/usteledirec07589.text.json OCR — HIT. work/loc/usteledirec07590.text.json OCR — HIT (negative for Indian).
- tile.loc.gov images reel usteledirec07590 — HIT (target cards, covers 1945/1947, 7 Motorcycles blocks, Bayhurst 1943).
- LOC Erie editions 1915-1933 — not on LOC (reel index seq11) — MISS/gap.

## Manual steps for Abe
- 1939 Polk Erie city directory (HathiTrust pst.000012006779, full view; HathiTrust blocked here): search Bayhurst / "Indian Motorcycle" / "302 E 11th" / "120 E 11th".
- Polk Erie city directories 1920-1938 (Erie County Public Library Heritage Room or Ancestry U.S. City Directories) to name the 1935-36 operator and find 1920s addresses (test E 10th there).
- LOC viewer links for every key page are in the structured result.
