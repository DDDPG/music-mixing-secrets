from pathlib import Path
from weasyprint import HTML
import fitz,json
from PIL import Image,ImageOps,ImageDraw
p=Path(__file__).resolve().parents[1]
for name,out in [('index.html','carousel.pdf'),('research-report.html','research-report.pdf')]:
 HTML(filename=str(p/name)).write_pdf(p/'output'/out)
 d=fitz.open(p/'output'/out)
 if name=='index.html':
  for i,pg in enumerate(d):
   pix=pg.get_pixmap(matrix=fitz.Matrix(4/3,4/3),alpha=False)
   pix.save(p/f'output/{i+1:02d}.png')
   Image.open(p/f'output/{i+1:02d}.png').resize((360,480),Image.Resampling.LANCZOS).save(p/f'phone-preview/{i+1:02d}.png')
  sheet=Image.new('RGB',(1080,1440),'#dddddd')
  for i in range(len(d)):sheet.paste(Image.open(p/f'phone-preview/{i+1:02d}.png'),((i%3)*360,(i//3)*480))
  sheet.save(p/'output/contact-sheet.jpg',quality=95)
 else:
  (p/'qa/report-preview').mkdir(exist_ok=True)
  for old in (p/'qa/report-preview').glob('*.png'):old.unlink()
  for i,pg in enumerate(d):pg.get_pixmap(matrix=fitz.Matrix(.65,.65)).save(p/f'qa/report-preview/{i+1:02d}.png')
 print(out,len(d),'pages')
