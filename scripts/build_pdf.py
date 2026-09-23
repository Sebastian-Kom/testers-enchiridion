"""Build the A5 PDF from the unchanged V103 manuscript. Requires ReportLab."""
from pathlib import Path
import html
import json
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A5
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, PageBreak, KeepTogether, TableStyle
from reportlab.platypus.tableofcontents import TableOfContents

from build import ROOT, PROJECT, chapters

WIDTH, HEIGHT=A5
INK=colors.HexColor('#243D31')
MUTED=colors.HexColor('#657269')
GOLD=colors.HexColor('#A1874D')

def inline(text):
    text=html.escape(text.replace('—',' - ').replace('–','-').replace('\u2011','-'),quote=False)
    text=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',text)
    return text

def chapter_inline(text, retained):
    """Italicize only the checked source passages, including documented adaptations."""
    text=' '.join(text.splitlines())
    if not retained:
        return inline(text)
    pattern=re.compile('|'.join(re.escape(q) for q in sorted(retained,key=len,reverse=True)))
    parts=[]
    position=0
    for match in pattern.finditer(text):
        parts.extend([inline(text[position:match.start()]),'<i>'+inline(match[0])+'</i>'])
        position=match.end()
    parts.append(inline(text[position:]))
    return ''.join(parts)

class BookDoc(BaseDocTemplate):
    def afterFlowable(self,flowable):
        if hasattr(flowable,'chapter_number'):
            n=flowable.chapter_number
            key=f'chapter-{n}'
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(flowable.toc_title,key,0,False)
            self.notify('TOCEntry',(0,flowable.toc_title,self.page,key))

def page(canvas,doc):
    canvas.saveState()
    if doc.page==1:
        canvas.setFillColor(INK);canvas.rect(0,0,WIDTH,HEIGHT,fill=1,stroke=0)
        canvas.setStrokeColor(GOLD);canvas.setLineWidth(1);canvas.line(42,HEIGHT-91,WIDTH-42,HEIGHT-91)
        canvas.setFillColor(colors.HexColor('#FAF7EC'))
        canvas.setFont('Times-Roman',40);canvas.drawString(40,HEIGHT-183,'The Tester’s')
        canvas.drawString(40,HEIGHT-228,'Handbook')
        canvas.setFont('Times-Italic',16);canvas.drawString(42,HEIGHT-279,'A handbook for people')
        canvas.drawString(42,HEIGHT-301,'who are paid to doubt')
        canvas.setFont('Helvetica',11);canvas.drawString(42,145,PROJECT['author'])
        canvas.setFont('Helvetica',9);canvas.setFillColor(colors.HexColor('#CDD8CC'))
        canvas.drawString(42,91,'A modern adaptation of Epictetus')
        canvas.drawString(42,75,'52 chapters for software and systems testers')
        canvas.drawRightString(WIDTH-42,40,PROJECT['edition'])
    else:
        canvas.setStrokeColor(colors.HexColor('#D7DDD5'));canvas.setLineWidth(.4)
        canvas.line(40,35,WIDTH-40,35)
        canvas.setFillColor(MUTED);canvas.setFont('Helvetica',7)
        canvas.drawString(40,23,'THE TESTER’S HANDBOOK  /  V103')
        canvas.drawRightString(WIDTH-40,23,str(doc.page))
    canvas.restoreState()

def build():
    target=ROOT/'docs/downloads/testers-enchiridion-V103.pdf'
    target.parent.mkdir(exist_ok=True,parents=True)
    doc=BookDoc(str(target),pagesize=A5,leftMargin=40,rightMargin=40,topMargin=42,bottomMargin=48,
        title=PROJECT['title'],author=PROJECT['author'],subject='A modern adaptation of Epictetus for software and systems testers. CC BY-SA 4.0.',
        pageCompression=1)
    frame=Frame(doc.leftMargin,doc.bottomMargin,doc.width,doc.height,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
    doc.addPageTemplates(PageTemplate(id='book',frames=frame,onPage=page))
    body=ParagraphStyle('Body',fontName='Times-Roman',fontSize=10.5,leading=14.8,textColor=INK,spaceAfter=7,allowWidows=0,allowOrphans=0)
    heading=ParagraphStyle('Chapter',fontName='Times-Roman',fontSize=17,leading=20.5,textColor=INK,spaceBefore=0,spaceAfter=13,keepWithNext=True)
    small=ParagraphStyle('Small',fontName='Helvetica',fontSize=8.3,leading=12,textColor=MUTED,spaceAfter=12)
    reading_note=ParagraphStyle('ReadingNote',fontName='Helvetica',fontSize=9,leading=12.5,textColor=INK,spaceAfter=22,keepWithNext=True)
    intro=ParagraphStyle('Intro',parent=body,fontSize=11,leading=16,spaceAfter=12)
    section=ParagraphStyle('Section',parent=heading,fontSize=23,leading=27,spaceAfter=24)
    story=[Spacer(1,400),PageBreak(),Paragraph('About this edition',section)]
    for p in [
        'Fifty-two short chapters bring the questions of Epictetus into the working life of a software and systems tester: what to trust, what to question, and how to act.',
        'The modern adaptation is by Sebastian Komarnicki. Its historical passages follow Elizabeth Carter’s 1759 edition. Their spelling and capitalization are retained; deliberate adaptations are documented in the accompanying source record.',
        'You may share this book, adapt it, and use it commercially under Creative Commons Attribution-ShareAlike 4.0 International. Credit the author, indicate changes, and share adaptations under the same or a compatible license.',
    ]: story.append(Paragraph(inline(p),intro))
    story.extend([Spacer(1,15),Paragraph('© 2026 Sebastian Komarnicki<br/>Version 1.03 · 22 September 2026',small),
        Paragraph('License: <link href="https://creativecommons.org/licenses/by-sa/4.0/" color="#294B3A">creativecommons.org/licenses/by-sa/4.0/</link><br/>Carter’s historical text is identified separately and remains public domain. See the accompanying NOTICE.md and source record for attribution details.',small),PageBreak(),Paragraph('Contents',section)])
    toc=TableOfContents()
    toc.levelStyles=[ParagraphStyle('ContentsEntry',fontName='Times-Roman',fontSize=9.8,leading=13.5,firstLineIndent=0,leftIndent=0,rightIndent=22,spaceBefore=2,textColor=INK)]
    toc.tableStyle=TableStyle([('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('VALIGN',(0,0),(-1,-1),'TOP')])
    toc.dotsMinLevel=0
    story.extend([toc,PageBreak()])
    source=json.loads((ROOT/'sources/carter-1759-passages.json').read_text(encoding='utf-8'))
    retained_by_chapter={entry['n']:entry['retained'] for entry in source['chapters']}
    for chapter in chapters():
        h=Paragraph(inline(f"{chapter['n']}. {chapter['title']}"),heading)
        h.chapter_number=chapter['n'];h.toc_title=f"{chapter['n']}. {chapter['title']}"
        retained=retained_by_chapter[chapter['n']]
        raw_paragraphs=re.split(r'\n\s*\n',chapter['text'])
        for quotation in retained:
            count=sum(' '.join(p.splitlines()).count(quotation) for p in raw_paragraphs)
            if count!=1:
                raise ValueError(f"Expected one source passage in chapter {chapter['n']}, found {count}: {quotation}")
        paragraphs=[Paragraph(chapter_inline(p,retained),body) for p in raw_paragraphs]
        lead=[]
        if chapter['n']==1:
            lead=[Paragraph('Passages in italics come from Elizabeth Carter’s 1759 translation of Epictetus. Their historical language is retained; a few deliberate adaptations are documented in the source record.',reading_note)]
        story.append(KeepTogether([*lead,h,*paragraphs,Spacer(1,16)]))
    story.extend([PageBreak(),Paragraph('Source and license',section),
        Paragraph('Epictetus, <i>All the Works of Epictetus, Which Are Now Extant</i>, translated by Elizabeth Carter (Dublin: Hulton Bradley, 1759). <i>The Enchiridion</i>, pp. 387-412. The passage in §29 follows <i>Discourses</i> III.15, p. 236, as directed by the note on p. 399.',intro),
        Paragraph('The retained passages were checked against scans of the printed edition. The source record lists each passage and documents the excerpt in §7, the adaptations in §§18 and 23, the omission in §40, and the closing formula in §52.',intro),
        Paragraph('Scanned edition: <link href="https://archive.org/details/allworksofepicte00epic" color="#294B3A">archive.org/details/allworksofepicte00epic</link>',small),
        Paragraph('Suggested attribution',heading),
        Paragraph('Sebastian Komarnicki, <i>The Tester’s Handbook</i>, V103 (2026). A modern adaptation of Epictetus using Elizabeth Carter’s 1759 translation. Licensed under CC BY-SA 4.0. Add a link to the edition you used and describe any changes you make.',intro),
        Paragraph('The license applies to the original modern material. It does not impose new restrictions on Carter’s public-domain text. The full license and attribution notice accompany this edition.',intro),
        Paragraph('Read the license: <link href="https://creativecommons.org/licenses/by-sa/4.0/" color="#294B3A">creativecommons.org/licenses/by-sa/4.0/</link>',small)])
    doc.multiBuild(story)
    print(target)

if __name__=='__main__': build()
