#!/usr/bin/env python3
"""Post-process the CSV: drop snippet/text rows superseded by an image-verified row of the same
year+business key, and mark the 302 E 11th Bayhurst/Indian rows CONFIRMED (2 independent publishers on images)."""
import csv, re
P = '/home/user/erie-indian-shop/erie_motorcycle_businesses_1920-1940.csv'
rows = list(csv.DictReader(open(P)))
def key(r):
    b = r['business'].lower()
    for k in ['bayhurst', 'kuivinen', 'goodyear', 'indian motorcycle agency']:
        if k in b: return (r['year'][:4], k)
    return None
verified = {key(r) for r in rows if key(r) and r['confidence'].startswith('PRIMARY-VERIFIED')}
out, dropped = [], 0
for r in rows:
    k = key(r)
    if k and k in verified and not r['confidence'].startswith('PRIMARY-VERIFIED'):
        dropped += 1; continue
    if ('302 e 11th' in r['address'].lower()) and r['confidence'].startswith('PRIMARY-VERIFIED') \
            and 'bayhurst' in r['business'].lower():
        r['confidence'] = 'CONFIRMED (2 independent publishers on page images: Jul 1937 phone book + Aug 1939 Atkinson directory)'
    elif ('302 e 11th' in r['address'].lower()) and r['confidence'].startswith('PRIMARY-VERIFIED') and 'indian' in r['business'].lower():
        r['confidence'] = 'PRIMARY-VERIFIED (page image). Address independently confirmed by 1939 directory; the Indian brand rests on the 1937 phone book only'
    out.append(r)
with open(P, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(out)
print('rows', len(out), 'dropped superseded', dropped)
