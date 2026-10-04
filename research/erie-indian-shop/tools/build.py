#!/usr/bin/env python3
"""Build erie_motorcycle_businesses_1920-1940.csv (actually 1908-1947 coverage, core 1920-1940) and sources.md
from workflow results. Usage: build.py wf1_result.json [wf2_result.json ...]"""
import json, csv, sys, re, os
OUT = '/home/user/erie-indian-shop'
rows, sources, = [], []
for p in sys.argv[1:]:
    d = json.load(open(p))
    lanes = d.get('lanes', []) + d.get('followups', [])
    for l in lanes:
        for b in l.get('businesses_rows', []):
            rows.append({**b, 'lane': l['lane']})
        for s in l.get('sources_checked', []):
            sources.append({**s, 'lane': l['lane']})

def norm_conf(c):
    c = (c or '').upper()
    if c.startswith('PRIMARY-VERIFIED'): return 'PRIMARY-VERIFIED (page image)'
    if c.startswith('PRIMARY-TEXT'): return 'PRIMARY-TEXT-ONLY (OCR, not image-checked)'
    if c.startswith('SNIPPET'): return 'SNIPPET-LEAD (search snippet only)'
    return 'UNVERIFIED'

def yr(s):
    m = re.search(r'(18|19)\d\d', s or ''); return int(m.group(0)) if m else 9999

# de-duplicate: same year + business + address + page_seq
seen, out = set(), []
for r in sorted(rows, key=lambda r: (yr(r['year']), r['year'], r['business'])):
    k = (r['year'].strip(), r['business'].strip().lower()[:40], r['address'].strip().lower()[:25], r['page_seq'].strip()[:30])
    if k in seen: continue
    seen.add(k); out.append(r)

with open(f'{OUT}/erie_motorcycle_businesses_1920-1940.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['year', 'business', 'owner', 'address', 'brands_products', 'source', 'url', 'page_seq',
                'line_as_printed', 'confidence', 'found_by_lane'])
    for r in out:
        w.writerow([r['year'], r['business'], r.get('owner', ''), r['address'], r.get('brands_products', ''),
                    r['source'], r['url'], r['page_seq'], r['line_as_printed'], norm_conf(r['confidence']), r['lane']])
print('csv rows', len(out), 'of', len(rows))

# sources.md
order = {'hit': 0, 'partial': 1, 'miss': 2, 'blocked': 3}
seen, srcs = set(), []
for s in sources:
    k = (s['url'].strip(), s['status'])
    if k in seen: continue
    seen.add(k); srcs.append(s)
cnt = {k: sum(1 for s in srcs if s['status'] == k) for k in order}
with open(f'{OUT}/sources.md', 'w') as f:
    f.write('# Sources checked\n\n')
    f.write('Every source the research lanes touched, with outcome. **hit** = useful evidence found; **partial** = reached '
            'but incomplete; **miss** = searched, nothing relevant; **blocked** = could not be reached from the cloud '
            'container (Cloudflare, IP block, login, paywall or outage).\n\n')
    f.write(f"Totals: {cnt['hit']} hit, {cnt['partial']} partial, {cnt['miss']} miss, {cnt['blocked']} blocked "
            f"({len(srcs)} entries).\n\n")
    for st in ['hit', 'partial', 'miss', 'blocked']:
        f.write(f'## {st.upper()}\n\n')
        for s in sorted([x for x in srcs if x['status'] == st], key=lambda x: x['lane']):
            url = s['url'].strip()
            link = f'[{url[:90]}]({url})' if url.startswith('http') else url
            note = s['note'].replace('\n', ' ').strip()
            f.write(f"- **{s['source'].strip()}** — {link}  \n  {note} _(lane: {s['lane']})_\n")
        f.write('\n')
with open(f'{OUT}/sources.md','a') as f:
    f.write(open('/home/user/erie-indian-shop/work/build/orchestrator_sources.md').read())
    f.write(open('/home/user/erie-indian-shop/work/build/sweep_sources.md').read())
print('sources', len(srcs), cnt)
