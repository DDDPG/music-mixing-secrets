from pathlib import Path
import re,html,json
from weasyprint import HTML
import fitz
from PIL import Image,ImageOps,ImageDraw
P=Path(__file__).resolve().parents[1]
for d in ["output","qa","phone-preview"]:(P/d).mkdir(exist_ok=True)
def inline(s):
 s=html.escape(s)
 return re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
parts=[]
for block in (P/'RESEARCH_REPORT.md').read_text().strip().split('\n\n'):
 if block.startswith('# '): parts.append('<h1>'+inline(block[2:])+'</h1><p class="subtitle">Attack 与 Release 的作用、条件与试听方法</p>')
 elif block.startswith('## '):parts.append('<h2'+(' class="references"' if block[3:]=='可复核资料与素材使用边界' else '')+'>'+inline(block[3:])+'</h2>')
 elif block.startswith('!['):
  m=re.match(r'!\[([^]]+)\]\(([^)]+)\)',block);parts.append(f'<figure><img src="{m[2]}" alt="{m[1]}"></figure>')
 elif block.startswith('- '):parts.append('<ul>'+''.join('<li>'+inline(a[2:])+'</li>' for a in block.splitlines())+'</ul>')
 elif re.match(r'\d\. ',block):parts.append('<ol>'+''.join('<li>'+inline(re.sub(r'^\d+\. ','',a))+'</li>' for a in block.splitlines())+'</ol>')
 else:parts.append('<p'+(' class="caption"' if block.startswith('图 ') else '')+'>'+inline(block)+'</p>')
css='''@font-face{font-family:NotoSC;src:url(assets/fonts/NotoSansSC-400.ttf);font-weight:400}@font-face{font-family:NotoSC;src:url(assets/fonts/NotoSansSC-600.ttf);font-weight:600}@font-face{font-family:"Noto Sans";src:url(assets/fonts/NotoSans-Regular.ttf)}@page{size:A4;margin:19mm 18mm 19mm;@bottom-center{content:"人声压缩塑形  ·  " counter(page);font-family:NotoSC;font-size:9pt;color:#697887}}*{box-sizing:border-box}body{font-family:NotoSC,"Noto Sans",sans-serif;color:#1d1d1f;font-size:10.8pt;line-height:1.78;margin:0}h1{font-size:25pt;line-height:1.35;margin:0 0 9pt;font-weight:600}h2{font-size:16pt;line-height:1.5;margin:22pt 0 9pt;break-after:avoid;font-weight:600;color:#1d1d1f}.references{break-before:page}p{margin:0 0 10pt;orphans:3;widows:3}a{color:#0066cc;text-decoration:none;overflow-wrap:anywhere}.subtitle{color:#697887;font-size:13pt;margin-bottom:20pt}.caption{font-size:9.4pt;color:#586673;line-height:1.65;break-before:avoid}figure{margin:12pt 0 9pt;break-inside:avoid}figure img{display:block;width:100%;max-height:350pt;object-fit:contain}ol,ul{padding-left:21pt;margin:0 0 12pt}li{padding-left:3pt;margin:0 0 9pt;orphans:3;widows:3}'''
s='<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>人声压缩塑形研究报告</title><style>'+css+'</style><body>'+''.join(parts)+'</body></html>'
(P/'RESEARCH_REPORT.html').write_text(s)
HTML(string=s,base_url=str(P)).write_pdf(P/'output/RESEARCH_REPORT.pdf')
doc=fitz.open(P/'output/RESEARCH_REPORT.pdf');q=P/'qa/report';q.mkdir(exist_ok=True)
thumbs=[]
for i,page in enumerate(doc):
 pix=page.get_pixmap(matrix=fitz.Matrix(1.25,1.25));pix.save(q/f'page-{i+1:02}.png')
 im=Image.open(q/f'page-{i+1:02}.png').convert('RGB');im.thumbnail((298,421));thumbs.append(im)
out=Image.new('RGB',(298*3,450*((len(thumbs)+2)//3)),'#dde1e5');d=ImageDraw.Draw(out)
for i,im in enumerate(thumbs):x=(i%3)*298;y=(i//3)*450;out.paste(im,(x,y));d.text((x+12,y+424),str(i+1),fill='black')
out.save(q/'contact-sheet.jpg');print('Report pages',len(doc))
(P/'qa/report/text.txt').write_text('\n'.join(page.get_text() for page in doc))
