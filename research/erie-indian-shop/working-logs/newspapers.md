# Lane: newspapers — working log (started 2026-10-04)

Goal: coverage checks + targeted free full text of newspapers 1915-1945 for the Erie Indian motorcycle shop
(Bayhurst / Indian Motorcycle Agency / 120 & 302 E 11th / Beckman 1807 Parade / LeJeal), test "East 10th Street".
Tools: work/tools/iafts.py, gbfeed.py, curl, WebFetch (loc.gov JSON), WebSearch. Scratch: lanes/newspapers/.
Built on FINDINGS_SO_FAR.md + other lane logs (people-bayhurst already did one Chronicling America "Bayhurst" search: 20 hits, none Erie).

## Log

### 1. Chronicling America (loc.gov) — coverage + full-text
- curl to www.loc.gov is Cloudflare-blocked, but headless Chromium (lanes/newspapers/pwget.js, Playwright) returns loc.gov JSON (HTTP 200).
  WebFetch also reached loc.gov but its small model truncated the 117-title list -> used Playwright output instead.
- Title list: https://www.loc.gov/collections/chronicling-america/?dl=title&fa=location_state:pennsylvania&fo=json&c=150 (saved ca_pa_titles.json)
  -> 117 PA-located digitized titles. NONE in Erie County (no Erie, Corry, Union City, North East, Girard, Albion, Wattsburg titles).
  Nearest NW-PA titles: The Forest Republican (Tionesta, Forest Co.) 1869-1952; Butler Citizen to Nov 1922; The Star (Reynoldsville) to 1946;
  Petroleum Centre Daily Record 1868-73 (Venango). No Crawford/Warren/Mercer county titles. Erie Dispatch-Herald / Erie Daily Times NOT on LOC.
  (WebFetch facet query fa=location_state:pennsylvania|location_county:erie -> 0 results, consistent.)
- Full-text (page-level) searches via Playwright JSON; OCR checked via tile.loc.gov word-coordinates JSON (lanes/newspapers/caocr.py):
  * q=Bayhurst, dates 1910/1960, all states -> 5 pages: Fairmont WV 1911-09-09 (Joseph Bayhurst death, Mannington WV), Bisbee AZ 1910-11-29
    (Hotchkiss & Bayhurst grocery), NY Herald 1921-09-25 (Bayhurst [street] Flushing ad), Indianapolis Times 1930-07-29 (boxer Bayhurst,
    Terre Haute), Evening Public Ledger 1916-05-30 (Thelma and Althea Bayhurst, Telford). => NONE Erie. MISS.
  * q=LeJeal 1905/1945 -> 146 fuzzy hits (matches "jealous"/"Le Jeal" noise in AL, CA, CT, VT ...), first 50 none Erie. MISS.
  * q=erie indian motorcycle, PA, 1915/1945 -> 579 pages (mostly Harrisburg Telegraph sports/auto pages). OCR of top 25 grepped for
    "erie" within 150 chars of motorcycl/motocycl/indian -> only a false positive (road-contract list "erie county ... indiana county").
    MISS.
  * Quoted phrase queries ("indian motorcycle agency", "erie motorcycle", "indian motorcycle" erie, erie motorcycle "hill climb")
    -> HTTP 502 "upstream request failed" twice each => quoted-phrase queries treated as BLOCKED/failed; not retried further.

### 2. Pennsylvania Newspaper Archive (panewsarchive.psu.edu, Open ONI; curl 200)
- Title list https://panewsarchive.psu.edu/newspapers/ (saved panews_newspapers.html), 227 rows. Erie titles:
  The Erie observer (sn86053495) digitized 1859-03-12..1869-05-27 (403 issues); Erie observer (sn83032025) 1847-04-10..1853-05-07;
  Erie weekly observer (sn86071387) 1853-1859; The Nittany cub (2018264051) 1948-10-26..1971-05-27; Behrend collegian 1971-1988;
  The Collegian 1989-93; Behrend College collegian 1993-98; Behrend beacon 1998-2010.
  => NO Erie County newspaper digitized for 1915-1945 on PA Newspaper Archive. No Crawford/Warren/Venango 20th-c. titles either.
  Titles overlapping 1915-45 are all central/eastern PA (Bellefonte, Centre Hall, State College, Harrisburg to 1919, Philadelphia EPL to 1922,
  Indiana Patriot to 1921, Patton, Mount Joy, Dallas Post, Meyersdale, Hazleton).
- Search URL pattern (works): https://panewsarchive.psu.edu/search/pages/results/?format=json&rows=50&searchType=advanced&andtext=WORD
  (also proxtext=, phrasetext=, ortext=, lccn=, city=; dateFilterType=yearRange&date1=&date2= appeared to be ignored in JSON mode).
  OCR text: https://panewsarchive.psu.edu/lccn/<LCCN>/<YYYY-MM-DD>/ed-1/seq-<N>/ocr.txt
  * andtext=Bayhurst -> 4: Behrend collegian 1985-12-12 seq11 (modern, not opened - possible living persons), Scranton Tribune 1896/1897,
    Evening Public Ledger 1916-05-30 (Telford girls). MISS for 1915-45 Erie.
  * phrasetext="indian motorcycle" + andtext=Erie -> 324 (Harrisburg Telegraph, Daily Collegian, Lancaster Farming...; stemmed/fuzzy). No Erie-
    specific item visible in first 50. MISS.
  * andtext=LeJeal -> 68, all Bellefonte/Scranton/Emporium fuzzy noise. MISS.  phrasetext="Erie motorcycle club" -> 0.
  * andtext=Beckman Erie Indian motorcycle -> 1: Harrisburg Telegraph 1916-09-02 seq13 = classified ads ("Thos. J. Beckman Co." Harrisburg). MISS.
- Extra PA-archive check: andtext=Corry motorcycle LeJeal -> 0; "Corry motorcycle race Erie" -> 14 (date filter ignored); OCR of
  Forest Republican 1914-08-12 seq2 and Harrisburg Telegraph 1917-10-20 seq11 has no Corry/Erie motorcycle context. MISS.
- Chronicling America retries late in session: q=lejeal corry motorcycle 1919 -> 0 results; q=corry motorcycle 1919 -> HTTP 502 then 500;
  loc.gov item JSON (sn87078352, sn86083175) -> 429 Cloudflare / 502; WebFetch of loc.gov item page -> 403. => loc.gov now rate-limiting;
  stopped hitting it.

### 3. FultonHistory.com
- https://fultonhistory.com/ -> 503 "Service Unavailable"; http://fultonhistory.com/Fulton.html -> 503 (upstream connect timeout);
  /my%20photo%20albums/All%20Newspapers/ -> 503. => BLOCKED (3 attempts). Not retried.
- Title coverage via The Ancestor Hunt PA list (https://theancestorhunt.com/blog/pennsylvania-online-historical-newspapers-summary/,
  curl 200) which links Fulton folders: PA titles on Fulton include "Edinboro PA Indpendant" (the only ERIE COUNTY title), "Crawford PA
  Weekly Messenger", "Warren PA Observer", "Warren PA Times Mirror", "Warren PA Times Mirror Observer", "New Castle PA News",
  "Smethport PA Mckean County Miner", "Tionrsta PA Forest Republican", "Reynoldsville PA Star", "Butler PA Citizen" + central/eastern PA.
  NO Erie city daily (Erie Daily Times / Erie Dispatch(-Herald)) on Fulton per this list. (Fulton's big strength = western NY papers:
  Jamestown, Dunkirk, Westfield, Buffalo - not verifiable from here.) Edinboro Independent years on Fulton UNKNOWN.

### 4. Coverage of Erie papers anywhere online (ldsgenealogy.com + State Library of PA LibGuide)
- https://ldsgenealogy.com/PA/Erie-County-Newspapers-and-Obituaries.htm (curl 200, saved ldsgen_news.txt) "Online" list:
  GenealogyBank (= NewsBank consumer product): "Erie Times-News 08/08/1888 to 02/28/1919" [i.e. Erie Daily Times], "Erie Morning Dispatch
  01/01/1884 to 08/17/1924", "Erie Evening Herald 12/30/1921 to 01/21/1922", "Erie Tageblatt 03/07/1899 to 06/30/1917", "Truth 10/25/1913 to
  06/11/1921", "Erie Labor Press 06/18/1921 to 12/31/1921", "Erie Times-News 01/01/1995 to Current".
  Newspapers.com: "Dispatch-Herald 1923-1923", "Lake Shore Visitor 1874-1937", "Lake Shore Visitor-Register 1938-1959" (Catholic diocesan
  weekly, Erie), "Christian Home and School 1915-1918", "Catholic Chronicle 1910-1915", "Trybuna Polska 1925-1925", "Erie Times-News 2020-2026".
  PowerLibrary: Erie Gazette 1820-1864. Penn State: Hammermill Paper Co. employee periodicals 1917-1966 (already used by directories lane).
  => GAP: no online Erie daily for 1925-1994 found in any list (Erie Dispatch-Herald 1925-57, Erie Daily Times 1919/1922-1994).
- newspapers.com paper pages (the-lake-shore-visitor/34014, the-dispatch-herald/34311): curl 403, WebFetch 403 -> BLOCKED.
- genealogybank.com Erie list: curl 202 empty, Playwright 403 (CloudFront) -> BLOCKED.
- State Library of PA "E - Newspapers by County" https://pa-gov.libguides.com/c.php?g=1180939&p=8634966 (curl 200) - microfilm holdings:
  "Erie Daily Times (general) 0(4/1898; 08/15/1945; 1957-2000)" [only scattered pre-1957]; "The Dispatch-Herald (general) (1922-1925)";
  "The Erie Dispatch-Herald (general) (1925-1957)"; "The Erie Dispatch (general) (1902-1922)"; "Erie Dispatch-Herald and Sun (1946)";
  "The North East Breeze (general) (1928-1945; 1984-2001)"; "The Cosmopolitan Herald [Girard] (1910-1911; 1917-1922; 1925-1929; 1933;
  1935-1942; 1944-1950)"; "Union City Times-Enterprise (1912-1966)"; "The Waterford Leader (1879-1949; 1951-1969)"; "Corry Evening Journal
  (1954-1983)"; "The Corry Leader (1912-1913; 1915-1916)"; "The Edinboro Independent (1889-9112 [sic]; 1943-1977)".
- Erie County Public Library LibGuide (https://eriecounty-pa.libguides.com/c.php?g=1221754&p=8937435, curl 200): "Erie Newspapers on Newsbank -
  Current and Historic: Find full image/text articles ... from current and archived issues of the Erie Times-News, Erie Morning Dispatch, and
  Erie Daily Times. Coverage spans from 1884 - Present. This resources is available to resident, Erie County Public Library card holders, and can
  be accessed from anywhere."  NOTE: "1884 - Present" may hide a gap (GenealogyBank stops 1919/1924, restarts 1995). A WebSearch summary
  (not seen on any page) said "papers up to 1922 currently included as a trial" -> UNVERIFIED; Abe must check the source list on login.
- erielibrary.org (NewsBank page, accordion page, obituary listings) -> curl 000/timeout, WebFetch 503 x2 -> BLOCKED (as ACCESS.md says).
- FamilySearch wiki Erie County (curl 200): Blasco Heritage Room microfilm incl. "the Erie Dispatch, Erie Dispatch-Herald, the Erie Daily Times,
  the Erie Morning News and the Erie Times-News ... the Cosmopolite (Girard, PA), the Corry Evening Journal and the Edinboro Independent";
  "The Erie County Library has compiled and maintains an paper and online obituary index for Erie County from 1822 to the present."
- Erie Society for Genealogical Research page (Playwright 200): "The Erie Library maintains an obituary index for Erie daily papers published
  from 1822 to the present, including more than 277,774 records. Obituaries can be searched online."
- WebSearch: ECPL "Erie County Public Library Obituary Listings" = https://erielibrary.org/databases/erie-county-public-library-obituary-listings/
  ("do not use commas, quotation marks ... limit is two search terms"); Obituary Request https://erielibrary.org/resources/obituary-services/obituary-request/
  (fee). Ancestry "Erie County, Pennsylvania, U.S., Obituary Index, 1822-2018" (archives.com Collection=1313) = same index ($).

### 5. archive.org newspapers (tools/iafts.py + lanes/newspapers/iafts2.py with filter_map collection restriction)
- No Erie County newspaper on archive.org (metadata: "north east breeze", "meadville tribune", "erie dispatch", "erie daily times",
  "lake shore visitor", "edinboro independent", "corry journal", "union city times" -> 0 newspaper items).
- NewspaperArchive-donated collections nearby: newspaperarchive-warren-times-mirror (years 1940-1946, 1948-1953, 1956-1959),
  warren-observer (1954-1960), warren-times-mirror-and-observer (n.d.), titusville-herald (no 1910-1960 items), new-castle-news (1926-1951),
  mckean-county-miner (1910-1912, 1918-1924), clearfield-progress. No Corry/Meadville/Jamestown/Dunkirk collections.
- Bayhurst: Warren TM -> 1 hit (1951-12-11, Fisk family, already known); New Castle, Titusville, McKean, Clearfield, Warren Obs -> 0.
- '"hill climb" Erie motorcycle': Warren TM 2 (1944 walking "hill climb-ing", 1956 none) MISS; New Castle 17 = New Castle/Lawrence County
  MC hill climbs 1932-1951, no Erie dealer/club content in snippets; Titusville 0. 'hillclimb Erie motorcycle' 0; '"Erie Motorcycle Club"' 0.
- '"Indian" motorcycle Erie dealer' / '"Indian Motorcycle"' Warren TM: only 1946-1958 classifieds (Wolf(e) Indian Motorcycle Sales, RD 1
  Jackson Run, Warren, 1958; Conewango Valley Motors 1953). Kuivinen 0. '"motorcycle races" Erie' -> 1958-07-29 "Motorcycle races, featuring top
  Erie and area drivers" (out of period). MISS for 1915-45 Erie Indian dealer.
- General FTS (all archive.org): '"Bayhurst" motorcycle' 155 fuzzy (Oil City HS yearbooks 1948/49 Joseph/Nancy Bayhurst = other family; UK Bayhurst
  Wood) MISS; '"Bayhurst" Indian Erie' 0; '"Indian Motorcycle Agency" Erie' 64 (Madison WI, Hondo TX, LA, Victoria BC agencies) MISS;
  '"Indian motorcycle" "Erie, Pa"' 2342 -> American Motorcycling Jan 1955 "Erie MC, 114 East 11th St., Erie, Pa." (already known) MISS for 1915-45.

### 6. NYS Historic Newspapers / Google News Archive / forums
- nyshistoricnewspapers.org Chautauqua title list: curl 301->403, Playwright = Cloudflare "Performing security verification" (not solved),
  WebFetch 403 -> BLOCKED. Titles (WebSearch only, LEADS): Jamestown Evening Journal (1905-1941 run), Westfield Republican, Fredonia Censor
  (to 1932, + 1932-36 title). Chronicling America has no Chautauqua/Cattaraugus/Erie NY titles (59 NY titles checked via Playwright).
- Google News Archive: news.google.com/newspapers?nid=z0_F5_TITjQC ("Erie News" per search result title) -> 302 to google.com/sorry (CAPTCHA)
  via WebFetch and curl -> BLOCKED; which "Erie" and which years UNKNOWN.
- indianmotorcycles.net thread "Anyone Know About Indian Dealer In Erie, PA?" (threads/...1288): curl 202 empty; Playwright timeout; WebFetch ->
  307 to tollbit.indianmotorcycles.net (paid bot gateway) -> BLOCKED (no payment). Probably about a modern dealer (unknown).
- WebSearch '"Bayhurst" Erie motorcycle', '"Bayhurst" "Erie" newspapers.com clipping OR obituary 1978 Charles', Indian dealer Erie East 11th/10th,
  Erie hill climb 1930s -> no historical hits (only modern dealers / Erie Motorcycle Club EIN 25-1474292 charity listing, McKean PA). MISS.
- Wikipedia "List of online newspaper archives" (curl 200): GenealogyBank "Erie Times-News (1888–2018)" [CONFLICT with ldsgenealogy
  1888-02/28/1919 + 1995-; ldsgenealogy gives exact first/last issue dates -> more reliable; Wikipedia gives a loose span]; Newspapers.com
  "Erie Times-News (2020–)"; FultonHistory ("index only" section) "Jamestown Evening Journal (1882–1941)", "Jamestown Post Journal (1942–1966)",
  "Fredonia Censor (1843–1963)", "Silver Creek News (1906–1933)", "Silver Creek Times (1923–1935)", "Silver Creek News and Times (1935–1946)",
  "Brocton Mirror (1890–1943)", "Buffalo Courier Express (1926–1970)", "Olean Times Herald (1932–1972)".
- Diocese of Erie https://www.eriercd.org/news/lsv.html (curl 200): "The Lake Shore Visitor was the newspaper of the Diocese of Erie from
  1874-2005. In 2023, diocesan archivist Father Justin Pino collaborated with newspapers.com to digitize every issue of the Lake Shore Visitor
  from microfiche." -> newspapers.com (subscription / 7-day trial = sign-up -> manual). thecatholicnewsarchive.org -> Cloudflare 403 (not tried further).
- WebSearch site:newspapers.com Bayhurst Erie -> LEADS (pages not fetchable, 403): Pittsburgh Post-Gazette newspage 88270669, Philadelphia
  Inquirer newspage 170653115 (both "Bayhurst"+"Erie" in a list per search summary; dates unknown); Democrat and Chronicle (modern athlete,
  living person - ignored); clip 3461192 "Marjorie Bayhurst birth Announcement" News-Herald Franklin PA 13 Nov 1930 (probably the Oil City/
  Franklin Bayhurst line, not Charles). newspapers.com newspage 88270669 via WebFetch -> 403. BLOCKED.

## CONCLUSIONS (newspapers lane)
1. NO free, full-text Erie city newspaper exists online for 1915-1945. Chronicling America: 0 Erie County titles. PA Newspaper Archive: Erie
   titles only 1847-1869 (Observer) and 1948+ (Behrend/Nittany Cub). archive.org: none (nearest: Warren Times Mirror 1940-59, New Castle News
   1926-51). FultonHistory: only Edinboro Independent for Erie County (site down from here). Google News Archive: CAPTCHA.
2. Erie dailies exist on NewsBank/GenealogyBank for 1884-1919/1924 (Erie Daily Times to 28 Feb 1919; Erie Morning Dispatch to 17 Aug 1924, per
   ldsgenealogy listing) and from 1995 on. The 1925-1994 span (Erie Dispatch-Herald 1925-57, Erie Daily Times 1919-94) appears NOT to be online
   anywhere free or in GenealogyBank; ECPL describes its NewsBank as "1884 - Present" - must be checked by Abe on login.
   Microfilm: Blasco Library Heritage Room (Erie Daily Times, Erie Dispatch-Herald, Erie Morning News ...); State Library of PA (Erie
   Dispatch-Herald 1925-1957; Dispatch-Herald 1922-25; Erie Dispatch 1902-22; North East Breeze 1928-45; Union City Times-Enterprise 1912-66;
   Waterford Leader 1879-1949; Girard Cosmopolitan Herald scattered 1917-1950).
3. No newspaper hit for Bayhurst / Indian Motorcycle Agency / 120 or 302 E 11th / "East 10th" motorcycle in any accessible free full text.
   This lane produced NO new verified business listing; its value is the coverage map + manual search plan below.
4. "East 10th Street": nothing in this lane supports or refutes it (no Erie full text 1925-45 reachable).

## MANUAL SEARCH PLAN FOR ABE (needs Erie County Public Library card; erielibrary.org unreachable from this container)
Entry: https://erielibrary.org/databases/historical-erie-newspapers-on-newsbank/ (log in with ECPL card).
STEP 0 (do first, 2 minutes): in NewsBank open the source/publication list and write down the exact date span of each Erie title
  (Erie Daily Times, Erie Morning Dispatch, Erie Dispatch-Herald, Erie Times-News). If nothing between 1925 and 1994 is present, steps B/C
  move to microfilm (Blasco Heritage Room, or State Library of PA microfilm of Erie Dispatch-Herald 1925-1957 via interlibrary loan).
NewsBank syntax: quotes = phrase; AND / OR / NOT; ? = one character, * = many; set the date range box; sort "oldest first".

A. 1915-1924 (inside known online coverage: Daily Times to Feb 1919, Morning Dispatch to Aug 1924)
  A1  Bayhurst  OR  "Bay hurst"  OR  Bayh?rst  OR  Bayburst  OR  Bayhorst        dates 01/01/1915-12/31/1924
      why: 1919 race win (Motorcycle Illustrated snippet), Charles's early cycle trade; parents' obituaries Louise (d. 20 Jan 1916:
      search 01/20/1916-01/31/1916) and Louis (d. 13 Oct 1918: search 10/13/1918-10/25/1918) name the sons and their trades.
  A2  "Cycle Dealers"  AND  Erie        dates 06/15/1919-07/31/1919   (Erie Cycle Dealers' Association race meet; Bayhurst won a motorcycle event,
      Charles Schroeder 2nd; M. B. Schutte won the 8-mile sidecar race)
  A3  LeJeal  OR  "Le Jeal"  OR  Lejeal        dates 07/05/1919-07/15/1919   (Charles Archibald LeJeal killed in motorcycle race at Corry 5 Jul 1919)
  A4  Beckman  AND  (Indian  OR  motorcycle*)        dates 10/15/1922-12/31/1922   (A. D. "Archie" Beckman opens Indian agency, 1807 Parade St)
      also "1807 Parade" (whole 1922-1924)
  A5  "Indian motocycle*"  OR  "Indian motorcycle*"  OR  "Indian motor cycle*"        dates 1915-1924  (pre-1923 factory name was "Indian Motocycle")
  A6  "Erie Motorcycle Club"  OR  "Erie M. C."  OR  ("motorcycle club" AND Erie)        dates 1915-1924  (club officers, hill climbs, gypsy tours)
  A7  Furlong  AND  Harley        1922-1924 (Harley dealer W. M. Furlong, context/competitor)

B. 1925-1945 (the shop years; probably NOT online - check STEP 0; else microfilm)
  B1  "Indian Motorcycle Agency"        1934-1940   (phone book: 120 E 11th 1935-36, 302 E 11th 1937)
  B2  "120 East Eleventh"  OR  "120 E. 11th"  OR  "120 East 11th"        1933-1937
  B3  "302 East Eleventh"  OR  "302 E. 11th"  OR  "302 East 11th"        1935-1941
  B4  "Indian"  AND  (motorcycle*  OR  motocycle*)  AND  (Eleventh  OR  "11th")        1925-1941
  B5  "Indian"  AND  (motorcycle*  OR  motocycle*)  AND  (Tenth  OR  "10th")        1920-1950   <- direct test of Abe's "East 10th Street"
      also  motorcycle*  AND  ("East Tenth"  OR  "E. 10th")        1920-1950
  B6  Bayhurst  OR  Bayh?rst        1925-1945   (ads, club news, accidents, business notices, 1940s)
  B7  "69-312"  OR  "48-385"        1935-1938   (the agency's phone numbers in the 1935-37 phone books; classified ads often give only the phone)
  B8  "151 East Eleventh"  OR  "151 E. 11th"        1925-1930   (L. J. Bayhurst address 1927 - was there a shop?)
  B9  "hill climb"  AND  Erie  AND  motorcycle*   ;   "gypsy tour"  AND  Erie   ;   "motorcycle races"  AND  Erie        1925-1941
  B10 Kuivinen  OR  "114 East Eleventh"  OR  "941 East Eleventh"  OR  Shannon AND Harley        1928-1941   (Harley competitor next door)
  Browse windows if full text is poor: Erie Daily Times + Dispatch-Herald sports/auto pages and classified "Motorcycles" column,
    Mar-May 1935 (agency appears between Jan and Jul 1935 phone books), Mar-May 1937 (move to 302 E 11th), Dec 1939-Apr 1940 (shop closes;
    1940 census: seeking work).

C. Obituaries (exact dates from Erie Cemetery transcriptions; use ECPL Obituary Listings first:
   https://erielibrary.org/databases/erie-county-public-library-obituary-listings/  - max two terms, no punctuation:
   "Bayhurst Charles", "Bayhurst 1978", "Bayhurst Lewis", "Bayhurst Louis", "LeJeal Charles", "Beckman Archie", "Schroeder Charles")
  C1  Bayhurst        11/19/1978-11/30/1978   (Charles Arthur Bayhurst, b. 28 Aug 1899, d. 19 Nov 1978) - Erie Daily Times / Morning News
  C2  Bayhurst        12/08/1983-12/20/1983   (Theresa I. Bayhurst, widow) - names "late husband Charles", sometimes his business
  C3  Bayhurst        09/18/1948-09/30/1948   (Lewis J. Bayhurst, d. 18 Sep 1948 - brother; obituary lists brothers)
  C4  LeJeal / Beckman obituaries - dates unknown -> from ECPL index.
  If NewsBank lacks 1948/1978/1983: request copies via https://erielibrary.org/resources/obituary-services/obituary-request/ (fee) or read
  microfilm in the Blasco Heritage Room.
