import re,html,sys,urllib.parse,subprocess,time
def feed(q, n=20, start=1):
    u="https://www.google.com/books/feeds/volumes?"+urllib.parse.urlencode({'q':q,'max-results':n,'start-index':start})
    s=subprocess.run(['curl','-s','-m','60','-A','Mozilla/5.0',u],capture_output=True,text=True).stdout
    out=[]
    for e in re.findall(r'<entry>(.*?)</entry>',s,re.S):
        g=lambda tag: [html.unescape(x) for x in re.findall(rf'<dc:{tag}>(.*?)</dc:{tag}>',e,re.S)]
        out.append(dict(title=' / '.join(g('title')),date=' '.join(g('date')),id=(g('identifier') or [''])[0],ids=g('identifier'),desc=html.unescape(' '.join(g('description'))),fmt=g('format')))
    tot=re.findall(r'<openSearch:totalResults>(\d+)<',s)
    return out, (tot[0] if tot else None), s
if __name__=='__main__':
    q=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 20
    res,tot,raw=feed(q,n)
    print('TOTAL',tot, '' if res else raw[:300])
    for r in res: print('*',r['title'][:90],'|',r['date'],'|',r['ids'],'\n    ',r['desc'][:500])
