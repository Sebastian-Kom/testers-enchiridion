"""Validate the publication package without third-party dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re

from build import ROOT, PROJECT, chapters

def main():
    canon=chapters()
    page=(ROOT/'docs/index.html').read_text(encoding='utf-8')
    match=re.search(r'<script type="application/json" id="enchiridion-atlas-data">(.*?)</script>',page,re.S)
    assert match, 'Missing map data'
    data=json.loads(match[1])
    assert data['edition']==PROJECT['edition']
    assert len(data['chapters'])==52
    assert all(a['n']==b['n'] and a['title']==b['title'] and a['text']==b['text'] for a,b in zip(canon,data['chapters'])), 'Map differs from canonical manuscript'
    ids={c['n'] for c in canon}; tests={t['id']:t for t in data['tests']}
    covered=set()
    for idea in data['ideas']:
        assert idea['chapters'] and set(idea['chapters'])<=ids
        assert len(idea['chapters'])==len(set(idea['chapters']))
        covered.update(idea['chapters'])
    assert covered==ids, 'At least one chapter is unreachable through concepts'
    for c in data['chapters']:
        assert c['tests'] and len(c['tests'])==len(set(c['tests']))
        for t in c['tests']: assert t in tests and c['n'] in tests[t]['chapters']
    for t in tests.values():
        assert t['chapters']==[c['n'] for c in data['chapters'] if t['id'] in c['tests']]
    source=json.loads((ROOT/'sources/carter-1759-passages.json').read_text(encoding='utf-8'))
    assert [p['n'] for p in source['chapters']]==list(range(1,53))
    for p,c in zip(source['chapters'],canon):
        for retained in p['retained']: assert retained in c['text'], f"Missing source anchor in chapter {c['n']}"
    assert (ROOT/PROJECT['manuscript']).read_bytes()==(ROOT/'docs/downloads/testers-enchiridion-V103.md').read_bytes()
    assert (ROOT/PROJECT['sourceRecord']).read_bytes()==(ROOT/'docs/downloads/testers-enchiridion-V103-source-check.md').read_bytes()
    assert 'appointed to govern you' in data['chapters'][17]['text']
    assert 'Socrates' in data['chapters'][45]['text'] and 'sheep' not in data['chapters'][45]['text'].lower()
    assert 'Supplied English text' not in page and 'V101' not in page
    assert 'Attribution-ShareAlike 4.0 International' in (ROOT/'LICENSE').read_text(encoding='utf-8')
    assert (ROOT/'docs/downloads/testers-enchiridion-V103.pdf').read_bytes().startswith(b'%PDF-')
    class Links(HTMLParser):
        def __init__(self): super().__init__();self.links=[];self.ids=[]
        def handle_starttag(self,tag,attrs):
            attrs=dict(attrs)
            if 'id' in attrs:self.ids.append(attrs['id'])
            if tag=='a' and 'href' in attrs:self.links.append(attrs['href'])
    for name in ['index.html','book.html','sources.html']:
        document=ROOT/'docs'/name
        parser=Links();parser.feed(document.read_text(encoding='utf-8'))
        assert len(parser.ids)==len(set(parser.ids)), f'Duplicate HTML id in {name}'
        for href in parser.links:
            split=urlsplit(href)
            if split.scheme or split.netloc or not split.path:continue
            target=(document.parent/unquote(split.path)).resolve()
            assert target.is_relative_to((ROOT/'docs').resolve()), f'Link escapes published folder: {href}'
            assert target.is_file(), f'Broken local link: {name} → {href}'
    print('PASS: 52 chapters; map/manuscript equality; reachable concepts; inverse links; source anchors; downloads; license; local HTML links.')

if __name__=='__main__':main()
