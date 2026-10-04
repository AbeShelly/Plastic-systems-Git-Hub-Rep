# Lane: verify-people (adversarial re-check of round-1 PRIMARY-VERIFIED "people" claims 42-49, 52-54)
Started 2026-10-04. Method: re-fetch each source image independently from its URL (not from round-1 scratch files),
read the line myself, check edition/date attribution and overreach, THEN open the saved evidence crop (crop_ok).
Pace: >= 3.5 s between requests to one host. Scratch: lanes/verify-people/.

## Log
### Hammermill Bond (Penn State CONTENTdm, collection behrend; IIIF https://digital.libraries.psu.edu/iiif/2/behrend:PTR/...)
- Compound-object structure fetched fresh (dmGetCompoundObjectInfo/behrend/4183 and /4967):
  4167 = Vol 8 No 12 pg 01; 4173 = Vol 8 No 12 pg 07; 4544 = Vol 11 No 11 pg 01; 4550 = Vol 11 No 11 pg 07;
  4708 = Vol 12 No 9 pg 01; 4713/4714/4715 = Vol 12 No 9 pg 06/07/08. So the round-1 pointer->issue attributions hold.
- #42 4173 (1196 px overview + full-res region 3100,4780,1650,340): under boxed "WELCOME TO OUR NEW EMPLOYEES", dept heads
  Yard ... Maintenance Dept. "April 22—Swan Lann" / "General" / "May 20—Charles Bayhurst" / "Dock" / "May 11—John Vega". Folio "[7]".
  No "reemployed" after his name (others have it) -> "joined" is fair. Masthead 4167: "VOL. VIII No. 12   ERIE, PA., JUNE 1, 1926
  Teach Don't Boss". -> CONFIRMED (date May 20 = 1926 by issue date). Identity with the dealer = name only (claim's note says so).
- #43 4550: "SERVICE PIN AWARDS" box, "Three Years" group: "Ira Martin ......May 19" / "Charles Bayhurst ..........May 20" /
  "Walter Trawka ..........May 20" / "Alex Bernodowicz ...May 24". Folio "[7]". Masthead 4544: "VOL. XI—NO. 11  ERIE, PA., MAY 1, 1929".
  Internal cross-check: several 1926 welcome-list names recur in the 3-year cohort with the same dates (Walter Trawka May 20, Ira Martin
  May 19, Grant Carr May 24, Peter Gartner May 24, Tony Schekofski May 24) -> same 1926 cohort. Nuance: list is published May 1 for
  anniversaries falling later in May, so "received ... in May 1929" is an announcement, not proof of receipt; employment c. late April 1929
  is what it shows. -> CONFIRMED (with that nuance).
- #44 4715: left col "... RESTAURANT ... 2 Weeks / Herbert Tong / GENERAL / 4 Days / Charles Bayhurst   Peter Gartner / 1 Week /
  Ellen Findley / 2 Weeks / Charles Campbell John Farrell ... Patrick Murphy Frank Tuzynski / Dennis Rinn Enoch Morford". Folio "[8]".
  Heading read myself on 4713 (pg 06): "Those Scheduled For Vacations With Pay In 1930" (FINISHING DEPARTMENT ...); 4714 (pg 07)
  continues the same list (... SULPHITE MILL, BEATER ROOM, PAPER MACHINES, YARD, POWER) with no new heading; 4715 continues
  (UTILITY, STORE ROOM, RESTAURANT, GENERAL). Masthead 4708: "VOL. XII—No. 9  ERIE, PA., March 1, 1930".
  -> CONFIRMED; the hedge "probably vacation" can be upgraded: it is the paid-vacation schedule for 1930.
### WWII draft cards (NARA medialz TIFs, RG 147, file unit 359321727)
- NARA catalog proxy (one request, 200 JSON): file unit "Baxter, Charles - Baylor, Howard (2 of 2)", 895 objects;
  object 412 = 44033_05_00028-01413.tif (Bayhurst, Charles Arthur, b. 1899 Aug 28), 413 = 01414 (back);
  object 418 = 01419 (Bayhurst, Edward Leo, b. 1898 Nov 12), 419 = 01420 (back); object 420 = 01421 (Bayhurst, Frank William,
  b. 1901 Sep 2), 421 = 01422 (back).
- #45 01413 front (1805x1190 TIF, read at 1800): header "REGISTRATION CARD—(Men born on or after February 17, 1897 and on or before
  December 31, 1921)"; SERIAL "T 293"; ORDER "T 10070"; "1. NAME Charles Arthur Bayhurst"; "2. ... 847 E. Seventh  Erie  Erie  Pa";
  "3. Same"; "4. TELEPHONE" blank; "5. AGE 42"; "DATE OF BIRTH Aug. 28 1899"; "6. Erie / Pa"; "7. Mrs. Theresa Bayhurst 847 E. Seventh St.";
  "8. Erie Forge and Steel"; "9. 16 th Cranberry  Erie  Erie  Pa."; signature "Charles Bayhurst"; "D.S.S. Form 1 (Revised 1-1-42)".
  01414 back: White; 5 7; 150; Hazel; Brown; Light; "Mark on the right foot"; registrar "Cecelia J. Rybinski"; "Registrar for Local Board
  1 Erie Pa"; "Date of registration Feb. 16, 1942"; stamp "LOCAL BOARD NO. 1 / CITY OF ERIE / .. West Ninth Street / ERIE, PENNA."
  ERROR in claim: "(WWII Fourth/'old man's' era registration ...)". The card form and the Feb 16 1942 date are the THIRD registration
  (men b. 17 Feb 1897-31 Dec 1921, ages 20-44; "T" serial prefix). The Fourth ("old man's") registration was 27 Apr 1942 for men
  b. 28 Apr 1877-16 Feb 1897. -> CORRECTED (all card facts right; registration label wrong).
- #54 01419 front: "SERIAL T 622"; "ORDER T 11748"; "EDWARD LEO BAYHURST"; "536 SHUNPIKE ... ERIE PA."; mailing "536 SHUNPIKE";
  tel "92-544 ERIE"; age "43"; DOB "Nov 12 1898"; "ERIE / PA"; "MRS. EDWARD L. BAYHURST. 536 SHUNPIKE"; employer "ERIE FORGE AND STEEL";
  place "ERIE FORGE AND STEEL 15th and CRANBERRY ST. ERIE PA". Back 01420: registrar "Mary Mehler(?)", "Local Board 5 Erie Pa",
  "Feb. 16. 1942", stamp "LOCAL BOARD NO. 5 CITY OF ERIE 121 East Ninth Street".
  01421 front: "SERIAL T 515"; "ORDER T 11949"; "Frank William Bayhurst"; "2314 Kilpatrick Ave Erie  Erie  Pa" (zoomed: 2314, not 2214);
  mailing "Same"; tel "Erie 54274"; age "40"; DOB "Sept 2 1901"; "Erie / Pa"; contact "George Miller 441 West 31 St Erie, Pa.";
  employer "W. J. Bridger RD4 Erie Pa"; place "Bridger Dairy  Erie  Erie  Pa". Back 01422: registrar "Ruth McNally", "Local Board 5
  Erie Pa", "Feb 16, 1942", stamp "LOCAL BOARD NO. 5".
  -> CORRECTED: card facts and 16 Feb 1942 registration confirmed (Local Board No. 5, not 1), but page_or_seq "objects 416 and 418" is
  wrong: catalog objects are 418 (01419) and 420 (01421). "The dealer's brothers" is not on the cards; kinship rests on the 1910 census
  (Edward 12, Charley 10, Frank 8 in Louis Bayhurst's household) plus name/age fit.
### #46 1940 census, T627 roll 3647 image 00396 (NARA medialz JPG, 7401x5664; read in full-res crops)
- Header: "SIXTEENTH CENSUS OF THE UNITED STATES: 1940 / POPULATION SCHEDULE"; "S.D. No. 29"; "E.D. No. 68-18"; "Enumerated by me on
  April 16, 1940"; "Sheet No. 11 A"; enumerator "Sophie A. Ros[inski]"; State Pennsylvania; County Erie; Incorporated place Erie;
  Ward 1; Block 120 (overview). Street margin (rotated crop): "East Seventh Street".
- Left (c1940_L1/L2): L23 "847 | 230 | O | 2000 | No | Murphy, Rachael (x) | Head | F | W | 70 | Wd | No | 6 | Pennsylvania | Same house";
  L24 "Bayhurst, Charles | Son-in-law | M | W | 40 | M | No | 8 | Pennsylvania | Same house";
  L25 ", Theresa | Daughter | F | W | 36 | M | No | 8 | Pennsylvania | Same house"; L26 ", Charles | grandson | M | W | 12 | S | Yes | 6 |
  Pennsylvania | Same house"; L27 "Stewart, John | Brother | M | W | 5[8?] | S | No | 6 | Pennsylvania | Same house".
- Right (c1940_R1/R2; right half is skewed ~1 row down, so rows fixed by the PRINTED right-margin line numbers 23-27):
  line 23 "no no no no H ... 0 0 yes"; line 24 "no | no | yes | - | - | 3 | 40 | mechanic | motorcycle repair shop | OA | 336 85 4 | 52 | 0 | yes";
  line 25 "no no no no H ... 0 0 no"; line 26 blank; line 27 "no no yes - - 3 | [col 27] 16 | Laborer | ... foundry | PW | 988 73 1 ...".
  Column rules in R1: col 26 (hours worked, only for "yes" in col 21) spans x~670-820, col 27 (weeks unemployed) x~820-970.
  Charles's "40" is at x~760-810 -> INSIDE col 26, near its right rule; John Stewart's "16" (col 27) sits clearly right of it.
  So the row is internally inconsistent: col 21 "no" + col 23 "yes" (seeking work) vs. 40 in hours-worked.
- Verdict: transcription and attribution right; claim overreaches by stating flatly "was seeking work in the census week" and by the note
  calling the 40 "ambiguous/on the line" (it is inside col 26). Also: for a person seeking work, cols 28-30 give the LAST occupation;
  "worked 52 weeks in 1939 as a self-employed mechanic" joins col 31 to cols 28-30 by inference. -> CORRECTED.

## Session 2 (resumed 22:38 after the first verify-people run stopped mid-#47). New agent; I re-read every image below myself.
Scratch re-use: files in lanes/verify-people/ were fetched from the SOURCE URLs by this lane (not round-1 scratch); I re-fetched
the #42 region myself (v2_4173_reg.jpg, IIIF region 3000,4300,1782,1000) and viewed the rest at <=1800 px.
- #42 re-read: p.[7] "WELCOME TO OUR NEW EMPLOYEES" ... "Maintenance Dept. / April 22—Swan Lann / General / May 20—Charles Bayhurst /
  Dock / May 11—John Vega". CONTENTdm tree (cpd4183.json): 4167 = Volume 8/No. 12/pg 01, 4173 = Volume 8/No. 12/pg 07.
  Masthead p.1: "VOL. VIII No. 12   ERIE, PA., JUNE 1, 1926   Teach Don't Boss". CONFIRMED.
  Crop: legible; it is a STITCH (p.1 masthead strip pasted above p.7 content) but the filename lacks "_composite".
- #43 re-read: p.[7] "SERVICE PIN AWARDS" ... "Three Years" ... "Ira Martin ......May 19 / Charles Bayhurst ..........May 20 /
  Walter Trawka ......May 20". cpd4967: 4544 = Vol 11/No. 11/pg 01; 4550 = pg 07. Masthead "VOL. XI—NO. 11  ERIE, PA., MAY 1, 1929".
  CONFIRMED (the May 1 list announces pins for anniversaries later in May). Crop legible; also a masthead stitch, no "_composite".
- #44 re-read: p.[8] "GENERAL / 4 Days / Charles Bayhurst   Peter Gartner / 1 Week / Ellen Findley / 2 Weeks / ... Patrick Murphy ...".
  p.[6] (4713) heading "Those Scheduled For Vacations With Pay In 1930"; p.[7] (4714) continues without new heading. Masthead 4708
  "VOL. XII—No. 9   ERIE, PA., March 1, 1930   Teach, Don't Boss". CONFIRMED; "probably vacation" -> it IS the 1930 paid-vacation
  schedule. Crop legible; masthead stitch, no "_composite". (Side note: "Patrick Murphy" in General 2 Weeks = same name as Charles's
  father-in-law, a paper-mill laborer in the 1930 census; name match only.)
- #45 re-read 01413 front myself (TIF size 5847552 = live NARA content-length, re-checked by HEAD today): every field as in the claim;
  "16 th Cranberry"; signature "Charles Bayhurst". Back 01414: "Registrar for Local Board 1 Erie Pa."; "Date of registration Feb. 16, 1942";
  stamp "LOCAL BOARD NO. 1 / CITY OF ERIE". nara_fu.json: object 412 = 01413 (index text "Bayhurst, Charles Arthur; 1899 Aug 28"), 413 = 01414.
  Verdict CORRECTED: the card form "Men born on or after February 17, 1897 and on or before December 31, 1921", serial prefix "T" and
  date 16 Feb 1942 = the THIRD registration; the Fourth ("old man's") registration was 27 Apr 1942 for men born 28 Apr 1877-16 Feb 1897.
  Crop: the full front at 1800 px, legible (back is a separate file).
- #54 re-read 01419 / 01421 fronts and 01420 / 01422 backs (sizes match live NARA). Edward Leo: T 622, 536 Shunpike, "92-544 ERIE",
  43, "Nov 12 1898", Erie Pa, "Mrs. Edward L. Bayhurst. 536 Shunpike", "Erie Forge and Steel", place "Erie Forge and Steel 15th and
  Cranberry St. Erie Pa". Frank William: T 515, "2314 Kilpatrick Ave Erie", "Erie 54274", 40, "Sept 2 1901", Erie Pa, contact
  "George Miller 441 West 31 St Erie, Pa.", employer "W. J Bridger RD4 Erie Pa", place "Bridger Dairy". Backs: both "Local Board 5",
  "Feb. 16, 1942". nara_fu.json: 01419 = object 418, 01421 = object 420 (NOT 416 and 418 as claimed).
  Verdict CORRECTED (object numbers; "the dealer's brothers" is not on the cards, it rests on the 1910 census + name/age fit; same
  Third-registration point as #45 if that label is reused). Crop: stitch of the two fronts, legible; backs (registration date) not in
  the crop; filename lacks "_composite".
- #46 re-read: own full-res crops (v2_c40_names/mid/occ/right/age.jpg) from T627-3647-00396 (size 4669801 = live NARA). Header "E.D. No.
  68-18", "Enumerated by me on April 16, 1940", "Sheet No. 11 A", enumerator "Sophie A. Ros[inski]". L23 "847 | 230 | O | 2000 | No |
  Murphy, Rachael (x) | Head | F | W | 7[0] | Wd" (first digit could be read 2; 70 fits her 1930 age 59); L24 "Bayhurst, Charles |
  Son-in-law | M | W | 40 | M | no | 8 | Pennsylvania | 58 | Same house"; L25 ", Theresa | Daughter | F | W | 36 | M"; L26 ", Charles |
  grandson | M | W | 12 | S"; L27 "Stewart, John | Brother". Employment (row 24 by printed right-margin numbers): "no | no | yes | - | - |
  [E-code 3] | 40 | mechanic | motorcycle repair shop | OA | 336 85 4 | 52 | 0 | yes". Column header read: col 26 = "If at private or
  nonemergency Government work ('Yes' in Col. 21): Number of hours worked during week of March 24-30, 1940"; col 27 = "If seeking work
  ... Duration of unemployment up to March 30, 1940—in weeks"; occupation block: "For a person seeking work ('Yes' in Col. 23): (a) If
  he has previous work experience, enter last occupation". The "40" lies between the col-26 rules (John Stewart's "16" is in col 27).
  Verdict CORRECTED: the transcription is right, but (a) the "40" is inside col 26 (hours worked), not on the 26/27 line, so the row
  contradicts itself (seeking work = yes, code 3, yet 40 hours worked); "was seeking work in the census week" must be stated as "the
  sheet marks him seeking work, but also enters 40 hours worked"; (b) "mechanic / motorcycle repair shop / OA" is, by the form's own
  rule for a person seeking work, his LAST occupation; "52" (col 31) = weeks worked in 1939. Crop: stitched 4-strip composite
  (header, names, birthplace, employment), legible; filename lacks "_composite".
- #47 1930 census (archive.org fifteenthcensus00reel2035). Re-fetched myself: /download/ID/page/n802.jpg, /page/n803.jpg and the
  BookReaderImages jp2 file _0803 (the round-1 route). md5: jp2 _0803 = 0298f071... = page/n802.jpg; page/n803.jpg = 8dccba9d... (different).
  scandata.xml (fetched): leaf 0 has addToAccessFormats=false, so BookReader index nN = jp2 leaf N+1. page/n803 is "Sheet No. 15 A"
  (Wiedele, Lewandowski, Moroz households) - NOT the Bayhurst sheet. The Bayhurst sheet 14 B is https://archive.org/details/
  fifteenthcensus00reel2035/page/n802 (jp2 leaf 0803). => the claim's URL is OFF BY ONE.
  Header n802: "Enumeration District No. 25-2[5]" (faint), "Sheet No. 14 B", "Erie city", "1st pt", "Enumerated by me on April 12, 1930,
  Mrs Rose McLeod"; margin "...Seventh". Own full-res crops (v2_c30_*.jpg): L82 "847 | 309 | 335 | Murphy, Patrick | Head | O | [3 or 5],200 |
  R | No | M | W | 60 | M | 30 | No | Yes"; L83 "Rachel | Wife-H | F W 59 M 29"; L84 "Bayhurst, Tresa | Daughter | F W 28 M 21" (given
  name written "Tresa", faint); L85 "Charles | Son-in-law | M W 30 M 23"; L86 "Stewart, John | Brother-in-law | M W 40 S".
  Dwelling number: "309", not "307" (sequence on sheet: 845/308/334, 847/309/335, 851/310/336).
  Alignment (image is rotated ~-0.039 px/px; left-margin "85" at y~4845 x~550 vs right-margin "85" at y~4530 x~8650): projecting along
  the rules, code "58 12 0" (x~6000,y~4630) -> y~4797 at the name column; "Owner" (x~6720,y~4620) -> ~4815; "9791 | O | yes" (x~7600,
  y~4570) -> ~4799 and onto right-margin label 85. Charles's name sits at y~4810. So Owner / Bicycle[s] / 9791 / O are on printed
  line 85 = Charles. (Round-1's "printed number beside Owner is 86" was a visual misread caused by the tilt; the assignment is right.)
  Industry word at 2.25x zoom: "B[i]cycle s" -> "Bicycles" probable. Patrick and John: "Laborer | Paper Mill | 7847 | W".
  Verdict CORRECTED: substance confirmed (son-in-law, 30, married at 23, Owner / Bicycles / O), but the viewer URL must be page/n802,
  dwelling 309 not 307, Theresa is written "Tresa", value of home first digit uncertain. Crop: 4-strip stitch, legible (shows header,
  names, birthplace/codes, occupation rows with margin numbers); filename lacks "_composite"; "leaf0803" in the filename is the jp2 index.
- #48 1950 census: re-fetched myself (IIIF info.json 4290x5058; overview + full-res regions 100/1500/2490,1750,1800,620 + header).
  Header: "Pennsylvania / Erie / Erie / E.D. 72-20"; "Date sheet started April 17, 1950"; enumerator "Mary A. Crotty"; "Sheet Number 14".
  L10 "850 | 235 | no | no | Levandow[ski], Leo A | Head | W M 50 Nev Pa | wk | 40 Stationary Engineer | Pig iron & coke Mfg | P | 583 336 1";
  L11 "847 | 247 | no | no | Bayhurst, Charles A | Head | W | M | 50 | Mar | Pa | wk | 40 | Floor Hand [Machine] Shop | Forge & Steel Mfg | P |
  690 337 1"; L12 ", Theresa I | Wife | W F 47 Mar Pa | H | no no no"; L13 ", Charles W | Son | W M 22 Nev Pa | wk | 40 | Cabinet Maker |
  Burial Case Mfg | P | 505 399 1"; L14 "Stewart, John H | Uncle in Law | W M 68 Nev Pa | U". Margin "East 7 St" (850 is "E 8th").
  Alignment: right-margin printed 11 carries "690 337 1"; rows 8-11 are all "wk" with exactly four occupations (Salesman, Bookkeeper,
  Stationary Engineer, Floor Hand) before Theresa's "H" -> no shift possible. Verdict CONFIRMED ("247" could also be read "241"; not
  material). Crop: 3-strip stitch (header / names / employment), legible; filename lacks "_composite".
- #49 1910 census: re-fetched T624_1343 image 0556 myself (5624x3987, 9082758 bytes). Header: "Pennsylvania / Erie / Mill Creek Township,
  3d District / Supervisor's District No. 19 / Enumeration District No. 124 / Sheet No. 8 B / Enumerated by me on the 4 day of May, 1910,
  James S. Taylor". L72 "194 | 202 | Bayhurst Louis | Head | M W 46 M1 22 | France French | France French | France French | 1889 | al. |
  English | Farmer | Emp. | ... | O M F 94"; L73 "Louise | Wife | F W 47 M1 22 6 5 | Ger. German (x3) | 1886 | English | None";
  L74 "Louis Jr. | Son | M W 15 S | Pennsylvania | France French | Ger. German | English | Farm Laborer | W no 0"; L75 "Edward | Son | M W 12 S";
  L76 "Charley | Son | M W 10 S"; L77 "Frank | Son | M W 8 S"; L78 "Rosa | Daughter | F W 6 S". Verdict CONFIRMED (immigration year reads
  1889). Crop: header strip + rows 71-78, legible; header strip omits the "4 day of May" line; 2-strip stitch without "_composite".
- #52 American Rifleman Nov 1927: re-fetched /download/sim_american-rifleman_1927-11_75_11/page/n27.jpg (3240x4288) and n28.jpg.
  n27 running head "26  THE AMERICAN RIFLEMAN  Vol. LXXV, No. 11", folio "542"; facing n28 head "November, 1927  THE AMERICAN RIFLEMAN  27".
  Col 2 (full-res crop): "...bers of the Lawrence Park Club have their own auxiliary and have their own shooting night on the club's indoor
  range. / Communications should be addressed to Mr. L. J. Bayhurst, 151 East 11th Street, Erie, Pa." / "OPEN CHALLENGE FROM LAWRENCE
  PARK / THE Lawrence Park Rifle Club, Erie, Pa., challenges any rifle club in the United States to a pistal match in any or all positions
  at 50 feet, teams of any size from two to twelve men; any sights. / Communications should be addressed to the team captain, Mr. L. J.
  Bayhurst, 151 E. 11th Street, Erie, Pa." Verdict CONFIRMED ("captain of its pistol team" = "the team captain" of the club's pistol
  challenge; fair). Crop legible; shows folio 26 and title but the date (on facing p.27) and "Vol. LXXV, No. 11" are not in the crop.
- #53 American Rifleman Apr 1929: re-fetched page/n23.jpg (3168x4248). Head "22  THE AMERICAN RIFLEMAN  April, 1929". "LAWRENCE PARK
  HOLDS NOVELTY SHOOT / WHEN the Lawrence Park Pistol Team, of Erie, Pa., recently challenged the rifle teams of the same club to a match,
  the riflemen shooting all offhand ..." Table "LAWRENCE PARK BUDDIES": "E. Bayhurst.......... 36 43 40 36 41 196" / "Loder ... 225" /
  "F. Hedderich ... 194" / "L. Bayhurst......... 34 43 45 43 38 203" / "W. Hedderich ... 176" / "Total ... 994".
  Verdict CORRECTED (date overreach): the shoot is reported in the April 1929 issue as "recently" held; its date is not printed, so
  "In April 1929 ... shot" should read "reported in the April 1929 issue (match held shortly before)". "Buddies" was one of the club's
  RIFLE teams in a pistol-vs-rifle match. Crop legible; running-head strip stitched on top, no "_composite".
- #47 alignment numbers, re-measured on v2_n802.jpg (full res): left-margin "85" at (550,4845), right-margin "85" at (8670,4530) -> tilt
  -0.0388 px/px. "9791 | O | yes" at (7600,4570) projects to y~4528 at the right margin = line 85. "Owner" at (6700,4620) projects to
  y~4808 at the name column, where "Charles" is written (y~4810). Next row "Laborer | Paper Mill | 7847 | W" projects onto line 86
  (John Stewart); "7847" on the 82 row = Patrick. (Supersedes the rougher numbers in the #47 entry above; the conclusion is unchanged.)
- After the media-limit reset I re-viewed every source crop and saved evidence file for #42-46 and #54 again; readings as logged.

## New evidence (this lane)
- evidence/1929-03-01_hammermill-bond_v11n9_p1-p6-p8_vacations-with-pay-1929-general-3days-charles-bayhurst_composite.png
  (stitched: p.1 masthead "VOL. XI—NO. 9  ERIE, PA., MARCH 1, 1929" [behrend:4512] / p.6 heading "Those Scheduled for Vacations with
  Pay in 1929" [4517] / p.8 "GENERAL / 3 Days / Wm. Quino   Charles Bayhurst / 4 Days / Ellen Findley" [4519]). Turns the OCR-only
  1929 line mentioned in #44's notes into an image-verified line.

## crop_ok summary (opened each saved crop AFTER reading the source)
All 11 saved crops legibly show the claimed line. Housekeeping: the crops for #42, #43, #44, #46, #47, #48, #49, #53 and #54 are
stitched strips (masthead/header strip + content) but their filenames lack the required "_composite" suffix. #45 back and #54 backs
(registration date / local board) are not in the #54 crop. #47 filename "leaf0803" = jp2 index; the viewer URL must be page/n802.

## VERDICTS
42 CONFIRMED | 43 CONFIRMED | 44 CONFIRMED (upgrade: list = "Those Scheduled For Vacations With Pay In 1930") |
45 CORRECTED (Third registration, not Fourth/"old man's") | 46 CORRECTED ("40" is inside col 26 hours-worked: row self-contradictory;
occupation = last occupation of a work-seeker) | 47 CORRECTED (viewer URL page/n802 not n803; dwelling 309 not 307; given name written
"Tresa"; value first digit uncertain) | 48 CONFIRMED | 49 CONFIRMED | 52 CONFIRMED | 53 CORRECTED (shoot reported in Apr 1929 issue as
"recently" held; date not printed) | 54 CORRECTED (catalog objects 418/420 not 416/418; Local Board 5; kinship not on the cards).
None REFUTED.
