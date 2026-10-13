from pathlib import Path
import json,html,math
R=Path(__file__).resolve().parents[1]
spec=json.loads((R/'design/production_spec.json').read_text())
def esc(s):return html.escape(str(s),quote=True)
def shape(e):
 typ=e['type'];fill=e.get('fill','none');stroke=e.get('stroke','none');sw=e.get('stroke_width',2);attrs=f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"'
 if typ=='rect':
  x,y,w,h=e['box'];return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{e.get("radius",0)}" {attrs}/>'
 if typ=='circle':
  x,y=e['center'];return f'<circle cx="{x}" cy="{y}" r="{e["radius"]}" {attrs}/>'
 if typ in ['line','polyline']:
  pts=e['points'];ps=' '.join(f'{x},{y}' for x,y in pts);dash=e.get('dash',e.get('stroke_dasharray',''));out=f'<polyline points="{ps}" fill="none" stroke="{stroke}" stroke-width="{sw}" stroke-dasharray="{dash}" stroke-linejoin="round"/>'
  if e.get('end_arrow'):
   x,y=pts[-1];xx,yy=pts[-2];a=math.atan2(y-yy,x-xx);size=e.get('arrow_size',13);w=size*.42;bx=x-size*math.cos(a);by=y-size*math.sin(a)
   p1=(bx+w*math.sin(a),by-w*math.cos(a));p2=(bx-w*math.sin(a),by+w*math.cos(a));out+=f'<polygon points="{x},{y} {p1[0]},{p1[1]} {p2[0]},{p2[1]}" fill="{stroke}"/>'
  return out
 if typ=='polygon':return '<polygon points="'+' '.join(f'{x},{y}' for x,y in e['points'])+f'" {attrs}/>'
 if typ=='path':return f'<path d="{e["d"]}" {attrs}/>'
 raise ValueError(typ)
css='''@font-face{font-family:Noto;src:url('assets/fonts/NotoSansSC-Variable.ttf');font-weight:100 900}@font-face{font-family:Formula;src:url('assets/fonts/NotoSans-Regular.ttf')}@page{size:1080px 1440px;margin:0}html,body{margin:0;padding:0;background:white;font-family:Noto,Formula,sans-serif}*{box-sizing:border-box}.poster{position:relative;width:1080px;height:1440px;overflow:hidden;break-after:page}.poster:last-child{break-after:auto}.shapes{position:absolute;left:0;top:0;width:1080px;height:1440px;z-index:0}.copy{position:absolute;margin:0;padding:0;white-space:pre;letter-spacing:0;font-kerning:normal;font-variant-numeric:tabular-nums;z-index:3}.source-image{position:absolute;display:block;object-fit:contain;z-index:1}a{color:inherit;text-decoration:none}'''
pages=[]
for p in spec['pages']:
 graphic=[];imgs=[];texts=[]
 for e in p['elements']:
  typ=e['type']
  if typ=='text':
   x,y,w,h=e['box'];s=str(e['text']).replace('\\n','\n');inner=esc(s);style=f'left:{x}px;top:{y}px;width:{w}px;height:{h}px;font-size:{e["font_size"]}px;font-weight:{e.get("font_weight",400)};line-height:{e.get("line_height",e["font_size"]*1.4)}px;color:{e.get("color","#1d1d1f")};text-align:{e.get("align","left")}'
   if e.get('href'):inner=f'<a href="{esc(e["href"])}">{inner}</a>'
   texts.append(f'<div class="copy" data-element="{e["id"]}" style="{style}">{inner}</div>')
  elif typ=='image':
   x,y,w,h=e['box'];assert (R/e['path']).is_file(),e['path'];imgs.append(f'<img class="source-image" src="{esc(e["path"])}" alt="{esc(e.get("alt",e["id"]))}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;object-fit:{e.get("fit","contain")}">')
  else:graphic.append(shape(e))
 pages.append(f'<section class="poster" id="page-{p["page"]:02d}" style="background:{p.get("background","#ffffff")}"><svg class="shapes" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1440">'+''.join(graphic)+'</svg>'+''.join(imgs)+''.join(texts)+'</section>')
(R/'index.html').write_text('<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>合成器的前后左右</title><style>'+css+'</style></head><body>'+''.join(pages)+'</body></html>')
print('BUILT',len(pages),'pages')
