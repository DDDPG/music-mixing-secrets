"""Build editable local HTML/SVG from independent design/production_spec.json.
Export shell derived from the retained AGPL Guizang cf4b810 scaffold.
"""
from pathlib import Path
import html,json,math,re
from PIL import ImageFont
from fontTools.ttLib import TTFont
from fontTools import subset
from fontTools.varLib.instancer import instantiateVariableFont
R=Path(__file__).resolve().parents[1]
s=json.loads((R/'design/production_spec.json').read_text())
full=''.join(e.get('text','') for p in s['pages'] for e in p['elements'])+(R/'research/RESEARCH_REPORT.md').read_text()
for weight in [400,600]:
 font=TTFont(R/'assets/fonts/NotoSansSC-Variable.ttf')
 instantiateVariableFont(font,{'wght':weight},inplace=True)
 opts=subset.Options();opts.layout_features='*';opts.name_IDs=['*'];opts.name_legacy=True;opts.name_languages=['*']
 sub=subset.Subsetter(options=opts);sub.populate(text=full);sub.subset(font);font.save(R/f'assets/fonts/NotoSansSC-{weight}.ttf')
seed=(R/'source/seed-editorial.html').read_text()
seed=re.sub(r'<link\b[^>]*>','',seed);seed=re.sub(r'<script\b[^>]*>[\s\S]*?</script>','',seed)
seed=re.sub(r'<title>[\s\S]*?</title>','<title>军鼓混响前的 ADT 拓宽</title>',seed)
seed=seed.replace('data-theme="ink-classic"','data-theme="v3-white-gray-blue"')
css='''@font-face{font-family:'Noto Sans SC';src:url('assets/fonts/NotoSansSC-400.ttf');font-weight:400}@font-face{font-family:'Noto Sans SC';src:url('assets/fonts/NotoSansSC-600.ttf');font-weight:600}@font-face{font-family:'Noto Sans Formula';src:url('assets/fonts/NotoSans-Regular.ttf');font-weight:400}@page{size:1080px 1440px;margin:0}html,body{margin:0;padding:0;background:#fff;font-family:'Noto Sans SC','Noto Sans Formula',sans-serif}*{box-sizing:border-box}figure{margin:0}.poster.xhs{position:relative;width:1080px;height:1440px;margin:0;padding:0;overflow:hidden;break-after:page}.poster.xhs:last-child{break-after:auto}.copy{position:absolute;margin:0;padding:0;white-space:pre;letter-spacing:0;font-kerning:normal;font-variant-numeric:tabular-nums;z-index:3}.diagram{position:absolute;left:0;top:0;width:1080px;height:1440px;z-index:0}.source-image{position:absolute;display:block;margin:0;padding:0;border:0;object-fit:contain;z-index:1}a{color:inherit;text-decoration:none}'''
seed=re.sub(r'<style>[\s\S]*?</style>',f'<style>{css}</style>',seed,count=1)
def box(e):return e['box'] if 'box' in e else [e[k] for k in ['x','y','w','h']]
def sh(e):
 t=e['type'];c=e.get('stroke') or 'none';sw=e.get('stroke_width',0);fill=e.get('fill') or 'none';id=e.get('id','')
 attr=f' id="{id}" stroke="{c}" stroke-width="{sw}" fill="{fill}"'
 if t=='rect':
  x,y,w,h=box(e);return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{e.get("radius",0)}"{attr}/>'
 if t=='circle':
  x,y=e['center'];return f'<circle cx="{x}" cy="{y}" r="{e["radius"]}"{attr}/>'
 if t in ['line','polyline']:
  ps=e.get('points',[[e.get('x1',0),e.get('y1',0)],[e.get('x2',0),e.get('y2',0)]]);points=' '.join(f'{x},{y}' for x,y in ps)
  out=f'<polyline points="{points}"{attr} stroke-linecap="round" stroke-linejoin="round"/>'
  if e.get('end_arrow'):
   x,y=ps[-1];a,b=ps[-2];dx,dy=x-a,y-b;le=math.hypot(dx,dy);ux,uy=dx/le,dy/le;bx,by=x-12*ux,y-12*uy
   out+=f'<polygon points="{x},{y} {bx-5*uy},{by+5*ux} {bx+5*uy},{by-5*ux}" fill="{c}"/>'
  return out
 if t=='path':return f'<path d="{e["d"]}"{attr}/>'
 if t=='polygon':return f'<polygon points="{e["points"]}"{attr}/>'
 raise ValueError(t)
posters=[];copy=[];issues=[]
for p in s['pages']:
 shapes=[];images=[];texts=[]
 for e in p['elements']:
  t=e['type']
  if t=='text':
   x,y,w,h=box(e);fs=e['font_size'];fw=e.get('font_weight',400);lh=e.get('line_height',round(fs*1.4));text=e['text'];font=ImageFont.truetype(str(R/f'assets/fonts/NotoSansSC-{600 if fw>=600 else 400}.ttf'),fs)
   maxw=max([font.getlength(ln) for ln in text.split('\n')] or [0])
   if maxw>w+1 or len(text.split('\n'))*lh>h+1:issues.append({'page':p['page'],'id':e.get('id'),'width':maxw,'available_width':w,'line_height_sum':len(text.split('\n'))*lh,'available_height':h})
   style=f'left:{x}px;top:{y}px;width:{w}px;height:{h}px;font-size:{fs}px;font-weight:{fw};line-height:{lh}px;color:{e.get("color","#1d1d1f")};text-align:{e.get("align","left")}'
   content=html.escape(text)
   if e.get('href') or e.get('link'):content=f'<a href="{e.get("href",e.get("link"))}">{content}</a>'
   texts.append(f'<div class="copy" data-element="{e.get("id","")}" style="{style}">{content}</div>');copy.append(f'P{p["page"]:02} {e.get("id","")}\n{text}\n')
  elif t=='image':
   x,y,w,h=box(e);src=e.get('file',e.get('src',e.get('path')));images.append(f'<img class="source-image" src="{src}" alt="{html.escape(e.get("alt","真实产品图或原创解释示意；详见来源与权属记录"))}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;object-position:center">')
  else:shapes.append(sh(e))
 svg='<svg xmlns="http://www.w3.org/2000/svg" class="diagram" width="1080" height="1440" viewBox="0 0 1080 1440">'+''.join(shapes)+'</svg>'
 (R/'assets/diagrams'/f'page-{p["page"]:02}-geometry.svg').write_text(svg)
 posters.append(f'<section class="poster xhs" id="xhs-{p["page"]:02}" style="background:{p.get("background","#ffffff")}">{svg}{"".join(images)}{"".join(texts)}</section>')
seed=re.sub(r'<body\b[^>]*>[\s\S]*</body>','<body>\n'+''.join(posters)+'\n</body>',seed)
(R/'index.html').write_text(seed);(R/'qa/visible-copy.txt').write_text('\n'.join(copy))
(R/'qa/font-metrics.json').write_text(json.dumps({'issues':issues,'pages':len(s['pages'])},ensure_ascii=False,indent=2))
print('Built',len(s['pages']),'pages; metric issues:',len(issues));print(issues)
