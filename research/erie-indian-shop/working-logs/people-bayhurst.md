# Lane: people-bayhurst — working log (started 2026-10-04)

Goal: life of Charles Bayhurst (Erie Indian agency 302 E 11th, July 1937), related Bayhursts (L. J., Frank W., Lewis, Edna),
and who ran Indian Motorcycle Agency at 120 E 11th 1935-36.
Tools: work/tools/iafts.py, work/tools/gbfeed.py, WebSearch, curl. Scratch: lanes/people-bayhurst/.

## Log
### 1. archive.org FTS (tools/iafts.py)
- '"Charles Bayhurst"' -> 0. '"Chas. Bayhurst"' -> 1 (Toronto 1947 dir, irrelevant). '"Bayhurst" motorcycle' -> error/none.
- '"L. J. Bayhurst"' -> 1: sim_american-rifleman_1927-11_75_11. '"Lewis Bayhurst"' 0. '"Frank Bayhurst"' 0.
- 'Bayhurst Erie' -> 593 hits, mostly Sask. gas co. noise; Erie yearbooks: 1943 Erie Tech (Charles Bayhurst, trade cert.), Oil City 1949,
  Cathedral Prep 1984/85, Wattsburg 1970 (later, not used; living people - not collected).

### 2. American Rifleman Nov 1927 (VERIFIED ON IMAGE)
- ID sim_american-rifleman_1927-11_75_11, leaf 27 (0-based, /page/n27.jpg 3240x4288), printed p.26 / cumulative p.542, Vol LXXV No 11.
- Col 1 "LADIES' TEAMS TAKE NOTICE": "THE women's team of the Lawrence Park Rifle Club, at Erie, Pa., would like the world to know..."
  col 2: "Communications should be addressed to Mr. L. J. Bayhurst, 151 East 11th Street, Erie, Pa."
- "OPEN CHALLENGE FROM LAWRENCE PARK": "THE Lawrence Park Rifle Club, Erie, Pa., challenges any rifle club in the United States to a
  pistal match ... Communications should be addressed to the team captain, Mr. L. J. Bayhurst, 151 E. 11th Street, Erie, Pa."
- Evidence: evidence/1927-11_american-rifleman_p26-542_leaf27_lj-bayhurst-lawrence-park.png
- Viewer: https://archive.org/details/sim_american-rifleman_1927-11_75_11/page/n27

### 3. interment.net Erie Cemetery + Laurel Hill transcriptions (curl 200, text)
URL https://www.interment.net/data/us/pa/erie/erie-cemetery/records-bau-ben.htm  (Erie Cemetery, "Surnames Bau-Ben"):
  "Bayhurst, Charles Arthur, b. 08/28/1899, d. 11/19/1978, Location: 09, 745, 2"
  "Bayhurst, Donald, b. 12/27/1931, d. 03/15/1933, Location: NN, 2, 55"
  "Bayhurst, Elma Hildegarde Fisk, b. 02/17/1897, d. 04/07/1981, Location: 07, 104C, 3"
  "Bayhurst, Lewis J., b. 08/16/1894, d. 09/18/1948, Location: 09, 83"
  "Bayhurst, Louis, b. 09/05/1863, d. 10/13/1918, Location: 06, 43, 2"
  "Bayhurst, Louise, b. 10/18/1862, d. 01/20/1916, Location: 06, 43, 1"
  "Bayhurst, Theresa I., b. 11/30/1901, d. 12/08/1983, Location: 09, 745, 1"
  "Bayhurst, William L., b. 04/29/1930, d. 02/04/1933, Location: NN, 2, 56"
URL https://interment.net/data/us/pa/erie/laurel-hill-cemetery/records-ba-bh.htm (Laurel Hill):
  "Bayhurst, Dorothy W., b. 01/12/1927, d. 07/20/1986, Location: 07, 45A, 1"; "Bayhurst, Edward L., b. 11/12/1897, d. 10/21/1981,
  Location: 07, 45A, 4"; "Bayhurst, Ruth B., b. 01/02/1898, d. 10/02/1987, Location: 07, 45A, 3"; Leigh Anne Victoria 1988 (modern).
Interpretation (NOT proven): Charles Arthur (1899-1978) and Theresa I. (1901-1983) share lot 09-745 -> probably husband & wife.
Louis (1863-1918) & Louise (1862-1916) share lot 06-43 -> probably a couple, possible parents of Lewis J./Charles/Edward. UNPROVEN.

### 4. American Rifleman April 1929 (VERIFIED ON IMAGE)
- ID sim_american-rifleman_1929-04_77_4, leaf 23 (page/n23.jpg 3168x4248), printed p.22, header "April, 1929".
- "LAWRENCE PARK HOLDS NOVELTY SHOOT / WHEN the Lawrence Park Pistol Team, of Erie, Pa., recently challenged the rifle teams of the same
  club to a match..." Table "LAWRENCE PARK BUDDIES": "E. Bayhurst.......... 36 43 40 36 41 196" ... "L. Bayhurst......... 34 43 45 43 38 203"
  (also Loder, F. Hedderich, W. Hedderich; total 994).
- Evidence: evidence/1929-04_american-rifleman_p22_leaf23_lawrence-park-buddies-e-l-bayhurst.png
- Viewer: https://archive.org/details/sim_american-rifleman_1929-04_77_4/page/n23
- Note: "E. Bayhurst" could be Edward L. Bayhurst (b.1897, Laurel Hill) - NOT proven. No "C. Bayhurst" on the team.

### 5. Google Books feed (snippets = LEADS)
- "Bayhurst" "Erie, Pa": The Tailor 1907 (sHUyAQAAMAAJ) "Erie, Pa.-G. M. Loeslein, G. Bayhurst, Jno. F. Bal- ter, A. Schwab."
  Iron Molders' Journal 1904 (mOlJAQAAMAAJ / JKSfAAAAMAAJ): Erie local list "... Bayhurst 37388, W. Beck 44784 ..." (initial cut off).
  Messenger of the Precious Blood 1932 (rcchbGwWz_EC): "Erie, Pa.: Matilda Bayhurst." Fiery Cross 1931 (8AGvnJnPsJUC) Erie lodge
  "...Bayhurst and Christie are all recovering." American Rifleman 1929 (R9-wHA-d71AC) = same as IA 1929-04 item (verified above).
  1917 Pa. Motor Vehicle Registrations (CxRbAAAAYAAJ): "Chas. ... Bayhurst, R. F. D. No. 5, Erie." (snippet).
- 'Bayhurst Indian motorcycle' -> 0 relevant. '"Charles A. Bayhurst"' / '"C. A. Bayhurst"' -> only modern/scientific noise.
- Modern Polk directories (1984-2006) list later Bayhursts - living people, NOT collected.

### 6. NARA 1950 census (https://1950census.archives.gov/) — API WORKS from this container
- JS bundle main.31db9cc9.chunk.js exposes /api/search, /api/manifest, /api/county, /api/state. Plain curl works (200, JSON).
- Query: https://1950census.archives.gov/api/search?name=Bayhurst&state=PA&size=50  (county=Erie filter alone only returns Erie
  COUNTY rural EDs 25-x; Erie CITY is county "Erie, Erie", EDs 72-x). Name index = machine handwriting recognition (garbled).
- Erie hits: 5306548 ED 72-20 img 43290879-Pennsylvania-140252-0036 rows: (11,'Bayhurat Ohanleoll'),(12,'Theresa I'),(13,'Charles W')
             5310141 ED 72-150 img 140382-0005 'Bayhurat Elma';  5310139 ED 72-147 img 140379-0013 'Bayhunat Edwas';
             5069061 ED 25-33 'Bayhurat Phillip'; 5070888 ED 25-77 'Bayhurst thomas'.
- VIEWED IMAGE ED 72-20 (IIIF https://1950census.archives.gov/iiif/2/1950census%2F43290879-Pennsylvania%2F43290879-Pennsylvania-140252%2F43290879-Pennsylvania-140252-0036.jpg/full/2145,/0/default.jpg
  + full-res regions). Header: Pennsylvania / Erie / Erie / E.D. 72-20 / date April 17 [1950] / enumerator Mary A. Crotty / Sheet 14.
  Street in margin "East 7 St".
  L11: "847 | 247 | no | no | Bayhurst, Charles A | Head | W | M | 50 | Mar | Pa | wk | 40 | Floor Hand Machine Shop | Forge & Steel Mfg | P | 690 337 1"
  L12: ", Theresa I | Wife | W | F | 47 | Mar | Pa | H | no no no"
  L13: ", Charles W | Son | W | M | 22 | Nev | Pa | wk | 40 | Cabinet Maker | Burial Case Mfg | P | 505 399 1"
  L14: "Stewart, John H | Uncle in Law | W | M | 68 | Nev | Pa | U"
  (Right half of sheet is skewed ~1 row upward; occupation rows aligned via printed right-margin line numbers 11 and 13.)
- Evidence: evidence/1950-04_census-ed72-20-sheet14_img140252-0036_bayhurst-847-e7th.png
- Viewer for Abe: https://1950census.archives.gov/search/?county=Erie%2C%20Erie&ed=72-20&name=Bayhurst&page=1&size=25&state=PA
  (or search name "Bayhurst" state PA, open ED 72-20 image 36 / sheet 14).
LINKS (reasoned): age 50 in Apr 1950 fits Erie Cemetery "Charles Arthur, b. 08/28/1899"; wife Theresa I. = cemetery "Theresa I."
 in same lot 09-745; 847 E 7th = phone book "Bayhurst Charles r 847 E 7th st" 1941-47. => Charles A. (Arthur) Bayhurst 1899-1978 is the
 847 E 7th St man. Link to 1937 "Bayhurst Charles motorcycles 302 E 11th st" = same name/city only (no Charles Bayhurst other than this
 one appears in the 1934-47 phone books) -> PROBABLE, not proven.

### 7. NARA catalog (catalog.archives.gov) — /proxy/records/search WORKS by curl (no key)
- https://catalog.archives.gov/proxy/records/search?q=Bayhurst&limit=50&page=1..3 -> 115 hits (saved nara_s_*.json).
- KEY: file unit 359321727 "Baxter, Charles - Baylor, Howard (2 of 2)", series "Draft Registration Cards for Pennsylvania" (RG 147,
  WWII, men b. 17 Feb 1897-31 Dec 1921). Object descriptions (Ancestry index) list Bayhurst cards 01413-01433.
  Catalog page for Abe: https://catalog.archives.gov/id/359321727 (objects 412-431 of 895).
- VIEWED IMAGE 44033_05_00028-01413.tif (front) / -01414.tif (back):
  https://catalog.archives.gov/medialz/partners/st-louis/rg-147/5324575/44033_05_00028/44033_05_00028-01413.tif
  "REGISTRATION CARD—(Men born on or after February 17, 1897 and on or before December 31, 1921)" SERIAL "T 293" ORDER "T10070"
  "1. NAME: Charles Arthur Bayhurst" / "2. PLACE OF RESIDENCE: 847 E. Seventh  Erie  Erie  Pa" / "3. MAILING ADDRESS Same" /
  "4. TELEPHONE" (blank) / "5. AGE IN YEARS 42" / "DATE OF BIRTH Aug. 28 1899" / "6. PLACE OF BIRTH Erie Pa" /
  "7. ... PERSON WHO WILL ALWAYS KNOW YOUR ADDRESS: Mrs. Theresa Bayhurst 847 E. Seventh St." /
  "8. EMPLOYER'S NAME AND ADDRESS: Erie Forge and Steel" / "9. PLACE OF EMPLOYMENT OR BUSINESS: 16th Cranberry Erie Erie Pa." /
  signature "Charles Bayhurst". Back: White; 5 7; 150; Hazel; Brown; Light; "Mark on the right foot"; registrar Cecelia J. Rybinski;
  "Registrar for Local Board 1 Erie Pa."; "Date of registration Feb. 16, 1942"; stamp "LOCAL BOARD NO. 1 CITY OF ERIE".
  Evidence: evidence/1942-02-16_nara-wwii-draft-card-pa_44033_05_00028-01413_charles-arthur-bayhurst-front.png (+ -01414 ...-back.png)
- VIEWED 01419 (Edward Leo Bayhurst, T 622/T11748, 536 Shunpike, tel "92-544 Erie", age 43, b. "Nov 12 1898" Erie Pa, contact
  "Mrs. Edward L. Bayhurst 536 Shunpike", employer "Erie Forge and Steel", place "Erie Forge and Steel 15th? Cranberry St. Erie Pa").
  VIEWED 01421 (Frank William Bayhurst, T 515/T11949, "2314 Kilpatrick Ave Erie", tel "Erie 54274", age 40, b. "Sept 2 1901" Erie Pa,
  contact "George Miller 441 West 31 St Erie Pa", employer "W. J. Bridger RD4 Erie Pa", place "Bridger Dairy").
  Evidence: evidence/1942-02-16_nara-wwii-draft-cards-pa_44033_05_00028-01419-01421_edward-leo-and-frank-william-bayhurst.jpg
- Index-only (not viewed): 01415 Charles William Bayhurst b. 1927 Sep 30, reg. 1945, "Father Name: Bayhurst, Charles Arthur";
  01429 Theodore Louis b. 1925 May 7, "Father Name: Bayhurst, Louis John"; 01427 Richard Junior b. 1924, father Edward;
  01423 Joseph August b. 1902 Oil City; 01425 Joseph Philip b. 1922, father Philip; 01433 Thomas Ralph 1923; 01417 Edward George 1926.
- 1910 census index (catalog scopeAndContentNote) + VIEWED IMAGE: T624 roll 1343 image 0556, Pennsylvania: ERIE County, ED 124
  (Mill Creek Township, 3d District), Sheet 8B, enumerated "4 day of May 1910" by James S. Taylor:
  L72 "194 | 202 | Bayhurst Louis | Head | M W 46 M1 22 | France French | France French | France French | 188? al. | English | Farmer"
  L73 "Louise | Wife | F W 47 M1 22 6 5 | Ger. German ..." ; L74 "Louis Jr. | Son | M W 15 S | Pennsylvania ... | Farm Laborer";
  L75 "Edward | Son | M W 12 S"; L76 "Charley | Son | M W 10 S"; L77 "Frank | Son | M W 8 S"; L78 "Rosa | Daughter | F W 6 S".
  URL https://catalog.archives.gov/medialz/microfilm-publications/T624-1910_Census/0001/T624_1343/T624_1343/images/0556.jpg
  catalog id 91401242. Evidence: evidence/1910-05-04_census-millcreek-ed124-sheet8B_T624-1343-img0556_bayhurst-family.png
  => FAMILY (strong): Louis (b. c1864 France, farmer; cemetery Louis 1863-1918) & Louise (b. c1863 Germany; cemetery 1862-1916);
     sons Louis Jr. (c1895 = Lewis J. 1894-1948 = "L. J." rifle captain, probable), Edward (c1898 = Edward Leo b. 12 Nov 1898 card /
     cemetery says 1897 - CONFLICT), Charley (c1900 = Charles Arthur b. 28 Aug 1899), Frank (c1902 = Frank William b. 2 Sep 1901), Rosa.
- Other 1910 Bayhursts (index only): ED 106 Erie city sheet 13B dwelling 272 Philip (42, Germany), Mathilda, Philip (13), Joseph (8)
  [= Messenger of Precious Blood "Matilda Bayhurst" 1932; Joseph August b.1902]; ED 87 sheet 6B Anna Bayhurst 17 (servant in Blake hh).

### 8. Family separation (who is who)
- Obituary of Mary E. Bayhurst Covey (d. 10 Feb 2015), https://www.burtonquinnscott.com/obituaries/mary-covey (curl 200, text):
  "She was born on July 8, 1923 in Erie, Pa to the late Lewis J. and Elma H. Fisk Bayhurst." ... "preceded in death by ...
  brothers, Ray, Ted, David, Larry, William, Donald, and James Bayhurst" (living survivors NOT recorded here).
  => Lewis J. Bayhurst (1894-1948) m. Elma H. Fisk (1897-1981). Children William L. (1930-1933) & Donald (1931-1933) in Erie Cemetery
     section NN are LEWIS J.'s sons (names match obituary), NOT Charles's. "Ted" = Theodore Louis b. 1925 whose draft index gives
     father "Bayhurst, Louis John" => Lewis J. = Louis John = 1910 "Louis Jr." (b. c1895). L. J. Bayhurst of the rifle club = Lewis J.
     (probable: initials, Erie, era; rifle club address 151 E 11th 1927 not otherwise tied to him).
- 1950 census ED 72-150 (img 140382-0005, viewed small): L10 "Bayhurst, Elma H | Head | W F 53 Wd Pa | H" with her children (names omitted here:
  possibly living people) -> widow of Lewis J. (consistent).
- Warren Times Mirror 1951-12-11 (IA FTS snippet): "...Richard Fisk, Union City; Mrs. Alma [Elma] Bayhurst, Miss Helen Bayhurst..." (Fisk family).
- 1943 Erie Technical HS yearbook (IA classmates-yearbook-53401..., text only, 53401_djvu.txt): "PATTERN MAKING--THOMAS B. MCGRAW,
  Instructor / Morning Session / ... Bayhurst, Charles; ..." and "10-1 Grade ... Bayhurst, Charles; ..." => the SON Charles W.
  (b. 30 Sep 1927; 1950 cabinet maker), not the motorcycle dealer.
- Academy HS yearbook 1939 (academe1939acad): "Bayhurst, Edna — Certified Public Accountant — Make-Up" (Edna, prob. Edward's daughter;
  1943 phone "Bayhurst Edna Miss r 530 Shunpike rd 92-544" shares phone 92-544 with Edward Leo's 1942 draft card at 536 Shunpike).
- Other Erie Bayhurst line (separate family, do not merge): Philip (b. c1868 Germany) & Mathilda; sons Philip (c1897) and Joseph
  August (b. 1902, Oil City by 1942); grandsons Joseph Philip & Thomas Ralph (Greene Twp). 1907 "G. Bayhurst" tailor (The Tailor) and
  1904 Iron Molders' Erie local "...Bayhurst 37388" = unknown, unlinked.

### 9. 1939 Polk Erie City Directory (Google Books setXAAAAYAAJ = HathiTrust pst.000012006779) — SNIPPET LEADS (gbfeed), NOT YET SEEN ON IMAGE
- '"Bayhurst Chas A" Theresa' -> "... Bayhurst Chas A ( Theresa I ) motor- cycles 302 E 11th h 847 E 7th " Edw L ( Ruth ) slsmn Born's Dairy
  Co h 536 Shunpike rd " Frank W ( Marie P ) truck driver h 2314 Kilpatrick av Bay'e Anthony L labr 2716 Pear ..."
- '"Motorcycle Dealers" Kuivinen' -> classified: "... Motorcycle Dealers Bayhurst Chas A 302 E 11th Kuivinen H Edw 114 E 11th * Movie Projectors ..."
- '"Bayhurst Chas A"' -> street guide: "... Bayhurst Chas A motorcycles Longwell Cath 304 Cioccio Crescenzo gro Preuss Edwin TEL 26-775 305 Grim Alex
  Upholstery 306-084Stone Arth L Co store fixtures 307 Blum Louis J ..." (house nos. run 302?,304,305,306,307 -> E 11th St block)
- 'Kuivinen "114 E 11th"' -> "Kuivinen H Edw ( Fern ) motorcycles 114 E 11th h 2915 Pine av" (Harley-Davidson shop operator 1939, lead)
=> If confirmed on the page: proves motorcycle dealer Charles = Charles A. (wife Theresa I.) of 847 E 7th, i.e. Charles Arthur 1899-1978,
   and shows the 302 E 11th business still listed in the 1939 directory (phone book July 1938 already lacks Indian -> timing conflict,
   directories are canvassed months before issue; keep both).
- GB classic search-inside -> 302 to google.com/sorry (CAPTCHA) => blocked; googleapis 429. HathiTrust blocked.

### 10. 1940 CENSUS FOUND (VERIFIED ON IMAGE) — via Steve Morse One-Step ED finder + NARA media server
- stevemorse.org/census/unified.php?year=1940&state=PA&city=ER&street1=7th&street2=Reed -> 68-16, 68-18; 7th x East Ave -> 68-18, 68-20.
  unifiedstreets2.php?...ed=68-18 -> "Streets in 1940 ED 68-18 in Erie, PA 6th 7th 8th East Ave Perry Reed Rosedale Wayne".
  getxml.php?state=PA&ed=68-18 -> images T627 roll 03647, 00376-00405.
- Image URL pattern (works by curl): https://catalog.archives.gov/medialz/census-1940/T627/PA/m-t0627-03647/m-t0627-03647-00396.jpg
  Paged 00376-00399 via name-column montages (human pace, 3 s).
- FOUND: image 00396 = Sheet 11 A, E.D. 68-18, Ward 1, Block 120, enumerated "April 16, 1940", enumerator Sophie A. Rosinski(?),
  street margin "East Seventh Street":
  L23 "847 | 230 | O | 2000 | No | Murphy, Rachael (x) | Head | F | W | ?? | Wd | No | ..." (informant mark)
  L24 "Bayhurst, Charles | Son-in-law | M | W | 40 | M | No | 8 | Pennsylvania | Same house | no | no | yes | - | - | [40] |
       mechanic | motorcycle repair shop | OA | 336 85 4 | 52 | 0 | yes"
  L25 ", Theresa | Daughter | F | W | 36(or 38) | M | No | 8 | Pennsylvania | Same house | no no no no H | 0 0 no"
  L26 ", Charles | Grandson | M | W | 12 | S | Yes | 6 | Pennsylvania | Same house"
  L27 "Stewart, John | Brother | M | W | 5? | S ..." (Rachael's brother = the 1950 "uncle in law" John H. Stewart)
  Column meanings: 21 at work? no; 22 emergency work? no; 23 SEEKING WORK? yes; 26/27 "40" written at the col-26/27 boundary
  (hours worked vs. weeks unemployed - ambiguous); 28 OCCUPATION "mechanic"; 29 INDUSTRY "motorcycle repair shop"; 30 CLASS "OA"
  (= working on own account); 31 weeks worked 1939 "52"; 32 wages 1939 "0"; 33 other income $50+ "yes".
  1935 residence (col 17) "Same house" => lived at 847 E 7th St on 1 April 1935.
- Evidence: evidence/1940-04-16_census-erie-ed68-18-sheet11A_T627-3647-img00396_bayhurst-847-e7th-motorcycle-repair.png
- Viewer for Abe: https://catalog.archives.gov/ (1940 Census Population Schedules - Pennsylvania - Erie County - ED 68-18, image 21 of 30)
  or FamilySearch 1940 census index "Charles Bayhurst" Erie.
- INTERPRETATION: In 1939 Charles worked all year (52 wks) as a self-employed ("OA") mechanic in a motorcycle repair shop, i.e. his own
  shop; by the census week (24-30 March 1940) he was seeking work. Theresa's maiden name = Murphy (daughter of Rachael Murphy).

### 11. 1930 CENSUS FOUND (VERIFIED ON IMAGE) — archive.org microfilm T626 roll 2035
- Steve Morse 1930: 7th x Reed / 7th x East Ave -> many EDs; unifiedstreets2.php year=1930 ED 25-25 -> "4th E 5th E 6th E 7th E 8th E
  Alane Rd Amber Ct East Ave Perry Reed Rosedale Ave Wayne". 1930reels/pa.js -> ED 25-15..37 on roll 2035; links1930.js ->
  archive.org item fifteenthcensus00reel2035 ("Reel 2035 - ... Erie, Erie City EDs 25-15 to 25-37", 1086 leaves).
- Images via https://ia800601.us.archive.org/BookReader/BookReaderImages.php?zip=/26/items/fifteenthcensus00reel2035/fifteenthcensus00reel2035_jp2.zip&file=fifteenthcensus00reel2035_jp2/fifteenthcensus00reel2035_0803.jp2&id=fifteenthcensus00reel2035&scale=1&rotate=0
  (IIIF 404s for this item). Header sampling: leaf 650 = 25-19 sh 18A; 806 = "25/25" sh 16A (enum. Mrs Rose McLeod); 812 = 25/26 sh 1A.
- FOUND leaf 0803 (0-based jp2 index) = Sheet 14 B, E.D. "25-2[5]" (faint; adjacent sheet 16A reads 25/25), Erie city, Ward "1st pt",
  "Enumerated by me on April 12, 1930, Mrs Rose McLeod". Street margin "East Seventh Street". Viewer:
  https://archive.org/details/fifteenthcensus00reel2035/page/n803
  L82 "847 | 307 | 335 | Murphy, Patrick | Head | O | 3,20[0] | R | No | M | W | 60 | M | 30 | No | Yes | Pennsylvania"
  L83 "Rachel | Wife-H | F W 59 M 29 | Pennsylvania"
  L84 "Bayhurst, Theresa | Daughter | F W 28 M 21 | Pennsylvania"
  L85 "Charles | Son-in-law | M W 30 M 23 | No | Yes | Pennsylvania | France | Germany | 58 12 0 | yes | Owner | Bicycle[s] | 9791 | O | yes | no"
  L86 "Stewart, John | Brother-in-law | M W 40 S | Pennsylvania | Scotland | Scotland | 58 01 0 | yes | Laborer | Paper Mill | 7847 | W"
  ALIGNMENT NOTE: the right-hand columns on this sheet are written ~1 printed line below the names (skew/enumerator drift; the right-edge
  printed number beside "Owner" is 86). Assignment of "Owner / Bicycle[s] / O" to Charles is fixed by the same-row parent-birthplace code
  "12" and the birthplace entries "France | Germany", which fit only Charles (1910: father Louis b. France, mother Louise b. Germany);
  the same logic puts "Laborer / Paper Mill" on Patrick (code 04, Irish Free State parents) and John Stewart (code 01, Scotland).
  Age at first marriage 23 => Charles married c.1922-23. Son Charles W. (b. Sep 1927) NOT listed in this household on this sheet.
- Evidence: evidence/1930-04-12_census-erie-ed25-25-sheet14B_T626-2035-leaf0803_murphy-bayhurst-847-e7th-owner-bicycles.png
- INTERPRETATION: April 1930 Charles Bayhurst was a self-employed OWNER of a bicycle business (industry word reads "Bicycle[s]"),
  living at 847 E 7th St with his in-laws. Business address NOT given by the census.

### 12. Misc checks
- Confirmed by eye the loc-phonebooks lane crops: evidence/1937-07_loc-erie-phonebook-white_seq542.png ("Bayhurst Charles motorcycles
  302 E 11th st..48-385", page header "16 BARBER ERIE") and evidence/1943-07_loc-erie-phonebook-white_reel07590_seq256.png
  ("Bayhurst Charles r 847 E 7th st.....50-232").
- LOC OCR grep: phone 69-312 appears ONLY on "Indian Motorcycle Agency 120 E 11th" lines (1935-36); 48-385 only on 1937 Bayhurst/Indian
  lines. Neighbours at 118 E 11th (Standard Sales & Service Garage 69-212; East Eleventh St Garage 69-412) and 124 E 11th (Fuessler Motor
  Sales 69-113). No Bayhurst in any 1934-40 yellow-pages Bicycles heading (only Joseph J Hoffman 362 W 8th; Marsh Hardware 416 Lake, Corry).
- GB: 302 East 11th St was a plumber's address earlier: Engineering Directory 1918 (2DM8AQAAMAAJ) "... 302 East 11th st." and Domestic
  Engineering 1922 (kjmVaB8Mz1wC) "Arthur E. Meyers, 302 East 11th" (snippets, premises history only).
- American Rifleman "1926" GB volume jn__q2T1UBoC snippet text is IDENTICAL to the Nov 1927 IA issue ("Bayhurst, 151 East 11th Street,
  Erie, Pa. OPEN CHALLENGE FROM LAWRENCE PARK ...") => same item; GB volume date is unreliable; the dated issue is Nov 1927 (verified).
- Chronicling America search "Bayhurst" (WebFetch loc.gov JSON): 20 hits, none Erie. Erie Dispatch-Herald 1925-57 NOT digitized on LOC.
- FamilySearch: search URL 307 -> /en/search..., API 401 (login) -> manual. findagrave 403 (per ACCESS). rootsweb paerie 403.
  sortedbyname 403. eriecemetery.discovereverafter.com = Cloudflare challenge (not attempted further). legacy.com/other obits: only modern.
- NARA catalog /proxy/records/search worked for ~10 requests, then began returning the HTML shell (blocked/throttled) on every
  query (tried 4+ times over ~20 min) -> logged PARTIAL/blocked; media server (catalog.archives.gov/medialz/...) kept working.
- Lewis J. 1940: checked 1940 ED 68-122 (W 25th St, images T627-3651-00585..00588): 129 W 25th = Flanagan(?)/Kennedy household,
  no Bayhurst -> Lewis not at 129 W 25th in April 1940 (he is listed there in 1941-43 phone books). Not pursued further.

## CONCLUSIONS (people-bayhurst)
1. The Erie motorcycle man is CHARLES ARTHUR BAYHURST, b. 28 Aug 1899 Erie (WWII draft card; cemetery), d. 19 Nov 1978 (cemetery
   transcription), buried Erie Cemetery Sec 09 Lot 745 Gr 2 beside wife THERESA I. (née Murphy, b. 30 Nov 1901, d. 8 Dec 1983, Gr 1).
   Son Charles William b. 30 Sep 1927 (draft index; 1940/1950 census; 1943 Erie Tech pattern-making).
2. Parents: Louis Bayhurst (b. c1863/64 France, farmer, Mill Creek Twp; d. 13 Oct 1918) & Louise (b. c1862/63 Germany; d. 20 Jan 1916).
   Brothers: Louis Jr./Lewis J. (1894-1948; = "L. J." Lawrence Park rifle team captain 1927, probable), Edward Leo (b. 12 Nov 1898
   [card] / 1897 [cemetery] CONFLICT; d. 1981), Frank William (b. 2 Sep 1901); sister Rosa (b. c1904).
3. Occupations: 1917 "Chas. Bayhurst, R.F.D. No. 5, Erie" in Pa. motor-vehicle list (snippet); July 1919 motorcycle race winner (snippet);
   1930 census OWNER, industry "Bicycle[s]", own account (O); July 1937 phone "Bayhurst Charles motorcycles 302 E 11th st 48-385" = Indian
   Motorcycle Agency same address/phone; 1939 Polk directory (snippet) "Bayhurst Chas A (Theresa I) motorcycles 302 E 11th h 847 E 7th" and
   classified "Motorcycle Dealers Bayhurst Chas A 302 E 11th"; 1940 census mechanic, "motorcycle repair shop", own account (OA), 52 weeks
   worked in 1939, but seeking work in March 1940; 1942 draft card employer Erie Forge and Steel (16th & Cranberry); 1950 census floor hand,
   machine shop, forge & steel mfg.
4. Residence 847 East 7th St from at least April 1930 (in-laws Patrick & Rachel Murphy's owned house) through 1950.
5. 120 E 11th (1935-36) operator: NOT NAMED in any source found. Circumstantial: Charles was in the cycle trade 1930 and motorcycles 1937-39
   and lived in Erie throughout (1940 census "same house" 1935). Treat "same man" as PLAUSIBLE, UNPROVEN.
6. No Bayhurst/East 10th Street connection found in this lane.

### 13. CONFLICT CHECK: 1930 census vs Hammermill Bond (directories lane)
- directories lane (Penn State Behrend CONTENTdm, image-verified there): Hammermill Bond 1 Jun 1926 "General / May 20—Charles Bayhurst"
  (new employee); 1 May 1929 3-year service pin "Charles Bayhurst ....May 20"; 1 Mar 1930 vacation-type list "GENERAL ... 4 Days Charles
  Bayhurst". I re-viewed nothing of theirs except file names.
- Re-checked the 1930 sheet alignment: right-side code column sequence (col 22) reads, row by row, 58 | 58 04 0 | 58 01 0 | 58 | 58 12 0 |
  58 01 0 | 56 | 14 14 v. Mapped onto persons by content: Alice Pherrin (PA parents, prev. household) 58; Patrick Murphy (Irish Free
  State parents) 04; Rachel (Scotland parents) 01; Theresa (PA parents) 58; Charles (father France) 12; John Stewart (Scotland, Rachel's
  brother) 01; next head (born New York) 56; next person (born Poland) 14. The occupation entries sit on the same rows as these codes:
  Patrick = "Laborer | Paper Mill | 7847 | W"; Rachel "None"; Theresa "None"; CHARLES = "Owner | Bicycle[s] | 9791 | O";
  John = "Laborer | Paper Mill | 7847 | W". High-zoom of the industry word: "B[i]cycle s" -> read "Bicycles" (probable, not certain).
- So: Hammermill (paper mill) employee lists to 1 Mar 1930 vs census 12 Apr 1930 "Owner, Bicycles, own account". Both primary.
  Possible readings: he left Hammermill in spring 1930 to run a bicycle business; or he had a side business reported by the household
  informant; note his father-in-law and John Stewart were paper-mill laborers (perhaps Hammermill too). KEEP BOTH; neither overrides.
