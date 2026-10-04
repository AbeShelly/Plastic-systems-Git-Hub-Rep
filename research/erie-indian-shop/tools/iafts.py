#!/usr/bin/env python3
"""archive.org FULL-TEXT search. Usage: iafts.py "query" [hits=50] [page=1]
Prints identifier | title | year | highlighted snippets ({{{...}}} marks the hit)."""
import json,sys,urllib.parse,subprocess
q=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 50; p=int(sys.argv[3]) if len(sys.argv)>3 else 1
u="https://archive.org/services/search/beta/page_production/?"+urllib.parse.urlencode({'service_backend':'fts','user_query':q,'hits_per_page':n,'page':p})
s=subprocess.run(['curl','-s','-m','120',u],capture_output=True,text=True).stdout
try:
    d=json.loads(s); b=d['response']['body']
except Exception as e:
    print('ERROR',s[:300]); sys.exit(1)
print('TOTAL',b['hits'].get('total'))
for h in b['hits']['hits']:
    f=h.get('fields',{}); hl=h.get('highlight',{}).get('text',[])
    print('*',f.get('identifier'),'|',str(f.get('title'))[:90],'|',f.get('year') or f.get('date'))
    for x in hl[:6]: print('     >',x.replace('\n',' / ')[:300])
