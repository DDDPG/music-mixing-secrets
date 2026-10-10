"""Build the independent V3 composition from authoritative production_spec.json.
Uses the Guizang seed as an export shell only; no inherited template aesthetics.
All source imagery remains unaltered. Rendering is local-only.
"""
from pathlib import Path
import html,json,math,re
from PIL import ImageFont
R=Path(__file__).resolve().parent
(R/'qa').mkdir(exist_ok=True)
s=json.loads((R/'production_spec.json').read_text())
# Port only file locations, never copy/layout/geometry, in the editable local spec.
for w in ['400','600']:s['tokens']['font_files'][w]=f'assets/fonts/NotoSansSC-{w}.ttf'
s['tokens']['font_license']='assets/fonts/OFL.txt'
(R/'production_spec.json').write_text(json.dumps(s,ensure_ascii=False,indent=2))
seed=(R/'seed-editorial.html').read_text()
seed=re.sub(r'<link\b[^>]*>','',seed)
seed=re.sub(r'<script\b[^>]*>[\s\S]*?</script>','',seed)
seed=seed.replace('[必填] 替换为社交卡组标题 · Social Card Set','人声空间与 Side EQ · 混音笔记')
seed=seed.replace('data-theme="ink-classic"','data-theme="apple-v3"')
css='''
@font-face{font-family:'Noto Sans SC';src:url('assets/fonts/NotoSansSC-400.ttf');font-weight:400;font-style:normal}
@font-face{font-family:'Noto Sans SC';src:url('assets/fonts/NotoSansSC-600.ttf');font-weight:600;font-style:normal}
@font-face{font-family:'Noto Sans Formula';src:url('assets/fonts/NotoSans-Regular.ttf');font-weight:400;font-style:normal}
@page{size:1080px 1440px;margin:0}
html,body{margin:0;padding:0;background:#fff;font-family:'Noto Sans SC','Noto Sans Formula',sans-serif}
*{box-sizing:border-box} figure{margin:0}
.poster.xhs{position:relative;width:1080px;height:1440px;margin:0;padding:0;overflow:hidden;break-after:page}
.poster.xhs:last-child{break-after:auto}
.copy{position:absolute;margin:0;padding:0;white-space:pre;letter-spacing:0;font-kerning:normal;font-variant-numeric:tabular-nums;z-index:3}
.diagram{position:absolute;left:0;top:0;width:1080px;height:1440px;z-index:0}
.source-image{position:absolute;display:block;margin:0;padding:0;border:0;object-fit:contain;z-index:1}
'''
seed=re.sub(r'<style>[\s\S]*?</style>',f'<style>\n{css}\n</style>',seed,count=1)
def sh(e):
 t=e['type'];c=e.get('stroke') or 'none';sw=e.get('stroke_width',0);fill=e.get('fill') or 'none'
 attr=f' id="{e["id"]}" stroke="{c}" stroke-width="{sw}" fill="{fill}"'
 if t=='rect':
  x,y,w,h=e['box'];return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{e.get("radius",0)}"{attr}/>'
 if t=='circle':
  x,y=e['center'];return f'<circle cx="{x}" cy="{y}" r="{e["radius"]}"{attr}/>'
 if t in ('line','polyline'):
  ps=e['points'];points=' '.join(f'{x},{y}' for x,y in ps)
  out=f'<polyline points="{points}"{attr} stroke-linecap="butt" stroke-linejoin="round"/>'
  if e.get('end_arrow'):
   # Filled triangle in exact canvas coordinates avoids renderer marker quirks.
   x,y=ps[-1];a,b=ps[-2];dx,dy=x-a,y-b;length=math.hypot(dx,dy);ux,uy=dx/length,dy/length
   bx,by=x-12*ux,y-12*uy
   q=f'{x},{y} {bx-5*uy},{by+5*ux} {bx+5*uy},{by-5*ux}'
   out+=f'<polygon points="{q}" fill="{c}"/>'
  return out
 raise ValueError(t)
posters=[];copy=[];issues=[]
for p in s['pages']:
 shapes=[];images=[];texts=[]
 for e in p['elements']:
  t=e['type']
  if t=='text':
   x,y,w,h=e['box'];fs=e['font_size'];fw=e['font_weight'];lh=e['line_height'];text=e['text'];font=ImageFont.truetype(str(R/f'assets/fonts/NotoSansSC-{fw}.ttf'),fs)
   maxw=max(font.getlength(ln) for ln in text.split('\n'))
   if maxw>w+1 or len(text.split('\n'))*lh>h+1:issues.append({'page':p['page'],'id':e['id'],'width':maxw,'available_width':w,'line_height_sum':len(text.split('\n'))*lh,'available_height':h})
   style=f'left:{x}px;top:{y}px;width:{w}px;height:{h}px;font-size:{fs}px;font-weight:{fw};line-height:{lh}px;color:{e["color"]};text-align:{e["align"]}'
   texts.append(f'<div class="copy" data-element="{e["id"]}" style="{style}">{html.escape(text)}</div>');copy.append(f'P{p["page"]:02} {e["id"]}\n{text}\n')
  elif t=='image':
   x,y,w,h=e['box'];images.append(f'<img class="source-image" src="{e["file"]}" alt="{html.escape(e.get("alt",""),quote=True)}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;object-position:center 50%">')
  else:shapes.append(sh(e))
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" class="diagram" width="1080" height="1440" viewBox="0 0 1080 1440">'+''.join(shapes)+'</svg>'
 (R/'assets'/f'page-{p["page"]:02}-geometry.svg').write_text(svg)
 posters.append(f'<section class="poster xhs" id="xhs-{p["page"]:02}" data-recipe="independent-apple-v3" style="background:{p["background"]}">{svg}{"".join(images)}{"".join(texts)}</section>')
seed=re.sub(r'<body\b[^>]*>[\s\S]*</body>','<body>\n<!-- Independent content-first V3. Seed used only for export shell. -->\n'+''.join(posters)+'\n</body>',seed)
(R/'index.html').write_text(seed)
(R/'visible-copy.txt').write_text('\n'.join(copy))
(R/'qa/font-metrics.json').write_text(json.dumps({'issues':issues,'pages':len(s['pages']),'checked_with':'packaged Noto Sans SC 400/600; no font shrinking'},ensure_ascii=False,indent=2))
print('Built',len(s['pages']),'pages; metric issues:',len(issues));print(issues)
