# Sources checked

Every source the research lanes touched, with outcome. **hit** = useful evidence found; **partial** = reached but incomplete; **miss** = searched, nothing relevant; **blocked** = could not be reached from the cloud container (Cloudflare, IP block, login, paywall or outage).

Totals: 52 hit, 27 partial, 45 miss, 32 blocked (156 entries).

## HIT

- **archive.org 1920 census microfilm 14thcensusofpopu1565/1566/1567unit (metadata + BookReaderImages.php images)** — [https://archive.org/details/14thcensusofpopu1567unit](https://archive.org/details/14thcensusofpopu1567unit)  
  The ED ranges are in the metadata. IIIF returns 404 for these items, so I used BookReaderImages.php. Reel 1567: all of Millcreek EDs 128-132 scanned, Louis/Frank/Rosa at leaf 623. Reel 1566: Edward at leaf 477. _(lane: census-followup)_
- **Steve Morse unified 1940 ED finder + getxml** — [https://stevemorse.org/census/unified.php?year=1940&state=PA&city=ER&street1=11th&street2=](https://stevemorse.org/census/unified.php?year=1940&state=PA&city=ER&street1=11th&street2=German)  
  11th x German = EDs 68-31A (images 03647-00701..00720) and 68-31B (00721..00736). _(lane: census-followup)_
- **NARA 1940 census media server** — [https://catalog.archives.gov/medialz/census-1940/T627/PA/m-t0627-03647/m-t0627-03647-00707](https://catalog.archives.gov/medialz/census-1940/T627/PA/m-t0627-03647/m-t0627-03647-00707.jpg)  
  All 36 images of 68-31A/B fetched, plus roll 3651 image 00044 (Lewis). _(lane: census-followup)_
- **Ancestry.com public search-results pages (no login) - 1920 (coll 6061) and 1940 (coll 2442)** — [https://www.ancestry.com/search/collections/6061?name=_Bayhurst&name_x=_1&residence=_penns](https://www.ancestry.com/search/collections/6061?name=_Bayhurst&name_x=_1&residence=_pennsylvania-usa_41)  
  Index only, with names, ward/county and image IDs visible in the page JSON. 1920: 10 Bayhursts in PA, no Charles. 1940: 37 entries, including Lewis (03651-00044). I stopped broader Charles B* paging (6,170 results) to avoid scraping. _(lane: census-followup)_
- **Penn State CONTENTdm behrend (Hammermill Bond) API/dmQuery/IIIF** — [https://digital.libraries.psu.edu/digital/api/search/collection/behrend/searchterm/bayhurs](https://digital.libraries.psu.edu/digital/api/search/collection/behrend/searchterm/bayhurst/maxRecords/100)  
  Mar 1930 heading verified, and the May 1936 ten-year pin list verified without Bayhurst. Sep 1930-Nov 1933 not digitized. One IIIF 502 error on the first try; the retry worked. _(lane: census-followup)_
- **LOC Erie phone books 8/1948-Fall 1951 (reel usteledirec07591): OCR JSON plus page images** — [https://www.loc.gov/item/usteledirec07591/](https://www.loc.gov/item/usteledirec07591/)  
  New reel. Indian Motorcycle Sales & Service / Indian Motorcycle Agency, A. Louis Straus, 1315 Peach St, in the 1948 and 1949 books (image-verified); gone in 1950 and 1951 (image). _(lane: dealer-lists)_
- **LOC Erie phone books 7/1952-7/1957 (reel usteledirec07592)** — [https://www.loc.gov/item/usteledirec07592/](https://www.loc.gov/item/usteledirec07592/)  
  Motorcycles = Harley only (John Menzel Prop) in 1952, 1953 and 1955 (15% images); 1957 OCR only. _(lane: dealer-lists)_
- **LOC Erie phone books 7/1958-7/1960 (reel usteledirec07593)** — [https://www.loc.gov/item/usteledirec07593/](https://www.loc.gov/item/usteledirec07593/)  
  OCR: Harley at 3001 Glenwood Pk av; Starvaggi's Garage (BSA etc.) at 3417 Peach; no Indian; nothing on E 10th. _(lane: dealer-lists)_
- **LDSgenealogy.com Erie County PA City Directories index** — [https://ldsgenealogy.com/PA/Erie-County-City-Directories.htm](https://ldsgenealogy.com/PA/Erie-County-City-Directories.htm)  
  Lists which Erie directory years are on Ancestry (every year 1915-1943), MyHeritage (13 interwar years), ACPL (1901-1943) and FamilySearch catalog IDs 541218, 148168, 534727. _(lane: directories)_
- **FamilySearch Wiki, Erie County PA Genealogy** — [https://www.familysearch.org/en/wiki/Erie_County,_Pennsylvania_Genealogy](https://www.familysearch.org/en/wiki/Erie_County,_Pennsylvania_Genealogy)  
  Directories section: 1936-1940 Erie City Directory, catalog 148168, 'index & images'. ECPL Heritage Room has directories from 1853. _(lane: directories)_
- **HathiTrust catalog API (volumes/brief)** — [https://catalog.hathitrust.org/api/volumes/brief/htid/pst.000012006779.json](https://catalog.hathitrust.org/api/volumes/brief/htid/pst.000012006779.json)  
  Record 009816870: only 1873-74 and 1939 are full view; 5 search-only volumes are 1972-1984. Returns 403 if a browser user-agent is sent, 200 without one. _(lane: directories)_
- **Google Books GData feed: 1939 Atkinson Erie directory (setXAAAAYAAJ)** — [https://www.google.com/books/feeds/volumes?q=Bayhurst+Kilpatrick](https://www.google.com/books/feeds/volumes?q=Bayhurst+Kilpatrick)  
  About 60 queries, 3.5 s apart. Snippets for Bayhurst (alphabetical, classified, street guide), Kuivinen, motorcycle club, bicycle dealers, Goodyear at 163 E 10th, and E 10th 107-130. The volume is view_no_pages, so no page images. Raw: lanes/directories/gb_raw.log. _(lane: directories)_
- **Google Books: Catalog of Copyright Entries 1939-1941** — [https://books.google.com/books?id=_EXQAAAAMAAJ](https://books.google.com/books?id=_EXQAAAAMAAJ)  
  Snippet: Atkinson's 1939 Erie directory registered Aug 30, 1939 (A 133135); a 1940 edition was also registered. _(lane: directories)_
- **Penn State Behrend collection: The Hammermill Bond (Erie employee magazine)** — [https://digital.libraries.psu.edu/digital/collection/behrend/id/4173](https://digital.libraries.psu.edu/digital/collection/behrend/id/4173)  
  'bayhurst' matched 4 pages (1926, 1929 x2, 1930); 3 verified on image. 'indian motorcycle', 'harley davidson', 'motorcycles erie' found no dealer items. _(lane: directories)_
- **Interment.net Erie Cemetery Bau-Ben** — [https://www.interment.net/data/us/pa/erie/erie-cemetery/records-bau-ben.htm](https://www.interment.net/data/us/pa/erie/erie-cemetery/records-bau-ben.htm)  
  Charles Arthur Bayhurst 1899-1978 and Theresa I. 1901-1983, same lot; Lewis J. 1894-1948; Louis 1863-1918; Louise 1862-1916. _(lane: directories)_
- **LOC Erie phone-book OCR (local work/loc/*.json) used to cross-check** — [https://www.loc.gov/resource/gdcmassbookdig.usteledirec07589/?sp=759](https://www.loc.gov/resource/gdcmassbookdig.usteledirec07589/?sp=759)  
  Haft's Garage at 124 E 11th first appears Jan 1939 (seq759), supporting the 1939 date of the GB volume. Kuivinen is not named in any phone-book OCR. _(lane: directories)_
- **Google Books Motorcycle Illustrated 1919 Jul-Sep (XXsAAAAAMAAJ), snippet images** — [https://books.google.com/books?id=XXsAAAAAMAAJ&q=Bayhurst](https://books.google.com/books?id=XXsAAAAAMAAJ&q=Bayhurst)  
  Bayhurst race page 40 image-verified via snippet crops. Exposition Park, July 4, 1919, Erie Cycle Dealers' Association; not Corry. _(lane: gap-1923-1934)_
- **Atkinson Erie Directory 1939 (setXAAAAYAAJ), in-volume search** — [https://books.google.com/books?id=setXAAAAYAAJ](https://books.google.com/books?id=setXAAAAYAAJ)  
  p.80 Archie D Beckman clerk (text); p.479 = Keystone Erie MC clubs list; bicycles at 1802 Parade (Firestone) and 406 State. _(lane: gap-1923-1934)_
- **LOC U.S. Telephone Directory Collection, reel usteledirec07589 (Erie 1911, 1914, 1934-1940): page images via tile.loc.gov IIIF** — [https://www.loc.gov/resource/gdcmassbookdig.usteledirec07589/](https://www.loc.gov/resource/gdcmassbookdig.usteledirec07589/)  
  About 110 image requests spaced 3 s or more apart. Covers and target cards confirm all edition dates. I read every Indian and Bayhurst listing and every Motorcycles heading on the images. Evidence crops are in evidence/*loc-erie-phonebook*. _(lane: loc-phonebooks)_
- **LOC reel usteledirec07589 OCR (work/loc/usteledirec07589.text.json)** — [https://tile.loc.gov/storage-services/service/gdc/gdcmassbookdig/usteledirec07589/](https://tile.loc.gov/storage-services/service/gdc/gdcmassbookdig/usteledirec07589/)  
  Searched for Indian, Bayhurst, motorcycles, phones 69-312 and 48-385, East 10th (with OCR variants), and occupants of 114/118/120/124/151/302 E 11th. _(lane: loc-phonebooks)_
- **LOC U.S. Telephone Directory Collection, reel usteledirec07590 (Erie Jul 1941 - Jul 1947): OCR and page images** — [https://www.loc.gov/resource/gdcmassbookdig.usteledirec07590/](https://www.loc.gov/resource/gdcmassbookdig.usteledirec07590/)  
  Mapped the editions from the target cards (seq19, 128, 243, 360, 478, 606, 762). All seven Motorcycles headings list only Harley-Davidson, read on the images. Charles Bayhurst appears as a residence only, from 1943. _(lane: loc-phonebooks)_
- **Reed, History of Erie County 1925 vol 2 (historyoferiecou02reed)** — [https://archive.org/details/historyoferiecou02reed/page/857](https://archive.org/details/historyoferiecou02reed/page/857)  
  LeJeal bio pp.857-858, checked on the page images; other bicycle-era bios. No Bayhurst, no Indian agency. _(lane: local-history)_
- **Miller, Twentieth Century History of Erie County 1909, vols 1-2** — [https://archive.org/details/twentiethcentury01mill/page/706](https://archive.org/details/twentiethcentury01mill/page/706)  
  p.706: LeJeal Cycle & Mobile Works begun 1894 (checked on image). No motorcycle dealers. _(lane: local-history)_
- **LOC Sanborn maps of Erie (collection JSON via WebFetch; images via tile.loc.gov IIIF)** — [https://www.loc.gov/collections/sanborn-maps/?q=erie+pennsylvania&fo=json](https://www.loc.gov/collections/sanborn-maps/?q=erie+pennsylvania&fo=json)  
  Editions 1888, 1900, 1917, 1921 (3 vols), 1921-Aug 1950 (3 vols), 1951. Dec 1923 not digitized. Read sheets 59, 60 (overview), 61, 63, 73, 74, 78. _(lane: local-history)_
- **The Ancestor Hunt - PA free online newspapers (Fulton title links)** — [https://theancestorhunt.com/blog/pennsylvania-online-historical-newspapers-summary/](https://theancestorhunt.com/blog/pennsylvania-online-historical-newspapers-summary/)  
  Coverage: Fulton's only Erie County title is the Edinboro Independent; Warren/New Castle/Forest titles also listed. _(lane: newspapers)_
- **ldsgenealogy Erie County Newspapers and Obituaries** — [https://ldsgenealogy.com/PA/Erie-County-Newspapers-and-Obituaries.htm](https://ldsgenealogy.com/PA/Erie-County-Newspapers-and-Obituaries.htm)  
  GenealogyBank Erie Daily Times 1888-02/1919, Morning Dispatch 1884-08/1924, 1995+; newspapers.com Lake Shore Visitor 1874-1959, Dispatch-Herald 1923. _(lane: newspapers)_
- **State Library of Pennsylvania - Newspapers by County E** — [https://pa-gov.libguides.com/c.php?g=1180939&p=8634966](https://pa-gov.libguides.com/c.php?g=1180939&p=8634966)  
  Microfilm holdings: Erie Dispatch-Herald 1925-1957; North East Breeze 1928-45; Union City Times-Enterprise 1912-66, etc. _(lane: newspapers)_
- **Erie County Public Library LibGuide (HistERIE)** — [https://eriecounty-pa.libguides.com/c.php?g=1221754&p=8937435](https://eriecounty-pa.libguides.com/c.php?g=1221754&p=8937435)  
  NewsBank described as 'Coverage spans from 1884 - Present', ECPL card, remote access. _(lane: newspapers)_
- **Erie Society for Genealogical Research - Erie County Libraries** — [https://www.genealogyerie.org/p/Erie-County-Libraries](https://www.genealogyerie.org/p/Erie-County-Libraries)  
  ECPL obituary index (277,774 records) searchable online. _(lane: newspapers)_
- **Diocese of Erie - Lake Shore Visitor archives** — [https://www.eriercd.org/news/lsv.html](https://www.eriercd.org/news/lsv.html)  
  LSV fully digitized on newspapers.com (2023). _(lane: newspapers)_
- **Wikipedia - List of online newspaper archives** — [https://en.wikipedia.org/wiki/Wikipedia:List_of_online_newspaper_archives](https://en.wikipedia.org/wiki/Wikipedia:List_of_online_newspaper_archives)  
  GenealogyBank 'Erie Times-News (1888–2018)' (conflicts with ldsgenealogy); Fulton Jamestown Evening Journal 1882-1941, Post Journal 1942-66. _(lane: newspapers)_
- **American Rifleman Nov 1927 (sim_american-rifleman_1927-11_75_11)** — [https://archive.org/details/sim_american-rifleman_1927-11_75_11/page/n27](https://archive.org/details/sim_american-rifleman_1927-11_75_11/page/n27)  
  Leaf 27 viewed and cropped; L. J. Bayhurst, 151 E 11th St, Lawrence Park Rifle Club. _(lane: people-bayhurst)_
- **American Rifleman Apr 1929 (sim_american-rifleman_1929-04_77_4)** — [https://archive.org/details/sim_american-rifleman_1929-04_77_4/page/n23](https://archive.org/details/sim_american-rifleman_1929-04_77_4/page/n23)  
  Leaf 23 viewed and cropped; E. and L. Bayhurst on Lawrence Park Buddies team. _(lane: people-bayhurst)_
- **interment.net Laurel Hill Cemetery Ba-Bh** — [https://interment.net/data/us/pa/erie/laurel-hill-cemetery/records-ba-bh.htm](https://interment.net/data/us/pa/erie/laurel-hill-cemetery/records-ba-bh.htm)  
  Edward L. 1897-1981, Ruth B., Dorothy W. _(lane: people-bayhurst)_
- **NARA 1950 Census API** — [https://1950census.archives.gov/api/search?name=Bayhurst&state=PA&size=50](https://1950census.archives.gov/api/search?name=Bayhurst&state=PA&size=50)  
  API works by curl. Erie city EDs show as county 'Erie, Erie' (72-x). ED 72-20 image 0036 (Charles A.) and ED 72-150 (Elma H.) viewed. _(lane: people-bayhurst)_
- **NARA WWII draft card images (medialz)** — [https://catalog.archives.gov/medialz/partners/st-louis/rg-147/5324575/44033_05_00028/44033](https://catalog.archives.gov/medialz/partners/st-louis/rg-147/5324575/44033_05_00028/44033_05_00028-01413.tif)  
  Charles Arthur, Edward Leo and Frank William cards viewed. _(lane: people-bayhurst)_
- **NARA 1910 census image T624-1343 #0556** — [https://catalog.archives.gov/medialz/microfilm-publications/T624-1910_Census/0001/T624_134](https://catalog.archives.gov/medialz/microfilm-publications/T624-1910_Census/0001/T624_1343/T624_1343/images/0556.jpg)  
  Bayhurst family, Mill Creek ED 124 sheet 8B. _(lane: people-bayhurst)_
- **Steve Morse One-Step ED finder (1930/1940) + ED image lists** — [https://stevemorse.org/census/unified.php?year=1940&state=PA&city=ER&street1=7th&street2=R](https://stevemorse.org/census/unified.php?year=1940&state=PA&city=ER&street1=7th&street2=Reed)  
  1940 ED 68-18 (847 E 7th), 1930 ED 25-25, 1940 ED 68-122 (W 25th). The ED description pages say 'NOTHING FOUND'; street lists and image arrays work. _(lane: people-bayhurst)_
- **NARA 1940 census images T627 roll 3647 (ED 68-18) 00376-00399** — [https://catalog.archives.gov/medialz/census-1940/T627/PA/m-t0627-03647/m-t0627-03647-00396](https://catalog.archives.gov/medialz/census-1940/T627/PA/m-t0627-03647/m-t0627-03647-00396.jpg)  
  Image 00396 sheet 11A: Bayhurst at 847 E 7th, motorcycle repair shop. _(lane: people-bayhurst)_
- **archive.org 1930 census microfilm roll 2035 (fifteenthcensus00reel2035)** — [https://archive.org/details/fifteenthcensus00reel2035/page/n802](https://archive.org/details/fifteenthcensus00reel2035/page/n802)  
  Leaf 0803 = ED 25-25 sheet 14B, Murphy/Bayhurst household at 847 E 7th. IIIF returned 404, so BookReaderImages.php was used. _(lane: people-bayhurst)_
- **Burton Quinn Scott obituary, Mary E. Bayhurst Covey** — [https://www.burtonquinnscott.com/obituaries/mary-covey](https://www.burtonquinnscott.com/obituaries/mary-covey)  
  Parents Lewis J. and Elma H. Fisk Bayhurst; list of deceased brothers. _(lane: people-bayhurst)_
- **Archive.org 1943 Erie Technical HS yearbook text** — [https://archive.org/download/classmates-yearbook-53401-1943-erie-technical-thru-1959-high-](https://archive.org/download/classmates-yearbook-53401-1943-erie-technical-thru-1959-high-school/53401_djvu.txt)  
  'Pattern Making ... Bayhurst, Charles' = son Charles W. _(lane: people-bayhurst)_
- **LOC Sanborn Erie 1921-Aug 1950 Vol.1 sheet 59 (full-res IIIF)** — [https://www.loc.gov/resource/g3824em.g3824em_g07660195001/?sp=63](https://www.loc.gov/resource/g3824em.g3824em_g07660195001/?sp=63)  
  Through-block geometry, junction close-up, scale bar, E 10th labels both sides. IIIF id found via WebFetch JSON. _(lane: through-block)_
- **LOC Sanborn Erie 1921 Vol.1 sheet 59 (full-res IIIF)** — [https://www.loc.gov/resource/g3824em.g3824em_g07660192101/?sp=61](https://www.loc.gov/resource/g3824em.g3824em_g07660192101/?sp=61)  
  Mid-block rear lot line; vacant 106-122 E 11th; E 10th labels (WICKER SHOP at 120). _(lane: through-block)_
- **LOC Sanborn Erie 1921 Vol.1 index sheet KEY legend** — [https://tile.loc.gov/image-services/iiif/service:gmd:gmd382m:g3824m:g3824em:g3824em_g07660](https://tile.loc.gov/image-services/iiif/service:gmd:gmd382m:g3824m:g3824em:g3824em_g07660192101:07660_01_1921-0000/4950,4300,1400,3300/full/0/default.jpg)  
  Symbols for fire walls, openings, windows. _(lane: through-block)_
- **LOC Sanborn Erie 1921 and 1921-1950 Vol.1 sheets 3, 60, 61, 62 (E 10th bands)** — [https://tile.loc.gov/image-services/iiif/service:gmd:gmd382m:g3824m:g3824em:g3824em_g07660](https://tile.loc.gov/image-services/iiif/service:gmd:gmd382m:g3824m:g3824em:g3824em_g07660192101:07660_01_1921-0060/info.json (and 0003/0061/0062; 1950 equivalents))  
  No cycle label on E 10th lots. Found 1921 'Bicycle Repairing' at 1015 Parade. Tile server returned 503 four times; each succeeded on retry after a pause. _(lane: through-block)_
- **LOC Erie phone-book page images (tile.loc.gov IIIF)** — [https://www.loc.gov/resource/gdcmassbookdig.usteledirec07589/?sp=561](https://www.loc.gov/resource/gdcmassbookdig.usteledirec07589/?sp=561)  
  Viewed seq291, 306, 460, 561, 580, 681, 749, 768, 854, 875 (reel 07589) and seq692 (reel 07590). _(lane: through-block)_
- **loc.gov resource JSON via WebFetch** — [https://www.loc.gov/resource/g3824em.g3824em_g07660195001/?sp=63&fo=json](https://www.loc.gov/resource/g3824em.g3824em_g07660195001/?sp=63&fo=json)  
  Used only to get IIIF ids for sheet 59 (1950 sp=63, 1921 sp=61). _(lane: through-block)_
- **archive.org item motorcycleillustrated (Crittenden Automotive Library; MI 1905a,1908,1909a,1912a,1912b,1913a,1914a,1915b,1916a,1916b,1917a,1917c,1922b,1922c,1922d)** — [https://archive.org/details/motorcycleillustrated](https://archive.org/details/motorcycleillustrated)  
  Downloaded all 15 djvu.txt files and grepped them. Page images via BookReaderImages.php (works). Main source for LeJeal 1908/1917, Beckman 1922, Anderson 1917, Erie M.C. 1917. There is no 1918-1921 or 1923+ volume in this item. _(lane: trade-press)_
- **archive.org Bicycling World and Motorcycle Review 1908-1912 (bicycli58261908201909newy, bicyclingwo5927181909newy, bicyc60251909191910newy, bicyc6126171910newy, bicyclingwo6325161911newy, bicyc6224191081911newy, bicycli64231911161912newy)** — [https://archive.org/details/bicycli64231911161912newy](https://archive.org/details/bicycli64231911161912newy)  
  1912 Erie show (all dealers by make), 1909 Erie M.C. meet (Le Jeal on an Indian), 1909 club organizing, 1910 race meet. _(lane: trade-press)_
- **Google Books GData full-text feed (tools/gbfeed.py)** — [https://www.google.com/books/feeds/volumes](https://www.google.com/books/feeds/volumes)  
  About 45 queries (raw output in lanes/trade-press/gb_raw.log). Snippet leads: 1919 Bayhurst race, 1911 police Le Jeal, 1920 Le Jeal's store, 1928 Lester Shannon H-D agency 941 E 11th, 1917 Pa. registration Chas. Bayhurst. One 'Internal error' was retried successfully. _(lane: trade-press)_
- **HathiTrust catalog API (volumes brief/full JSON)** — [https://catalog.hathitrust.org/api/volumes/full/recordnumber/008608578.json](https://catalog.hathitrust.org/api/volumes/full/recordnumber/008608578.json)  
  Confirmed Full view: MI 1908-1922 (record 008608578), American Motorcyclist and Bicyclist 1928 (000503323), American Bicyclist and Motorcyclist Jan-Jun 1911 (012313767), Pa. List of Motor Vehicle Registrations 1917 (012306389). _(lane: trade-press)_

## PARTIAL

- **NARA catalog proxy search** — [https://catalog.archives.gov/proxy/records/search?q=Bayhurst&limit=100&levelOfDescription=](https://catalog.archives.gov/proxy/records/search?q=Bayhurst&limit=100&levelOfDescription=fileUnit)  
  Works again (JSON). It gave only the known draft-card file unit; there is no 1920 or 1940 index text for Lewis. _(lane: census-followup)_
- **AMCA forum: 'CAIMAG website' thread and guest search** — [https://forum.antiquemotorcycle.org/bboard/forum/general-amca-forum/parking-lot-chatter/23](https://forum.antiquemotorcycle.org/bboard/forum/general-amca-forum/parking-lot-chatter/23629-caimag-website)  
  Confirms CAIMAG offline in 2020; last Wayback copy Feb 2020. Guest search 'Straus Erie' and 'Erie Indian dealer' = 0 results. _(lane: dealer-lists)_
- **Google Books GData feed (tools/gbfeed.py)** — [https://www.google.com/books/feeds/volumes?q=%22Indian+Motorcycle+Sales%22+Erie](https://www.google.com/books/feeds/volumes?q=%22Indian+Motorcycle+Sales%22+Erie)  
  About 10 queries worked (American Motorcyclist 1955-63: Erie = H-D only). Then 'Internal error - please retry later' on 5 tries (Straus queries). _(lane: dealer-lists)_
- **The Ancestor Hunt - free online PA city directories** — [https://theancestorhunt.com/blog/free-online-pennsylvania-city-directories/](https://theancestorhunt.com/blog/free-online-pennsylvania-city-directories/)  
  Free Erie items are the LOC phone books, DPLA 'Erie Directory, 19-', HathiTrust 1982+ Polk, and the 1918 PSU farm directory. Nothing for 1915-1938. _(lane: directories)_
- **Hagen History Center research page** — [https://www.hagenhistory.org/research](https://www.hagenhistory.org/research)  
  Reachable, but no list of directory holdings online. _(lane: directories)_
- **WebSearch (Erie directory 1925 digitized; Charles Bayhurst Erie; Hagen holdings)** — [https://www.google.com/search?q=%22Charles+Bayhurst%22+Erie+Pennsylvania](https://www.google.com/search?q=%22Charles+Bayhurst%22+Erie+Pennsylvania)  
  Led to Masthof, The Ancestor Hunt and interment.net. No free scans of Erie directories 1915-1938. _(lane: directories)_
- **archive.org item motorcycleillustrated (full file list)** — [https://archive.org/metadata/motorcycleillustrated](https://archive.org/metadata/motorcycleillustrated)  
  Docs: 1905a, 1908, 1909a, 1912a/b, 1913a, 1914a, 1915b, 1916a/b, 1917a/c, 1922b/c/d only. No 1918-1921 and no 1923+ volumes (session 1). _(lane: gap-1923-1934)_
- **Google Books SearchWithinVolume2 JSON (new method, headless Chromium)** — [https://books.google.com/books?id=R24hAAAAMAAJ&jscmd=SearchWithinVolume2&q=Erie](https://books.google.com/books?id=R24hAAAAMAAJ&jscmd=SearchWithinVolume2&q=Erie)  
  Works; at most 3 text hits per query on snippet-view books; zeros are unreliable under soft throttling (use positive controls). _(lane: gap-1923-1934)_
- **LOC 1911 and 1914 Erie editions (seq19-53, seq56-101), cycle and motorcycle search** — [https://www.loc.gov/resource/gdcmassbookdig.usteledirec07589/?sp=32](https://www.loc.gov/resource/gdcmassbookdig.usteledirec07589/?sp=32)  
  No Motorcycles heading or Indian/Harley agency. Found LeJeal Cycle Works (1911, 1914), Gas Engine & Cycle Co. (1914) and the Erie Rubber Co. motorcycle-supplies ad (1914), all read on the images. _(lane: loc-phonebooks)_
- **Reed, History of Erie County 1925 vol 1 (historyoferiecou01reed) djvu.txt** — [https://archive.org/download/historyoferiecou01reed/historyoferiecou01reed_djvu.txt](https://archive.org/download/historyoferiecou01reed/historyoferiecou01reed_djvu.txt)  
  No motorcycle/Bayhurst. Context: 124 E 11th aviation school, 135 E 11th Keystone Rubber (text only). _(lane: local-history)_
- **archive.org Erie yearbooks (Academe 1926/27/39/41-43; SV Spokesman 1937-39; Central Spokesman 1918/27/29; Sunrise 1924/26; classmates 1922, 1935, 1937-43; Kaldron 1942; Lawrentian 1942/44; Kernel 1935; Eriez 1931)** — [https://archive.org/advancedsearch.php?q=subject%3A%28%22Erie%2C+Pa.%22%29+AND+subject%3A%](https://archive.org/advancedsearch.php?q=subject%3A%28%22Erie%2C+Pa.%22%29+AND+subject%3A%28%22School+yearbooks%22%29)  
  No motorcycle ads. 1922 Academy: LeJeal and Shade Cycle Works ads (checked on image). Hoffman bicycle ads. literulae00cath djvu.txt returned HTTP 500. _(lane: local-history)_
- **PowerLibrary Erie County Yearbooks (papd:percp-ecy)** — [https://digitalarchives.powerlibrary.org/papd/islandora/object/papd:percp-ecy](https://digitalarchives.powerlibrary.org/papd/islandora/object/papd:percp-ecy)  
  Loads, no login. 269 PDFs with OCR; site search indexes them. Academy 1920, 1922-1992; Sunrise 1923+; Spokesman 1931+ (no 1934; 1938 duplicates 1937). PDFs for 1920-1940 grepped: no motorcycle ads. _(lane: local-history)_
- **Penn State Sanborn collection maps1 (CONTENTdm API)** — [https://digital.libraries.psu.edu/digital/collection/maps1](https://digital.libraries.psu.edu/digital/collection/maps1)  
  Erie 1888, 1900, 1917, 1921 vols 1-3 only (same as LOC). Nothing newer. _(lane: local-history)_
- **Old Time Erie blog searches (motorcycle, Indian, Bayhurst, 11th, Harley, bicycle)** — [https://oldtimeerie.blogspot.com/search?q=motorcycle](https://oldtimeerie.blogspot.com/search?q=motorcycle)  
  Only the Anderson Cycle Works 1914 H-D ad post; Bayhurst 0 posts; nothing on Indian or E 10th/11th shops. _(lane: local-history)_
- **Google Books feed: LeJeal Corry / Archie LeJeal** — [https://www.google.com/books/feeds/volumes?q=%22LeJeal%22+Corry+motorcycle](https://www.google.com/books/feeds/volumes?q=%22LeJeal%22+Corry+motorcycle)  
  Reed 1925 snippet (now confirmed on image); Motor 1909 dealer list; Musical America 1926 (Archie LeJeal music store, 1007 State). _(lane: local-history)_
- **Pennsylvania Newspaper Archive - title list** — [https://panewsarchive.psu.edu/newspapers/](https://panewsarchive.psu.edu/newspapers/)  
  Erie titles only 1847-1869 and 1948+; none 1915-1945. _(lane: newspapers)_
- **archive.org metadata - regional newspapers (Warren, Corry, Titusville, North East Breeze, Meadville, Erie Dispatch/Daily Times, Union City, Jamestown, Lake Shore Visitor, Edinboro)** — [https://archive.org/advancedsearch.php?q=collection:newspaperarchive%20AND%20mediatype:col](https://archive.org/advancedsearch.php?q=collection:newspaperarchive%20AND%20mediatype:collection&output=json)  
  No Erie County paper; Warren TM 1940-59, New Castle News 1926-51, McKean Co. Miner 1910-24 present. _(lane: newspapers)_
- **Google Books GData feed (gbfeed.py), ~25 queries** — [https://www.google.com/books/feeds/volumes](https://www.google.com/books/feeds/volumes)  
  1939 directory snippets, 1917 PA registrations snippet, The Tailor 1907 'G. Bayhurst', Iron Molders 1904, Messenger of Precious Blood 1932 'Matilda Bayhurst', 302 E 11th plumber 1917-22. Some queries returned 'Internal error'. _(lane: people-bayhurst)_
- **NARA catalog proxy search** — [https://catalog.archives.gov/proxy/records/search?q=Bayhurst&limit=50&page=1](https://catalog.archives.gov/proxy/records/search?q=Bayhurst&limit=50&page=1)  
  First ~10 requests returned JSON (115 hits: PA WWII draft cards file unit 359321727, 1910 census index, Theodore Louis Navy file). Later requests returned only the HTML shell (throttled or blocked), tried 5+ times. Image server /medialz/ kept working. _(lane: people-bayhurst)_
- **LOC phone book OCR (grep_loc.py) for 120 E 11, 69-312, 48-385, Bicycles, Bayhurst** — [https://www.loc.gov/resource/gdcmassbookdig.usteledirec07589/](https://www.loc.gov/resource/gdcmassbookdig.usteledirec07589/)  
  Confirms the 1935-36 and 1937 agency lines and 1943-47 residence lines. No Bayhurst under Bicycles. The 120 E 11th operator is not named. _(lane: people-bayhurst)_
- **WebSearch (Charles Bayhurst Erie; findagrave; obituaries; Indian dealer Erie; Theresa Bayhurst; Charles Arthur Bayhurst; 1940 census)** — [https://www.google.com/search?q=%22Charles+Bayhurst%22+Erie](https://www.google.com/search?q=%22Charles+Bayhurst%22+Erie)  
  Led to interment.net and the Covey obituary. Otherwise only modern people-search and Indian dealer pages. _(lane: people-bayhurst)_
- **archive.org The Motorcycle Enthusiast (Harley-Davidson Enthusiast) 1918, 1919, 1923-24** — [https://archive.org/details/motorcycleenthus1923unse](https://archive.org/details/motorcycleenthus1923unse)  
  1918 and 1919: no Erie dealer. 1923-24: Furlong as H-D dealer, Erie Gypsy Tour, Tony De Santi of Erie at factory mechanics' school (text). _(lane: trade-press)_
- **archive.org full-text search (tools/iafts.py)** — [https://archive.org/services/search/beta/page_production/?service_backend=fts](https://archive.org/services/search/beta/page_production/?service_backend=fts)  
  Queries: Bayhurst Erie; "Erie Cycle Dealers" (0); "Erie Motorcycle Club" (led to the motorcycleillustrated item); LeJeal; "Le Jeal"; "Indian dealer" "Erie, Pa."; "Indian agency" "Erie, Pa."; "Bayhurst" motorcycle. Too noisy for name searches; useful only for finding items. _(lane: trade-press)_
- **New American Motorcyclist and Bicyclist 1911** — [https://books.google.com/books?id=XyNaAAAAYAAJ](https://books.google.com/books?id=XyNaAAAAYAAJ)  
  Snippet only (Le Jeal Indian agent, police machines). No archive.org copy. _(lane: trade-press)_
- **American Motorcyclist and Bicyclist 1928** — [https://books.google.com/books?id=R24hAAAAMAAJ](https://books.google.com/books?id=R24hAAAAMAAJ)  
  Snippet only (Erie captain Lester Shannon, Harley-Davidson Agency, 941 East 11th St.). _(lane: trade-press)_
- **Pennsylvania Highway Dept. List of Motor Vehicle Registrations and Licenses 1917** — [https://catalog.hathitrust.org/Record/012306389](https://catalog.hathitrust.org/Record/012306389)  
  Snippet only: 'Chas. Bayhurst, R. F. D. No. 5, Erie'. _(lane: trade-press)_
- **Google Books: Erie county histories / Tales of Old Erie (LeJeal background)** — [https://books.google.com/books?id=GA_YAAAAMAAJ](https://books.google.com/books?id=GA_YAAAAMAAJ)  
  Snippets: LeJeal Cycle & Mobile Works begun 1894 (1909 history); 'LeJeal's motorcycle store on Sassafras Street ... Indian Motorcycle tanks' (1958); LeJeal Automotive Service (1925). _(lane: trade-press)_

## MISS

- **Steve Morse ED descriptions (ed2.php) for 1920 Erie** — [https://stevemorse.org/ed/ed2.php?year=1920&state=PA&county=Erie](https://stevemorse.org/ed/ed2.php?year=1920&state=PA&county=Erie)  
  Every query returned 'NOTHING FOUND' (4 tries). unifiedstreets2 has no 1920 street data for Erie. _(lane: census-followup)_
- **Google Books GData feed (tools/gbfeed.py)** — [https://www.google.com/books/feeds/volumes?q=Bayhurst+%22120+E%22](https://www.google.com/books/feeds/volumes?q=Bayhurst+%22120+E%22)  
  Nothing linking Bayhurst to 120 E 11th. Two 'Internal error' responses; one retry succeeded. _(lane: census-followup)_
- **archive.org full-text search (tools/iafts.py)** — [https://archive.org/services/search/beta/page_production/?service_backend=fts&user_query=%](https://archive.org/services/search/beta/page_production/?service_backend=fts&user_query=%22120%20E.%2011th%22%20Erie)  
  All hits were Gary IN directories or noise. Two queries returned null (API error). _(lane: census-followup)_
- **WebSearch '"Bayhurst" 1920 census Erie'** — [https://www.google.com/search?q=%22Bayhurst%22+1920+census+Erie](https://www.google.com/search?q=%22Bayhurst%22+1920+census+Erie)  
  Only generic census guides. _(lane: census-followup)_
- **Common Crawl CDX via data.commoncrawl.org (cluster.idx binary search, ccsearch.py)** — [https://data.commoncrawl.org/cc-index/collections/](https://data.commoncrawl.org/cc-index/collections/)  
  oldindiandealers.com: 0 captures in 36 crawls from 2008 to 2020. Method validated on antiquemotorcycle.org. _(lane: dealer-lists)_
- **Common Crawl captures of caimag.com** — [https://data.commoncrawl.org/cc-index/collections/CC-MAIN-2019-13/indexes/cluster.idx](https://data.commoncrawl.org/cc-index/collections/CC-MAIN-2019-13/indexes/cluster.idx)  
  7 crawls checked: 331 to 2,793 captures each, 1,123 distinct thread URLs, no dealer-history thread. Indian forum f27 listing (Mar 2019) has none. Member SIDECAR = id 5409; his blog page is empty. _(lane: dealer-lists)_
- **WebSearch: eBay / WorthPoint / general (11 queries)** — [https://www.worthpoint.com/worthopedia/1938-indian-motorcycle-co-dealer-1923128030](https://www.worthpoint.com/worthopedia/1938-indian-motorcycle-co-dealer-1923128030)  
  Only modern dealers and generic Indian memorabilia. No Erie-marked item for LeJeal, Beckman, Bayhurst, the Indian Motorcycle Agency or Straus. _(lane: dealer-lists)_
- **Journal of Erie Studies, 'The Early Automobile and its Influence on Erie, Pennsylvania, 1896-1920'** — [https://journals.psu.edu/eriestudies/article/download/74/74/146](https://journals.psu.edu/eriestudies/article/download/74/74/146)  
  LeJeal/Hagenlocher 1895 car and Roth bicycles; nothing about motorcycle dealers. _(lane: dealer-lists)_
- **Google Books title scan for Erie directories 1915-1938** — [https://www.google.com/books/feeds/volumes?q=intitle:Erie+intitle:directory](https://www.google.com/books/feeds/volumes?q=intitle:Erie+intitle:directory)  
  The only scanned Erie city directories are 1873, 1939 and 1972+. 'Erie County Directory 1916' (QHrTHAAACAAJ) is metadata only. _(lane: directories)_
- **archive.org metadata search (title erie + directory)** — [https://archive.org/advancedsearch.php?q=title%3A%28erie%29+AND+title%3A%28directory%29](https://archive.org/advancedsearch.php?q=title%3A%28erie%29+AND+title%3A%28directory%29)  
  6 items, none an Erie PA city directory 1915-1940. _(lane: directories)_
- **archive.org full-text search (iafts)** — [https://archive.org/services/search/beta/page_production/?service_backend=fts](https://archive.org/services/search/beta/page_production/?service_backend=fts)  
  Queries '"Bayhurst" motorcycles', '"Indian Motorcycle Agency" "E 11th"', 'Erie city directory Atkinson 1925', '"Atkinson Erie Directory"': nothing relevant. Raw: lanes/directories/ia_raw.log. _(lane: directories)_
- **Penn State University Libraries digital collections (CONTENTdm) - Erie directories** — [https://digital.libraries.psu.edu/digital/api/search/searchterm/erie%20directory/maxRecord](https://digital.libraries.psu.edu/digital/api/search/searchterm/erie%20directory/maxRecords/50)  
  Only the 1918 American Agriculturalist rural farm directory of Erie County; no city directories. _(lane: directories)_
- **American Bicyclist and Motorcyclist on Google Books (editions of x_I6AAAAMAAJ)** — [https://books.google.com/books?q=editions:UOM39015023086989&id=x_I6AAAAMAAJ](https://books.google.com/books?q=editions:UOM39015023086989&id=x_I6AAAAMAAJ)  
  Vols 66-82 = 1945-1961 only; nothing for the gap. _(lane: gap-1923-1934)_
- **Motor Cycle, Motor Boat & Automobile Trade Directory (editions of on4AAAAAMAAJ)** — [https://books.google.com/books?q=editions:NYPL33433069077141&id=on4AAAAAMAAJ](https://books.google.com/books?q=editions:NYPL33433069077141&id=on4AAAAAMAAJ)  
  1909-1911 only. _(lane: gap-1923-1934)_
- **Chilton Automobile Directory 1924-32 / Automobile Trade Directory to 1922** — [https://books.google.com/books?id=filPMgm9zkUC](https://books.google.com/books?id=filPMgm9zkUC)  
  Manufacturers' buyers' guides (format image-checked in session 2); no dealers by town. _(lane: gap-1923-1934)_
- **Automotive Daily News 1925-1940 (archive.org pub_automotive-news)** — [https://archive.org/search?query=collection%3Apub_automotive-news](https://archive.org/search?query=collection%3Apub_automotive-news)  
  Full-text search: Indian appears only as stock and corporate news; no Erie dealer item; 'Bayhurst' 0 issues. _(lane: gap-1923-1934)_
- **LOC Erie phone-book OCR (local), 1920 cycle-dealer names, Furlong and Shannon** — [https://www.loc.gov/item/usteledirec07589/](https://www.loc.gov/item/usteledirec07589/)  
  Wickles Jno E wheel toys 657 W 18th (1934). No Furlong. Lester E Shannon residences only. No E 10th motorcycle business. _(lane: gap-1923-1934)_
- **LOC Erie telephone directories 1915-1933** — [https://www.loc.gov/resource/gdcmassbookdig.usteledirec07589/?sp=11](https://www.loc.gov/resource/gdcmassbookdig.usteledirec07589/?sp=11)  
  The reel index (seq11) lists only 1911, 1914 and 1934-1940 for Erie. The 1920s cannot be tested from LOC. _(lane: loc-phonebooks)_
- **Nelson's Biographical Dictionary of Erie County 1896 (nelsonsbiog00whit)** — [https://archive.org/download/nelsonsbiog00whit/nelsonsbiog00whit_djvu.txt](https://archive.org/download/nelsonsbiog00whit/nelsonsbiog00whit_djvu.txt)  
  Bicycle era only (Tribune Bicycle Works, J. F. Stuntz). _(lane: local-history)_
- **WPA Erie: a guide to the city and county 1938 (erieguidetocitya00federich, erieaguidetothe00fedemiss)** — [https://archive.org/details/erieguidetocitya00federich](https://archive.org/details/erieguidetocitya00federich)  
  No motorcycle, bicycle, Indian or Bayhurst. _(lane: local-history)_
- **Ries, History of Northwestern Pennsylvania 1943, 3 vols** — [https://archive.org/details/historyofnorthwe03ries](https://archive.org/details/historyofnorthwe03ries)  
  No motorcycle, Bayhurst or Kuivinen. _(lane: local-history)_
- **PowerLibrary site search (bayhurst, "Indian motorcycle(s)")** — [https://digitalarchives.powerlibrary.org/papd/islandora/search/bayhurst?type=dismax](https://digitalarchives.powerlibrary.org/papd/islandora/search/bayhurst?type=dismax)  
  Bayhurst: 22 hits, all yearbooks 1938-81 plus a Pa. Bulletin. Indian motorcycle hits are non-Erie. _(lane: local-history)_
- **Penn State CONTENTdm all collections (motorcycle, bayhurst, indian motorcycle)** — [https://digital.libraries.psu.edu/digital/bl/dmwebservices/index.php?q=dmQuery/all/CISOSEA](https://digital.libraries.psu.edu/digital/bl/dmwebservices/index.php?q=dmQuery/all/CISOSEARCHALL^bayhurst^all^and/title!date!subjec/date/100/1/0/0/0/0/json)  
  Only the 4 known Hammermill Bond pages. _(lane: local-history)_
- **AMCA forum thread 'Old Dealers web sites?' pages 1-5** — [https://forum.antiquemotorcycle.org/bboard/forum/technical-discussions-indian/scout/7062-o](https://forum.antiquemotorcycle.org/bboard/forum/technical-discussions-indian/scout/7062-old-dealers-web-sites)  
  No Erie. Points to oldindiandealers.com and to the CAIMAG 'Sidecar' dealer thread. _(lane: local-history)_
- **AMCA forum search (guest): Bayhurst / erie indian dealer / erie pennsylvania indian / beckman erie / erie** — [https://forum.antiquemotorcycle.org/bboard/search](https://forum.antiquemotorcycle.org/bboard/search)  
  0 hits for the specific terms. 'erie' = modern Lake Erie Chapter posts. _(lane: local-history)_
- **indianmotorcycles.net thread 'Anyone Know About Indian Dealer In Erie, PA?'** — [https://www.indianmotorcycles.net/threads/anyone-know-about-indian-dealer-in-erie-pa.1288/](https://www.indianmotorcycles.net/threads/anyone-know-about-indian-dealer-in-erie-pa.1288/)  
  2014-15 posts about the modern dealer only. _(lane: local-history)_
- **Harley-Davidson of Erie About Us** — [https://www.hderie.com/Dealer-Info/About-Us](https://www.hderie.com/Dealer-Info/About-Us)  
  Opened 1972; no pre-1972 history. _(lane: local-history)_
- **WebSearch: eBay/WorthPoint/collectibles (Erie Pa Indian dealer matchbook/decal/plate; worthpoint Erie Indian dealer)** — [https://www.ebay.com/itm/364725456088](https://www.ebay.com/itm/364725456088)  
  Only unrelated Erie plates and AAA toppers. No Erie Indian or Bayhurst items. _(lane: local-history)_
- **WebSearch: Bayhurst motorcycle Erie; Keystone Erie Motorcycle Club history; Indian Motorcycle Agency Erie 1936 11th; 1930s shop photo E 11th; Erie Harley-Davidson Sales 114 East 11th Kuivinen** — [https://www.indianmotorcycle.com/en-us/dealer-directory/pennsylvania/erie/3103300/](https://www.indianmotorcycle.com/en-us/dealer-directory/pennsylvania/erie/3103300/)  
  Modern dealers only. No historical photos. _(lane: local-history)_
- **Chronicling America - PA title list (loc.gov JSON via Playwright)** — [https://www.loc.gov/collections/chronicling-america/?dl=title&fa=location_state:pennsylvan](https://www.loc.gov/collections/chronicling-america/?dl=title&fa=location_state:pennsylvania&fo=json&c=150)  
  117 PA titles, 0 in Erie County. WebFetch facet query location_county:erie also returned 0. _(lane: newspapers)_
- **Chronicling America - full text 'Bayhurst' 1910-1960** — [https://www.loc.gov/collections/chronicling-america/?q=Bayhurst&dl=page&fo=json&dates=1910](https://www.loc.gov/collections/chronicling-america/?q=Bayhurst&dl=page&fo=json&dates=1910/1960)  
  5 pages, all non-Erie (OCR checked via tile.loc.gov word-coordinates). _(lane: newspapers)_
- **Chronicling America - full text 'LeJeal' 1905-1945** — [https://www.loc.gov/collections/chronicling-america/?q=LeJeal&dl=page&fo=json&dates=1905/1](https://www.loc.gov/collections/chronicling-america/?q=LeJeal&dl=page&fo=json&dates=1905/1945)  
  146 fuzzy hits; first 50 none Erie. _(lane: newspapers)_
- **Chronicling America - 'erie indian motorcycle' PA 1915-1945** — [https://www.loc.gov/collections/chronicling-america/?q=erie+indian+motorcycle&dl=page&fo=j](https://www.loc.gov/collections/chronicling-america/?q=erie+indian+motorcycle&dl=page&fo=json&dates=1915/1945&fa=location_state:pennsylvania)  
  579 pages (mostly Harrisburg Telegraph); OCR of top 25 grepped, only a false positive. _(lane: newspapers)_
- **Chronicling America - NY titles (western NY check)** — [https://www.loc.gov/collections/chronicling-america/?dl=title&fa=location_state:new+york&f](https://www.loc.gov/collections/chronicling-america/?dl=title&fa=location_state:new+york&fo=json&c=200)  
  59 NY titles, none in Chautauqua/Cattaraugus/Erie NY. _(lane: newspapers)_
- **Pennsylvania Newspaper Archive - searches (Bayhurst, 'indian motorcycle'+Erie, LeJeal, 'Erie motorcycle club', Beckman Erie Indian motorcycle, Corry motorcycle LeJeal)** — [https://panewsarchive.psu.edu/search/pages/results/?format=json&searchType=advanced&andtex](https://panewsarchive.psu.edu/search/pages/results/?format=json&searchType=advanced&andtext=Bayhurst)  
  No Erie-relevant item. OCR of 3 candidate pages checked. Date filter is ignored in JSON mode. _(lane: newspapers)_
- **archive.org FTS restricted to regional collections (Bayhurst, hill climb, Erie Motorcycle Club, Indian motorcycle, Kuivinen, motorcycle races)** — [https://archive.org/services/search/beta/page_production/?service_backend=fts&user_query=B](https://archive.org/services/search/beta/page_production/?service_backend=fts&user_query=Bayhurst&filter_map=%7B%22collection%22%3A%7B%22newspaperarchive-warren-times-mirror%22%3A%22inc%22%7D%7D)  
  Only 1951 Fisk-family Bayhurst item and post-1945 Warren Indian classifieds. _(lane: newspapers)_
- **archive.org FTS general ('"Bayhurst" motorcycle', '"Bayhurst" Indian Erie', '"Indian Motorcycle Agency" Erie', '"Indian motorcycle" "Erie, Pa"')** — [https://archive.org/services/search/beta/page_production/?service_backend=fts&user_query=%](https://archive.org/services/search/beta/page_production/?service_backend=fts&user_query=%22Bayhurst%22+Indian+Erie)  
  No Erie 1915-45 newspaper hit; only already-known 1955 Erie MC 114 E 11th. _(lane: newspapers)_
- **WebSearch (Bayhurst Erie motorcycle; Bayhurst obituary 1978; Indian dealer Erie East 11th/10th; Erie hill climb 1930s; site:newspapers.com Bayhurst Erie; site:newspaperarchive.com Erie Indian motorcycle)** — [https://www.bing.com/](https://www.bing.com/)  
  No historical hits; only leads newspage 88270669 / 170653115 (unverified). _(lane: newspapers)_
- **NARA 1940 census images T627 roll 3651 (ED 68-122) 00585-00592** — [https://catalog.archives.gov/medialz/census-1940/T627/PA/m-t0627-03651/m-t0627-03651-00586](https://catalog.archives.gov/medialz/census-1940/T627/PA/m-t0627-03651/m-t0627-03651-00586.jpg)  
  129 W 25th held a non-Bayhurst household in Apr 1940; Lewis J. not found there. _(lane: people-bayhurst)_
- **Chronicling America search 'Bayhurst' (WebFetch loc.gov JSON)** — [https://www.loc.gov/collections/chronicling-america/?q=Bayhurst&fo=json&c=50](https://www.loc.gov/collections/chronicling-america/?q=Bayhurst&fo=json&c=50)  
  20 hits, none in Erie. Erie Dispatch-Herald 1925-57 is not digitized at LOC (sn87078352, directory_only). _(lane: people-bayhurst)_
- **Journal of Erie Studies 'additions to collections' PDF** — [https://journals.psu.edu/eriestudies/article/download/275/265/525](https://journals.psu.edu/eriestudies/article/download/275/265/525)  
  No Bayhurst or motorcycle entries. _(lane: people-bayhurst)_
- **archive.org Motorcycling (Chicago) issues 1914-1919 (motorcycling-190514 set, motorcycling-magazine, -130217, -1918, -240919, -221019_20211026, -020614)** — [https://archive.org/details/motorcycling-190514](https://archive.org/details/motorcycling-190514)  
  20 issues grepped; no Erie dealer mentions. _(lane: trade-press)_
- **archive.org metadata searches: 'motorcycle and bicycle illustrated', 'motorcycling and bicycling', 'pacific motorcyclist', 'harley-davidson enthusiast', 'american motorcyclist and bicyclist', 'Indian news', motorcyclist 1919-1940** — [https://archive.org/advancedsearch.php](https://archive.org/advancedsearch.php)  
  No 1918-1921 or 1923-1940 motorcycle trade journals on archive.org apart from those listed above. No Indian News house organ. _(lane: trade-press)_
- **Popular Mechanics (ads) via Google Books snippets** — [https://books.google.com/books?id=vN4DAAAAMBAJ](https://books.google.com/books?id=vN4DAAAAMBAJ)  
  No Erie motorcycle dealer ads among the hits. _(lane: trade-press)_
- **The Motorcyclist / Pacific Motorcyclist / Indian News 1920s-1930s** — [https://www.google.com/books/feeds/volumes](https://www.google.com/books/feeds/volumes)  
  No Erie dealer or Bayhurst hits in any Google Books-indexed volume. Not on archive.org. _(lane: trade-press)_

## BLOCKED

- **Common Crawl index server (index.commoncrawl.org)** — [https://index.commoncrawl.org/collinfo.json](https://index.commoncrawl.org/collinfo.json)  
  Connection reset twice; empty reply on CC-MAIN-2014-10-index query. _(lane: dealer-lists)_
- **CAIMAG forum live (caimag.com/forum)** — [http://www.caimag.com/forum/forum.php](http://www.caimag.com/forum/forum.php)  
  HTTP 522 twice (site offline since 2020 per AMCA thread 23629). _(lane: dealer-lists)_
- **indianmotorcycles.net 'List of Indian Dealerships in the United States and Canada' (thread 2610)** — [https://www.indianmotorcycles.net/threads/list-of-indian-dealerships-in-the-united-states-](https://www.indianmotorcycles.net/threads/list-of-indian-dealerships-in-the-united-states-and-canada.2610/)  
  Proof-of-work bot challenge (202), and WebFetch was redirected to tollbit pay gate. Snippets show it is a modern dealer list anyway. _(lane: dealer-lists)_
- **chiefmotorcycleforum.com topic 5526 'Indian Motorcycle of Erie Pa.'** — [https://www.chiefmotorcycleforum.com/index.php?topic=5526.0](https://www.chiefmotorcycleforum.com/index.php?topic=5526.0)  
  Same bot challenge and tollbit redirect. Likely about the modern dealer. _(lane: dealer-lists)_
- **Jerry Hatfield, Indian Chief Motorcycles 1922-1953 (archive.org indianchiefmotor00hatf)** — [https://archive.org/details/indianchiefmotor00hatf](https://archive.org/details/indianchiefmotor00hatf)  
  Lending-only; djvu.txt returns 401. FTS 'Erie' hit = a person, Indian News road tester Erie 'Red' Armstrong. _(lane: dealer-lists)_
- **FamilySearch catalog 541218 (WebFetch) and catalog API** — [https://www.familysearch.org/en/search/catalog/541218](https://www.familysearch.org/en/search/catalog/541218)  
  WebFetch got only a sign-in page; the API /service/search/catalog/item/541218 returned 401. Login required. Not retried. _(lane: directories)_
- **HathiTrust babel full-text search (1939 Erie directory)** — [https://babel.hathitrust.org/cgi/pt/search?q1=Bayhurst&id=pst.000012006779](https://babel.hathitrust.org/cgi/pt/search?q1=Bayhurst&id=pst.000012006779)  
  403 Cloudflare 'Just a moment'; the IP block is known from ACCESS.md. One attempt. Added to manual steps. _(lane: directories)_
- **DPLA item 'Erie Directory, 19-'** — [https://dp.la/item/233fc59390a68f6234b292642a598155](https://dp.la/item/233fc59390a68f6234b292642a598155)  
  curl 202 (bot check) and WebFetch empty. Probably the HathiTrust record. _(lane: directories)_
- **Masthof Erie County PA Directory Collection (1873-1960)** — [https://www.masthof.com/products/erie-county-pa-directory-collection-1873-1960](https://www.masthof.com/products/erie-county-pa-directory-collection-1873-1960)  
  404 to curl (twice, including .json) and to WebFetch. Search-engine summary says it contains the Atkinson 1925-26 and 1937 directories. _(lane: directories)_
- **MyHeritage public names page** — [https://www.myheritage.com/names/charles_bayhurst](https://www.myheritage.com/names/charles_bayhurst)  
  curl 403; WebFetch empty. _(lane: directories)_
- **Erie Society for Genealogical Research - Hagen holdings page** — [https://www.genealogyerie.org/p/Hagen-History-Center-Holdings](https://www.genealogyerie.org/p/Hagen-History-Center-Holdings)  
  Page needs JavaScript; curl got an empty shell. One attempt. _(lane: directories)_
- **HathiTrust (babel)** — [https://babel.hathitrust.org/](https://babel.hathitrust.org/)  
  IP-blocked (per ACCESS.md); manual steps M7 and M8. _(lane: gap-1923-1934)_
- **oldindiandealers.com** — [https://www.oldindiandealers.com](https://www.oldindiandealers.com)  
  Unreachable (per ACCESS.md). No mirror found; web.archive.org blocked here. _(lane: local-history)_
- **Hagen PastPerfect online catalog** — [https://eriehistory.catalogaccess.com/](https://eriehistory.catalogaccess.com/)  
  curl default UA 403. Browser UA loads the shell but results are JS-only. Headless Chromium 403. Manual step. _(lane: local-history)_
- **Chronicling America - quoted phrase queries and later queries** — [https://www.loc.gov/collections/chronicling-america/?q=%22indian+motorcycle+agency%22&dl=p](https://www.loc.gov/collections/chronicling-america/?q=%22indian+motorcycle+agency%22&dl=page&fo=json)  
  HTTP 502 'upstream request failed' on every quoted-phrase query; later 500/429 Cloudflare; WebFetch item page 403. Stopped. _(lane: newspapers)_
- **FultonHistory.com** — [https://fultonhistory.com/](https://fultonhistory.com/)  
  503 Service Unavailable x3 (home, Fulton.html, All Newspapers folder). _(lane: newspapers)_
- **erielibrary.org (NewsBank page, accordion page, obituary listings)** — [https://erielibrary.org/databases/historical-erie-newspapers-on-newsbank/](https://erielibrary.org/databases/historical-erie-newspapers-on-newsbank/)  
  curl timeout/000; WebFetch 503 x2. _(lane: newspapers)_
- **newspapers.com paper/newspage pages** — [https://www.newspapers.com/paper/the-lake-shore-visitor/34014/](https://www.newspapers.com/paper/the-lake-shore-visitor/34014/)  
  curl 403 x2, WebFetch 403 x2 (also newspage 88270669). _(lane: newspapers)_
- **GenealogyBank Erie newspaper list** — [https://www.genealogybank.com/explore/newspapers/all/usa/pennsylvania/erie](https://www.genealogybank.com/explore/newspapers/all/usa/pennsylvania/erie)  
  curl 202 empty; Playwright 403 CloudFront. _(lane: newspapers)_
- **Catholic News Archive** — [https://www.thecatholicnewsarchive.org/?a=cl&cl=CL1](https://www.thecatholicnewsarchive.org/?a=cl&cl=CL1)  
  301 then Cloudflare 403; not pursued (LSV is on newspapers.com anyway). _(lane: newspapers)_
- **NYS Historic Newspapers - Chautauqua County titles** — [https://www.nyshistoricnewspapers.org/titles/place/new_york_chautauqua/](https://www.nyshistoricnewspapers.org/titles/place/new_york_chautauqua/)  
  403 / Cloudflare 'Performing security verification' (not solved); WebFetch 403. _(lane: newspapers)_
- **Google News Archive ('Erie News' nid=z0_F5_TITjQC)** — [https://news.google.com/newspapers?nid=z0_F5_TITjQC&hl=en](https://news.google.com/newspapers?nid=z0_F5_TITjQC&hl=en)  
  302 to google.com/sorry CAPTCHA (curl and WebFetch). _(lane: newspapers)_
- **Google Books edition page and search-inside (headless Chromium)** — [https://www.google.com/books/edition/_/setXAAAAYAAJ?gbpv=1&bsq=Bayhurst](https://www.google.com/books/edition/_/setXAAAAYAAJ?gbpv=1&bsq=Bayhurst)  
  'Preview unavailable'. Classic books.google.com search-inside redirects to google.com/sorry (CAPTCHA, not attempted); googleapis returns 429. _(lane: people-bayhurst)_
- **Find a Grave** — [https://www.findagrave.com/cemetery/44764/erie-cemetery](https://www.findagrave.com/cemetery/44764/erie-cemetery)  
  403 Cloudflare according to ACCESS.md; not retried. _(lane: people-bayhurst)_
- **rootsweb paerie Mt of Olives cemetery page** — [https://sites.rootsweb.com/~paerie/cemeteries/MtofOlivesCem.htm](https://sites.rootsweb.com/~paerie/cemeteries/MtofOlivesCem.htm)  
  curl 403; WebFetch 403. _(lane: people-bayhurst)_
- **FamilySearch record search** — [https://www.familysearch.org/search/record/results?q.givenName=Charles&q.surname=Bayhurst](https://www.familysearch.org/search/record/results?q.givenName=Charles&q.surname=Bayhurst)  
  307 to /en/ page; API returns 401 (login required). _(lane: people-bayhurst)_
- **indianmotorcycles.net and chiefmotorcycleforum.com Erie dealer threads** — [https://www.indianmotorcycles.net/threads/anyone-know-about-indian-dealer-in-erie-pa.1288/](https://www.indianmotorcycles.net/threads/anyone-know-about-indian-dealer-in-erie-pa.1288/)  
  Proof-of-work challenge page, then tollbit redirect; not pursued. _(lane: people-bayhurst)_
- **sortedbyname.com** — [https://sortedbyname.com/letter_b/index.html](https://sortedbyname.com/letter_b/index.html)  
  403 for curl and WebFetch. _(lane: people-bayhurst)_
- **Erie Cemetery Association burial search (discovereverafter)** — [https://eriecemetery.discovereverafter.com/](https://eriecemetery.discovereverafter.com/)  
  Cloudflare 'Just a moment' challenge; not attempted. _(lane: people-bayhurst)_
- **DPLA search** — [https://dp.la/search?q=%221940+Census+Enumeration+District+Descriptions%22+Erie](https://dp.la/search?q=%221940+Census+Enumeration+District+Descriptions%22+Erie)  
  HTTP 202 with no content. _(lane: people-bayhurst)_
- **Google Books volume pages / search-inside (books.google.com/books?id=XXsAAAAAMAAJ&q=Bayhurst)** — [https://books.google.com/books?id=XXsAAAAAMAAJ&q=Bayhurst](https://books.google.com/books?id=XXsAAAAAMAAJ&q=Bayhurst)  
  302 redirect to google.com/sorry (CAPTCHA). One attempt only, not retried. GData says the 1919 volumes are view_no_pages anyway. _(lane: trade-press)_
- **HathiTrust babel full-text/page viewer** — [https://babel.hathitrust.org/cgi/pt?id=nyp.33433069061871](https://babel.hathitrust.org/cgi/pt?id=nyp.33433069061871)  
  Hard IP block per ACCESS.md; not attempted. Listed in manual_steps. _(lane: trade-press)_

## ORCHESTRATOR ACCESS TESTS (before the lanes ran, 4 Oct 2026)

- **LOC item JSON www.loc.gov/item/usteledirec07589/?fo=json** — curl: Cloudflare challenge (403). Headless Chromium: "Verify you are human" CAPTCHA (not solved, by rule). WebFetch tool: **worked**, gave the tile.loc.gov paths. → partial
- **tile.loc.gov storage-services/public/gdcmassbookdig/usteledirec07589/usteledirec07589.text.json** (and 07590) — **hit**: full per-page OCR for both Erie reels (951 and ~950 sequences); page images via IIIF.
- **LOC reel index (seq 11)** — **hit**: "ERIE, PA. 1911, 1914, 1934, 1935, 1936, 1937, 1938, 1939, 1940" → no 1915-1933 phone books exist on LOC. Reel 07590: 1941-1947.
- **HathiTrust babel.hathitrust.org** (pt, pt/search, ls, imgsrv, htd, ssd) — **blocked**: "Sorry, your attempt to access HathiTrust has been blocked ... IP address' reputation" + Cloudflare. WebFetch: 403.
- **HathiTrust catalog API** catalog.hathitrust.org/api/volumes/full/htid/… — **hit**: pst.000012006779 = 1939, full view (pdus); the five "search-only" volumes in the brief (pst.000045169922, 000045170812, 000029952809, 000008598660, 000010091890) are 1972-1984 editions (dates from Google Books metadata), so out of scope.
- **Google Books classic** books.google.com/books?id=…&q=… — **blocked** (429 rate limit). googleapis.com/books/v1 — 429.
- **Google Books GData full-text feed** www.google.com/books/feeds/volumes?q=… — **hit**: snippet search across the whole corpus (lead generator).
- **archive.org** advancedsearch + full-text search API (services/search/beta/page_production, backend fts) — **hit**.
- **web.archive.org (Wayback Machine)** — **blocked** (connection reset at the egress proxy; WebFetch refuses the host).
- **oldindiandealers.com** — **blocked** (no response).
- **findagrave.com** — **blocked** (Cloudflare 403; WebFetch 403).
- **erielibrary.org** — **blocked** (503 / timeout).
- **AMCA forum thread "Old Dealers web sites?"** — reachable (200); pages 1-5 read by the local-history lane: no Erie entry.
- **Gemini Deep Research (optional lead generator)** — **not run**: needs the NUC agent-desktop browser and a fresh AUTH_OK; NUC offline.
- **Flight Recorder / Brain changelogs** — **not available** (NUC offline). This file is the run log.

## BROAD SWEEP "anything Indian motorcycle in Erie" (orchestrator, 4 Oct 2026)

- **Motorcycle & Bicycle Illustrated, 10 Aug 1922, p.39** — [archive.org leaf 305](https://archive.org/details/motorcycleillustrated/motorcycleillustrated1922c/page/n305) — **hit**: "Frank J. Weschler Heads Hendee Co.", "in his native town of Erie, Pa." (image).
- **Western Massachusetts: A History 1636-1925, v.4 (1926), p.799** — [archive.org leaf 591](https://archive.org/details/westernmassachus04lock/page/799) — **hit**: Weschler born Erie 6 Mar 1883; Indian president 1923 (image).
- **Springfield, MA city directories 1915, 1923 (archive.org full text)** — [1915](https://archive.org/details/springfieldcityd1915spri) · [1923](https://archive.org/details/springfieldwests1923spri) — **hit**: Weschler's Hendee/Indian offices (text).
- **Google Books feed: Weschler / Erie / Indian** — **hit** (snippets): Iron Age 1927 (resigned to Baldwin Chain), Iron Trade Review 1927, History of Massachusetts Industries 1930, Reed 1925 (a Weschler brother in Erie).
- **Google Books feed: Erie race meet 1920** — **partial**: "Erie, Pa., race meet at Exposition grounds half-mile track. Erie Exposition Association, promoters" (snippet; the "Indian Motorcycle Club" in that list is Hammond, Ind.).
- **Google Books feed: post-war Erie Indian dealer, clubs, hill climbs** — **miss** (only club calendars and modern listings); the feed began returning "Internal error" (rate limit), so searching stopped.
- **WebSearch: modern Erie Indian dealer** — **hit** (summaries): Indian Motorcycle of Erie / Off-Road Express, 10320 Wattsburg Rd, 814-825-2396; Great Lake Gypsies Chapter 1901 (2014).
- **indianmotorcycle.com dealer directory, offroaderie.com** — **blocked** (403 to curl and WebFetch).
- **indianmotorcycles.net thread "Anyone Know About Indian Dealer In Erie, PA?", chiefmotorcycleforum.com topic 5526** — **blocked** (JS check, then TollBit pay-per-crawl, HTTP 402; not paid).
- **policemotorunits.com Erie PA page** — **blocked** (DNS failure for WebFetch, timeout for curl). Its claim that Erie police "always" rode Harley-Davidsons (from the search summary) is contradicted by Motorcycle Illustrated, 13 Apr 1916 ("ordering two Indians", image).
- **City of Erie Police Motorcycle Unit page** — [erie.pa.us](https://www.erie.pa.us/community/police_department/divisions/patrol/motorcycle_unit.php) — **hit** (WebFetch summary): "started in 1910 … has always ridden Harley-Davidson motorcycles". Contradicted by the 1916 Indian order (image).
- **Bicycling World 1909-1911 (archive.org: bicyc60251909191910newy, bicyc6126171910newy, bicyc6224191081911newy, bicyclingwo6325161911newy)** — **miss**: no Erie police motorcycle item; the 1911 Le Jeal/Thor police snippet comes from New American Motorcyclist and Bicyclist 1911 (HathiTrust nyp.33433017524582, IP-blocked here).
- **archive.org full text "Erie police" motorcycle** — **partial**: a 1934 wire item names an Erie "Motorcycle Patrolman Ames Kiddle/Kindle" (Bremer kidnapping clippings, item BremerKidnapping); make not stated.
