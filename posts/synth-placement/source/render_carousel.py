from pathlib import Path
import json,re,hashlib
from weasyprint import HTML
import fitz
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[1]
html=(R/'index.html').read_text()
expected=len(re.findall(r'<section class="poster',html))
assert expected>0,'No pages'
out=R/'output';phone=R/'phone-preview';out.mkdir(exist_ok=True);phone.mkdir(exist_ok=True)
pdf=out/'合成器的前后左右_图文.pdf'
HTML(filename=str(R/'index.html')).write_pdf(pdf)
doc=fitz.open(pdf);assert len(doc)==expected,(len(doc),expected)
problems=[];pages=[]
for n,p in enumerate(doc,1):
 assert abs(p.rect.width-810)<0.1 and abs(p.rect.height-1080)<0.1
 full=out/f'{n:02d}.png';small=phone/f'{n:02d}.png'
 p.get_pixmap(matrix=fitz.Matrix(4/3,4/3),alpha=False).save(full)
 im=Image.open(full);assert im.size==(1080,1440);im.resize((360,480),Image.Resampling.LANCZOS).save(small)
 spans=[]
 for block in p.get_text('dict')['blocks']:
  for line in block.get('lines',[]):
   for s in line['spans']:
    x0,y0,x1,y1=s['bbox']
    if x0<48 or x1>762 or y0<25 or y1>1071: problems.append({'page':n,'text':s['text'],'bbox':s['bbox']})
    spans.append(s)
 pages.append({'page':n,'text':p.get_text(),'text_spans':len(spans),'sha256':hashlib.sha256(full.read_bytes()).hexdigest(),'phone_sha256':hashlib.sha256(small.read_bytes()).hexdigest()})
assert 'Kangdi, Wang' in pages[-1]['text']
assert any(l.get('uri')=='https://github.com/DDDPG/music-mixing-secrets' for l in doc[-1].get_links())
for start in range(0,len(doc),6):
 sheet=Image.new('RGB',(360*3,510*2),'#e5e5ea');d=ImageDraw.Draw(sheet)
 for j,n in enumerate(range(start,min(start+6,len(doc)))):
  im=Image.open(phone/f'{n+1:02d}.png');sheet.paste(im,((j%3)*360,(j//3)*510));d.text(((j%3)*360+10,(j//3)*510+482),str(n+1),fill='black')
 sheet.save(R/f'qa/contact-{start//6+1}.png')
(R/'qa/render.json').write_text(json.dumps({'pages':len(doc),'dimensions':[1080,1440],'phone_dimensions':[360,480],'out_of_safe_area':problems,'page_text':pages,'renderer':'WeasyPrint 66.0 / PyMuPDF'},ensure_ascii=False,indent=2))
print(json.dumps({'pages':len(doc),'out_of_safe_area':problems},ensure_ascii=False))
