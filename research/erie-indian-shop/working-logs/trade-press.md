# Lane: trade-press — working log (started 2026-10-04)

Goal: Erie, Pa. motorcycle dealers (Indian, Harley, Excelsior/Henderson etc.) named in motorcycle trade journals 1910-1940;
Charles Bayhurst racing/club ties. Tools: tools/gbfeed.py (Google Books full-text snippets), tools/iafts.py (archive.org FTS).

## Log

### 1. Google Books feed (gbfeed) — raw output in lanes/trade-press/gb_raw.log
- '"Erie, Pa." Bayhurst' -> only non-motorcycle hits (tailor's union 1907 G. Bayhurst, American Rifleman 1929 L. Bayhurst rifle team).
- 'Bayhurst motorcycle' -> Motorcycle Illustrated 1919 (XXsAAAAAMAAJ) snippet "(motorcycle) -Won by Charles Bay- hurst ; second , Charles Schroeder" (LEAD, already known).
- '"Charles Bayhurst"' -> 1 hit: "List of Motor Vehicle Registrations and Licenses" 1917 (yhRbAAAAYAAJ, NYPL) no snippet. LEAD (prob. Pa. registrations).

### 2. archive.org FTS (iafts) — raw output in lanes/trade-press/ia_raw.log
- 'Bayhurst Erie' -> only yearbooks (1943 Erie Tech Charles Bayhurst etc.), no trade press.
- '"Erie Cycle Dealers"' -> 0.
- '"Erie Motorcycle Club"' -> hits in item `motorcycleillustrated` (Crittenden Automotive Library: MI compilations
  1905a,1908,1909a,1912a,1912b,1913a,1914a,1915b,1916a,1916b,1917a,1917c,1922b,1922c,1922d), Automobile Journal,
  American Motorcycle Girls (Keystone Erie Motorcycle Club), Greater Erie 1913.
- Downloaded all 15 MI djvu.txt to lanes/trade-press/txt/mi_*.txt and grepped locally.
- Leaf numbers via archive.org search-inside (lanes/trade-press/si.py); page images via BookReaderImages.php
  (zip=/31/items/motorcycleillustrated/<doc>_jp2.zip, file=<doc>_jp2/<doc>_NNNN.jp2, scale=2/4/8).

### 3. VERIFIED ON IMAGE
- Motorcycle and Bicycle Illustrated, Dec 7, 1922, p.21, item motorcycleillustrated doc motorcycleillustrated1922d leaf 373
  "Turning a Fan Into a Dealer": "A. D. Beckman, who has hung out his sign on the new Indian agency at 1807 Parade street,
  and opened up with a full line of Indian motorcycles, sidecars, bicycles, parts and accessories." Also: riding since 1909;
  charter member of the Erie club organized 1910, club rooms at 2510 Peach street; club secretary and F.A.M. Commissioner six
  years, president past three years, M. and A.T.A. referee; asst. branch manager Armour & Co. Erie branch 16 years.
  "Mr. Beckman has installed Charles Schroeder, who was in the repair department of the LeJeal Mobile and Cycle Works,
  former Indian dealers at Erie, for the past five years, in the service department of the new agency."
  Caption: "A. D. Beckman, new Indian dealer at Erie, Pa." (portrait photo). Niece Miss Louise Weschler.
  Evidence: evidence/1922-12-07_motorcycle-bicycle-illustrated_p21_leaf373_beckman-1807-parade.png, ..._schroeder-lejeal.png
- Motorcycle and Bicycle Illustrated, Nov 23, 1922 (date from facing leaves 291/293), p.20 "Among the Dealers", leaf 292:
  "NEW INDIAN DEALER AT ERIE / Erie, Pa.—"Archie" Beckman, a well-known and popular figure among motorcyclists in this city
  for the past fifteen years, has taken on the local Indian agency."
  Evidence: evidence/1922-11-23_motorcycle-bicycle-illustrated_p20_leaf292_new-indian-dealer-erie.png
=> "Beckna" in the 1917 GB snippet = OCR damage of A. D. Beckman.

### 4. More VERIFIED ON IMAGE (archive.org item motorcycleillustrated / Bicycling World items)
- Bicycling World and Motorcycle Review, Vol. LXIV No. 25, Sat. March 9, 1912, pp.1214-1215, item bicycli64231911161912newy
  leaves 1286-1287. "ERIE'S ATTRACTIVE SHOW" (Erie, Pa., March 1; first auto & motorcycle show, Arbuckle's garage).
  "The largest exhibit was that of the LeJeal Cycle Works, agent for the Indian, while the honors for the best decorated booth
  went to M. A. Reinholtz, the Thor agent". Exhibitors: M. A. Reinholtz (Thor; Cleveland & Vim bicycles; M.A. & H.H. Reinholtz,
  C. A. Kent); Penn Sales Co. (Pierce; M. M. Gillespie, H. G. Pohl); Coleman Bros. (Excelsior & Flanders; Rambler & Pierce bicycles;
  George W. Coleman); Anderson Cycle Works (Harley-Davidson; C. Brown, John Wills, T. R. Anderson); Miller Hardware Co.
  (Iver-Johnson); John P. Arbuckle (bicycles, Cleveland & Vim); "LeJeal Cycle Works—Indian motorcycles; Pope bicycles.
  Represented by C. H. LeJeal, George Fry, Claude Torrance." Photos: Indian booth sign "INDIAN MOTOCYCLES LeJeal Cycle Works";
  Anderson sign "ANDERSON CYCLE WKS. 546 WEST 18th"; Thor sign "M.A. REINHOLTZ 1717 S[ASSAFRAS]".
  Evidence: evidence/1912-03-09_bicycling-world-motorcycle-review_p1214_leaf1286_erie-show-lejeal-indian.png,
  ..._p1215_leaf1287_erie-show-exhibitors.png, ..._p1215_leaf1287_lejeal-indian-booth-photo.png
- Motor Cycle Illustrated, Jan 4, 1917, p.35, doc motorcycleillustrated1917a leaf 43: "ERIE M. C.'S STAFF FOR 1917" O. R. Sonneson
  pres.; Wm. Edwards v-p; A. D. Beckman secretary; R. J. Oboth fin. sec.; F. F. Farrell treas.; Lamont Vance captain; H. C. Schaefer
  lieut.; exec. com. adds O. H. Busche, T. L. Mowery. "...Mr. Beckman's sixth year in the capacity of secretary."
  Evidence: evidence/1917-01-04_motorcycle-illustrated_p35_leaf43_erie-mc-officers.png
- Motor Cycle Illustrated, Jan 11, 1917, p.19, leaf 75: photo of Indian Powerplus motor sled; sled lettered "LE JEAL CYCLE WORKS
  18TH [&] SASSAFRAS"; caption "The Winter Machine Built Around an Indian Twin by the Le Jeal Cycle Works, of Erie, Pa., the Local
  Hendee Representative". Evidence: evidence/1917-01-11_motorcycle-illustrated_p19_leaf75_lejeal-hendee-representative.png
- Motor Cycle Illustrated, March 29, 1917, p.23, leaf 627: store interior photo, caption "The Store of the Anderson Cycle Works,
  Harley-Davidson Agents in Erie, Pa., ..." Evidence: evidence/1917-03-29_motorcycle-illustrated_p23_leaf627_anderson-cycle-works-store.png
- Motorcycle and Bicycle Illustrated, Aug 30, 1917, p.32, doc motorcycleillustrated1917c leaf 448: "TRADE ACTIVITIES IN ERIE /
  Erie, Pa., Aug. 20.—Charles LeJeal of the LeJeal Cycle & Mobile Works, of Erie, states that he will specialize hereafter on repairs
  for magnetos and speedometers, in addition to handling Indian motorcycles and bicycles." Also C. H. Retcher / Gas Engine and Cycle
  Company, 9 East 7th street (Pope bicycles); F. J. Seifert, 1015 Parade street; H. D. Trow, 337 W. 18th street; F. E. Montgomery &
  E. E. Sury, Erie Cycle & Supply House, 1718 State street ("Casino" tires); Anderson Cycle Works, Harley-Davidson agents, 75 machines,
  bicycles Harley-Davidson, Emblem, Star. Evidence: ..._p32_leaf448_trade-activities-erie-a.png and -b.png
- Motorcycle and Bicycle Illustrated, Sept 27, 1917, p.43, leaf 667: photo No. 8 storefront "ANDERSON CYCLE WORKS / CYCLE SUPPLIES /
  MOTOR-CYCLES"; text "Erie, Pa., is "some cycle town" as everyone knows, and the Anderson Cycle Works, No. 8, maintains a prosperous
  store at 540 West 18th street". Evidence: evidence/1917-09-27_motorcycle-bicycle-illustrated_p43_leaf667_anderson-540-w18th.png
  NOTE address conflict: 546 W. 18th (1912 F.A.M. registered shop list + 1912 show sign) vs 540 W. 18th (1917 text). Both kept.

### 5. Text-only (OCR read, not yet image-verified)
- MI 1908 (mi_1908.txt l.34396): agents list "...Le Jeal Cycle Co., 1721 Sassafras st." (Erie line, OCR garbled city).
- MI 1905a: F.A.M. local commissioner "Erie, C. H. LeJeal".
- BW 1909 (bicyclingwo5927181909newy leaf 1007): Erie (Pa.) Motorcycle Club meet, "Charles Le Jeal, Indian" 3rd in twin mile, won
  5-mile handicap; W. R. Kellam (Merkel) won 10-mile; T. Anderson (H-D); George Frye (Merkel); Harry Reinholz (Thor).
- BW 1909 (bicycli58261908201909newy l.150124): "Erie Motorcyclists Organizing Club. In response to a call issued by W. R. Kellam".
- BW 1910: May 30 "Erie Motorcycle Association's racemeet at Reed track".
- MI 1912b: F.A.M. clubs "No. 72, Erie, Erie, Pa. 24 members". MI 1912a: registered F.A.M. shop "T. R. Anderson, 546 W. 18th St., Erie".
- MI 1915b: "Erie Motor Sales Co., local R-S agents" (Reading Standard). MI 1916a: "Photo by Agent Ackerman" (R-S, Erie).
- MI 1916a: "ERIE, Pa—This city is determined that its police department shall keep abreast of the times, and has indicated this
  policy by ordering two Indians." MI 1916a: Jno. E. Wickles, Bicycles & Supplies, 724 E. 26th St., Erie.
- MI 1916a: Frank J. Weschler (Hendee treasurer & sales manager) "was born at Erie, Pa. March 6, 1883"; MI 1922c: began 1898 in
  repair dept of Black Mfg. Co. (Tribune bicycles), Erie. Beckman's niece = Miss Louise Weschler (relationship to F.J. UNVERIFIED).
- MI 1922c Aug 10 1922 p.26: "Archie Beckman, of Erie, Pa., brought his wife and niece with him." (Rochester rally)
- MI 1922c: "RACES AT ERIE, P." July 29 [1922]: Harley riders C. F. Bratt, R. C. Phillips, Vern Squire; referee H. W. Hahne.
- Harley-Davidson Enthusiast 1923-24 (motorcycleenthus1923unse): Erie Gypsy Tour "managed" by W. M. Furlong; Tony De Santi, Erie, Pa.
  at 3rd Mechanics' School at factory.

### 6. Google Books / HathiTrust
- 1919 MI volumes XXsAAAAAMAAJ (= HathiTrust nyp.33433069061871, v.15 July-Sept 1919) and jHsAAAAAMAAJ (= nyp.33433069061889, v.15
  Oct-Dec 1919): GData viewability = view_no_pages (snippet only). books.google.com search-inside -> 302 to google.com/sorry (CAPTCHA)
  = BLOCKED (1 attempt, not retried). HathiTrust babel blocked (per ACCESS.md). Catalog API: both "Full view" -> manual step.
- HathiTrust record 008608578 = Motorcycle Illustrated full view 1908-1922 (list in ht_008608578.json).
- GB snippet leads: 1911 New American Motorcyclist and Bicyclist (XyNaAAAAYAAJ = NYPL 33433017524582): "...Le Jeal, Thor and Indian
  agents, respectively, in Erie, Pa., have each placed a machine with the Erie police department". 1920 MI (UHoAAAAAMAAJ =
  nyp.33433069061905 Apr-June 1920): "Erie can feel justly proud of its progress in cycling ... Le Jeal's store was held and the
  program mapped out." Tales of Old Erie 1958: "LeJeal's motorcycle store on Sassafras Street and borrowed two Indian Motorcycle tanks".
  Twentieth Century History of Erie County 1909: "Lejeal Cycle & Mobile Works, begun in 1894". Gas Engine 1914: "Le Jeal Cycle & Mobile
  Works, 1721- 1723 Sassafras St., Erie, Pa."

### 7. Further VERIFIED ON IMAGE
- Motorcycle Illustrated Vol. III No. 8, July 15, 1908, p.[1], doc motorcycleillustrated1908 leaf 265: "SWENSON'S RIDE" (B. A.
  Swenson, Indian rider, NY-Chicago); checking points list: "Erie, Pa. ...........Le Jeal Cycle Co., 1721 Sassafras st."
  Evidence: evidence/1908-07-15_motorcycle-illustrated_leaf265_swenson-checkpoint-lejeal-1721-sassafras.png
- Bicycling World and Motorcycle Review, Sat. Sept 11, 1909, p.929, item bicyclingwo5927181909newy leaf 1007: "Motorcycles Save the Day
  at Erie." meet promoted by the Erie (Pa.) Motorcycle Club "on the 30th ult." [= Aug 30, 1909]; "Charles Le Jeal, Indian, third" in
  twin-cylinder mile; Le Jeal won 5-mile handicap; 2nd in 10-mile handicap. Also T. Anderson (Harley-Davidson), George Frye (Merkel),
  W. R. Kellam (Merkel), Harry Reinholz (Thor), Eugene Gallagher (H-D).
  Evidence: evidence/1909-09-11_bicycling-world-motorcycle-review_p929_leaf1007_erie-mc-meet-lejeal-indian.png
- Motor Cycle Illustrated, Aug 19, 1915, p.14, doc 1915b leaf 520: photo + "DEMONSTRATED WITH A TRAILER ... demonstrated by the Erie
  Motor Sales Co., local R-S agents". Evidence: evidence/1915-08-19_motorcycle-illustrated_p14_leaf520_erie-motor-sales-rs-agents.png
- Motor Cycle Illustrated, April 13, 1916, p.13, doc 1916a leaf 957: "MOUNTING THE ERIE COPS / ERIE, Pa.—This city is determined that
  its police department shall keep abreast of the times, and has indicated this policy by ordering two Indians."
  Evidence: evidence/1916-04-13_motorcycle-illustrated_p13_leaf957_erie-police-two-indians.png
- The Harley-Davidson Enthusiast No. 63, p.9, item motorcycleenthus1923unse leaf 181: photo; "Erie, Pa., had such a big turnout for its
  Gypsy Tour that we're able to show only one-half of them here. "Everybody had a good time," wrote W. M. Furlong, who managed things."
  Evidence: evidence/1923_harley-davidson-enthusiast_no63_p9_leaf181_erie-gypsy-tour-furlong.png
- The Harley-Davidson Enthusiast No. 64, p.21, leaf 221: J. E. Young trip (left Altoona Sunday June 10th on a "23JD" => 1923):
  "After leaving Oil City, Pa., we headed for Erie, stopped there long enough to enjoy the hospitality of Mr. Furlong, the
  Harley-Davidson dealer". Exact month of No.63/64 not printed on these pages (1923, summer/autumn).
  Evidence: evidence/1923_harley-davidson-enthusiast_no64_p21_leaf221_furlong-hd-dealer-erie.png
- MI 1922c (text only): Rochester rally attendee list includes "A. D. Beckman Erie", "Walter M. Furlong Erie", "Roy J. Bierbour Erie",
  "August Hardner Erie". MI 1922b May 18, 1922 (text only): "Erie—Erie M. C.—Geo. Witterauer, Wood St., R. F. D. 4."
  NOTE: GB snippet showing "Erie M. C. - Geo. Witterauer ... E. 10th St." is misleading - the "E. 10th St." belongs to a later
  (non-Pennsylvania) entry before "HAWAII"; it is NOT an Erie address.

### 8. 1919 Bayhurst race - snippet analysis (Google Books, snippet-only volume XXsAAAAAMAAJ = HT nyp.33433069061871, v.15 Jul-Sep 1919)
Snippets assembled from queries 'Bayhurst motorcycle', '"Charles Rainbow" Erie', 'Billman Erie bicycle race 1919',
'Schutte Bayhurst Schroeder', 'Erie bicycle motorcycle races July 1919 Schroeder':
  "... Erie Cycle Dealers' Association. The eight-mile motorcycle race for sidecar outfits was won by M. B. Schutte. The summary:
  Two-mile handicap - Won by Walter Brierly; second, Charles Rainbow; third, Henry Billman; fourth, Richard Baker. Time, 5:07 3/5 ..."
  "... (motorcycle) -Won by Charles Bay- hurst; second, Charles Schroeder. Time, 7:13 3/5. Three-mile handicap - Won by Walter Brierly;
  second, Charles Rainbow; third, Henry Billman; fourth, Wilbur Wilson. Time, 8:07 3/5. Eight-mile (motorcycle) -Won by M. B. Schutte"
  "... Schutte; second, Archie Lewis; third, Charles Schroeder; fourth ..."   One snippet page footer: "July 17, 1919 MOTORCYCLE AND
  BICYCLE ILLUSTRATED" (may or may not be the same page). => SNIPPET-LEAD: a July 1919 race meet connected with the Erie Cycle Dealers'
  Association; Charles Bayhurst won a motorcycle event, Charles Schroeder (LeJeal's Indian repairman per Dec 1922 article) 2nd.
  Exact date/venue/make ridden NOT confirmed. The separate Oct-Dec 1919 volume (jHsAAAAAMAAJ) mentions the Erie Cycle Dealers'
  Association re a salesmanship talk - different item.
- GB "Chas. Bayhurst": Pa. Highway Dept "List of Motor Vehicle Registrations and Licenses" Jan 2-31, 1917 (CxRbAAAAYAAJ =
  HT nyp.33433090814942): "Chas. Bayhurst, R. F. D. No. 5, Erie." (snippet; vehicle type unknown). "A. D. Beckman" appears in the
  June-Nov 1917 volume (TxRbAAAAYAAJ = nyp.33433090814553) (no snippet text).
- No other Bayhurst hit in any GB/IA motorcycle trade journal 1910-1940 (queries: Bayhurst motorcycle / Indian / Erie / "C. Bayhurst" /
  "Chas. Bayhurst" / "Charles Bayhurst" / hillclimb / "Bay- hurst"). NEGATIVE result for 1920s-30s trade press (coverage is thin).

### 9. Other snippet leads (UNVERIFIED)
- American Motorcyclist and Bicyclist v.24 1928 (R24hAAAAMAAJ = HT mdp.39015021076149, Full view): Gypsy Tour captains, Pennsylvania:
  "Erie. Captain, Lester Shannon, Harley-Davidson Agency, 941 East 11th St."
- MI Oct-Dec 1920 (jXsAAAAAMAAJ = nyp.33433069061921): "... Erie, Pa., completed arrangements whereby he will act as direct factory ..."
- MI Apr-Jun 1920 (UHoAAAAAMAAJ = nyp.33433069061905): "Erie can feel justly proud of its progress in cycling ... Le Jeal's store was
  held and the program mapped out."
- New American Motorcyclist and Bicyclist v.6 Jan-Jun 1911 (XyNaAAAAYAAJ = nyp.33433017524582): "... Le Jeal, Thor and Indian agents,
  respectively, in Erie, Pa., have each placed a machine with the Erie police department".
- National Provisioner 1927 (eHVJ4_NUt8QC): Erie meat-trade committee incl. "A. D. Beckman" (suggests Beckman back in provisions by 1927).
- American Motorcyclist 1955-57: "Erie MC, 114 E. 11th St."; "Erie Harley-Davidson Sales, 114 E. 11th St." (moved by Dec 1957 to 3001
  Glenwood Park Ave). Out of period, shows continuity of 114 E 11th Harley shop.
- Tales of Old Erie (1958, GA_YAAAAMAAJ): "LeJeal's motorcycle store on Sassafras Street and borrowed two Indian Motorcycle tanks".
- A Twentieth Century History of Erie County (1909, N3_Vw_-bx6oC): "Lejeal Cycle & Mobile Works, begun in 1894 ..."
- History of Erie County 1925 (-OdQAQAAMAAJ): "LeJeal Automotive Service ..." (son of LeJeal).

### 10. CONCLUSIONS (trade-press lane)
1. Erie's Indian agency 1908-c.1922 = LeJeal Cycle (& Mobile) Works, Charles H. LeJeal, 1721(-1723) Sassafras St (18th & Sassafras).
   Image-verified for 1908, 1909 (racing), 1912, Jan 1917, Aug 1917; called "former Indian dealers" in Dec 1922.
2. Nov 1922: A. D. ("Archie") Beckman took the Indian agency, 1807 Parade St (image-verified, Nov 23 & Dec 7, 1922). Charles Schroeder
   (ex-LeJeal repairman 5 yrs) ran service. Beckman = Erie M.C. charter member 1910, secretary/F.A.M. commissioner, president 1919-22.
3. Harley-Davidson: Anderson Cycle Works (T. R. Anderson) 546 W. 18th (1912) / 540 W. 18th (1917) [address conflict kept];
   Walter M. Furlong = H-D dealer 1923 (image-verified); Lester Shannon at H-D Agency 941 E. 11th St 1928 (snippet).
4. Other makes 1912 show: Thor (M. A. Reinholtz, 1717 Sassafras per booth sign), Pierce (Penn Sales Co.), Excelsior & Flanders
   (Coleman Bros.), Iver-Johnson (Miller Hardware Co.); Reading-Standard (Erie Motor Sales Co., 1915).
5. Charles Bayhurst: only trade-press trace = July 1919 race win (snippet) with Schroeder 2nd. No Bayhurst Indian-dealer item found in
   accessible trade press; his 1935-37 Indian agency (E 11th St) rests on the LOC phone books (other lane).
6. "East 10th Street": NOT supported by any trade-press item. Addresses found: Sassafras St (LeJeal), Parade St (Beckman), W 18th
   (Anderson), E 11th St (Harley 1928 snippet; Indian 1935-37 phone books). The only "E. 10th St." hit near "Erie M. C." is an OCR/snippet
   artefact belonging to another state's entry.
