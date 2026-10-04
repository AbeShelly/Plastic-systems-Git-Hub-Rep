# Lane: through-block (round 2) - working log, 2026-10-04

Question: is "East 10th Street" explained by the 114 and 118-120 E 11th shops sitting back to back with the
E 10th auto row (117-129 E 10th) on the same block? Is there any primary evidence of a motorcycle business
with an E 10th address or an E 10th entrance?
Scratch: lanes/through-block/ (sb.sh = Sanborn IIIF fetch helper, tl.py/tl2.py = OCR timeline, ctx.py = OCR context).
All images viewed by me at <=1800 px. LOC tile server gave HTTP 503 four times (each retried once after a pause, then OK).

## 1. Sanborn sheet 59 through-block test (image-verified)
IIIF ids (from WebFetch of loc.gov JSON, sp=63 / sp=61):
- 1950: service:gmd:gmd382m:g3824m:g3824em:g3824em_g07660195001:07660_01_1950-0059 (6716x7795)
  viewer https://www.loc.gov/resource/g3824em.g3824em_g07660195001/?sp=63
- 1921: service:gmd:gmd382m:g3824m:g3824em:g3824em_g07660192101:07660_01_1921-0059 (6450x7650)
  viewer https://www.loc.gov/resource/g3824em.g3824em_g07660192101/?sp=61
- KEY legend: ...g3824em_g07660192101:07660_01_1921-0000 region 4950,4300,1400,3300.
  Key (read on image): crossbars on a wall line = "Fire wall 6/12/18/36 inches above roof"; semicircles = "Openings
  protected by single/double iron or tin clad door"; "Wall with openings, figures indicate on which floor";
  stem-and-dot marks = "Window opening in first story" / "Windows second and third stories" ("DOTS REPRESENT OPENINGS.
  STEMS INDICATE STORIES").
- Scale (1950 sheet 59, scale bar read at full res): 50 ft = ~302 px, i.e. ~6.0 px/ft. E 10th frontage (y~5378) to
  E 11th frontage (y~7400) = ~2022 px = ~335 ft; mid-block line ~y 6389.

1950 (corrected to Aug 1950), full-res crops x1950-3500 / x1350-2450, y5200-7550:
- 117-129 E 10th: one building "TAXI GARAGE", "CONC. FL. STEEL COLS. & BEAMS", "REP.", "OFF." "REST." (front, 2 st.),
  "FURNE 1ST" (127 side), front "IR. CL. BETWEEN PIERS". It runs from the E 10th frontage south to the mid-block line.
- 118-120 E 11th: "AUTO SALES & SERV. / STEEL FR. CONC. FL. TILE", "OFF." at front, rear section "6- SMALL W.G.
  SKYLIGHTS", running from the E 11th frontage north to the mid-block line.
- Junction: the taxi garage's south wall and the 118-120 rear section's north wall are drawn as two separate wall
  lines about 15-28 px apart (~2.5-4.5 ft at ~6 px/ft; my measurement from pixel rows), not one shared party wall.
  Both walls carry stem-and-dot window/opening marks. No door symbol (semicircle), no "opening" figure, no passage,
  driveway or "thru" label is drawn between them. The two buildings are back to back, but they are separate structures.
- 114-116 E 11th: "MOTOR CYCLE SHOP / TILE", 1-storey, with a 1-storey frame rear addition. Behind it is open yard, then
  a 1-storey concrete-block auto garage "A / 7 STALLS (C.B.)" across the rear of the ~106-116 E 11th lots ("AUTO
  PARKING" lot and 114). Its north wall is on the mid-block line, against the rear of "R. 113 E 10TH ST." (2-st. C.B.
  "AUTO REP. 1ST / SIGN SHOP 2ND") and "R. 107 10TH ST." (3 stalls / 4 stalls). Its east end abuts the 118-120 rear
  section. Nothing on the sheet shows the 114 lot reaching E 10th.
- Evidence: evidence/1950-08_sanborn-erie-v1-sheet59_loc-g3824em_g07660195001_117-129-e10th-taxi-garage-backs-onto-114-120-e11th_composite.png
  (header strip "ERIE, PA., VOL. I 59" pasted above; composite) and ..._mid-block-junction-taxi-garage-118-120-e11th-closeup.png (full res).

1921 (full-res crop x1350-3650, y5150-7350):
- A continuous horizontal rear lot line runs along the mid-block line. The E 10th lots (107-109, 113, 117, empty
  119-125, 127-129, 131-133) end on it from the north and the E 11th lots end on it from the south. The vertical lot
  lines do not continue across it (offset ~18 px). No lot ran through from E 10th to E 11th in 106-132.
- E 11th side: one wide vacant parcel (later 106-122) next to F. D. Schultz Co (102-104), then 124 "GARAGE CAPCY: 20 CARS
  ... AUTO SHOW RM", 126 S, 128 "Furn'e".
- E 10th rear buildings on the mid-line: "AUTO REPAIRING" (1-st. brick, 15', rear of 127-129 E 10th; window marks on its
  south wall); "AUTO" (iron clad, rear of 113 E 10th); "AUTOS TILE" (rear of 107-109).
- Evidence: evidence/1921_sanborn-erie-v1-sheet59_loc-g3824em_g07660192101_e10th-e11th-block-mid-block-rear-lot-line_composite.png
  (header pasted; composite); key: evidence/1921_sanborn-erie-v1-index-sheet_loc-g3824em_g07660192101_key-legend-walls-openings-windows.png

## 2. E 10th frontage label sweep, 0-460 blocks, both sides, 1921 and 1950 (image-verified at 50%, doubtful labels at 100%)
Sheets: 3 (State-French), 59 (French-Holland), 60 (Holland-German), 61 (German-Parade), 62 (Parade-Wallace).
IIIF files 07660_01_{1921,1950}-00{03,59,60,61,62}; sheet number read on every overview.
Band viewed = mid-block (E 9th-10th) to mid-block (E 10th-11th), i.e. all buildings on E 10th lots.
RESULT: no "MOTOR CYCLE", "CYCLE" or "BICYCLE" label on any E 10th lot, 1921 or 1950.
Labels found (house numbers as printed):
- 1921 sheet 3: N side 12-14 rear "Shoe Repairg" (full-res check), 14 "Elec.", 16 "Tailor in B.", "GASOLINE FILLING
  STATION" (20-30), 32 St Mark's P.E. Church, rear "Paint Stge / Auto", "Auto". S side 1-15 Office / Pool / stores;
  11, 15, 17, 23 D; 31 D vend; "Auto (Ir.Cl.)" rear.
- 1950 sheet 3: N 8-10 OFF./S, 12-14 S, 16 A, 18 REST., 22-30 PENNSYLVANIA TELEPHONE CORP., 32 St Mark's. S 1-15 THE NATL.
  BANK & TRUST BLDG (built 1935), 17-23, "AUTO PARKING".
- 1921 sheet 59: N 106-108 D, 114 Harden's Dancing Academy entrance, 116 S, rear "AUTO REPAIRING" (2-st. frame), 118 D +
  rear "AUTO", 120 "WICKER SHOP" (full-res check), 122 D vend, 124-130 D, 132 D, 134-160 JARECKI M'F'G COMPANY. S 101 D,
  107-109 D vend, 113 D vend, 117 D, 127-129 D, 131-133 D, 133 1/2 D, 137 D, 149 D, "AUTO HOUSES" 1-14 (rear), J. H.
  Marshall Cleaning & Dyeing Co, 151-157 D, 163 D, rear "AUTO", "AUTOS TILE", "AUTO REPAIRING", "AUTOS", Erie Armature Works.
- 1950 sheet 59: N 106-108 D/S vend, 114 S + bowling ENTRANCE, 114 1/2, 116, A-116 1/2-B S/REST., rear "AUTO REPAIRING
  CONC. FL." and "8 CARS C.B.", 122 CONVALESCENT HOME, 124-130 D vend, SEARS ROEBUCK & CO DEPT STORE (built 1947), SERVICE
  STA./FILL'G STA. S 101 FILLING STA. + GREAS'G (C.B.), 107-109 D vend, 113 APTS vend, R.113 AUTO REP. 1ST / SIGN SHOP 2ND,
  R.107 3 STALLS / 4 STALLS, 117-129 TAXI GARAGE, 131-133 F, 137 D, 141 D, R. of 137 AUTO STALLS, AUTO HOUSES, 145 AUTO REP.
  C.B., 149-151 AUTO SALES & SERVICE, 155 S, STGE (VEND), 157 D, 163 AUTO TIRES / AUTO GREASING / TIRE SERVICE, WHOL. CHEESE.
- 1921 sheet 60: N 202 S, 206 D vend, 208-230 D, 232-240 D, 244 OUR LADY OF PEACE HO. (R.C.), 248-254 D, 260 Swedish Evangl
  Luthn Beth. Church, rear AUTO / AUTOS / AUTO TILE / C.B. AUTO TILE. S 201-203 FRIES BROS. WAGON REPAIRING (painting 1st,
  Bl.Sm. & wood working), rear Bell Telephone Co store rm, 207-231 D, SHED, AUTO C.B., 233-235 D, 237-239 D, 241 D + AUTO
  C.B., 245 Seventh Day Adventist Church, 249-257 D, 1002-1014 German D.
- 1950 sheet 60: N 202-260 as 1921 (234 S C.B., 238-240 APTS vend, 244 ROOM'G, 260 Bethany Evangl Luthn Beth. Church), rear
  AUTO C.B. (R. of 208), AUTO, AUTOS, A (R. of 248), AUTO TILE. S 201-203 AUTO SALES & SERV. (UPHOLSTG 2D), AUTO REP. C.B.,
  AUTO PAINTG C.B., 203 S, 207 S, 211 D, 213-215 APTS, 217-221 USED CAR SALES, 225-227 D, AUTO C.B., 231-257 D/APTS,
  245 Seventh Day Adventist Church + School Annex.
- 1921 sheet 61: N 302 D, St Mary's R.C. Church, 326 St Mary's Ushers Club, COOP, AUTO, 340-354 D, 364 / 922-932 Parade S
  (candy kitchen, 2-ton ice machine), MFG. CHEMIST (918 1/2 Parade), AUTO. S 301 Swedish Evangl Mission, 307-359 D, AUTO
  IR.CL., AUTO, AUTO C.B., 1002-1010 Parade S (Hardw., Paints & Oils), Lunch car (1012), Motion Picture Theatre (1014-16).
- 1950 sheet 61: N 302 D vend, St Mary's Parochial School, St Mary's Auditorium, 340-354 D, AUTO C.B., HALL 3RD (356-364).
  S 301 Swedish Evangl Mission, 307-359 D, AUTO IR. CL., AUTO, A (C.B.), R. of 341 AUTO C.B., WALL PAPER PAINTS (1002
  Parade), AUTO, AUTO STALLS (R. of 1014 Parade), REST. C.B.
- 1921 sheet 62: N 402-416 PARADE ST MARKET, TIE SHED, AUTO REPG. (cement fl., rear), 420-460 D, AUTO, PLANING MILL. S
  401-407 S, Chine Laundry, 411 SHEET METAL WORKING (C.B.), 415 D, 417 D, 421-457 D, AUTOS C.B., AUTO TILE; on the PARADE
  frontage of the same block: 1009 "Auto Repairing", 1011 "Vulcanizing", 1013 "Clo. Cleaning", 1015 "Bicycle Repairing"
  (1-st. frame, part tin clad; full-res check), with "AUTO REPG. HEAT: STOVE (C.B.)" and "MACH. SHOP" behind it,
  1017-19 REGENT MOVING PICTURES.
  Evidence: evidence/1921_sanborn-erie-v1-sheet62_loc-g3824em_g07660192101_1015-parade-bicycle-repairing-401-411-e10th.png
- 1950 sheet 62: N 402-416 S (conc. fl.), HALL C.B. (R. 422 E 10th), 420-460 D/APTS, CONTRACTORS W. HO. S 401-407 REST./OILS/S,
  AUTO REP. WOOD & CEM. FL. (1009 Parade), 411 ERECTING SHOP / SHEET METAL WKG, STGE, 415 STGE, 417-457 D/APTS, AUTO REPG.
  (C.B.), MACH. SHOP, A (C.B.)s, AUTO TILE; 1015 Parade now just "S".
=> The only cycle label anywhere near E 10th is the 1921 "Bicycle Repairing" at 1015 PARADE St (Parade frontage, 5th lot
   south of the E 10th corner). The phone books (OCR) put Erie Clouse Vulcanizing Co at 1015 Parade in 1934-40, J W Auto
   Body garage there in 1946-47, and no cycle business at that address.

## 3. Phone-book OCR timeline, 113-131 E 10th and 112-124 E 11th (tl2.txt; IMG = I viewed the page image)
112 E 11th: 1911 Zimmerley William, Livery.
113 E 10th: res. 1911 (Carey, Fogarty), 1934-36 Uhlman M Mrs r, 1937-40 Hogue Ruth Miss r, 1941-44 Meyers r; Everett R L Garage
  (Jul 1935 yellow "Garages" seq342; white seq288 reads 118 E 10th); Graham Garage (1945-46); Yost's Service garage, Nanni A
  signs, Santia Elmer signs (1947). This matches the 1950 Sanborn "R.113 E 10TH ST. AUTO REP. 1ST / SIGN SHOP 2ND".
114 E 10th: Geneva Beauty Shop, Cook Ruth H r (1934-35). 116 E 10th: Sander's Confectionery (1938), Jack's Dairy Bar (1947).
114 E 11th: Harley-Davidson Motorcycle Agency 52-140, every edition Jul 1934-Jul 1947 (IMG Jul 1935 seq291).
117 E 10th: Harry J Klick Furniture Galleries Inc / Klick Harry J Better Furniture 23-175 (Jan 1935-Jul 1938; IMG Jul 1935 seq291);
  Erie Buick Company / Buick Sales & Service / Beck Buick Inc 25-671 (Jan 1939-Jan 1944; ad "117-125 E. 10th ST."); Checker Cab Co,
  Erie Taxicab Co, Yellow Cab, Morehouse Garage 72-206 (1946-47; IMG Jul 1946 yellow seq692). (No Jul 1945 listing found.)
118 E 10th: Erie News Co, F M Plate (1911, 1914); later residences.
118 E 11th: Brown & Kelly garage 24-130 (Jul 1934, Jan 1935); Standard Sales & Service Garage 69-212 (Jul 1935, IMG seq306);
  May's Auto Exchange (Jan 1936); East Eleventh St Garage 69-412 (Jul 1936, IMG seq460); Moorhouse Motor Co Used Car Dept 22-487
  (Jul 1937 IMG seq561 white + seq580 yellow; Jul 1938 IMG seq681 yellow, OCR seq661 white; Jan 1939 IMG seq768 white, OCR seq786
  yellow); Barnhart Al M garage 22-590 (Jul 1940 IMG seq854; Jul 1941), Black Carl R garage (Jul 1940), Erie Motor Service 22-590
  (1940-41); Reslink & Wiggers Motors / GMC Trucks Sales & Service 22-590 (1942-47; IMG Jul 1946 seq692).
120 E 10th: Ford Dry Cleaning Co (1934-36), Nu-Way Cleaners (Jan 1939).
120 E 11th: only Indian Motorcycle Agency 69-312 (Jul 1935, Jan 1936, Jul 1936). NO entry at 120 E 11th in any edition Jul 1937-Jul 1947
  (OCR negative). The phone books list the 1937-39 Moorhouse used-car lot as "118 E 11th" only. The "118-20" reading rests on the
  1939 Atkinson snippet.
122 E 10th: Erne Leah r (1934-43), Donaldson Convalescent Home (1945-47). 123 E 11th: Tyser's Filling Station No 2 (1936-42).
124 E 10th: residences 1938-45. 124 E 11th: Fuessler Motor Sales 69-113 (1934-36), Erie Brake Service 40-230 (1938), Haft's Garage (1939-41),
  Firch Supply (1945-47). 125 E 10th: Rex Uptown Restaurant (1947). 126 E 10th: Daylight Service Co window cleaning (1937-39), residences.
127/129 E 10th: Better Homes 23-026 (1935-36 at 129); Klick Harry J Better Furniture 23-175 (127 in Jan 1939; 129 in 1940-47; "House of Klicks");
  Kalamazoo Sales & Service, Pieper O R furnaces (1947). 128, 131 E 10th: residences.
Moorhouse vs Morehouse: Moorhouse Motor Co = 144 E 12th 26-465 (main) + 118 E 11th 22-487 (used cars), Jul 1934-Jan 1939. Gone by Jul 1940
  (IMG seq875: "Moorhouse H M r 1002 Weschler av....24-875" then "Moose Club Kitchen"; no Motor Co). The 1946-47 "Morehouse Garage
  117 E 10th ... 72-206" is a different spelling and a different phone. A separate "Johnson & Morehouse Garage" (119 W 8th 69-127, 1934-42;
  138 W 10th 62-164, 1943-45) also existed. The round-1 / critic statement that "one firm (Moorhouse) held 118 E 11th and later 117 E 10th"
  is a spelling merge; no evidence links them.

## 4. Bayhurst / 302 E 11th checks (IMG)
- Jan 1939 seq749 (pp. 14 BAR-BEL / BEL-BIS 15): "BAYERSON OIL WORKS 848 E 12th st.23-765" / "Bayhurst Frank W r 2314 Kilpatrick av.....54-274" /
  "Bayle R L r 2509 German st....09-514" / "Bayton Albert r 2808 Greely av". No Charles Bayhurst.
- Jul 1940 seq854 (14 BAL-BAX / BAX-BEN 15): same sequence, no Charles Bayhurst.
- 302 E 11th (OCR, both reels): only Jul 1937 "Bayhurst Charles motorcycles" + "Indian Motorcycle Agency" 48-385. Nothing in Jul 1938, Jan 1939,
  Jul 1940, Jul 1941. Then "Cioccio J r 304 E 11th" (1942) and "Cioccio J r 302 E 11th st" (1943-47, residence). Phone 48-385 does not recur
  (48-386 = MacInnes Steel, unrelated). 69-312 recurs only as "Cappabianca John r 1618 Chestnut st" (Jul 1945). No "Longwell" in any edition.
  Not a full image read of 1938-40 white pages; it is an OCR negative.

## CONCLUSION
No primary evidence was found of a motorcycle business with an East 10th address or an E 10th entrance, 1911-1950.
- Sanborn 1921 and 1950: E 10th lots and E 11th lots meet at a mid-block rear line. No lot or building runs through. The 118-120 E 11th
  auto building and the 117-129 E 10th taxi garage are separate buildings back to back, and no opening is drawn between them. The 114 E 11th
  motorcycle shop's lot ends at a 7-stall garage on the mid-line.
- No E 10th frontage (0-460 blocks, both sides, 1921 and 1950) has any cycle label.
- In the phone books, the E 10th neighbours behind the shops were a furniture store (Klick, 117 E 10th, 1935-38), Erie Buick (1939-44), cab
  companies and Morehouse Garage (1946-47). None is a motorcycle business.
Best reconciliation (interpretation only): the 1935-36 Indian Motorcycle Agency (120 E 11th) and the Harley agency (114 E 11th) stood in the
block bounded by E 10th and E 11th, back to back with E 10th car businesses. A client could remember it as "the Tenth Street block", or could
have entered through an E 10th auto building, but nothing on paper shows such a rear entrance.
