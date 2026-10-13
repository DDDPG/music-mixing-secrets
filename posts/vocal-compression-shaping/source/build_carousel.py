"""Build editable HTML from the independently reviewed page specification.
AGPL-3.0 derivative export shell; vendor image and font terms remain separate.
"""
from pathlib import Path
import html,json,math,re
from PIL import ImageFont
P=Path(__file__).resolve().parents[1]
s=json.loads((P/'design/production_spec.json').read_text())
css='''@font-face{font-family:NotoSC;src:url(assets/fonts/NotoSansSC-400.ttf);font-weight:400}@font-face{font-family:NotoSC;src:url(assets/fonts/NotoSansSC-600.ttf);font-weight:600}@font-face{font-family:Noto;src:url(assets/fonts/NotoSans-Regular.ttf)}@page{size:1080px 1440px;margin:0}html,body{margin:0;padding:0;background:white;color:#1d1d1f;font-family:NotoSC,Noto,sans-serif}*{box-sizing:border-box}section.poster{position:relative;width:1080px;height:1440px;overflow:hidden;break-after:page}section.poster:last-child{break-after:auto}.copy{position:absolute;margin:0;padding:0;white-space:pre;letter-spacing:0;font-variant-numeric:tabular-nums;z-index:3}.geometry{position:absolute;left:0;top:0;width:1080px;height:1440px;z-index:0}.source-image{position:absolute;display:block;border:0;object-fit:contain;z-index:1}.active-link{position:absolute;z-index:4;color:transparent;text-decoration:none}'''
def shape(e):
 t=e['type'];stroke=e.get('stroke','none');sw=e.get('stroke_width',0);fill=e.get('fill','none');a=f' id="{e["id"]}" stroke="{stroke}" stroke-width="{sw}" fill="{fill}"'
 if e.get('dash'):a+=f' stroke-dasharray="{e["dash"]}"'
 if t=='rect':
  x,y,w,h=e['box'];return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{e.get("radius",0)}"{a}/>'
 if t=='circle':
  x,y=e['center'];return f'<circle cx="{x}" cy="{y}" r="{e["radius"]}"{a}/>'
 if t in ['line','polyline']:
  points=' '.join(f'{x},{y}' for x,y in e['points']);out=f'<polyline points="{points}"{a} stroke-linejoin="round"/>'
  if e.get('end_arrow'):
   x,y=e['points'][-1];u,v=e['points'][-2];length=math.hypot(x-u,y-v);dx,dy=(x-u)/length,(y-v)/length;bx,by=x-12*dx,y-12*dy
   out+=f'<polygon points="{x},{y} {bx-5*dy},{by+5*dx} {bx+5*dy},{by-5*dx}" fill="{stroke}"/>'
  return out
 if t=='path':return f'<path d="{e["d"]}"{a}/>'
 raise ValueError(t)
sections=[];issues=[];visible=[]
for p in s['pages']:
 shapes=[];images=[];texts=[]
 for e in p['elements']:
  t=e['type']
  if t=='text':
   x,y,w,h=e['box'];fs=e['font_size'];fw=e.get('font_weight',400);lh=e['line_height'];text=e['text'];font=ImageFont.truetype(str(P/f'assets/fonts/NotoSansSC-{fw}.ttf'),fs)
   widths=[font.getlength(line) for line in text.split('\n')]
   if max(widths)>w+1 or len(widths)*lh>h+1:issues.append(dict(page=p['page'],id=e['id'],width=max(widths),available_width=w,height=len(widths)*lh,available_height=h))
   st=f'left:{x}px;top:{y}px;width:{w}px;height:{h}px;font-size:{fs}px;font-weight:{fw};line-height:{lh}px;color:{e["color"]};text-align:{e.get("align","left")}'
   texts.append(f'<div class="copy" data-id="{e["id"]}" style="{st}">{html.escape(text)}</div>');visible.append(f'Page {p["page"]} {e["id"]}\n{text}')
  elif t=='image':
   x,y,w,h=e['box'];src=e.get('path',e.get('file'));images.append(f'<img class="source-image" src="{src}" alt="{html.escape(e.get("alt","FabFilter Pro-C 3 official source image"))}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">')
  else:shapes.append(shape(e))
 svg='<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1440" viewBox="0 0 1080 1440" class="geometry">'+''.join(shapes)+'</svg>'
 (P/f'assets/diagrams/page-{p["page"]:02}-geometry.svg').write_text(svg)
 links=[]
 for link in p.get('links',[]):
  x,y,w,h=link['box'];links.append(f'<a class="active-link" aria-label="{html.escape(link["url"])}" href="{html.escape(link["url"])}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"> </a>')
 sections.append(f'<section class="poster" id="page-{p["page"]:02}" style="background:{p["background"]}">{svg}{"".join(images)}{"".join(texts)}{"".join(links)}</section>')
seed=(P/'source/seed-editorial.html').read_text();seed=re.sub(r'<link\b[^>]*>','',seed);seed=re.sub(r'<script\b[^>]*>[\s\S]*?</script>','',seed)
seed=re.sub(r'<title>[\s\S]*?</title>','<title>人声压缩怎样塑形</title>',seed)
seed=re.sub(r'<style>[\s\S]*?</style>','<style>'+css+'</style>',seed,count=1)
seed=re.sub(r'<body\b[^>]*>[\s\S]*</body>','<body>'+''.join(sections)+'</body>',seed)
(P/'index.html').write_text(seed);(P/'qa/visible-copy.txt').write_text('\n\n'.join(visible));(P/'qa/font-metrics.json').write_text(json.dumps({'issues':issues,'page_count':len(s['pages'])},ensure_ascii=False,indent=2))
print('Built',len(s['pages']),'pages; metric issues:',len(issues));print(json.dumps(issues,ensure_ascii=False))
