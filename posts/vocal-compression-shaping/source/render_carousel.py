from pathlib import Path
from urllib.parse import urlparse
from weasyprint import HTML,default_url_fetcher
from weasyprint.text.fonts import FontConfiguration
import fitz,json
from PIL import Image,ImageDraw
P=Path(__file__).resolve().parents[1]
for d in ['output','qa','phone-preview']:(P/d).mkdir(exist_ok=True)
spec=json.loads((P/'design/production_spec.json').read_text())
def local(url,*args,**kwargs):
 if urlparse(url).scheme not in ['file','data']:raise RuntimeError('Rendering must be offline')
 return default_url_fetcher(url,*args,**kwargs)
doc=HTML(filename=str(P/'index.html'),url_fetcher=local).render(font_config=FontConfiguration());assert len(doc.pages)==len(spec['pages'])
doc.write_pdf(P/'output/vocal-compression-shaping.pdf');pdf=fitz.open(P/'output/vocal-compression-shaping.pdf');qa=[];thumbs=[]
for i,page in enumerate(pdf):
 pix=page.get_pixmap(matrix=fitz.Matrix(4/3,4/3),alpha=False);assert (pix.width,pix.height)==(1080,1440);pix.save(P/f'output/xhs-{i+1:02}.png')
 im=Image.open(P/f'output/xhs-{i+1:02}.png');im.resize((360,480),Image.Resampling.LANCZOS).save(P/f'phone-preview/xhs-{i+1:02}-360.png');thumbs.append(im.resize((270,360),Image.Resampling.LANCZOS))
 boxes=[]
 for b in page.get_text('dict')['blocks']:
  for l in b.get('lines',[]):
   for s in l['spans']:
    x0,y0,x1,y1=[v*4/3 for v in s['bbox']];boxes.append(dict(text=s['text'],box=[x0,y0,x1,y1]))
 qa.append(dict(page=i+1,text_bounds_warnings=[b for b in boxes if b['box'][0]<60 or b['box'][2]>1020 or b['box'][1]<20 or b['box'][3]>1438],text_boxes=boxes,links=[dict(uri=l.get("uri"),rect=list(l["from"])) for l in page.get_links()]))
out=Image.new('RGB',(3*294+24,((len(thumbs)+2)//3)*408+24),'#e5e5ea');d=ImageDraw.Draw(out)
for i,im in enumerate(thumbs):x=24+i%3*294;y=24+i//3*408;out.paste(im,(x,y));d.text((x,y+367),f'{i+1:02} / {len(thumbs):02}',fill='#1d1d1f')
out.save(P/'output/contact-sheet.png');(P/'qa/layout-report.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2));print('Rendered',len(pdf),'pages; text bounds warnings:',sum(len(p['text_bounds_warnings']) for p in qa))
