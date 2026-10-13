from pathlib import Path
from urllib.parse import urlparse
import json,fitz
from PIL import Image,ImageDraw
from weasyprint import HTML,default_url_fetcher
from weasyprint.text.fonts import FontConfiguration
R=Path(__file__).resolve().parents[1];O=R/'output';P=R/'phone-preview';P.mkdir(exist_ok=True);O.mkdir(exist_ok=True)
def local_only(url,*a,**kw):
 if urlparse(url).scheme not in ('file','data'):raise RuntimeError('External fetch prohibited during render')
 return default_url_fetcher(url,*a,**kw)
spec=json.loads((R/'design/production_spec.json').read_text())
doc=HTML(filename=str(R/'index.html'),url_fetcher=local_only).render(font_config=FontConfiguration())
assert len(doc.pages)==len(spec['pages']),(len(doc.pages),len(spec['pages']))
doc.write_pdf(O/'snare-adt-before-reverb.pdf');d=fitz.open(O/'snare-adt-before-reverb.pdf')
result={'renderer':'WeasyPrint 66.0, PyMuPDF 1.26.6','external_requests':False,'pages':[]};thumbs=[]
for i,p in enumerate(d):
 pix=p.get_pixmap(matrix=fitz.Matrix(4/3,4/3),alpha=False);assert (pix.width,pix.height)==(1080,1440);q=O/f'xhs-{i+1:02}.png';pix.save(q)
 im=Image.open(q);im.resize((360,480),Image.Resampling.LANCZOS).save(P/f'xhs-{i+1:02}-360.png');thumbs.append(im.resize((270,360),Image.Resampling.LANCZOS))
 boxes=[]
 for b in p.get_text('dict')['blocks']:
  for l in b.get('lines',[]):
   for t in l['spans']:
    x0,y0,x1,y1=[v*4/3 for v in t['bbox']];boxes.append({'text':t['text'],'bbox':[x0,y0,x1,y1],'font':t['font']})
 outside=[b for b in boxes if b['bbox'][0]<60 or b['bbox'][2]>1020 or b['bbox'][1]<38 or b['bbox'][3]>1425]
 result['pages'].append({'page':i+1,'text_bounds_warnings':outside,'text_boxes':boxes,'links':[{'uri':x.get('uri'),'from':list(x['from'])} for x in p.get_links()]})
cols=4;rows=(len(thumbs)+3)//4;sheet=Image.new('RGB',(cols*294+24,rows*412+24),'#e5e5ea');dr=ImageDraw.Draw(sheet)
for i,im in enumerate(thumbs):x=24+i%4*294;y=24+i//4*412;sheet.paste(im,(x,y));dr.text((x,y+367),f'{i+1:02}',fill='#1d1d1f')
sheet.save(O/'contact-sheet.png');(R/'qa/layout-report.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print('Rendered',len(d),'pages; text warnings',sum(len(p['text_bounds_warnings']) for p in result['pages']))
