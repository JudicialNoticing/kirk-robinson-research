# Longform HTML builder for TJR-P01 and siblings.
#   python3 tools/build-html.py <source.md> <out.html>
# Theme: centered reading column, TOC drawer, reading progress, collapsible front-matter.
# Moved out of the session scratchpad 2026-09-14 so the deliverables stay regenerable.
import re, html, sys, io

SRC, OUT = sys.argv[1], sys.argv[2]
lines = open(SRC, encoding='utf-8').read().split('\n')

def inline(s):
    s = html.escape(s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', s)
    return s

def slug(s):
    s = re.sub(r'<[^>]+>', '', s)
    s = re.sub(r'[^\w\s§.-]', '', s).strip().lower()
    return re.sub(r'[\s.]+', '-', s)[:60] or 'sec'

def callout_kind(txt):
    if '🚨' in txt: return 'crit'
    if '⚠'  in txt: return 'warn'
    if '⚖'  in txt: return 'bal'
    if '🛠'  in txt: return 'fix'
    return 'note'

out, toc = [], []
i = 0
is_tbl = lambda s: s.strip().startswith('|')

while i < len(lines):
    t = lines[i].strip()
    if not t:
        i += 1; continue

    if t == '---':
        out.append('<hr>'); i += 1; continue

    if is_tbl(lines[i]):
        rows = []
        while i < len(lines) and is_tbl(lines[i]):
            raw = lines[i].strip().strip('|')
            cells = [c.strip() for c in raw.split('|')]
            if not all(re.fullmatch(r':?-{2,}:?', c) for c in cells):
                rows.append(cells)
            i += 1
        if rows:
            b = ['<div class="tw"><table>']
            b.append('<thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in rows[0]) + '</tr></thead><tbody>')
            for r in rows[1:]:
                b.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>')
            b.append('</tbody></table></div>')
            out.append('\n'.join(b))
        continue

    m = re.match(r'^(#{1,4})\s+(.*)$', t)
    if m:
        lvl, txt = len(m[1]), inline(m[2])
        sid = slug(m[2])
        if lvl in (2, 3):
            toc.append((lvl, sid, re.sub(r'<[^>]+>', '', txt)))
        out.append(f'<h{lvl} id="{sid}">{txt}</h{lvl}>')
        i += 1; continue

    if t.startswith('>'):
        buf = []
        while i < len(lines) and lines[i].strip().startswith('>'):
            buf.append(re.sub(r'^>\s?', '', lines[i].strip()))
            i += 1
        body = []
        for q in buf:
            if not q.strip(): continue
            qh = re.match(r'^(#{1,4})\s+(.*)$', q)
            if qh:   body.append(f'<p class="ch">{inline(qh[2])}</p>')
            elif q.strip().startswith(('- ', '* ')):
                body.append(f'<p class="cb">{inline(q.strip()[2:])}</p>')
            else:    body.append(f'<p>{inline(q)}</p>')
        joined = '\n'.join(body)
        out.append(f'<aside class="co {callout_kind(" ".join(buf))}">{joined}</aside>')
        continue

    if re.match(r'^[-*]\s+', t):
        items = []
        while i < len(lines) and re.match(r'^[-*]\s+', lines[i].strip()):
            items.append(f'<li>{inline(re.sub(r"^[-*]\s+", "", lines[i].strip()))}</li>')
            i += 1
        out.append('<ul>' + ''.join(items) + '</ul>'); continue

    if re.match(r'^\d+\.\s+', t):
        items = []
        while i < len(lines) and re.match(r'^\d+\.\s+', lines[i].strip()):
            items.append(f'<li>{inline(re.sub(r"^\d+\.\s+", "", lines[i].strip()))}</li>')
            i += 1
        out.append('<ol>' + ''.join(items) + '</ol>'); continue

    out.append(f'<p>{inline(t)}</p>')
    i += 1

nav = '\n'.join(
    f'<a class="l{l}" href="#{s}">{x}</a>' for l, s, x in toc
)

CSS = r"""
/* ── D · LONGFORM — personal-site article. Centered column, warm paper, TOC on demand. */
:root{--bg:#fdfbf7;--fg:#2a2724;--soft:#544e46;--mut:#8b8178;--line:#e8e1d6;--card:#fffdfa;
--acc:#b4531f;--acc2:#1f5f6b;--rule:#ded5c7;--code:#f2ece2;
--crit:#a8321f;--critbg:#fcf1ee;--warn:#8a6414;--warnbg:#fdf7e9;--bal:#1f5f6b;--balbg:#edf5f6;
--fix:#1f6b47;--fixbg:#eef6f1;--note:#c3b8a8;--notebg:#f8f4ec;}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]){
--bg:#17161a;--fg:#e9e4dc;--soft:#c3bcb2;--mut:#8f8880;--line:#2c2a2f;--card:#1d1c21;
--acc:#e3a06a;--acc2:#7fc4d0;--rule:#3a373d;--code:#232227;--crit:#f0887a;--critbg:#241816;
--warn:#e8bd6a;--warnbg:#241f14;--bal:#7fc4d0;--balbg:#14212400;--fix:#77cfa4;--fixbg:#152420;
--note:#3a373d;--notebg:#1d1c21;}}
:root[data-theme="dark"]{--bg:#17161a;--fg:#e9e4dc;--soft:#c3bcb2;--mut:#8f8880;--line:#2c2a2f;
--card:#1d1c21;--acc:#e3a06a;--acc2:#7fc4d0;--rule:#3a373d;--code:#232227;--crit:#f0887a;
--critbg:#241816;--warn:#e8bd6a;--warnbg:#241f14;--bal:#7fc4d0;--balbg:#142124;--fix:#77cfa4;
--fixbg:#152420;--note:#3a373d;--notebg:#1d1c21;}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);
font:19px/1.78 "Iowan Old Style",Charter,"Palatino Linotype",Georgia,serif;
-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
/* single centered column — the sidebar rail is gone */
.wrap{display:block;max-width:none;margin:0}
main{max-width:70ch;margin:0 auto;padding:0 26px 180px}
/* reading progress */
#prog{position:fixed;top:0;left:0;height:3px;width:0;background:var(--acc);z-index:50;
transition:width .08s linear}
/* article header */
h1{font:700 clamp(32px,5.4vw,50px)/1.13 "Iowan Old Style",Charter,Georgia,serif;
letter-spacing:-.02em;margin:0 0 20px;color:var(--fg)}
.dek{font-size:21px;line-height:1.6;color:var(--soft);margin:0 0 26px;font-style:italic}
.byline{display:flex;flex-wrap:wrap;gap:8px 16px;align-items:center;font:14px/1.5 -apple-system,
BlinkMacSystemFont,"Segoe UI",sans-serif;color:var(--mut);padding:16px 0 18px;
border-top:1px solid var(--line);border-bottom:1px solid var(--line);margin:0 0 40px}
.byline .tag{font:12px/1 ui-monospace,Menlo,monospace;letter-spacing:.06em;background:var(--code);
color:var(--soft);padding:5px 9px;border-radius:20px}
.byline .dot{color:var(--rule)}
h2{font:700 clamp(25px,3.3vw,32px)/1.24 "Iowan Old Style",Charter,Georgia,serif;
letter-spacing:-.014em;margin:76px 0 20px;color:var(--fg);scroll-margin-top:24px}
h3{font:700 19px/1.4 "Iowan Old Style",Charter,Georgia,serif;margin:42px 0 12px;
color:var(--acc);scroll-margin-top:24px}
p{margin:0 0 22px;color:var(--fg)}
strong{font-weight:700}
em{font-style:italic}
a{color:var(--acc);text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:2px}
code{font:.8em/1.5 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;background:var(--code);
color:var(--soft);padding:2px 6px;border-radius:4px}
ul,ol{padding-left:26px;margin:0 0 22px}li{margin:9px 0}
blockquote{margin:28px 0;padding:0 0 0 26px;border-left:3px solid var(--acc);
font-size:20px;line-height:1.65;color:var(--soft);font-style:italic}
hr{border:0;height:1px;background:var(--line);margin:52px auto;width:100%}
/* the provisional banner reads as an editor's note, not a system alarm */
.banner{background:var(--notebg);border:1px solid var(--rule);border-radius:12px;color:var(--soft);
padding:16px 20px;margin:0 0 36px;font:italic 16px/1.6 "Iowan Old Style",Charter,Georgia,serif}
.banner::before{content:"A note before you start — ";font-style:normal;font-weight:700;color:var(--acc)}
/* callouts as author asides */
.callout{margin:26px 0;padding:18px 22px;border-radius:12px;background:var(--notebg);
border:1px solid var(--line);font-size:17.5px;line-height:1.7}
.callout.crit{background:var(--critbg);border-color:color-mix(in srgb,var(--crit) 26%,transparent)}
.callout.warn{background:var(--warnbg);border-color:color-mix(in srgb,var(--warn) 26%,transparent)}
.callout.bal {background:var(--balbg); border-color:color-mix(in srgb,var(--bal) 26%,transparent)}
.callout.fix {background:var(--fixbg); border-color:color-mix(in srgb,var(--fix) 26%,transparent)}
/* tables can exceed the measure */
.tw{overflow-x:auto;margin:32px 0;border:1px solid var(--line);border-radius:12px;
width:calc(100% + 120px);margin-left:-60px;background:var(--card)}
table{border-collapse:collapse;width:100%;
font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
th{background:var(--notebg);text-align:left;font-weight:700;font-size:12.5px;letter-spacing:.05em;
text-transform:uppercase;color:var(--mut);padding:13px 16px;border-bottom:1px solid var(--line)}
td{padding:12px 16px;border-bottom:1px solid var(--line);vertical-align:top;color:var(--soft)}
tr:last-child td{border-bottom:none}
/* floating controls */
.fab{position:fixed;right:22px;z-index:40;background:var(--card);color:var(--soft);
border:1px solid var(--rule);border-radius:999px;cursor:pointer;box-shadow:0 2px 10px rgba(0,0,0,.09);
font:14px/1 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;padding:12px 17px}
.fab:hover{color:var(--acc);border-color:var(--acc)}
#tocBtn{bottom:22px}
.tog{bottom:74px;position:fixed;right:22px}
/* TOC drawer — hidden until asked for */
#toc{position:fixed;inset:0 0 0 auto;width:min(400px,86vw);background:var(--card);z-index:60;
border-left:1px solid var(--rule);padding:30px 26px 60px;overflow-y:auto;
transform:translateX(102%);transition:transform .26s cubic-bezier(.4,0,.2,1);
box-shadow:-8px 0 30px rgba(0,0,0,.12)}
#toc.open{transform:translateX(0)}
#toc h2{font:700 13px/1 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;letter-spacing:.14em;
text-transform:uppercase;color:var(--mut);margin:0 0 18px}
#toc a{display:block;color:var(--soft);text-decoration:none;padding:7px 10px;border-radius:7px;
font:15px/1.4 "Iowan Old Style",Charter,Georgia,serif;margin-bottom:1px}
#toc a:hover{background:var(--notebg);color:var(--acc)}
#toc a.on{color:var(--acc);font-weight:700;background:var(--notebg)}
#toc a.l3{padding-left:24px;font-size:14px;color:var(--mut)}
#scrim{position:fixed;inset:0;background:rgba(0,0,0,.34);z-index:55;opacity:0;pointer-events:none;
transition:opacity .26s}
#scrim.open{opacity:1;pointer-events:auto}
@media(max-width:820px){main{padding:0 20px 140px;font-size:18px}
.tw{width:100%;margin-left:0}h2{margin-top:54px}}

/* collapsible front-matter card */
.docinfo{border:1px solid var(--line);border-radius:12px;background:var(--notebg);
margin:0 0 46px;padding:0 20px;font-size:16.5px;line-height:1.68}
.docinfo summary{cursor:pointer;list-style:none;padding:15px 0;color:var(--acc);
font:600 14px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;letter-spacing:.01em}
.docinfo summary::-webkit-details-marker{display:none}
.docinfo summary::before{content:"▸  ";color:var(--mut)}
.docinfo[open] summary::before{content:"▾  "}
.docinfo[open] summary{border-bottom:1px solid var(--line);margin-bottom:14px}
.docinfo p{color:var(--soft);margin:0 0 14px}
.docinfo p:last-child{margin-bottom:18px}
"""

JS = r"""
/* Longform reading shell: progress bar, on-demand TOC drawer, article header, scrollspy. */
(function(){
  var main=document.querySelector('main'), nav=document.querySelector('nav');
  if(!main) return;

  /* 1 ── reading progress */
  var prog=document.createElement('div'); prog.id='prog'; document.body.appendChild(prog);

  /* 2 ── TOC becomes a drawer, opened on demand */
  var scrim=document.createElement('div'); scrim.id='scrim'; document.body.appendChild(scrim);
  if(nav){ nav.id='toc'; document.body.appendChild(nav); }
  var btn=document.createElement('button');
  btn.id='tocBtn'; btn.className='fab'; btn.type='button'; btn.textContent='☰  Contents';
  document.body.appendChild(btn);
  function setOpen(o){ if(nav) nav.classList.toggle('open',o); scrim.classList.toggle('open',o); }
  btn.onclick=function(){ setOpen(!(nav&&nav.classList.contains('open'))); };
  scrim.onclick=function(){ setOpen(false); };
  if(nav) nav.addEventListener('click',function(e){ if(e.target.tagName==='A') setOpen(false); });
  document.addEventListener('keydown',function(e){ if(e.key==='Escape') setOpen(false); });

  /* 3 ── article header: lift the metadata paragraphs into a byline, promote Scope to a dek */
  var h1=main.querySelector('h1');
  if(h1){
    var LABELS=['File ID','Scope','Case context','Prepared','Status/version'];
    var meta={}, node=h1.nextElementSibling, eaten=[];
    while(node && node.tagName==='P' && eaten.length<8){
      var st=node.querySelector('strong'); if(!st) break;
      var key=st.textContent.replace(/:\s*$/,'').trim();
      if(LABELS.indexOf(key)===-1) break;
      meta[key]=node; eaten.push(node); node=node.nextElementSibling;
    }
    var words=(main.textContent.match(/\S+/g)||[]).length;
    var mins=Math.max(1,Math.round(words/230));
    var hrs=Math.floor(mins/60), rem=mins%60;
    var readable=hrs?(hrs+' hr '+(rem?rem+' min':'')).trim():(mins+' min');

    if(meta['Scope']){
      var d=document.createElement('p'); d.className='dek';
      d.innerHTML=meta['Scope'].innerHTML.replace(/^<strong>Scope:<\/strong>\s*/,'');
      h1.insertAdjacentElement('afterend',d);
      meta['Scope'].remove();
    }
    var by=document.createElement('div'); by.className='byline';
    var bits=[];
    if(meta['File ID']) bits.push('<span class="tag">'+meta['File ID'].textContent.replace(/^File ID:\s*/,'').trim()+'</span>');
    if(meta['Prepared']) bits.push('<span>'+meta['Prepared'].textContent.replace(/^Prepared:\s*/,'').trim()+'</span>');
    bits.push('<span>'+words.toLocaleString()+' words</span>');
    bits.push('<span>'+readable+' read</span>');
    by.innerHTML=bits.join('<span class="dot">•</span>');
    (document.querySelector('.dek')||h1).insertAdjacentElement('afterend',by);
    ['File ID','Prepared'].forEach(function(k){ if(meta[k]) meta[k].remove(); });

    /* fold the remaining front-matter into a collapsible card so the article opens on prose */
    var carry=['Case context','Status/version'].filter(function(k){return meta[k];});
    if(carry.length){
      var det=document.createElement('details'); det.className='docinfo';
      var sum=document.createElement('summary'); sum.textContent='About this document — status, version and case context';
      det.appendChild(sum);
      carry.forEach(function(k){ det.appendChild(meta[k]); });
      by.insertAdjacentElement('afterend',det);
    }
  }

  /* 4 ── progress + scrollspy */
  var links=new Map([].slice.call(document.querySelectorAll('#toc a'))
    .map(function(a){return [a.getAttribute('href').slice(1),a];}));
  var heads=[].slice.call(document.querySelectorAll('h2[id],h3[id]'));
  function onScroll(){
    var h=document.documentElement;
    var max=h.scrollHeight-h.clientHeight;
    prog.style.width=(max>0?(h.scrollTop/max*100):0)+'%';
    var cur=null;
    for(var i=0;i<heads.length;i++){ if(heads[i].getBoundingClientRect().top<140) cur=heads[i]; else break; }
    links.forEach(function(a){a.classList.remove('on');});
    if(cur&&links.get(cur.id)) links.get(cur.id).classList.add('on');
  }
  document.addEventListener('scroll',onScroll,{passive:true}); onScroll();

  /* 5 ── theme toggle */
  var t=document.querySelector('.tog');
  if(t){ t.className='tog fab'; t.textContent='◐  Theme';
    t.onclick=function(){ var r=document.documentElement;
      var cur=r.getAttribute('data-theme')||(matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light');
      r.setAttribute('data-theme',cur==='dark'?'light':'dark'); }; }
})();
"""

doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>TJR-P01 — Tyler James Robinson, Comprehensive Evidentiary Profile</title>
<style>{CSS}</style></head><body>
<button class="tog">◐ theme</button>
<div class="wrap">
<nav><h2>Contents</h2>{nav}</nav>
<main>
<div class="banner">PROVISIONAL — no verification cycle has run on this file. Not citable by another file until one has.</div>
{chr(10).join(out)}
</main></div>
<script>{JS}</script>
</body></html>"""

open(OUT, 'w', encoding='utf-8').write(doc)
print("wrote", OUT, len(doc), "chars ·", len(toc), "TOC entries")
