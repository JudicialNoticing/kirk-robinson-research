import xml.etree.ElementTree as ET, datetime, re
f="~/Documents/Kirk Robinson Research/files - Bride of Charlie series/BOC-E08_transcript-artifacts/feed.xml"
t=ET.parse(f); r=t.getroot()
lo=datetime.datetime(2026,3,5); hi=datetime.datetime(2026,4,2)
out=[]
for it in r.iter('item'):
    pd=it.findtext('pubDate') or ''
    try: d=datetime.datetime.strptime(pd[:25].strip(),'%a, %d %b %Y %H:%M:%S')
    except Exception: continue
    if lo<=d<=hi:
        title=(it.findtext('title') or '').strip()
        link=(it.findtext('link') or '').strip()
        desc=re.sub(r'<[^>]+>','',(it.findtext('description') or '')).strip()
        dur=it.findtext('{http://www.itunes.com/dtds/podcast-1.0.dtd}duration') or ''
        guid=(it.findtext('guid') or '').strip()
        out.append((d,title,link,desc,dur,guid))
out.sort()
print("ITEMS IN WINDOW 2026-03-17..2026-04-02:",len(out))
for d,title,link,desc,dur,guid in out:
    print("\n"+"="*80)
    print("DATE :",d.strftime('%Y-%m-%d %H:%M'),"(%s)"%d.strftime('%a'))
    print("TITLE:",title)
    print("DUR  :",dur)
    print("LINK :",link[:200])
    print("GUID :",guid[:120])
    print("DESC :",desc[:1400])
