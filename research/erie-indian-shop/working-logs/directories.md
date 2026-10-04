# Lane: directories — working log (started 2026-10-04)

Goal: find ANY accessible text of Erie city directories (Atkinson / Polk) 1915-1940; read E 10th / E 11th St;
Bayhurst; Indian Motorcycle Agency; produce manual list for Abe.
Tools: work/tools/gbfeed.py (Google Books GData feed snippets), work/tools/iafts.py (archive.org FTS), curl, WebFetch.
Scratch: lanes/directories/.

## Log

### 1. ldsgenealogy.com index (curl 200) — https://ldsgenealogy.com/PA/Erie-County-City-Directories.htm (saved ldsgen.html/.txt)
- Ancestry "U.S. City Directories, 1822-1995" (collection 2469, https://www.ancestry.com/search/collections/2469/) lists Erie, Pa.
  EVERY year 1861-1943 except 1900/1904 (1915,1916,...,1943 all present), then 1945,1946,1948,... (no 1944, 1947).
- MyHeritage "U.S. City Directories" (collection-10705) Erie City Directory years: 1888,1890,1891,1892,1899,1902,1904,1906,1908,
  1915,1916,1919,1921,1922,1926,1927,1929,1930,1931,1932,1935,1936,1942,1946,1949,1951-53,1955,1957-60.
- Allen County Public Library (Fort Wayne): Erie, PA 1861-1863, 1865-1900, 1901-1935; 1936-1943, 1945-1960 (microfiche/print).
  Wesleyville 1919-1930, 1932-1935; Pennside 1922-1935.
- FamilySearch catalog entries: 541218 "Erie (Pennsylvania) city directories", 148168 "Erie city directory, Erie County, Pennsylvania",
  534727 "Erie County (Pennsylvania) directories".
- LOC phone books: 9/1911-7/1940, 7/1941-7/1947 (already done by loc-phonebooks lane).

### 2. FamilySearch
- WebFetch https://www.familysearch.org/en/search/catalog/541218 -> sign-in page only (catalog now requires login). curl API
  /service/search/catalog/item/541218 -> 401. => BLOCKED (login). Not retried.
- FamilySearch Wiki (public, curl 200) https://www.familysearch.org/en/wiki/Erie_County,_Pennsylvania_Genealogy, section Directories:
  "1936-1940 Erie City Directory, Erie County, Pennsylvania (*) ; at FamilySearch Catalog — index & images" -> catalog 148168.
  So FamilySearch has DIGITAL IMAGES of Erie city directories 1936-1940 (free account needed). Also wiki: Erie County Public Library
  Heritage Room "has city directories for Erie beginning in 1853"; library subscribes to Ancestry Library Edition.

### 3. HathiTrust catalog API (catalog.hathitrust.org/api/volumes/brief/htid/pst.000012006779.json -> 200 without custom UA;
  with UA "Mozilla/5.0" -> 403 Cloudflare). Record 009816870 "Erie directory (Erie County, Pa.)", OCLC 777123351. 7 items:
  pst.000012006779 (pdus, Full view, no enumcron) = GB setXAAAAYAAJ "1939"; pst.000012006762 1873-74 (pd);
  5 "Limited (search-only)" und items = GB 1972 (pst.000045170812), 1973 (pst.000029952809), 1979 (pst.000045169922),
  1983 (pst.000008598660), 1984 (pst.000010091890) [GB editions:PSU000012006779 list]. => no interwar volume besides 1939.

### 4. Google Books GData snippet harvest of the 1939 Atkinson directory (setXAAAAYAAJ, view_no_pages = snippet only, 1430 pages,
  publisher "Atkinson Erie Directory Company"). Raw log: lanes/directories/gb_raw.log, gb_q1..q4.txt
  Date check: Catalog of Copyright Entries 1939/1940 (GB _EXQAAAAMAAJ, ZHhaAAAAIAAJ) snippet: "Atkinson Erie directory com- pany's
  Erie ( Erie County , Pa . ) city directory , 1939 , including Lawrence Park , Wesleyville and Westminster . Aug. 30 , 1939 ;
  A 133135 ; Atkinson Erie directory co . , Erie , Pa ." -> 1939 edition published Aug 30 1939. GB volume title matches.
  Internal consistency: the volume lists "Haft's Garage 124 E 11th"; Haft's Garage first appears at 124 E 11th in the LOC phone book
  Jan 1939 (seq759) (1938 = Erie Brake Service) -> consistent with 1939 edition.
  SNIPPETS (all SNIPPET-LEAD, volume setXAAAAYAAJ):
  a) alphabetical: "Bayhurst Chas A ( Theresa I ) motor- cycles 302 E 11th h 847 E 7th " Edw L ( Ruth ) slsmn Born's Dairy Coh 536
     Shunpike rd " Frank W ( Marie P ) truck driver h 2314 Kilpatrick av Bay'e Anthony Llabr 2716 Pear"  (q 'Bayhurst Kilpatrick')
  b) classified: "Motorcycle Dealers Bayhurst Chas A 302 E 11th Kuivinen H Edw 114 E 11th * Movie Projectors - Supplies and Equipment"
  c) street guide (E 11th): "H German intersects 301-034Studebaker LH Laboratories 302 Bayhurst Chas A motorcycles Longwell Cath 304
     Cioccio Crescenzo gro Preuss Edwin TEL 26-775 305 Grim Alex Upholstery 306-084Stone Arth L Co store fixtures 307 Blum Louis J O"
     and "... Motor- cycle Club 118-204Moorhouse Motor Co ( used car dept ) 1234Tyser Chas E ( filling sta No 2 ) DAVIS 124 Haft's
     Garage auto ... Bayhurst Chas A motorcycles Longwell Cath 304 Cioccio Crescenzo gro"
  d) alphabetical: "Kuivinen H Edw ( Fern ) motorcycles 114 E 11th h 2915 Pine av Kujan Frank Jr 1326 Lynn"
  e) clubs: "Keystone Erie Motorcycle Club 114 E 11th Keystone Gun Club 630 State Lawrence Park Rifle Club 3812 Field ( LP )"
  f) classified: "Bicycle Dealers and Repairers Adams Alf R 744 E 21st Bike Shop The 623 W 26th Hoffman Jos J 362 W 8th Howard's 406
     State Trow Harry D 337 W 18th Billiard Room Supplies"
  g) "Bicycles , 163 E 10th , Tel 23-633" (end of a bold GOODYEAR SERVICE STORES entry: "GOODYEAR SERVICE STORES , Don W Ellison
     Store Mgr , Distributors Goodyear ...") -> a tire/battery store selling bicycles at 163 E 10th in 1939.
  h) classified auto accessories: "... 10th Le Jeal Automotive Service 1721 Sas- safras Miller GJ Auto Supply 2001 ..."
  i) "HART TRESSA AUTO LAUNDRY , Frank J Gangle Mgr ... 150 E 10th , Tel 23-189"

### 5. Other places checked for Erie directory text
- archive.org metadata (title:erie AND title:directory): only 1873 gazetteer, 1881/1883 railway guides, Buffalo/Erie Co NY. No Erie PA
  city directory 1915-1940. iafts: '"Bayhurst" motorcycles', '"Indian Motorcycle Agency" "E 11th"', 'Erie city directory Atkinson 1925',
  '"Atkinson Erie Directory"' -> nothing relevant (raw: ia_raw.log). MISS.
- Google Books title scan (intitle:Erie intitle:directory etc., 5 queries x 2 pages): only scanned Erie city directories are
  1873, 1939 (setXAAAAYAAJ) and 1972+ ; "Erie County Directory 1916" (QHrTHAAACAAJ, OCLC 32428191) = metadata only. MISS for 1915-38.
- Penn State digital collections (CONTENTdm API search 'erie directory'): only "American agriculturalist farm directory ... Erie County
  1918" (digitalbks4/1270, rural). No Erie city directories. MISS.
- theancestorhunt.com free PA directories list: Erie = LOC phone books, DPLA "Erie Directory, 19-" (dp.la item 233fc593...; dp.la
  returned 202 bot-check twice -> blocked; almost certainly the HathiTrust record), HathiTrust 1982-2006 Polk. MISS for 1915-38.
- Masthof "Erie County PA - Directory Collection (1873-1960)" product page: curl 404 x2 (and .json 404). BLOCKED. Search-engine
  snippets say it includes "Atkinson Erie City Directory 1925-1926" and "... Erie City Directory 1937". -> manual.

### 6. Side find (Penn State Behrend "Hammermill Bond" employee magazine, CONTENTdm, full OCR + IIIF images) — query 'bayhurst'
- Vol. VIII No. 12, ERIE, PA., JUNE 1, 1926, p.[7] (behrend item 4173, parent 4183): "WELCOME TO OUR NEW EMPLOYEES" ... "General /
  May 20—Charles Bayhurst". VERIFIED ON IMAGE. evidence/1926-06-01_hammermill-bond_v8n12_p7_new-employee-charles-bayhurst.png
- Vol. XI—No. 11, ERIE, PA., MAY 1, 1929, p.[7] (item 4550, parent 4967): "SERVICE PIN AWARDS ... Three Years ... Charles Bayhurst
  ........May 20". VERIFIED ON IMAGE. evidence/1929-05-01_hammermill-bond_v11n11_p7_service-pin-3yrs-charles-bayhurst.png
- Vol. XI—No. 9, March 1, 1929, p.8 (item 4519) and Vol. XII—No. 9, March 1, 1930, p.[8] (item 4715): lists by department with
  "3 Days / 4 Days / 1 Week / 2 Weeks" groups (heading on an earlier page, probably vacation allowance): "GENERAL ... 4 Days
  Charles Bayhurst Peter Gartner" (1930, viewed on image; 1929 OCR only).
  => A Charles Bayhurst worked at Hammermill Paper Co., Erie (General dept), from May 20, 1926 to at least March 1930.
  Identity with motorcycle dealer Chas A Bayhurst = PLAUSIBLE, not proven (same name, same city).
- 'indian motorcycle', 'harley davidson', 'motorcycles erie' in the same magazine: no dealer items (only employee gossip). MISS.

### 7. 1939 street guide, East 10th 100 block (SNIPPET-LEAD, setXAAAAYAAJ), chained:
  "... FRENCH 1074Buchwald Elmer E 1071⁄2 Allen Martin 108 Martha's Beauty Shoppe 1094Eichler Otto J 1104Blue Ribbon Recrea- tion
  bowling Harden Edna K Mrs 1134Hogue Henry c 114 Heinlein Jacob barber 116 Kosiorek Edw 117-25 Erie Buick Co 118 ..."
  "... Erie Buick Co 118 Garrison Earl E 120 Glassman Jos clo clnr 1224Erne Leah V Mrs 1244St George Louis 1264 Daylight Service Co
  window clnrs Allevato Anthony Horanic Frank J 127-294Klick Harry J furn 128 Harris Margt F 130 Weisman Eliz R ..."
  (stray digit '4' after numbers = OCR of a symbol/phone marker). No motorcycle/bicycle occupant in 107-130 E 10th.
  Further chaining (140-160 block, 200-400 blocks) failed: feed returned other volumes or nothing. 
- People check in 1939 vol: "Shannon ... Lester E ( Florence L ) paper wkr h 1046 E 8th" (1928 H-D captain's namesake);
  Schroeder/Beckman/Furlong/LeJeal personal entries: no snippet returned.
- MyHeritage public names page (myheritage.com/names/charles_bayhurst): curl 403, WebFetch empty -> BLOCKED (2 tries).
- HathiTrust babel full-text search: curl 403 "Just a moment" (Cloudflare) -> BLOCKED (1 try; IP-block known from ACCESS.md).

### 8. Erie Cemetery transcription (interment.net, curl 200)
  https://www.interment.net/data/us/pa/erie/erie-cemetery/records-bau-ben.htm :
  "Bayhurst, Charles Arthur, b. 08/28/1899, d. 11/19/1978, Location: 09, 745, 2"
  "Bayhurst, Theresa I., b. 11/30/1901, d. 12/08/1983, Location: 09, 745, 1"  (same lot -> couple; matches 1939 "Bayhurst Chas A ( Theresa I )")
  "Bayhurst, Lewis J., b. 08/16/1894, d. 09/18/1948, Location: 09, 83"; "Bayhurst, Louis, b. 09/05/1863, d. 10/13/1918, Location: 06, 43, 2";
  "Bayhurst, Louise, b. 10/18/1862, d. 01/20/1916, Location: 06, 43, 1"; "Bayhurst, Donald, b. 12/27/1931, d. 03/15/1933";
  "Bayhurst, William L., b. 04/29/1930, d. 02/04/1933"; "Bayhurst, Elma Hildegarde Fisk, b. 02/17/1897, d. 04/07/1981".
  (secondary transcription of cemetery records; not the register itself)

### 9. Reading the 1939 street-guide notation
  The stray "4" glued to house numbers is OCR of a marker glyph: "1074Buchwald" = 107 Buchwald, "127-294Klick" = 127-29 Klick,
  "301-034Studebaker" = 301-03 Studebaker, "306-084Stone" = 306-08 Stone. So the E 11th snippet reads (interpretation):
  "... [Keystone Erie] Motorcycle Club / 118-20 Moorhouse Motor Co (used car dept) / 123 Tyser Chas E (filling sta No 2) /
  124 Haft's Garage auto ..." and "GERMAN INTERSECTS / 301-03 Studebaker L H Laboratories / 302 Bayhurst Chas A motorcycles,
  Longwell Cath / 304 Cioccio Crescenzo gro, Preuss Edwin / 305 Grim Alex upholstery / 306-08 Stone Arth L Co store fixtures /
  307 Blum Louis J ..."  => in 1939 the 1935-36 Indian address (120 E 11th) was within Moorhouse Motor Co's used-car lot (118-20).
- 1973 directory (GB r5MrAQAAMAAJ, snippet): "847 Bayhurst Charles A 848 Taflinski Barbara A ... PERRY INTERSECTS" -> Charles A
  Bayhurst still at No. 847 (street = E 7th per 1939 h 847 E 7th) in 1973. SNIPPET-LEAD.
- Buffalo NY 1934 Polk street guide has an "Indian Motorcycle Sales" — Buffalo, NOT Erie PA (ignored).

## CONCLUSIONS (directories lane)
1. No 1915-1938 Erie city directory text is reachable from this container: not on Google Books (only 1873, 1939, 1972+ scanned),
   not on archive.org, not at Penn State digital collections; HathiTrust has only 1873 + 1939 (blocked here anyway).
   They exist on Ancestry (every year 1915-1943), MyHeritage (1915,16,19,21,22,26,27,29,30,31,32,35,36), FamilySearch images
   1936-1940 (catalog 148168, login), ACPL Fort Wayne (1901-1943), Erie County Public Library Heritage Room, Masthof CDs (1925-26, 1937).
2. The 1939 Atkinson Erie City Directory (published Aug 30 1939; GB setXAAAAYAAJ = HT pst.000012006779) — snippets (not images):
   - "Bayhurst Chas A ( Theresa I ) motor- cycles 302 E 11th h 847 E 7th"
   - classified "Motorcycle Dealers": only "Bayhurst Chas A 302 E 11th" and "Kuivinen H Edw 114 E 11th"
   - street guide: "302 Bayhurst Chas A motorcycles"
   - "Kuivinen H Edw ( Fern ) motorcycles 114 E 11th h 2915 Pine av" (114 E 11th = the Harley-Davidson Motorcycle Agency address)
   - "Keystone Erie Motorcycle Club 114 E 11th"
   - Bicycle Dealers and Repairers: Adams Alf R 744 E 21st; Bike Shop The 623 W 26th; Hoffman Jos J 362 W 8th; Howard's 406 State;
     Trow Harry D 337 W 18th.  Goodyear Service Stores, 163 E 10th, also lists "Bicycles".
   => Bayhurst's motorcycle shop at 302 E 11th is still listed in Aug 1939, though without a phone listing after July 1937.
   The snippets never name the brand; the Indian link rests on the 1937 phone book (same address & phone as Indian Motorcycle Agency).
3. East 10th Street: in 1939 no motorcycle dealer on E 10th (classified list has 2 dealers, both E 11th); 107-130 E 10th street guide
   has no cycle business; only cycle-related E 10th item = Goodyear Service Stores 163 E 10th selling bicycles (tire/battery store).
4. Owner identity: Charles Arthur Bayhurst, b. 28 Aug 1899, d. 19 Nov 1978, wife Theresa I. (1901-1983), Erie Cemetery sec 09 lot 745
   (interment.net transcription) — matches "Bayhurst Chas A ( Theresa I )". He (or a namesake) worked at Hammermill Paper Co.,
   General dept, from May 20 1926 to at least March 1930 (Hammermill Bond, image-verified) — so the shop was likely NOT a full-time
   1920s business; consistent with it first appearing in the phone book in July 1935.

## MANUAL STEPS FOR ABE (exact URLs / strings)
A. HathiTrust 1939 Atkinson Erie directory (full view, public domain) — confirm snippets on page images, save page PDFs:
   https://babel.hathitrust.org/cgi/pt?id=pst.000012006779
   https://babel.hathitrust.org/cgi/pt/search?q1=Bayhurst&id=pst.000012006779
   https://babel.hathitrust.org/cgi/pt/search?q1=Kuivinen&id=pst.000012006779
   https://babel.hathitrust.org/cgi/pt/search?q1=%22Motorcycle+Dealers%22&id=pst.000012006779
   https://babel.hathitrust.org/cgi/pt/search?q1=%22Keystone+Erie+Motorcycle+Club%22&id=pst.000012006779
   https://babel.hathitrust.org/cgi/pt/search?q1=%22Bicycle+Dealers%22&id=pst.000012006779
   https://babel.hathitrust.org/cgi/pt/search?q1=%22German+intersects%22&id=pst.000012006779  (E 11th & E 10th street-guide pages)
   https://babel.hathitrust.org/cgi/pt/search?q1=%22Indian+Motorcycle%22&id=pst.000012006779
   https://babel.hathitrust.org/cgi/pt/search?q1=%22163+E+10th%22&id=pst.000012006779
   Google Books snippet view of same: https://books.google.com/books?id=setXAAAAYAAJ&q=Bayhurst
B. Ancestry "U.S. City Directories, 1822-1995" https://www.ancestry.com/search/collections/2469/ (Erie PA every year 1915-1943):
   search Last name "Bayhurst", Lived in "Erie, Pennsylvania"; then browse each Erie volume 1919-1941 for:
   alphabetical "Bayhurst" (Chas/Charles A; Lewis J / L J; Frank W; Edw L; Louis); "Indian Motorcycle" / "Indian Motocycle";
   classified "Motorcycles" / "Motorcycle Dealers" / "Bicycles" ; street guide East 10th St 100-400 and East 11th St 100-400
   (esp. 114, 118-20, 120, 124, 151, 302 E 11th). Also "Beckman A D" (1807 Parade, Indian 1922), "Schroeder Chas", "LeJeal",
   "Kuivinen H Edw", "Furlong Walter M" (H-D 1923), "Shannon Lester" (H-D agency 941 E 11th 1928).
C. MyHeritage U.S. City Directories https://www.myheritage.com/research/collection-10705/us-city-directories (Erie 1915, 1916, 1919,
   1921, 1922, 1926, 1927, 1929, 1930, 1931, 1932, 1935, 1936, 1942): same names.
D. FamilySearch (free account): catalog 148168 "Erie city directory, Erie County, Pennsylvania" 1936-1940 images
   https://www.familysearch.org/en/search/catalog/148168 ; also 541218 https://www.familysearch.org/en/search/catalog/541218 ;
   Full-Text search https://www.familysearch.org/search/full-text  query: Bayhurst motorcycles Erie
E. Masthof CDs: https://www.masthof.com/products/erie-county-pa-directory-collection-1873-1960 (1925-26, 1937 Atkinson per descr.)
F. Erie County Public Library Heritage Room (directories from 1853; Erie Times obits): obit Charles A. Bayhurst d. 19 Nov 1978;
   Lewis J. Bayhurst d. 18 Sep 1948; and directory lookups as in B. https://www.erielibrary.org/ (blocked here)
G. ACPL Genealogy Center (Erie 1901-1935, 1936-1943 directories) lookup request: https://www.genealogycenter.info/
H. Hagen History Center library & archives: https://www.hagenhistory.org/research
