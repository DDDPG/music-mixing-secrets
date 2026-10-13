from pathlib import Path
import json,math,hashlib,shutil,datetime,csv
from PIL import Image
P=Path(__file__).resolve().parents[1]
for d in ['assets/source','assets/derived','assets/diagrams','assets/fonts','research','design','source','output','qa','phone-preview']:(P/d).mkdir(parents=True,exist_ok=True)
# Genuine pixel-preserving crops. Coordinates in the unmodified 1680 x 1442 source.
src=P/'assets/source/fabfilter-pro-c-3-official.jpg'; im=Image.open(src)
crops={'compressor-controls.png':(170,680,1420,1040),'attack-release.png':(806,695,1235,925),'gain-controls.png':(1240,694,1410,1010)}
assets=[]
base={'entity':'FabFilter Pro-C 3','version':'Pro-C 3; exact point version is not stated on official image','component':'Official desktop product screenshot; channel format not identifiable','source_page':'https://www.fabfilter.com/products/pro-c-3-compressor-plug-in','asset_url':'https://cdn-b.fabfilter.com/img/products/pro-c-3-screenshot.jpg?v=1768467508','retrieved_at':'2026-10-13','rights_holder':'FabFilter','rights_status':'limited_editorial_reference_not_blanket_cleared','rights_basis':'Official product page links this image under Press and View screenshot; official Press Area supplies press kits with screenshots. This supports genuine editorial source provenance but provides no explicit broad reuse, commercial, sublicensing, or repository redistribution license. Included only as limited product-specific educational reference; rights retained by FabFilter. Publication rights assessment remains required.','attribution':'FabFilter Pro-C 3 official screenshot © FabFilter','limitations':'Official promotional image shows Nice Pumping preset and Pumping style. AUTO beside RELEASE is gray; AUTO beside GAIN is yellow. The two AUTO labels must not both be described as enabled. These settings and the displayed curves are not this tutorial’s vocal settings, and are not measurements of this tutorial. No permission to relicense vendor pixels under AGPL is asserted.'}
def record(path,id,mods,pages,**kw):
 a=dict(base);a.update(asset_id=id,path=str(path.relative_to(P)),dimensions=list(Image.open(path).size),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),modifications=mods,used_on_pages=pages);a.update(kw);assets.append(a)
record(src,'A01','Unmodified official downloaded JPEG.',[2,'report'])
for idx,(n,box) in enumerate(crops.items(),2):
 out=P/'assets/derived'/n;im.crop(box).save(out);record(out,f'A0{idx}',f'Lossless rectangular crop of decoded original pixels; box {box}, no retouching, recoloring, labels or value changes.',[3,'report'] if idx==2 else ([] if idx==3 else [7]),crop_box=list(box),parent_asset='A01')
(P/'assets.json').write_text(json.dumps({'assets':assets},ensure_ascii=False,indent=2))
blue='#0066cc'; gray='#697887'; ink='#1d1d1f';grid='#d2d2d7'
def svgstart(w,h):return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="100%" height="100%" fill="white"/><g font-family="Noto Sans,Arial,sans-serif" fill="{ink}">'
def txt(x,y,s,size=26,color=ink,anchor='start'):return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}">{s}</text>'
def line(x1,y1,x2,y2,color=grid,dash=''):return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="2"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
def path(points,color):return '<path d="'+ ' '.join(('M' if i==0 else 'L')+f'{x:.3f},{y:.3f}' for i,(x,y) in enumerate(points)) + f'" fill="none" stroke="{color}" stroke-width="5"/>'
# Shared chart geometry. Positive GR plotted upwards, with explicit scale.
W,H=936,530;x0,x1,y0,y1=100,896,425,105
s=svgstart(W,H)+txt(100,42,'Illustrative model  |  GR target: 0 → 6 dB',28)
for v in [0,2,4,6]:
 y=y0-(y0-y1)*v/6;s+=line(x0,y,x1,y)+txt(77,y+8,str(v),25,anchor='end')
for t in [0,10,30,60,90]:
 x=x0+(x1-x0)*t/90;s+=line(x,y0,x,y0+9)+txt(x,y0+42,str(t),25,anchor='middle')
s+=txt(8,88,'GR / dB',25)+txt(896,508,'Time / ms',25,anchor='end')
for tau,col in [(5,blue),(30,gray)]:s+=path([(x0+(x1-x0)*t/90,y0-(y0-y1)*(1-math.exp(-t/tau))) for t in range(91)],col)
s+=txt(534,82,'τ = 5 ms',28,blue)+txt(704,82,'τ = 30 ms',28,gray)
x=x0+(x1-x0)*10/90;s+=line(x,y0,x,y1,gray,'5 7')
for tau,col in [(5,blue),(30,gray)]:
 v=6*(1-math.exp(-10/tau));y=y0-(y0-y1)*v/6;s+=f'<circle cx="{x}" cy="{y}" r="7" fill="{col}"/>'
s+='</g></svg>';(P/'assets/diagrams/attack-model.svg').write_text(s)
s=svgstart(W,H)+txt(100,42,'Illustrative model  |  GR starts at 6 dB',28)
for v in [0,2,4,6]:
 y=y0-(y0-y1)*v/6;s+=line(x0,y,x1,y)+txt(77,y+8,str(v),25,anchor='end')
for t in [0,100,180,300,400]:
 x=x0+(x1-x0)*t/400;s+=line(x,y0,x,y0+9)+txt(x,y0+42,str(t),25,anchor='middle')
s+=txt(8,88,'GR / dB',25)+txt(896,508,'Time / ms',25,anchor='end')
for tau,col in [(100,blue),(300,gray)]:s+=path([(x0+(x1-x0)*t/400,y0-(y0-y1)*math.exp(-t/tau)) for t in range(401)],col)
s+=txt(490,82,'τ = 100 ms',28,blue)+txt(700,82,'τ = 300 ms',28,gray)
x=x0+(x1-x0)*180/400;s+=line(x,y0,x,y1,gray,'5 7')
for tau,col in [(100,blue),(300,gray)]:
 v=6*math.exp(-180/tau);y=y0-(y0-y1)*v/6;s+=f'<circle cx="{x}" cy="{y}" r="7" fill="{col}"/>'
s+='</g></svg>';(P/'assets/diagrams/release-model.svg').write_text(s)
# Bar graphic shares one linear millisecond scale; note onsets, not recovery gap.
s=svgstart(936,460)+txt(84,42,'Note-onset intervals  |  not release settings',28)
x0,x1=84,882
for t in [0,100,200,300,400,500]:
 x=x0+(x1-x0)*t/500;s+=line(x,85,x,370)+txt(x,409,str(t),25,anchor='middle')
for y,ms,col,label in [(160,187.5,blue,'80 BPM · 1/16'),(305,60000/140,gray,'140 BPM · 1/4')]:
 w=(x1-x0)*ms/500;s+=f'<rect x="{x0}" y="{y-22}" width="{w}" height="44" rx="3" fill="{col}"/>'+txt(x0,y-43,label,29,col)+txt(x0+w+16,y+10,f'{ms:.1f} ms',30,col)
s+=txt(882,450,'Time / ms',25,anchor='end')+'</g></svg>';(P/'assets/diagrams/tempo-spacing.svg').write_text(s)
# Conceptual syllable parts, not a waveform.
s=svgstart(936,320)+txt(38,40,'Syllable envelope · conceptual, not measured',27)
s+=path([(40,246),(95,246),(116,70),(150,165),(245,179),(390,188),(450,218),(525,246),(575,246),(612,103),(651,180),(750,202),(830,246),(902,246)],blue)
s+=txt(112,292,'Onset',28,anchor='middle')+txt(330,292,'Body',28,anchor='middle')+txt(543,292,'Gap',28,anchor='middle')+txt(750,292,'Next syllable',28,anchor='middle')+'</g></svg>';(P/'assets/diagrams/syllable-concept.svg').write_text(s)
data={'description':'Deliberately simplified first-order smoothing of gain reduction in the dB domain. Not a FabFilter emulation or audio measurement. τ values are model constants, not calibrated plugin knob values.','attack':{'formula':'GR(t)=6*(1-exp(-t/tau)) dB','target_step_dB':[0,6],'tau_ms':[5,30],'sample_t_ms':10,'sample_GR_dB':[6*(1-math.exp(-10/t)) for t in [5,30]],'assumptions':'Constant target after t=0; no lookahead, hold, knee or detector smoothing modelled.'},'release':{'formula':'GR(t)=6*exp(-t/tau) dB','initial_GR_dB':6,'tau_ms':[100,300],'sample_t_ms':180,'sample_GR_dB':[6*math.exp(-180/t) for t in [100,300]],'assumptions':'Target steps to zero and stays there, no retrigger or hold; 180 ms is the assumed recovery window after release starts, not necessarily onset-to-onset spacing.'},'tempo':{'formula':'quarter_ms=60000/BPM; sixteenth_ms=quarter_ms/4','examples':[{'bpm':80,'division':'1/16','ms':187.5},{'bpm':140,'division':'1/4','ms':60000/140}],'limitation':'Onset intervals are timing references, not release settings; articulation and sustained signal shorten actual recovery window.'},'static_ratio':{'threshold_dBFS':-18,'input_dBFS':-10,'ratio':4,'output_dBFS':-16,'GR_dB':6,'assumptions':'Steady state hard-knee downward compression with no makeup gain; not transient response.'}}
(P/'research/diagram_data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
with (P/'research/model_samples.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['model','t_ms','tau_ms','GR_dB'])
 for name,taus,n in [('attack',[5,30],90),('release',[100,300],400)]:
  for tau in taus:
   for t in range(n+1):w.writerow([name,t,tau,6*(1-math.exp(-t/tau)) if name=='attack' else 6*math.exp(-t/tau)])

# Record original explanatory diagrams with their separate rights and limitations.
manifest=json.loads((P/'assets.json').read_text())
for path in sorted((P/'assets/diagrams').glob('*.svg')):
 name=path.name
 entry={'asset_id':'D_'+path.stem,'path':str(path.relative_to(P)),'entity':'Original explanatory diagram','dimensions':[1080,1440] if name.startswith('page-') else ([936,320] if name=='syllable-concept.svg' else ([936,460] if name=='tempo-spacing.svg' else [936,530])),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'rights_status':'original_educational_diagram','rights_basis':'Original deterministic drawing from explicitly documented assumptions and calculations; no third-party UI is recreated.','limitations':'Conceptual illustration or simplified calculation; not an audio measurement or a Pro-C 3 algorithm emulation.','data_source':'research/diagram_data.json','used_on_pages':'Report or page-specific carousel geometry as indicated by file name'}
 manifest['assets'].append(entry)
(P/'assets.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
