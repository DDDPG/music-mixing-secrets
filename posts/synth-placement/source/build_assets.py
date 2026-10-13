from pathlib import Path
import json, hashlib, math
from PIL import Image
R=Path(__file__).resolve().parents[1]
B='#0066cc'; G='#697887'; K='#1d1d1f'; L='#e5e5ea'; BG='#f5f5f7'
def text(x,y,s,size=30,color=K,anchor='start',weight=400):return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}">{s}</text>'
def line(x1,y1,x2,y2,color=L,w=3,dash=''):return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}" stroke-dasharray="{dash}"/>'
def rect(x,y,w,h,color=BG,rx=8):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}" rx="{rx}"/>'
def svg(name,body,w=936,h=520):
 p=R/'assets/diagrams'/f'{name}.svg';p.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="100%" height="100%" fill="white"/><g font-family="Noto Sans SC, sans-serif">{body}</g></svg>')
a=''
for i,(head,sub) in enumerate([('Pan','横向位置'),('Width','展开范围'),('Depth','前后层次')]):
 y=50+i*170;a+=text(0,y,head,34,B,weight=600)+text(0,y+43,sub,30,G)+(line(270,y+20,900,y+20,G,2) if i<2 else '')
 if i==0:a+=text(270,y+67,'L',28,G)+text(900,y+67,'R',28,G,'end')+rect(470,y-7,24,54,B,3)
 elif i==1:a+=rect(370,y+1,370,38,'#c8def5',5)+rect(540,y+1,30,38,B,5)+text(555,y+83,'中心相同，也能有不同宽度',28,G,'middle')
 else:
  for x,label in [(270,'电平'),(470,'相对空间量'),(705,'频谱与起音')]:a+=rect(x,y-8,190,62,BG,5)+text(x+95,y+33,label,27,B,'middle')
  a+=text(270,y+98,'共同形成层次；不是距离刻度',28,G)
svg('three-decisions',a,h=560)
a=text(0,38,'同源、同窗、同一 RMS 标尺',30,G);x0=275;scale=15
for j in range(0,37,6):
 x=x0+j*scale;a+=line(x,80,x,395,L,2)+text(x,446,str(j-36),25,G,'middle')
for y,label,dry,wet in [(120,'A',-18,-30),(280,'B',-18,-24)]:
 a+=text(5,y+28,label,36,B,weight=600)+text(62,y+8,'Dry',30,K)+text(62,y+67,'Wet',30,G)
 a+=rect(x0,y-18,(dry+36)*scale,36,B,0)+rect(x0,y+40,(wet+36)*scale,36,G,0)+text(x0+(dry+36)*scale+16,y+10,f'{dry} dBFS',27,K)+text(x0+(wet+36)*scale+16,y+68,f'{wet} dBFS',27,G)
a+=text(930,490,'dBFS RMS',28,G,'end')
svg('dry-wet-example',a,h=530)
a=text(0,34,'只改变混响开始的时间',32,K);x0=175;scale=6.7
for ms in [0,10,25,40,60,80,100]:
 x=x0+ms*scale;a+=line(x,85,x,400,L,2)+text(x,443,str(ms),25,G,'middle')
for y,delay in [(180,10),(340,40)]:
 a+=text(0,y-30,f'{delay} ms',32,B,weight=600)+line(x0,y,x0,y-90,B,7)+text(x0,y+40,'Dry',26,B,'middle')
 start=x0+delay*scale
 points=[(start,y)] + [(start+t*scale, y-75*math.exp(-t/22)*(1-math.exp(-t/3))) for t in range(0,61,2)] + [(start+60*scale,y)]
 a+=f'<polygon points="'+ ' '.join(f'{x:.1f},{yy:.1f}' for x,yy in points)+f'" fill="#c8def5" stroke="{G}" stroke-width="2"/>'+text(start+80,y-75,'Wet',26,G)
a+=text(900,485,'时间 / ms',28,G,'end')+text(0,528,'示意包络，非真实音频或脉冲响应',27,G)
svg('predelay-timeline',a,h=560)
a=''
for x,y,w,h,t in [(0,40,180,80,'Synth'),(270,40,230,80,'轨道推子'),(710,40,210,80,'总输出'),(270,230,230,80,'Post Send'),(610,230,310,80,'Reverb 100% Wet')]:a+=rect(x,y,w,h)+text(x+w/2,y+49,t,28,K,'middle',600)
a+=line(180,80,268,80,B,4)+line(500,80,707,80,B,4)+line(550,80,550,195,B,4)+line(550,195,385,195,B,4)+line(385,195,385,228,B,4)+line(500,270,607,270,G,4)+line(815,230,815,125,G,4)
a += ''.join(f'<polygon points="{pts}" fill="{col}"/>' for pts,col in [('268,80 254,73 254,87',B),('707,80 693,73 693,87',B),('385,228 378,214 392,214',B),('607,270 593,263 593,277',G),('815,125 808,139 822,139',G)])
a+=text(0,380,'推子 −6 dB → 干声与混响输入一起下降',33,B,weight=600)+text(0,434,'要改变相对 Wet，请核对发送点与 Send / Return。',29,K)+text(0,487,'比例推导限近似线性、静态处理；尾声有过渡。',27,G)
svg('send-routing',a,h=520)
a=text(0,45,'先约定编码，再检查折叠',34,K,weight=600)+rect(0,95,430,185)+rect(506,95,430,185)
a+=text(35,158,'L = M + S',40,B,weight=600)+text(35,225,'R = M − S',40,B,weight=600)+text(540,158,'Mono = (L + R) / 2',32,K)+text(540,225,'= M',44,B,weight=600)
a+=text(0,365,'S 是左右差异项，不等于“两侧乐器”。',32,K)+text(0,423,'关键旋律应在实际折叠试听中仍然成立。',31,K)+text(0,491,'约定 M=(L+R)/2，S=(L−R)/2；这是代数示意。',27,G)
svg('mono-fold',a,h=530)
# Exact crops, no in-pixel edits
for source,name,box in [('ableton-utility-official.png','utility-width-balance.png',(7,142,270,319)),('fabfilter-pro-r-2-maincontrols-official.jpg','pro-r-predelay-distance.png',(27,43,520,205)),('fabfilter-pro-r-2-maincontrols-official.jpg','pro-r-brightness-width-mix.png',(775,43,1270,205))]:
 im=Image.open(R/'assets/source'/source); im.crop(box).save(R/'assets/derived'/name)

data={'dry_wet_examples':[{'name':'A','dry_dBFS_RMS':-18,'wet_dBFS_RMS':-30,'difference_dB':12,'wet_to_dry_RMS_amplitude':10**(-12/20)},{'name':'B','dry_dBFS_RMS':-18,'wet_dBFS_RMS':-24,'difference_dB':6,'wet_to_dry_RMS_amplitude':10**(-6/20)}], 'measurement_status':'constructed examples, not measured audio','predelay_examples_ms':[10,40],'sample_rate_Hz':48000,'predelay_samples':[480,1920],'sample_difference':1440,'chart_axis_dBFS_RMS':[-36,0]}
(R/'research/data.json').write_text(json.dumps(data,indent=2))
assets=[]
def asset(path,**kw):
 p=R/path;e={'asset_id':p.stem,'file':path,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),**kw}
 if p.suffix in ['.png','.jpg']:e['dimensions']=list(Image.open(p).size)
 assets.append(e)
asset('assets/source/ableton-utility-official.png',entity='Ableton Utility',version='Live 12 manual; exact build not specified',component='stereo-capable Utility',source_page='https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#utility',asset_url='https://ableton-production.imgix.net/live-manual/12/UtilityL12.png',retrieved_at='2026-10-13',rights_status='limited_educational_commentary_no_general_republication_license',rights_basis='Necessary visual quotation to explain identified controls; no explicit general redistribution license obtained',attribution='Ableton AG official Live 12 manual',modifications='None',state='Stereo input; Width 100%; Gain 0.00 dB; Balance C; Mono and Bass Mono not highlighted; 120 Hz is displayed but not proof enabled',used_on_pages=[3],limitations='Official documentation image, not our software run or recommended settings; general public republication clearance unverified')
asset('assets/source/fabfilter-pro-r-2-maincontrols-official.jpg',entity='FabFilter Pro-R 2',version='Pro-R 2 help, exact build not specified',component='main control strip; stereo/surround instance not established',source_page='https://www.fabfilter.com/help/pro-r/using/maincontrols',asset_url='https://www.fabfilter.com/help_pages/pro-r/images/maincontrols%402x.jpg',retrieved_at='2026-10-13',rights_status='limited_educational_commentary_no_general_republication_license',rights_basis='Necessary visual quotation to explain identified controls; no explicit general redistribution license obtained',attribution='FabFilter Software Instruments official help',modifications='None',state='Vintage; preset Vintage Hall; Space 3.20 s; Mix lock icon visible; other numerical values not readable',used_on_pages=[6,7],limitations='State not recommended; cannot infer unseen knob values; general public republication clearance unverified')
for name,src,box,pages in [('utility-width-balance.png','ableton-utility-official.png',[7,142,270,319],[3]),('pro-r-predelay-distance.png','fabfilter-pro-r-2-maincontrols-official.jpg',[27,43,520,205],[6]),('pro-r-brightness-width-mix.png','fabfilter-pro-r-2-maincontrols-official.jpg',[775,43,1270,205],[7])]:
 asset('assets/derived/'+name,entity='Exact crop of '+src,source_file='assets/source/'+src,crop_xyxy=box,rights_status='same_as_source',rights_basis='inherits source restrictions',attribution='See source',modifications='Axis-aligned crop only; no redraw or parameter edit',used_on_pages=pages)
asset('assets/derived/depth-concept-ai.png',entity='Depth visual metaphor',version='original generated illustration',component='conceptual',source_page=None,asset_url=None,retrieved_at='2026-10-13',rights_status='ai_generated_conceptual',rights_basis='Created for this educational project; no third-party reference image supplied',attribution='AI-generated conceptual illustration',modifications='None',used_on_pages=[1],limitations='Not audio evidence, waveform, room simulation or product imagery')
for p in sorted((R/'assets/diagrams').glob('*.svg')):asset(str(p.relative_to(R)),entity='Original educational diagram',rights_status='original_explanation',rights_basis='Independent geometry and original text based on cited facts and disclosed arithmetic',attribution='Kangdi Wang',modifications='Editable SVG',used_on_pages={'three-decisions':[2],'dry-wet-example':[4],'predelay-timeline':[5],'send-routing':[8],'mono-fold':[10]}.get(p.stem,[]),limitations='No measured audio')
(R/'assets.json').write_text(json.dumps(assets,ensure_ascii=False,indent=2))
