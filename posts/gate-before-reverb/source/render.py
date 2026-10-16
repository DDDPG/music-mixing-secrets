from pathlib import Path
import fitz,json
from PIL import Image,ImageDraw
from weasyprint import HTML,default_url_fetcher
from urllib.parse import urlparse
R=Path(__file__).resolve().parents[1];P=R/'phone-preview';P.mkdir(exist_ok=True)
def fetch(url,*a,**k):
 if urlparse(url).scheme not in ('file','data'):raise ValueError(url)
 return default_url_fetcher(url,*a,**k)
qa={}
for name,src,out in [('carousel',R/'source/index.html',R/'output/gate-before-reverb.pdf'),('report',R/'research/RESEARCH_REPORT.html',R/'research/RESEARCH_REPORT.pdf')]:
 HTML(filename=str(src),url_fetcher=fetch).write_pdf(out);d=fitz.open(out);thumbs=[];warnings=[]
 for i,p in enumerate(d):
  dest=R/'output'/f'xhs-{i+1:02}.png' if name=='carousel' else R/'qa'/f'report-{i+1:02}.png';pix=p.get_pixmap(matrix=fitz.Matrix(4/3,4/3),alpha=False);pix.save(dest);im=Image.open(dest)
  if name=='carousel':
   assert im.size==(1080,1440);im.resize((360,480)).save(P/f'xhs-{i+1:02}-360.png')
  im.thumbnail((270,380));thumbs.append(im.copy())
  for b in p.get_text('blocks'):
   if b[0]<0 or b[1]<0 or b[2]>p.rect.width+1 or b[3]>p.rect.height+1:warnings.append([i+1,list(b[:4])])
 sheet=Image.new('RGB',(4*290,((len(thumbs)+3)//4)*410),'#e5e5ea');draw=ImageDraw.Draw(sheet)
 for i,im in enumerate(thumbs):x=(i%4)*290+10;y=(i//4)*410+10;sheet.paste(im,(x,y));draw.text((x,y+382),str(i+1),fill='#1d1d1f')
 sheet.save(R/('output' if name=='carousel' else 'qa')/(name+'-contact-sheet.png'))
 qa[name]={'pages':len(d),'bounds_warnings':warnings,'text_characters':sum(len(p.get_text()) for p in d)}
 if name=='carousel':assert len(d)==8
(R/'qa/layout-report.json').write_text(json.dumps(qa,indent=2));print(qa)
