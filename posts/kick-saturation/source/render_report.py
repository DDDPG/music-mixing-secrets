from pathlib import Path
import re,html,fitz
from weasyprint import HTML
from PIL import Image,ImageDraw
P=Path(__file__).resolve().parents[1]
for d in ['output','qa']:(P/d).mkdir(exist_ok=True)
s=(P/'RESEARCH_REPORT.md').read_text();s=re.sub(r'(^#{1,2} [^\n]+)\n',r'\1\n\n',s,flags=re.M);parts=[]
for p in s.split('\n\n'):
 p=p.strip()
 if p.startswith('# '):parts.append('<h1>'+html.escape(p[2:])+'</h1>')
 elif p.startswith('## '):parts.append('<h2>'+html.escape(p[3:])+'</h2>')
 else:
  t=html.escape(p).replace('\n','<br>');t=re.sub(r'(https://[^ <]+)',r'<a href="\1">\1</a>',t);parts.append('<p>'+t+'</p>')
body=''.join(parts)
for title,path,caption in [('解析模型的完整计算','assets/diagrams/transfer.svg','图1 共尺度的线性参照与非线性教学曲线'),('可执行试听协议','assets/diagrams/harmonics.svg','图2 解析谱线，处理后基频归一化为 0 dB'),('低频与相位的边界','assets/diagrams/parallel.svg','图3 并行路由与低频关系'),('过采样分析的适用条件','assets/diagrams/aliasing.svg','图4 未滤除高次谐波的采样折叠示意')]:
 body=body.replace('<h2>'+title+'</h2>',f'<h2>{title}</h2><figure><img src="{path}"><figcaption>{caption}</figcaption></figure>')
body=body.replace('<h2>操作失败时如何回退</h2>','<h2>操作失败时如何回退</h2><figure><img src="assets/derived/saturn-band-controls.png"><figcaption>图5 以 Saturn 2 为例：Mix、Drive 与 Level 的位置与角色。</figcaption></figure>')
css='''@font-face{font-family:Noto;src:url(assets/fonts/NotoSansSC-400.ttf)}@font-face{font-family:Noto;src:url(assets/fonts/NotoSansSC-600.ttf);font-weight:600}@page{size:A4;margin:20mm 18mm 22mm;@bottom-center{content:counter(page);font-size:9pt;color:#697887}}body{font-family:Noto;color:#1d1d1f;font-size:10.5pt;line-height:1.75}h1{font-size:25pt;line-height:1.4}h2{font-size:16pt;margin-top:24pt;break-after:avoid}p{margin:10pt 0;orphans:3;widows:3}figure{margin:16pt 0;break-inside:avoid}img{width:100%;max-height:72mm;object-fit:contain}figcaption{font-size:9pt;color:#515154}a{color:#0066cc;overflow-wrap:anywhere}'''
(P/'RESEARCH_REPORT.html').write_text('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>底鼓饱和处理研究</title><style>'+css+'</style><body>'+body+'</body></html>')
HTML(filename=str(P/'RESEARCH_REPORT.html')).write_pdf(P/'output/research-report.pdf');doc=fitz.open(P/'output/research-report.pdf');thumb=[]
for i,page in enumerate(doc):
 pix=page.get_pixmap(matrix=fitz.Matrix(1,1),alpha=False);pix.save(P/f'qa/report-{i+1:02}.png');im=Image.open(P/f'qa/report-{i+1:02}.png');im.thumbnail((240,340));thumb.append(im)
sheet=Image.new('RGB',(800,370*((len(thumb)+2)//3)),'#e5e5ea');d=ImageDraw.Draw(sheet)
for i,im in enumerate(thumb):x=20+(i%3)*260;y=15+(i//3)*370;sheet.paste(im,(x,y));d.text((x,y+340),str(i+1),fill='black')
sheet.save(P/'qa/report-contact-sheet.png');print('Report pages:',len(doc))
