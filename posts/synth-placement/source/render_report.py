from pathlib import Path
import re,html,json
from weasyprint import HTML
import fitz
from PIL import Image,ImageOps,ImageDraw
R=Path(__file__).resolve().parents[1]
md=(R/'RESEARCH_REPORT.md').read_text()
def inline(s):
 s=html.escape(s)
 return re.sub(r'\[([^]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
parts=[];in_code=False;lst=None
for block in md.split('\n\n'):
 if block.startswith('```'):
  parts.append('<pre>'+html.escape(block.strip().split('\n',1)[1].rsplit('\n',1)[0])+'</pre>');continue
 if block.startswith('!['):
  m=re.match(r'!\[(.*?)\]\((.*?)\)',block);src=m.group(2);cls='utility' if 'utility-official' in src else 'figure';parts.append(f'<figure class="{cls}"><img src="{src}" alt="{m.group(1)}"></figure>');continue
 if block.startswith('## '):parts.append(('<h2 class="refs">' if block[3:]=='参考资料' else '<h2>')+inline(block[3:])+'</h2>');continue
 if block.startswith('# '):parts.append('<h1>'+inline(block[2:])+'</h1>');continue
 if block.startswith('- '):parts.append('<ul>'+''.join('<li>'+inline(x[2:])+'</li>' for x in block.split('\n'))+'</ul>');continue
 if re.match(r'\d+\. ',block):parts.append('<ol>'+''.join('<li>'+inline(re.sub(r'^\d+\. ','',x))+'</li>' for x in block.split('\n'))+'</ol>');continue
 parts.append('<p>'+inline(block)+'</p>')
css='''@font-face{font-family:Noto;src:url(assets/fonts/NotoSansSC-Variable.ttf)}@font-face{font-family:Formula;src:url(assets/fonts/NotoSans-Regular.ttf)}@page{size:A4;margin:18mm 18mm 20mm;@bottom-left{content:"MUSIC MIXING SECRETS / SYNTH PLACEMENT";font-family:Noto;font-size:8pt;color:#697887}@bottom-right{content:counter(page);font-family:Noto;font-size:9pt;color:#697887}}body{font-family:Noto,Formula,sans-serif;font-size:10.5pt;line-height:1.75;color:#1d1d1f;margin:0}h1{font-size:24pt;line-height:1.35;margin:0 0 14pt;color:#000}h2.refs{break-before:page}h2{font-size:16pt;line-height:1.4;margin:20pt 0 8pt;color:#000;break-after:avoid}p{margin:0 0 10pt;orphans:3;widows:3}ul,ol{break-inside:avoid;margin:4pt 0 12pt;padding-left:20pt}li{margin-bottom:6pt}figure{margin:12pt 0 9pt;text-align:center;break-inside:avoid;break-after:avoid}figure img{max-width:100%;max-height:72mm;object-fit:contain}.utility{float:right;width:40mm;margin:0 0 8pt 14pt;break-after:auto}.utility img{height:50mm}a{color:#0066cc;text-decoration:none;word-break:break-all}pre{font-family:Formula,monospace;font-size:10pt;line-height:1.5;white-space:pre-wrap;break-inside:avoid;padding:12pt;background:#f5f5f7}'''
htmltext='<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>合成器的左右宽度与前后层次</title><style>'+css+'</style><body>'+''.join(parts)+'</body></html>'
(R/'research-report.html').write_text(htmltext)
HTML(string=htmltext,base_url=str(R)).write_pdf(R/'output/合成器的左右宽度与前后层次_研究报告.pdf')
doc=fitz.open(R/'output/合成器的左右宽度与前后层次_研究报告.pdf')
thumbs=[]
for i,p in enumerate(doc):
 pix=p.get_pixmap(matrix=fitz.Matrix(1.6,1.6),alpha=False);pix.save(R/f'qa/report/page-{i+1:02d}.png')
 im=Image.open(R/f'qa/report/page-{i+1:02d}.png');im.thumbnail((360,510));thumbs.append(im.copy())
contact=Image.new('RGB',(360*3,550*((len(thumbs)+2)//3)), '#e5e5ea')
for i,im in enumerate(thumbs):contact.paste(im,((i%3)*360,(i//3)*550))
contact.save(R/'qa/report/contact.png')
(R/'qa/report/render.json').write_text(json.dumps({'pages':len(doc),'size':'A4','full_page_pngs':len(thumbs),'text_characters':sum(len(p.get_text()) for p in doc)},indent=2))
print('REPORT_PAGES',len(doc))
