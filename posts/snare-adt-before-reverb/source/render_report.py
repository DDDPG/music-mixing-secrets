from pathlib import Path
from weasyprint import HTML,default_url_fetcher
from urllib.parse import urlparse
import fitz,json
from PIL import Image,ImageOps,ImageDraw
R=Path(__file__).resolve().parents[1]
def local_only(url,*a,**kw):
 if urlparse(url).scheme not in ('file','data'):raise RuntimeError('External fetch prohibited during rendering')
 return default_url_fetcher(url,*a,**kw)
HTML(filename=str(R/'research/RESEARCH_REPORT.html'),url_fetcher=local_only).write_pdf(R/'research/RESEARCH_REPORT.pdf')
d=fitz.open(R/'research/RESEARCH_REPORT.pdf'); thumbs=[]
for i,p in enumerate(d):
 q=R/f'qa/report-{i+1:02}.png';p.get_pixmap(matrix=fitz.Matrix(1.2,1.2)).save(q)
 im=Image.open(q);im.thumbnail((320,450));thumbs.append(im.copy())
w=960;h=((len(thumbs)+2)//3)*480
sheet=Image.new('RGB',(w,h),'#dedede');draw=ImageDraw.Draw(sheet)
for i,im in enumerate(thumbs):x=i%3*320;y=i//3*480;sheet.paste(im,(x,y));draw.text((x+10,y+455),str(i+1),fill='black')
sheet.save(R/'qa/report-contact-sheet.jpg')
print('report pages',len(d));print('text length',sum(len(p.get_text()) for p in d))
