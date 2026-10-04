import json, re, sys
pat = re.compile(sys.argv[2], re.I)
d = json.load(open(sys.argv[1]))
for k in sorted(d, key=int):
    t = d[k].get('fulltext','')
    for line in t.split('\n'):
        if pat.search(line):
            print(f"seq{k}\t{d[k]['jp2-path']}\t{line.strip()[:160]}")
