# Lane: verify-press-history (adversarial verifier, round 2) — started 2026-10-04

Method: for each claim in verify_groups.json["press_history"] (ids 26-41, 55-66) re-fetch the page image from the source
(archive.org BookReader/IIIF leaf image; LOC tile.loc.gov IIIF for Sanborn), read the line myself, check date/edition
attribution from masthead/running head/cover, and only THEN open the saved evidence crop (crop_ok).
Scratch: work/lanes/verify-press-history/. Pace >= 3 s between hits on one host.

## Log
### Claims 26-29 (Motorcycle and Bicycle Illustrated 1922, archive.org item motorcycleillustrated, doc motorcycleillustrated1922d)
- scandata (motorcycleillustrated1922d_scandata.xml): 511 leaves, all addToAccessFormats, leafNum 0-based => /page/n373 = leaf 373 = jp2 _0373.
  scandata pageNumber: leaf 291=19, 292=20, 293=21, 372=20, 373=21.
- Fetched myself via BookReaderImages (ia.sh) leaf 373 scale 2 + full (5195x7135). Running head "December 7, 1922", folio "21".
  Read: "There must be many more enthusiasts just like A. D. Beckman, who has hung out his sign on the new Indian agency at 1807
  Parade street, and opened up with a full line of Indian motorcycles, side- cars. bicycles, parts and accessories." (#26 CONFIRMED)
  Read: "Mr. Beckman has installed Charles Schroeder, who was in the repair department of the LeJeal Mobile and Cycle Works, former
  Indian dealers at Erie, for the past five years, in the service department of the new agency." (#27: line exact; claim's "went to
  RUN Beckman's service department" overreaches "installed ... in the service department" -> CORRECTED; "for the past five years" is
  syntactically ambiguous (could modify "former Indian dealers"), the reading 'Schroeder 5 yrs in LeJeal repair dept' is the natural one.)
  Read: "Since 1909 Beckman has been riding, winter and summer" / "was a charter member of the Erie club, organized in 1910 and still in a
  flourishing condition with club rooms at 2[5]10 Peach street. He acted as secretary of the club and F. A. M. Commissioner for six years
  and for the past three years has been president and M. and A. T. A. referee." The '5' of 2510 is a damaged glyph (full-res zoom), reads 5.
  "giving up his position as assistant branch manager of the Armour & Co., Erie branch, with which he has been connected for sixteen years"
  (#28 CORRECTED: '16 years' = years connected with Armour & Co., not 16 years as asst. branch manager; 'president 1919-22' is inference
  from 'for the past three years' as of Dec 7 1922 -> say 'president c.1920-22 (past three years as of Dec 1922)'.)
- Leaf 292 (p.20, "Among the Dealers", running head "Motorcycle and Bicycle Illustrated", no date on this page). Leaves 291 (p.19) and
  293 (p.21) both carry running head "November 23, 1922" -> p.20 is in the Nov 23, 1922 issue. Read: "NEW INDIAN DEALER AT ERIE / Erie,
  Pa.—"Archie" Beckman, a well-known and popular figure among motorcyclists in this city for the past fifteen years, has taken on the local
  Indian agency." (#29 CONFIRMED)
- Crops: beckman-1807-parade.png shows date head + 1807 line + club/secretary/president lines (not the Armour line) -> ok for 26, 28.
  schroeder-lejeal.png legible, no date head (caption gives context) -> ok. leaf292 crop legible with headline, no date -> ok.
### Claims 30, 37, 38 (doc motorcycleillustrated1917c)
- scandata 1917c: 728 leaves, 0-based, all in access formats; leaf 448 = p.32, leaf 667 = p.43.
- Leaf 448 fetched (scale 2 + full 5037x6980). Running head "32  MOTORCYCLE AND BICYCLE ILLUSTRATED  August 30, 1917" (the '7' damaged).
  Col 2 "TRADE ACTIVITIES IN ERIE / ERIE, Pa., Aug. 20.—Charles LeJeal of the LeJeal Cycle & Mobile Works, of Erie, states that he will
  specialize hereafter on repairs for magnetos and speedometers, in addition to handling Indian motorcycles and bicycles." (#30 CONFIRMED)
  Col 3 (continuation of same Erie section): "The Anderson Cycle Works. Harley- Davidson agents at Erie, have delivered 75 machines so far
  this season and expect continuance of the good business. Bicycles have been added to the company's lines, the Harley-Davidson, Emblem
  and Star brands being handled." ('75' = broken type, zoomed 4x: 7 and 5; 'Works.' printed with a period/comma blob) (#38 CONFIRMED)
- Leaf 667 fetched (scale 2 + full). Running head "September 27, 1917  MOTORCYCLE AND BICYCLE ILLUSTRATED  43". Col 3: "Erie, Pa., is
  "some cycle town" as everyone knows, and the Anderson Cycle Works, No. 8, maintains a prosperous store at 540 West 18th street; it
  devotes its two show windows to a pleasing display." '540' crisp at full res (not 546). Photo No. 8 storefront: signs "ANDERSON CYCLE
  WORKS", "CYCLE SUPPLIES", "MOTOR-CYCLES."; no street number visible in photo. (#37 CONFIRMED as printed; 540-vs-546 conflict stands.)
- Crops: erie-a (heading + LeJeal para) ok; erie-b (col-3 continuation, no heading/date, self-identifying 'at Erie') ok;
  anderson-540 (photo 8 + paragraph, no date head) ok.
### Claims 31, 35, 36 (doc motorcycleillustrated1917a; scandata 667 leaves, 0-based, all access; leaf 43=p.35, 75=p.19, 627=p.23)
- Leaf 43: running head "January 4, 1917  MOTOR CYCLE ILLUSTRATED  35". Col 1 "ERIE M. C.'S STAFF FOR 1917 / ERIE, Pa.—The Erie M. C. has
  elected the following officers for 1917: O. R. Sonneson, president; Wm. Edwards, vice-presiden: A. D. Beckman, secretary; R. J. Oboth,
  financial secretary; F. F. Farrell, treasurer; Lamont Vance, captain; H. C. Schaefer, lieutenant." (printed 'vice-presi- den:' and
  'Oboth' with a broken O). Col 2 top continuation: "This is Mr. Sonneson's second term as president; Mr. Edwards' third year as
  vice-president and Mr. Beckman's sixth year in the capacity of secretary." -> officer facts CONFIRMED.
  BUT the claim's 2nd sentence ("This resolves the snippet's 'A. D. Beckna' as OCR damage") is inference: the 'Beckna' snippet is from a
  different page (Google Books 9aYAAAAAMAAJ, Apr 1917 club list, quoted in trade-press/gb_raw.log l.1158) which nobody has seen as an image;
  archive.org has no 1917b (Apr-Jun) volume (file list checked). -> #35 CORRECTED ('makes it very likely', not 'resolves').
- Leaf 75: running head "January 11, 1917  MOTOR CYCLE ILLUSTRATED  19". Photo pair "AN OUT-OF-THE-ORDINARY MOTOR SLED"; caption "The Winter
  Machine Built Around an Indian Twin by the Le Jeal Cycle Works, of Erie, Pa., the Local Hendee Representative". Sled lettering (full-res,
  4x zoom): "Indian Power- -plus MOTOCYCLE" / "LEJEAL CYCLE WORKS 18TH SASSAFRAS" -> superscript 'TH' with underline, NO '&' visible
  (the lane's "18TH [&] SASSAFRAS" bracket should be dropped). #31 CONFIRMED (caption exact; '18th & Sassafras' only as a paraphrase).
- Leaf 627: running head "March 29, 1917  MOTOR CYCLE ILLUSTRATED  23". Photo "CLEAN UP WEEK NOT NEEDED HERE", caption "The Store of the
  Anderson Cycle Works, Harley-Davidson Agents in Erie, Pa., Where There's a Place for Everything and Everything Is Kept Strictly in Its
  Place" (interior view). #36 CONFIRMED.
- Crops: leaf75 photo+caption ok; leaf43 officers para ok (no date head; 'sixth year' line not in crop); leaf627 photo+caption ok.
### Claims 33, 40, 41
- 1908 (scandata 713 leaves, 0-based, all access; leaf 265 has no pageNumber = issue front page). Leaf 265 fetched (scale 2 + full):
  masthead "TEN CENTS / MOTORCYCLE ILLUSTRATED / Vol. III. No. 8  July 15, 1908"; "SWENSON'S RIDE / NEW YORK TO CHICAGO: 49 HOURS, 40
  MINUTES"; "B. A. Swenson, the hardy Indian rider from Providence"; "Following are the checking points in the different towns Swenson
  passed through:" ... "Erie, Pa. ...........Le Jeal Cycle Co., 1721 Sassafras st." (#33 CONFIRMED; note the text says rain stopped him at
  Dunkirk Tuesday night, so he passed Erie on Wednesday; 'mostly Indian agents' in notes is interpretation, not printed.)
- 1915b (scandata leaf 519=p.13, 520 no number). Leaf 520 running head "14  MOTOR CYCLE ILLUSTRATED  August 19, 1915." "DEMONSTRATED WITH A
  TRAILER / In the accompanying photograph is shown a Reading Standard motorcycle which made motorcyclists of Erie, Pa., sit up ... The
  machine, which was demonstrated by the Erie Motor Sales Co., local R-S agents, pulled the 600-lb trailer and its 175-lb. passenger and
  carried the 165-lb. rider without the slightest difficulty." (#40 CONFIRMED)
- 1916a (scandata leaf 957=p.13). Running head "April 13, 1916.  MOTOR CYCLE ILLUSTRATED  13". "MOUNTING THE ERIE COPS / ERIE, Pa.—This city
  is determined that its police department shall keep abreast of the times, and has indicated this policy by ordering two Indians."
  (#41 CONFIRMED; no dealer named, as the claim notes.)
- Crops: leaf265 (masthead+list) ok; leaf520 (photo+para) ok; leaf957 (para) ok (no date head).

### Session 2 (resumed) — re-check of the above
- Re-fetched leaf 373 (1922d) at scale 1 from archive.org BookReaderImages: md5 976ec471... identical to the earlier scratch file
  mi1922d_373_full.jpg -> scratch fetches are faithful source images. Re-viewed myself (overview pages <=1800 px + zooms) for leaves
  1922d 373/292 (+291/293 heads), 1917c 448/667, 1917a 43/75/627, 1908 265, 1915b 520, 1916a 957, and re-checked scandata pageNumbers.
  All readings above re-confirmed by eye. Verdicts unchanged: 26 C, 27 CORR, 28 CORR, 29 C, 30 C, 31 C, 33 C, 35 CORR, 36 C, 37 C, 38 C,
  40 C, 41 C. Evidence crops then opened: all legible (notes: #28 crop lacks the Armour line; #35 crop lacks the 'sixth year' line;
  #31/#35/#37/#38/#41/#27/#29 crops lack date heads).

### Claims 32, 34, 39 (new this session)
- KEY FINDING (URL attribution): in items bicycli64231911161912newy, bicyclingwo5927181909newy and motorcycleenthus1923unse, leaf 0 (and in
  the 1912 vol. also leaves 854-855) are NOT in the access formats (scandata addToAccessFormats=false). BookReader /page/nN is the 0-based
  index into the ACCESS list, not the jp2 leaf number. Proven two ways: *_page_numbers.json (pages[n].leafNum) and the IIIF v3 manifest
  (iiif.archive.org/iiif/3/ID/manifest.json canvas n -> body ..._LLLL.jp2):
    1912: n1283 -> jp2 1286 = p.1214; n1284 -> jp2 1287 = p.1215; the cited /page/n1286 -> jp2 1289 = p.1217 (WRONG PAGE).
    1909: n1006 -> jp2 1007 = p.929; the cited /page/n1007 -> jp2 1008 = p.930 (WRONG PAGE).
    1923-24 Enthusiast: n220 -> jp2 221 = p.21; the cited /page/n221 -> jp2 222 = p.22 (WRONG PAGE); n180 -> jp2 181 = No.63 p.9.
  The leaf (jp2) numbers and printed pages in the claims are right; only the viewer URLs are off. Fix: use /page/n1283, /page/n1006,
  /page/n220 (or printed-page URLs /page/1214, /page/929, /page/21).
- #32: jp2 1286 fetched (scale 1, 3098x4014). Running head "1214 THE BICYCLING WORLD AND MOTORCYCLE REVIEW". "ERIE'S ATTRACTIVE SHOW /
  Seven Exhibitors of Cycles Lend Variety to the Automobile Exhibits—Trade's Showing a Pleasant Surprise. / Erie, Pa., March 1.—Booked for a
  three-day run, Erie's first automobile and motorcycle show opened in Arbuckle's garage last night, and large crowds poured in for the
  curtain raising." ... "Six makes of motorcycle were exhibited. The largest exhibit was that of the LeJeal Cycle Works, agent for the Indian,
  while the honors for the best decorated booth went to M. A. Reinholtz, the Thor agent, ..."
  jp2 1287 (p.1215): "LeJeal Cycle Works—Indian motorcycles; Pope bicycles. Represented by C. H. LeJeal, George Fry, Claude Torrance.—One 4-h.p.
  belt single; one 5-h.p. chain twin racer; two 7-h.p. standard chain twins, one with tandem; one 7-h.p. Tourist Trophy chain twin; one 4-h.p.
  chain single with sidecar; bicycles." Booth photo "INDIAN MOTOCYCLES / LeJeal Cycle Works".
  Issue date: search-inside hit + image of jp2 1275 (p.1203) masthead "Vol. LXIV. New York, U. S. A., Saturday, March 9, 1912. No. 25";
  pp.1203-1215 continuous; next masthead (Mar 16) is after the article in the djvu text. => Mar 9, 1912 issue; show opened night of Feb 29, 1912.
  Verdict CORRECTED (URL only). Crops p1214 + p1215 exhibitors legible.
- #34: jp2 1007 (p.929) "Motorcycles Save the Day at Erie. / Billed as the headliners at a mixed automobile and motorcycle meet promoted by
  the Erie (Pa.) Motorcycle Club on the 30th ult., ... W. R. Kellam, Merkel, captured the one mile open for twin cylinders in 1:33. Harry
  Reinholz, Thor, was second, and Charles Le Jeal, Indian, third. Le Jeal, with 150 yards, won the 5 miles handicap by 10 feet, from Kellam,
  scratch, ... Kellam turned the tables in the 10 miles handicap ... Le Jeal was second and Reinholz third." Issue: jp2 985 masthead
  "Volume LIX. New York, U. S. A., Saturday, September 11, 1909. No. 25" (image viewed); Sept 18 masthead at jp2 1023 -> p.929 is in the
  Sept 11 issue -> "30th ult." = Aug 30, 1909. Verdict CORRECTED (URL only). Crop legible.
- #39: jp2 221: "No. 64  The Harley-Davidson Enthusiast  21" / "Vacationing via Harley-Davidson / By J. E. Young" ... "early Sunday morning,
  June 10th, in my 23JD" ... "After leaving Oil City, Pa., we headed for Erie, stopped there long enough to enjoy the hospitality of Mr.
  Furlong, the Harley-Davidson dealer, and left for Niagara Falls." June 10 = Sunday only in 1923 (1922 Sat, 1924 Tue). NEW: issue No. 64
  cover = jp2 201 "The Harley-Davidson Enthusiast ... September, 1923" (pp.5..21 continuous from jp2 205) -> issue dated Sept 1923.
  jp2 181: "No. 63 ... 9" "Erie, Pa., had such a big turnout for its Gypsy Tour ... "Everybody had a good time," wrote W. M. Furlong, who
  managed things." -> 'W. M.' is a name-match inference (No. 63 calls him tour manager, not dealer). Verdict CORRECTED (URL; date now
  'Sept 1923 issue, trip of June 1923'). Crop legible (has 'No. 64' head, not the folio).

### Claims 55-59 (local-history books; archive.org; fetched jp2 at scale 1 myself)
- Reed, History of Erie County v.2 (archive.org metadata: Topeka, Historical Pub. Co., 1925). page_numbers.json: n228 = jp2 243 = p.857;
  n229 = jp2 244 = p.858 -> printed-page URLs /page/857, /page/858 are right (leaf 0,60,61,80,81,... not in access, so /page/n243 would
  be WRONG; the claim uses /page/857 -> fine).
  #55 p.857 (head "HISTORY OF ERIE COUNTY 857"): "Charles H. LeJeal, proprietor of the LeJeal Automotive Service, 1721 Sassafras Street, is one
  of Erie's representative business men and prominent citizens. He was born in this city, Aug. 27, 1873, and is the son of John and Mary
  (Weis) LeJeal." ... "associated in business with his father until he was 19 years of age, when he engaged in the bicycle business at 1617
  Peach Street. Two years later he removed to 1507 Sassafras Street and finally to his present location." CONFIRMED.
  #56 p.858: "Mr. LeJeal's business continued under the name of the LeJeal Cycle & Mobile Works until 1922, when it became known as the LeJeal
  Automotive Service." / "The LeJeal Automotive Service consists of the distribution of all kinds of automobile accessories and is the only
  speedometer service station in the city. They are local dealers for Bosch electrical products." / "Charles Archibald, died suddenly while
  riding in a motorcycle race at Corry, Pa., July 5, 1919, at the age of 19 years". CONFIRMED.
- #57 Miller, Twentieth Century History of Erie County v.1 (Chicago, Lewis Pub. Co., 1909). n723 = jp2 728 = p.706 (/page/706 right).
  "The Lejeal Cycle & Mobile Works, begun in 1894, at first builders of bicycles, later of automobiles, engaged in the manufacture of marine
  gasoline engines in 1909." CONFIRMED ("from 1909" ~ "in 1909"). Note: Reed puts his bicycle start at age 19 (~1892, 1617 Peach); Miller's
  1894 is the firm, not necessarily the first shop - not a contradiction of the line.
- Academy HS yearbook "ACADEME 1922" (item classmates-yearbook-60893-1922-academy-high-school; files are named 60893_*; no leaves outside
  access -> n = leaf). Title-page frame on jp2 3 reads "ACADEME ... 1922" (image), OCR "ACADEME 1922 / Published by the Students of Academy
  High School". #58 jp2 124, folio "125": "BUY A TRIBUNE HIGH GRADE BICYCLE for 20 Year Service—Plus TIRES, SUPPLIES, REPAIRS" + logo
  "LeJeal CYCLE ~ MOBILE WORKS / 1721-23 SASSAFRAS ST. ERIE, PA." (4x zoom). No motorcycle/Indian. CONFIRMED.
  #59 jp2 111, folio "114": "Coast all the time / with a / Johnson Motor Wheel / SHADE CYCLE WORKS / 2101 Parade Street / ERIE, PA." CONFIRMED.
- Crops (opened after reading): all five legible (Reed 857/858, Miller 706, yearbook p125 small but readable, p114).

### Claims 60-66 (LOC Sanborn; www.loc.gov JSON via WebFetch, images curl tile.loc.gov IIIF regions at full res)
- sp mapping checked via WebFetch JSON: 1950 vol1 sp=63 -> 07660_01_1950-0059; sp=65 -> 1950-0061. 1921 vol1 sp=61 -> 1921-0059;
  sp=65 -> 1921-0063; sp=76 -> 1921-0074; sp=80 -> 1921-0078. (1950 sp=67/78 not JSON-checked; I fetched files 1950-0063/0074 directly and
  the printed sheet numbers 63/74 are on the images.) Every sheet's printed number checked on the image ("ERIE, PA. VOL. I. 59 (16-17)",
  "61 (30-34)", "63 (17-18)", "74 (46-98)", "78", "60 (29-33)").
- Edition: LOC item sanborn07660_006 created_published "Sanborn Map Company, 1921 - Oct 1950 Vol. 1, 1921 - Aug 1950"; _007 "Vol. 2, 1921 -
  Aug 1950"; _008 "Vol. 3, 1921 - Oct 1950" -> Vol.1 = base 1921 corrected to Aug 1950 (the 'Oct 1950' is the edition span). Label OK.
- 503 from tile.loc.gov twice (sheet 63 full overview; sheet 78 region first try) -> switched to region requests, which worked; no other blocks.
- #60 1950 sheet 59 E 11th frontage: "E. 11TH ST 102 104" V.F.W. CLUB / BOWLING B. HALL 2D; "AUTO PARKING"; "110 ... Rest."; "114 / 116"
  1-story "MOTOR CYCLE SHOP / TILE" (frame 1-story rear addition); "118 ... 120" "AUTO SALES & SERV. / STEEL FR. CONC. FL. TILE" with "OFF.";
  "124" S; "126 128" "C.I.O. HEAD QTS UNION HALL"; "130 ... 134" "TRUCK SALES & SERVICE CONC. FL.". CONFIRMED (lot also numbered 116).
- #61 1921 sheet 59 same frontage: "102 104" F. D. SCHULTZ CO. MF'G CONFECTIONERS (+1-story Storage wing); then NO buildings, NO numbers;
  "124" GARAGE CAP'Y: 20 CARS ... AUTO SHOW RM; "126" S.; "128" Furn'e; "130 132" D. CONFIRMED (the '1921-1934' bracket uses the July 1934
  phone book for 114 E 11th - inference).
- #62 sheet 61 at German St: 1921 "302" 2-story frame "Plumber" with 1-story "AUTO" at rear; "304" S.; "306 308" brick S. S.
  1950: "R. 302 E. 11TH ST.", "302 E. 11TH ST." "2 D."; "304" S.; "306 308 E. 11TH ST." "WHOL. STORE FIXTURES" "ONE S.". CONFIRMED.
- #63 sheet 63 (1921): "133-135 KEYSTONE RUBBER M'F'G CO. (From Plans)", "137", "145", "149" 2 D. (set back), "151" 2 D., "153" 2 D.,
  "157" 2 D., "159 161 163"; interior parcel behind 151-157: "Repair Shop / 1 / B.I.", "2 AUTOS C.I.", "AUTO", D "A.I.". The Repair Shop sits
  directly behind 151's lot but on a separate parcel (lot line closes 151 above it). 1950 sheet 63: "141 143 ... 145" "AUTO REP. & BODY SHOP
  1ST / W.H.O. 2ND"; "149 <-149 11TH ST."; E 11th frontage 149..Holland = blank paste-over, BUT set back behind it stand large "AUTO SALES &
  SERVICE" (C.B., steel fr., steel deck rf., conc. fl., 12 W.G. skyts, "BLR RM") and "STEEL FR. BR. & TILE CURTAIN WALLS ... SALES & SERVICE"
  buildings - one stands exactly on the 1921 Repair Shop parcel. => claim 'everything from 149 to Holland was blank (cleared)' overreaches:
  only the street frontage is blank. CORRECTED. (Also '149 D' is '2 D.'.)
- #64 sheet 74: 1921 "401" [E 18th] / "1801 1803" 2-story "AUTO TIRES (TILE)" + attached 1-story "CYCLE REPAIRING (C.B.)" east of it on the
  E 18th side; Parade frontage south of 1803 empty, no numbers. 1950: "1801" S., "1803" S. "BR. & TILE"; "1805" 2; "1807" "2 BATTERY CHARGING";
  "1809" "2 Rest."; 1811; "1813 PRINT'G"; "1815 FURN'E"; "1817 APTS"; "R. 1811 PARADE"; "1817 1/2 AUTO REP". CONFIRMED ('1807 lot empty in
  1921' uses 1950 numbering - no number printed in 1921).
- #65 sheet 78 (1921): "From Plans" over "401 ... 405" / "2101" "2103" 2-story S. S. (brick colour) / "INTERIOR WALLS ARE TILE OUTER WALLS ARE
  TILE FACED WITH 4" BRICK"; "409", "411" D. CONFIRMED ("under construction" = usual meaning of "From Plans", interpretive).
- #66 1950 sheet 59 E 10th 100 block, read at full res: S side "101 E.10TH FILLING STA." (GREAS'G C.B., G.T.S); "107 109" D. VEN'D; "113" APTS;
  "R.113" AUTO REP. 1ST SIGN SHOP 2ND; "117 119 121 ... 125 127 129" TAXI GARAGE (OFF., REST., FURN'E 1ST); "131 133" F F; "137" D; "141 143" D;
  "145" AUTO REP. C.B.; "149 151" AUTO SALES & SERVICE; "155" S. (rear "TIRE STGE (VEN'D)"); "157" D; "163" AUTO TIRES / AUTO GREASING / TIRE
  SERVICE / OFF. / WHOL. CHEESE. N side: "106 E.10TH 108" D/VEN'D/S; "114", "114 1/2", "116", "A-116 1/2-B" S./REST.; BOWLING (rear), AUTO
  REPAIRING (rear); "122" CONVALESCENT HOME; "124-126-128 130" D. VEN'D; "134" SEARS ROEBUCK & CO. DEPT STORE ... BUILT 1947; SERVICE STA. /
  FILL'G STA. (built 1947). No motorcycle/cycle label anywhere.
  EXTRA (new): sheet 60 E 10th 200 block read at full res (the claim had only an overview): S side 201-203 UPHOLST'G 2ND / AUTO SALES & SERV.,
  AUTO REP. behind; 207 S.; 211 D; 213-215 APTS / S IN B'ST; 217-221 USED CAR SALES (+ rear S.); 225-227 D; 231 D; 233-235 D "FRAME GABLES";
  237-239 APTS; 241 APTS; 245 SEVENTH DAY ADVENTIST CHURCH / SCHOOL ANNEX; 249-257 D. N side 202 S. VEN'D; 206-232 D.; 234 S. (C.B.); 238-240
  APTS; 244 ROOM'G; 248-254 D; 264 BETHANY EVANG'L LUTH'N CHURCH. No motorcycle label.
  CORRECTED: readings right, but the wording 'has no motorcycle shop' should be 'no building LABELED as a motorcycle/cycle shop in Aug 1950';
  several generic stores ("S.") carry no trade (106-108, 114, 114 1/2, 116, 155; 200 block 202, 207, 215, 217-21 rear, 234); a 1950 map says
  nothing about 1920s-30s tenants; and the Goodyear-sold-bicycles detail is Google Books snippet only (not on the map).
  New evidence (composites, labelled): evidence/1950-08_sanborn-erie-v1-sheet59_loc-g3824em_g07660195001_e10th-100-block-both-sides-no-
  motorcycle-label_composite.png ; evidence/1950-08_sanborn-erie-v1-sheet60_loc-g3824em_g07660195001_e10th-200-block-both-sides-no-motorcycle-
  label_composite.png
- Crops opened after reading: #60, #61, #62, #63, #64, #65 all legible. FILE-NAMING ISSUE: #60, #61, #63 crops are stitched (frontage + sheet-
  number inset) and #62, #64 are two-map composites, but none carries the "_composite" suffix required by the rules (#62/#64 at least have
  in-image captions). #63 inset has a grey filler block. Recommend renaming.

## SUMMARY OF VERDICTS
CONFIRMED: 26, 29, 30, 31, 33, 36, 37, 38, 40, 41, 55, 56, 57, 58, 59, 60, 61, 62, 64, 65
CORRECTED: 27 (installed in, not 'run'), 28 (16 yrs with Armour, not as asst mgr; president 'past three years' to Dec 1922), 32/34/39 (BookReader
  /page/nN off by one -> n1283, n1006, n220; 39 issue = No. 64, Sept 1923), 35 ('Beckna' resolution is inference), 63 (1950 frontage blank but
  set-back auto sales buildings behind), 66 (labelled-use negative only; generic stores; snippet detail)
REFUTED: none.  COULD-NOT-CHECK: none.
