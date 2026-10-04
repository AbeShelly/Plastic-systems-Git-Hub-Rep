# Lane: local-history — working log (started 2026-10-04)

Goal: Erie local histories (Reed 1925, Miller 1909, Nelson 1896, WPA 1938), Erie yearbooks 1920-40 ads, Sanborn maps of
E 10th/E 11th 100-300 blocks, AMCA forum dealer thread, Old Time Erie blog, Hagen History Center, collectibles (eBay/WorthPoint).
Scratch: lanes/local-history/. Evidence crops: ../../evidence/.

## Log

### 1. Erie county histories on archive.org (djvu.txt downloaded to lanes/local-history/, grep motorcycl|bicycle|cycle|Bayhurst|LeJeal|garage)
- Reed, History of Erie County (1925) vol 1 historyoferiecou01reed, vol 2 historyoferiecou02reed.
  NO "motorcycle" business, NO Bayhurst, NO Indian agency. Hits: bicycle-era bios (Suerken, Chambers, Roth, Schlaudecker,
  Montgomery 1922 Peach/1718 State, Mayo pro cyclist), Tribune Bicycle Co.
  KEY (VERIFIED ON IMAGE): vol 2 pp.857-858 (BookReader leaves 243-244) bio of Charles H. LeJeal:
   p.857 "Charles H. LeJeal, proprietor of the LeJeal Automotive Service, 1721 Sassafras Street, ... born in this city, Aug. 27, 1873"
   "... engaged in the bicycle business at 1617 Peach Street. Two years later he removed to 1507 Sassafras Street and finally to his
   present location."
   p.858 "Mr. LeJeal's business continued under the name of the LeJeal Cycle & Mobile Works until 1922, when it became known as the
   LeJeal Automotive Service." "... the only speedometer service station in the city. They are local dealers for Bosch electrical
   products." "Charles Archibald, died suddenly while riding in a motorcycle race at Corry, Pa., July 5, 1919, at the age of 19 years"
   => LeJeal (Erie's pre-1922 Indian agent) dropped "Cycle" in 1922 = same year A. D. Beckman took the Indian agency (trade-press lane).
   Evidence: evidence/1925_reed-history-erie-county-v2_p857_leaf243_charles-h-lejeal-bio.png, ..._p858_leaf244_lejeal-son-killed-motorcycle-race-1919.png
  Context lines (text only): vol 1 p.663 "The school [for fliers] is located at 124 East 11th Street, which is also the headquarters of the
  Great Lakes Airways." (later Haft's Garage 1939); vol 1 p.664 Keystone Rubber Mfg Co plant "located at 135 East 11th Street";
  vol 2 (Plate bio) 1915 Mill Creek flood destroyed home at "117 East 10th Street" and Erie News Co delivery "118 East Tenth Street".
- Miller, A Twentieth Century History of Erie County (1909) twentiethcentury01mill / 02mill: VERIFIED ON IMAGE vol 1 p.706 (leaf 728):
  "The Lejeal Cycle & Mobile Works, begun in 1894, at first builders of bicycles, later of automobiles, engaged in the manufacture of
  marine gasoline engines in 1909." Also "Roths' Cycle Works was founded in 1898". No motorcycle dealers named.
  Evidence: evidence/1909_miller-twentieth-century-history-erie-v1_p706_leaf728_lejeal-cycle-mobile-works-1894.png
- Nelson's Biographical Dictionary (1896) nelsonsbiog00whit: bicycle era only (Tribune Bicycle Works p.497; J. F. Stuntz bicycle dealer).
  No motorcycle. MISS for 1920-39.
- WPA "Erie: a guide to the city and county" (1938) erieguidetocitya00federich + erieaguidetothe00fedemiss: no motorcycl/bicycle/Indian/
  Bayhurst hits. MISS.
- Ries, History of Northwestern Pennsylvania (1943) 3 vols historyofnorthwe01-03ries: no motorcycle/Bayhurst/LeJeal(cycle)/Kuivinen. MISS.

### 2. Erie yearbooks 1918-1944 (full text grep: motorcycl|motocycl|cycle|Indian|Harley|bicycl|Bayhurst|Kuivinen|LeJeal|E 10th/11th)
A) archive.org (djvu.txt in lanes/local-history/yb/): academe1926acad, academe1927acad, academe1939acad, academe1941/42/43acad (Academy HS);
   seniorclassofstr1937/1938/1939stro (Strong Vincent "Spokesman"); spokesman00cent (1918), spokesman1918cent, spokesman1927cent,
   spokesman1929cent (Central HS); sunrise1924east, sunrise1926east (East HS); kaldron1942mcdo; kernel1935kern; eriez1931edin;
   lawrentian1942/1944lawr; wilsoncitizen00wils; classmates-yearbook-60893 (Academy 1922), -58126 (East 1935), -56147/-56780/-54060/
   -11707/-39716 (Strong Vincent 1937-41), -16610/-18817 (Academy 1941/42), -60746/-53401 (Tech 1942/43), -26723 (Millcreek 1943).
   (literulae00cath djvu.txt = HTTP 500, skipped.)
B) PowerLibrary (digitalarchives.powerlibrary.org/papd, collection papd:percp-ecy "Erie County Public Library - Erie County Yearbooks")
   LOADS (HTTP 200, no login). 269 items: Academe 1920, 1922-1992 (papd:44181-44199 = 1920,1922-1939; 44800-44852 = 1940-1992),
   East HS "Sunrise" 1923-2016 (papd:49133 = 1923 ... 49150 = 1940), Strong Vincent "Spokesman" 1931-2003 (papd:343232 = 1931,
   343233 1932, 343234 1933, [no 1934], 343235 1935 ... 343240 1940), NW PA Collegiate Academy 1998-2016. No Central/Tech/Prep/Villa.
   Each item = one PDF (OBJ datastream, 12-16 MB, ABBYY FineReader OCR text layer => searchable with pdftotext);
   FULL_TEXT datastream is empty (0 bytes); site Solr search not tested further. NOTE papd:343238 "Spokesman 1938" PDF is byte-identical
   (md5 1452c0a6...) to papd:343237 "Spokesman 1937" -> the 1938 SV book is effectively missing online.
   Downloaded + pdftotext (then deleted PDFs): Academe 1920,1923,1924,1925,1928-1940; Sunrise 1923,1925,1927-1940; Spokesman 1931-1933,
   1935-1940. Text in lanes/local-history/pl/*.txt.
RESULT: NO motorcycle dealer ad (Indian, Harley or other) in ANY Erie yearbook 1918-1944 checked. NEGATIVE for Bayhurst/Indian agency ads.
   Only incidental: "Bayhurst, Edna" (Academy 1938, 1939), M. Bayhurst / T. Bayhurst (Academy 1940/42), "Kuivinen, Dorothy" (Academy 1938),
   "Bill Shannon ... leaves school so he can ride his motorcycle" (Sunrise 1940 class will).
VERIFIED ON IMAGE (archive.org classmates-yearbook-60893-1922-academy-high-school, Academy HS Erie 1922, 1100x1422 scans):
 - p.114 (leaf 111): "Coast all the time / with a / Johnson Motor Wheel / SHADE CYCLE WORKS / 2101 Parade Street / ERIE, PA."
   Evidence: evidence/1922_academy-hs-yearbook-erie_p114_leaf111_shade-cycle-works-2101-parade-johnson-motor-wheel.png
 - p.125 (leaf 124): "BUY A TRIBUNE HIGH GRADE BICYCLE for 20 Year Service—Plus TIRES, SUPPLIES, REPAIRS" with script logo
   "LeJeal / CYCLE ~ MOBILE WORKS / 1721-23 SASSAFRAS ST. ERIE, PA." (no Indian/motorcycle mentioned in this 1922 ad).
   Evidence: evidence/1922_academy-hs-yearbook-erie_p125_leaf124_lejeal-cycle-mobile-works-1721-23-sassafras-tribune-bicycle.png
Text-only (OCR, not image-checked): Hoffman bicycles ads: "Hoffman for Bicycles 362 West 8th St." (Academy 1939, 1941; SV 1941),
   "Ride a Perry Bicycle ... HOFFMAN'S 362 West Eighth Street" (Kaldron 1942), "Joseph J. Hoffman Bicycles" (SV 1938; Academy/Sunrise 1938);
   "SHOES — BICYCLES ... 3716 West Lake Road F. DeMARCO, Prop." (Millcreek 1943); "Vitalic Bicycle Tires ... made right here in ERIE"
   (Academy/Sunrise 1928); Academy 1927 senior "Lee Montgomery / Monty, the Bicycle Man" (son of F. L. Montgomery, tire/bicycle shop per
   Reed 1925 - inference); "A. L. LeJEAL" music store ads 1922-1927 (Archie LeJeal, 1023 State per Reed) - NOT the cycle works.

### 3. Sanborn fire insurance maps (LOC via WebFetch for item JSON + curl tile.loc.gov IIIF; Penn State CONTENTdm API)
- LOC Erie items: sanborn07660_001 (1888), _002 (1900), _003/_004/_005 (1921 vols 1-3), _006/_007/_008 (1950 = "1921 - Oct 1950 Vol. 1,
  1921 - Aug 1950", i.e. 1921 base sheets with paste-over corrections to 1950), _009-_011 (1951), _012 (1917-03), _013 (Dec 1923, 1 sheet,
  NOT digitized). No 1930s edition online; the 1921-1950 corrected volume is the nearest to the 1935-39 shop years.
- Penn State maps1 (CONTENTdm dmQuery 'erie'): Erie 1888, 1900, 1917 new & additional, 1921 vols 1-3 only (same as LOC). Nothing newer.
- 1921 Vol.1 key map (07660_01_1921-0000): blocks E 10th-11th: sheet 3 (State-French), 59 (French-Holland = 100 blocks), 60 (Holland-German
  = 200 blocks), 61 (German-Parade = 300 blocks); E 11th-12th: 4, 63, 64, 65. House numbers: north side of E 11th = even, south side = odd;
  German St = start of 300 block (consistent with 1939 directory "GERMAN INTERSECTS 301-03 ... 302 Bayhurst").
- VIEWED (full-res IIIF regions, read on image):
  * 1921 Vol.1 sheet 59 (g3824em_g07660192101, 07660_01_1921-0059), E 11th north side 100 block: 102-104 "F. D. SCHULTZ CO. MFG CONFECTIONERS";
    then an unbuilt/vacant stretch with NO buildings or numbers (where 106-122 incl. 114 and 118-120 later stood); 124 "GARAGE CAPCY: 20 CARS ...
    AUTO SHOW RM"; 126 "S."; 128 "Furn'e"; 130-132 dwellings.
    Evidence: evidence/1921_sanborn-erie-v1-sheet59_loc-g3824em_g07660192101_e11th-100-block-north-side-vacant-106-122.png
  * 1921-Aug 1950 Vol.1 sheet 59 (g3824em_g07660195001, 07660_01_1950-0059), same frontage: 102-104 "V. F. W. CLUB / BOWLING B. HALL 2D";
    "AUTO PARKING"; 110 "Rest."; 114 "MOTOR CYCLE SHOP / TILE" (1-story); 118-120 "AUTO SALES & SERV. / STEEL FR. CONC. FL. TILE"; 124 "S";
    126-128 "C.I.O. HEAD QTS UNION HALL"; 130 "TRUCK SALES & SERVICE".
    => 114 E 11th (Harley-Davidson agency 1934-1955) = 1-story tile motorcycle shop; 120 E 11th (Indian Motorcycle Agency 1935-36) = part of the
    118-20 auto sales & service building (1939 directory: Moorhouse Motor Co used car dept 118-20). Buildings post-date 1921.
    Evidence: evidence/1950-08_sanborn-erie-v1-sheet59_loc-g3824em_g07660195001_114-e11th-motor-cycle-shop.png
  * 1921 Vol.1 sheet 63, E 11th south side 100 block: "133-135 KEYSTONE RUBBER M'F'G CO. (From Plans)", 137, 145, 149 D, 151 = 2-story frame
    dwelling ("2 D."), 153 D, 157 D, 159, 161, 163 S. A 1-story "Repair Shop" stands in the interior parcel behind 151-157 (lot attribution unclear).
    1950 sheet 63: 141-145 "AUTO REP. & BODY SHOP 1ST / W.H.O. 2ND"; 149 to Holland = blank paste-over (lots cleared; no building at 151).
    Evidence: evidence/1921_sanborn-erie-v1-sheet63_loc-g3824em_g07660192101_151-e11th-dwelling.png
  * Sheet 61, E 11th north side 300 block at German St: 1921: 302 = 2-story frame, "Plumber" with 1-story "AUTO" garage at rear; 304 "S." 2-story
    frame; 306, 308 "S." 2-story brick; 312 D; 314-316 S/vend; 318 D. 1921-1950: 302 "D." 2-story frame (+ "R. 302 E. 11th St."), 304 "S.",
    306-308 "WHOL. STORE FIXTURES" (= 1939 "Stone Arth L Co store fixtures 306-08"), 314 "ONE STORE".
    => Bayhurst's 1937-39 motorcycle shop at 302 E 11th was a small 2-story frame corner building (store front, garage at rear), German St corner.
    Evidence: evidence/1921-1950_sanborn-erie-v1-sheet61_302-e11th-german-corner.png
  * 1950 sheet 59 E 10th 100 block (both sides): no motorcycle shop; S side 101 filling sta, 117-129 "TAXI GARAGE", 145 auto rep, 149-151 "AUTO
    SALES & SERVICE", 163 "AUTO TIRES"/"TIRE SERVICE" (= Goodyear Service Stores 163 E 10th, 1939, which also sold bicycles). N side: Sears 1947.
    Sheet 60 (200 blocks E 8th-11th) viewed only at 1500 px overview: dwellings, churches, auto sales/repair, "USED CAR SALES"; no motorcycle
    label noticed (not exhaustively zoomed).
  * Other cycle-business sites on the same maps:
    - Sheet 74 (Parade St east side, E 18th-19th). 1921: "1801 / 1803 AUTO TIRES (TILE)" 2-story at the E 18th corner with a 1-story
      "CYCLE REPAIRING (C.B.)" building immediately east of it, fronting E 18th (only house number printed there: "401" [E 18th]);
      the 1805-1807 Parade frontage is EMPTY (no building) in 1921.
      1921-1950: 1801 S, 1803 S, 1805 (2-story), 1807 "BATTERY CHARGING" (2-story), 1809 "Rest.".
      => A. D. Beckman's Indian agency "at 1807 Parade street" (Motorcycle & Bicycle Illustrated, Dec 7 1922 - trade-press lane) occupied a
      building put up after the 1921 survey. Evidence: evidence/1921-1950_sanborn-erie-v1-sheet74_parade-1801-1807-cycle-repairing-beckman-site.png
    - Sheet 78 (Parade east side at E 21st), 1921: "From Plans / 401 ... 405 / 2101 / 2103" 2-story stores "S", "INTERIOR WALLS ARE TILE /
      OUTER WALLS ARE TILE FACED WITH 4" BRICK" = new building where Shade Cycle Works (Johnson Motor Wheel, 1922 Academy yearbook ad) was.
      Evidence: evidence/1921_sanborn-erie-v1-sheet78_loc-g3824em_g07660192101_2101-parade-new-store-bldg.png

### 4. AMCA forum thread "Old Dealers web sites?" (forum.antiquemotorcycle.org/.../7062-old-dealers-web-sites), curl 200, pages 1-5 read
  (62 posts, Oct 2009 - Jan 2019). NO Erie, Pa. dealer mentioned. Pennsylvania dealers named: "Fritz's, 236 N. Ninth Street, Reading, Penn."
  (p3 list), "Elmer Wolfe & Sons / Indian Motocycles and bicycles / Route Number 3 / Northampton, Pa / 1920's" (p4 #51), Kreidersville PA (#60).
  Post #37 (mdunn, 11-04-2009): "https://www.oldindiandealers.com" = the dealer-list site (unreachable here; no mirror found; web.archive.org
  blocked). Post #62 (Steve Swan, 01-11-2019): "'Sidecar' has a fantastic 42 page thread listing dealer info from the very early 1900's" on
  CAIMAG -> manual lead. AMCA forum search (guest, searchJSON keywords): "Bayhurst" 0, "erie indian dealer" 0, "erie pennsylvania indian" 0,
  "beckman erie" 0; "erie" 148 hits = modern Lake Erie Chapter chatter (page 1 checked; paging param ignored).
### 5. Web / blogs / collectibles
- WebSearch (US): '"Erie, Pa" Indian motorcycle dealer 1930s Bayhurst', '"Bayhurst" motorcycle Erie', '"Keystone Erie Motorcycle Club" history',
  'oldindiandealers.com Pennsylvania Erie', '"Indian Motorcycle Agency" Erie 1936 OR 1937 "11th"', 'Erie ... 1930s motorcycle shop photo
  "East 11th Street"', '"Erie, Pa" Indian motorcycle dealer matchbook OR decal OR "license plate"', 'worthpoint "Erie, Pa" "Indian" motorcycle
  dealer', '"Erie Harley-Davidson Sales" "114 East 11th" Kuivinen' -> only modern dealers / unrelated collectibles. MISS (no photos, no
  matchbooks/decals for Bayhurst or the Erie Indian agency surfaced). indianmotorcycles.net thread "Anyone Know About Indian Dealer In Erie, PA?"
  (2014-15) = modern Off Road Express only. hderie.com About Us: H-D of Erie opened 1972 (no pre-1972 history).
- Old Time Erie blog (oldtimeerie.blogspot.com, Debbi Lyon): search q=motorcycle, Indian, Bayhurst (0 posts), 11th, Harley, bicycle. Only
  motor-related post: "Harley-Davidson 1915 Anderson Cycle Works" (2012-10-01): "-ad in Erie Dispatch-Herald, October 11, 1914. Anderson Cycle
  Works was located at 546 West 18th Street ... owned by Theodore R. Anderson. A 1917 advertisement ... shows an address of 540 West 18th St."
  (ad image viewed: "1915 Harley-Davidson ... $275.00 ... ANDERSON CYCLE WORKS, Erie, Pa." - blog copy, newspaper not seen). Also mention of a
  1977-79 "motorcycle shop owned by Tech teacher Bernie Novotny" near Wayne/Reed & E 21st-22nd (out of period). Nothing on Indian/Bayhurst/E 10th.
- Hagen History Center (hagenhistory.org/research): Library & Archives in King-Mertens Archive Building, 800+ collections, 8,200+ linear ft,
  access by appointment/email (814) 454-1813 x 28; online catalog https://eriehistory.catalogaccess.com/ (PastPerfect): curl default UA 403;
  with browser UA the shell loads but results are JS-only; headless Chromium 403 -> PARTIAL/BLOCKED -> manual step. (A 'home-page-trap-url'
  honeypot link exists - not touched.) Home-history research program from $250 (title search) - paid, not used.
- Penn State CONTENTdm (all collections) 'bayhurst' = 4 Hammermill Bond pages already known; 'motorcycle' 266 hits, none Erie-titled.
- PowerLibrary site search (Islandora dismax, indexes PDF OCR): 'bayhurst' 22 hits (Erie yearbooks 1938-1981 + a Pennsylvania Bulletin);
  quoted '"Indian motorcycle(s)"' hits = New Castle directories, Wilkes-Barre, Mount Pleasant etc. - no Erie business. ECPL PowerLibrary
  collections: yearbooks, Erie County Maps (7 maps: 1872, 1914, 1949, 1963, 1965, 1977, 1989), Erie Gazette 1820-25, GAR sketches, library
  reports, COVID oral histories, Erie Gay News. No Erie directories/newspapers for 1915-45 there.
- Google Books feed: '"LeJeal" Corry motorcycle' -> Reed 1925 (confirmed above) + Motor 1909 dealer list "Lejeal Cycle & Mobile Works, 1721
  Sassafras Ave."; '"Archie LeJeal"' -> Musical America's Guide 1926 "Archie LeJeal, 1007 State St." (music dealer - not cycles).

## CONCLUSIONS (local-history lane)
1. County histories: none of Reed 1925, Miller 1909, Nelson 1896, WPA 1938 guide, Ries 1943 mentions Bayhurst, an Indian agency or any 1920s-30s
   motorcycle dealer. Reed 1925 (image-verified) gives the fullest life sketch of Erie's pre-1922 Indian agent Charles H. LeJeal (b. 27 Aug 1873;
   bicycle business from c.1892 at 1617 Peach, then 1507 Sassafras, then 1721 Sassafras; "LeJeal Cycle & Mobile Works until 1922, when it became
   known as the LeJeal Automotive Service"; son Charles Archibald killed in a motorcycle race at Corry, Pa., July 5, 1919, aged 19).
2. Yearbooks: Erie yearbooks 1918-1944 (archive.org + PowerLibrary PDFs, ~60 volumes) contain NO motorcycle-dealer advertisement (OCR-based
   negative). 1922 Academy yearbook (image-verified): LeJeal Cycle ~ Mobile Works 1721-23 Sassafras (Tribune bicycles) and Shade Cycle Works,
   2101 Parade (Johnson Motor Wheel). PowerLibrary yearbooks DO load, are full-text searchable (site search + PDF OCR), cover Academy 1920,
   1922-1992, East 1923-2016, Strong Vincent 1931-2003 (1938 file is a duplicate of 1937; no 1934 SV).
3. Sanborn (image-verified): 114 E 11th = "MOTOR CYCLE SHOP" (1-story tile) on the 1921-Aug 1950 sheet 59; 118-120 E 11th = "AUTO SALES & SERV."
   building; both lots were EMPTY in 1921 (so the buildings date 1921-1934). 302 E 11th = small 2-story frame corner building at German St
   (1921 plumber + rear auto garage; 1950 dwelling). 151 E 11th = 2-story frame dwelling in 1921, cleared by 1950. 1807 Parade (Beckman Indian
   agency 1922) was empty in 1921; 2101 Parade (Shade Cycle Works 1922) was a new store block "From Plans" in 1921; a "CYCLE REPAIRING" shop
   stood at E 18th & Parade (beside 1801-03 Parade "AUTO TIRES") in 1921.
4. "East 10th Street" test: NOT supported. E 10th 100 block (1950 Sanborn, both sides) has no motorcycle shop; only cycle-related E 10th business
   found anywhere = Goodyear tire store 163 E 10th (sold bicycles 1939; "AUTO TIRES" on 1950 map). Interpretation only (not evidence): the 114/120
   E 11th shops stand on the north side of E 11th, i.e. in the block bounded by E 10th and E 11th (Sanborn sheet 59), which could blur into
   "East 10th" in memory.
5. No photographs of the 1930s Erie Indian shop, no Bayhurst collectibles, and no Erie entry in the AMCA dealer thread were found. Hagen History
   Center's PastPerfect catalog could not be searched from here (JS-only / 403) -> manual.

### Viewer links (for Abe)
- archive.org printed-page URLs: Reed v2 https://archive.org/details/historyoferiecou02reed/page/857 (jp2 leaf 243; page_numbers.json n-index 228),
  /page/858 (leaf 244); Miller v1 https://archive.org/details/twentiethcentury01mill/page/706 (leaf 728);
  Academy 1922 https://archive.org/details/classmates-yearbook-60893-1922-academy-high-school/page/n111 (p.114) and /page/n124 (p.125).
- LOC Sanborn sp numbers (checked via WebFetch JSON): 1921 Vol.1 resource g3824em.g3824em_g07660192101 ?sp=61 = file 0059 (offset +2);
  1921-1950 Vol.1 resource g3824em.g3824em_g07660195001 ?sp=63 = file 0059, ?sp=61 = file 0057 (offset +4). Other sheets computed with the same
  offsets (1921: sheet 61 sp=63, 63 sp=65, 74 sp=76, 78 sp=80; 1950: sheet 61 sp=65, 63 sp=67, 74 sp=78) - not individually checked.
