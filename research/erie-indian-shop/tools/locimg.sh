#!/bin/bash
# Download an LOC phone-book page image. Usage: locimg.sh REEL SEQ PCT OUTFILE
#   REEL = usteledirec07589 (Erie 1911-1940) or usteledirec07590 (Erie 1941-1947)
#   SEQ  = 1-based sequence number (as in grep_loc.py output "seqN"); file index = SEQ-1
#   PCT  = 6.25 | 12.5 | 25 | 50 | 100
# Also supports region crops: set REGION="x,y,w,h" (pixels at full size) env var.
REEL=$1; SEQ=$2; PCT=$3; OUT=$4; F=$(printf "%04d" $((SEQ-1)))
R=${REGION:-full}
curl -s -m 120 -o "$OUT" "https://tile.loc.gov/image-services/iiif/public:gdcmassbookdig:${REEL}:${REEL}_${F}/${R}/pct:${PCT}/0/default.jpg"
identify "$OUT" 2>/dev/null || { echo "FAILED"; head -c 200 "$OUT"; }
