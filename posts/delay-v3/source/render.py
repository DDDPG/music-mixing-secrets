"""Render the adapted Guizang HTML with a local-only WeasyPrint pipeline."""
from pathlib import Path
from urllib.parse import urlparse
import json
import sys
from weasyprint import HTML, default_url_fetcher
from weasyprint.text.fonts import FontConfiguration
import fitz
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'output'
OUT.mkdir(exist_ok=True)
(ROOT / 'phone-preview').mkdir(exist_ok=True)

def local_only(url, *args, **kwargs):
    if urlparse(url).scheme not in ('file', 'data'):
        raise RuntimeError('External URL forbidden during rendering')
    return default_url_fetcher(url, *args, **kwargs)

document = HTML(filename=str(ROOT / 'index.html'), url_fetcher=local_only).render(font_config=FontConfiguration())
assert len(document.pages) == 8, f'Expected 8 pages, rendered {len(document.pages)}'
document.write_pdf(OUT / 'vocal-delay-v3.pdf')

pdf = fitz.open(OUT / 'vocal-delay-v3.pdf')
report = {'renderer': 'WeasyPrint 66.0 + PyMuPDF', 'external_requests': False, 'coordinate_units': 'canvas px from PDF glyph boxes', 'pages': []}
for i, page in enumerate(pdf):
    boxes=[]
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines', []):
            for span in line['spans']:
                x0,y0,x1,y1=[v*4/3 for v in span['bbox']]
                boxes.append({'text':span['text'],'x':round(x0,2),'y':round(y0,2),'width':round(x1-x0,2),'height':round(y1-y0,2),'font':span['font']})
    outside=[b for b in boxes if b['x']<60 or b['x']+b['width']>1020 or b['y']<40 or b['y']+b['height']>1440]
    report['pages'].append({'page':i+1,'text_bounds_warnings':outside,'text_boxes':boxes})
names = ['cover', 'routing', 'time', 'pingpong', 'feedback', 'filter', 'audition', 'check']
for i, (page, name) in enumerate(zip(pdf, names)):
    pix = page.get_pixmap(matrix=fitz.Matrix(4 / 3, 4 / 3), alpha=False)
    assert (pix.width, pix.height) == (1080, 1440)
    pix.save(OUT / f'xhs-{i+1:02}-{name}.png')
    thumb=Image.open(OUT / f'xhs-{i+1:02}-{name}.png'); thumb.resize((360,480),Image.Resampling.LANCZOS).save(ROOT / 'phone-preview' / f'xhs-{i+1:02}-{name}-360.png')
    print(f'xhs-{i+1:02}-{name}.png: {pix.width} × {pix.height}')

thumb_w, thumb_h = 270, 360
sheet = Image.new('RGB', (4 * thumb_w + 5 * 24, 2 * (thumb_h + 28) + 3 * 24), '#e8e8e5')
draw = ImageDraw.Draw(sheet)
font = ImageFont.truetype(str(ROOT / 'assets/fonts/NotoSansSC-400.ttf'), 16)
for i, name in enumerate(names):
    im = Image.open(OUT / f'xhs-{i+1:02}-{name}.png')
    im.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
    x, y = 24 + (i % 4) * (thumb_w + 24), 24 + (i // 4) * (thumb_h + 52)
    sheet.paste(im, (x, y))
    draw.text((x, y + thumb_h + 6), f'{i+1:02} / 08', font=font, fill='#222222')
sheet.save(OUT / 'vocal-delay-v3-contact-sheet.png')
(OUT / 'layout-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2))
print('Text bounds warnings:', sum(len(p['text_bounds_warnings']) for p in report['pages']))
