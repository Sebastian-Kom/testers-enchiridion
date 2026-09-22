"""Build the static book and map from the canonical manuscript and map data.

Run from any directory: python3 scripts/build.py
The website has no runtime dependencies, CDN requests, or build server.
"""
from pathlib import Path
import html
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
PROJECT = json.loads((ROOT / 'data/project.json').read_text(encoding='utf-8'))
DOCS = ROOT / 'docs'

def chapters():
    text = (ROOT / PROJECT['manuscript']).read_text(encoding='utf-8')
    assert f"Version {PROJECT['version']}" in text, 'Version metadata differs from manuscript'
    text = text.split('\n---\n\n*Source:', 1)[0]
    pieces = re.split(r'^## (\d+)\. (.+)\n', text, flags=re.M)
    result = [{'n':int(pieces[i]), 'title':pieces[i+1], 'text':pieces[i+2].strip()} for i in range(1,len(pieces),3)]
    assert [c['n'] for c in result] == list(range(1,53)), 'Expected 52 consecutive chapters'
    return result

def inline(text):
    text = html.escape(text, quote=False)
    text = text.replace('&lt;br&gt;', '<br>')
    def link(match):
        target = html.unescape(match[2])
        if not (target.startswith(('https://','http://','#','./','../')) or ':' not in target):
            return match[1]
        return '<a href="'+html.escape(target, quote=True)+'">'+match[1]+'</a>'
    text = re.sub(r'\[([^\]]+)\]\(([^\s]+?)\)', link, text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    return text

def markdown(text):
    """Render the deliberately small Markdown subset used in this book."""
    result=[]
    for block in re.split(r'\n\s*\n', text.strip()):
        lines=block.splitlines()
        if all(line.startswith('|') for line in lines):
            rows=[[inline(cell.strip()) for cell in line.strip('|').split('|')] for line in lines]
            result.append('<div class="table-wrap"><table><thead><tr>'+''.join('<th scope="col">'+c+'</th>' for c in rows[0])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+c+'</td>' for c in row)+'</tr>' for row in rows[2:])+'</tbody></table></div>')
        elif lines[0].startswith('#'):
            m=re.match(r'^(#{1,6}) (.+)$', block)
            if m: result.append(f'<h{len(m[1])}>{inline(m[2])}</h{len(m[1])}>')
            else: result.append('<p>'+inline(' '.join(lines))+'</p>')
        elif all(line.startswith('- ') for line in lines):
            result.append('<ul>'+''.join('<li>'+inline(line[2:])+'</li>' for line in lines)+'</ul>')
        elif all(line.startswith('> ') for line in lines):
            result.append('<blockquote>'+inline(' '.join(line[2:] for line in lines))+'</blockquote>')
        elif block=='---': result.append('<hr>')
        else: result.append('<p>'+inline(' '.join(lines))+'</p>')
    return '\n'.join(result)

STYLE='''
:root{color-scheme:light;--ink:#25382e;--muted:#5e6d64;--paper:#f8f7f2;--line:#cbd2c9;--green:#294b3a}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.65 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
a{color:var(--green);text-underline-offset:3px}a:focus-visible,select:focus-visible{outline:3px solid #477a60;outline-offset:3px}
.site-header{max-width:1220px;margin:auto;padding:26px 24px;display:flex;gap:20px;align-items:center;justify-content:space-between;flex-wrap:wrap;border-bottom:1px solid var(--line)}
.brand{color:var(--green);text-decoration:none;font-size:13px;letter-spacing:.08em;font-weight:650}.brand span{display:block;font:16px Georgia,serif;letter-spacing:0;font-weight:400;margin-top:4px}
nav{display:flex;gap:22px;flex-wrap:wrap;font-size:14px}main{max-width:1220px;margin:auto;padding:28px 24px 50px}.site-footer{max-width:1172px;margin:0 auto;padding:22px 0 34px;border-top:1px solid var(--line);font-size:12px;color:var(--muted)}
.skip-link{position:absolute;left:20px;top:-80px;background:white;padding:8px;z-index:10}.skip-link:focus{top:10px}
.book{max-width:760px;margin:auto}.book h1{font:46px/1.1 Georgia,serif;margin:14px 0 20px}.book .subtitle{font:italic 22px/1.4 Georgia,serif;color:var(--muted)}
.book .meta{font-size:14px;color:var(--muted)}.book details{padding:18px 22px;background:#edf0e9;border:1px solid var(--line);border-radius:8px;margin:30px 0}
.book summary{cursor:pointer;font-weight:600}.book details ol{padding-left:22px;columns:2;column-gap:35px}.book details li{break-inside:avoid;padding:3px 0;font-size:13px;line-height:1.45}
.chapter{padding:34px 0 22px;border-bottom:1px solid var(--line);scroll-margin-top:20px}.chapter h2{font:27px/1.3 Georgia,serif;margin:0 0 20px}.chapter p{font:19px/1.8 Georgia,serif}.chapter .map-link{font:13px system-ui,sans-serif;margin-top:20px}
.source-page h1{font:36px/1.2 Georgia,serif}.source-page h2{font:26px/1.3 Georgia,serif;margin-top:36px}.source-page p,.source-page li{max-width:85ch}.source-page li{margin:9px 0}blockquote{border-left:3px solid #a6b6a8;padding:2px 0 2px 20px;max-width:85ch;font-family:Georgia,serif}
.table-wrap{overflow-x:auto}table{border-collapse:collapse;font-size:14px;width:100%;min-width:640px}th,td{padding:12px 14px;border-bottom:1px solid var(--line);vertical-align:top;text-align:left}th{background:#edf0e9}td:first-child{white-space:nowrap}code{overflow-wrap:anywhere;font-size:.88em}
.notice{padding:18px 22px;border:1px solid var(--line);border-radius:8px;background:#edf0e9}.noscript{padding:20px;color:#633b27}
@media(max-width:600px){.site-header{padding:20px 16px}main{padding:20px 12px 35px}nav{gap:18px}.site-footer{margin:0 16px}.book{padding:0 8px}.book h1{font-size:37px}.book details ol{columns:1}.chapter p{font-size:18px}.source-page h1{font-size:30px}}
@media print{.site-header,nav,.site-footer,.map-link,details{display:none}body{background:white}main{padding:0}.chapter{break-inside:avoid}.chapter p{font-size:12pt;line-height:1.5}}
'''

def shell(title, content):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} | Open Books</title>
<meta name="description" content="The Tester’s Handbook by Sebastian Komarnicki: 52 short chapters, an interactive map, and a PDF. A modern adaptation of Epictetus. CC BY-SA 4.0.">
<meta name="author" content="Sebastian Komarnicki"><meta name="color-scheme" content="light"><style>{STYLE}</style></head>
<body><a class="skip-link" href="#main">Skip to content</a><header class="site-header"><a class="brand" href="index.html">OPEN BOOKS<span>The Tester’s Handbook</span></a><nav aria-label="Main navigation"><a href="index.html">Map</a><a href="book.html">Read</a><a href="sources.html">Sources</a><a href="downloads/testers-enchiridion-V103.pdf">PDF</a></nav></header>
<main id="main">{content}</main>
<footer class="site-footer">© 2026 Sebastian Komarnicki · {PROJECT['edition']} · <a rel="license" href="{PROJECT['licenseUrl']}">CC BY-SA 4.0</a> · <a href="downloads/NOTICE.md">Attribution and reuse</a><br>Carter’s historical text is identified separately in the source record.</footer></body></html>'''

def build():
    DOCS.mkdir(exist_ok=True)
    (DOCS/'downloads').mkdir(exist_ok=True)
    canon=chapters()
    mapping=json.loads((ROOT/'data/concepts.json').read_text(encoding='utf-8'))
    passages=json.loads((ROOT/'sources/carter-1759-passages.json').read_text(encoding='utf-8'))
    source={p['n']:p for p in passages['chapters']}
    meta={c['n']:c for c in mapping['chapters']}
    data={'edition':PROJECT['edition'],'ideas':mapping['ideas'],'tests':[],'chapters':[]}
    for c in canon:
        n=c['n']; p=source[n]
        source_text=p['text'] or 'This chapter deliberately departs from the original. No Carter passage is reproduced here. Follow the source link to compare the historical section.'
        data['chapters'].append({**meta[n],**c,'source':source_text,
            'sourceCredit':f"Selected passage from Elizabeth Carter’s 1759 edition; printed page(s) {p['printedPages']}." if p['text'] else 'Deliberate departure; see Carter’s 1759 edition, pp. 406–407.',
            'sourceUrl':p['url']})
    for t in mapping['tests']:
        related=[c['n'] for c in data['chapters'] if t['id'] in c['tests']]
        if related: data['tests'].append({**t,'chapters':related})
    template=(ROOT/'src/atlas.html').read_text(encoding='utf-8')
    serialized=json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
    fragment=template.replace('@@ATLAS_DATA@@',serialized).replace('@@EDITION@@',PROJECT['edition'])
    assert '@@ATLAS_DATA@@' not in fragment
    fragment='<noscript><p class="noscript">The map needs JavaScript. You can still <a href="book.html">read the complete book</a> or download the PDF.</p></noscript>'+fragment
    (DOCS/'index.html').write_text(shell('An atlas of ideas',fragment),encoding='utf-8')
    toc='<details><summary>All 52 chapters</summary><ol>'+''.join(f'<li><a href="#chapter-{c["n"]}">{html.escape(c["title"])}</a></li>' for c in canon)+'</ol></details>'
    content=f'<div class="book"><p class="meta">OPEN BOOKS · {PROJECT["edition"]}</p><h1>{html.escape(PROJECT["title"])}</h1><p class="subtitle">{PROJECT["subtitle"]}</p><p class="meta">{PROJECT["author"]}<br>{PROJECT["date"]} · <a href="downloads/testers-enchiridion-V103.md">Download Markdown</a></p>'+toc
    content+='\n'.join(f'<section class="chapter" id="chapter-{c["n"]}"><h2>{c["n"]}. {html.escape(c["title"])}</h2>{markdown(c["text"])}<p class="map-link"><a href="index.html#chapter-{c["n"]}">Explore this chapter in the map →</a></p></section>' for c in canon)
    content+='<p class="meta">Source: Epictetus, translated by Elizabeth Carter (Dublin, 1759). <a href="sources.html">Read the source record and quotation exceptions</a>.</p></div>'
    (DOCS/'book.html').write_text(shell(PROJECT['title'],content),encoding='utf-8')
    source_text=(ROOT/PROJECT['sourceRecord']).read_text(encoding='utf-8')
    # The archival record describes the text-editing step; clarify the later package separately.
    pre='<p class="notice">Publication package: the manuscript remains V103. Its PDF, map, and website are now included. The record below describes the earlier source check and copyedit. <a href="downloads/testers-enchiridion-V103-source-check.md">Download the record</a>.</p>'
    (DOCS/'sources.html').write_text(shell('Sources and editorial record','<div class="source-page">'+pre+markdown(source_text)+'</div>'),encoding='utf-8')
    for source_path,name in [(ROOT/PROJECT['manuscript'],'testers-enchiridion-V103.md'),(ROOT/PROJECT['sourceRecord'],'testers-enchiridion-V103-source-check.md'),(ROOT/'LICENSE','LICENSE.txt'),(ROOT/'NOTICE.md','NOTICE.md')]:
        shutil.copyfile(source_path,DOCS/'downloads'/name)
    (DOCS/'.nojekyll').write_text('')
    print('Built map, complete web reader, source page, and downloads from V103.')

if __name__=='__main__': build()
