from pathlib import Path
import json, math, html, subprocess, base64, hashlib, re
from PIL import Image, ImageDraw, ImageFont

OUT=Path(__file__).resolve().parent; ROOT=OUT.parent
DATA=json.loads((ROOT/'diagram_data.json').read_text()); SOURCES=json.loads((ROOT/'assets.json').read_text())
BG='#ffffff'; INK='#1d1d1f'; BLUE='#0066cc'; SECOND='#7c8997'; MUTED='#62666d'; GRID='#dfe3e8'; SOFT='#f5f6f8'
FONT='Noto Sans CJK SC'; REG='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'; BOLD='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
manifest=[]
class SVG:
 def __init__(self,w,h,title,desc):
  self.w=w; self.h=h; self.title=title; self.desc=desc; self.n=0
  self.parts=[f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',f'<title id="title">{html.escape(title)}</title>',f'<desc id="desc">{html.escape(desc)}</desc>',f'<rect id="background" width="{w}" height="{h}" fill="{BG}"/>','<defs>']
  for n,c in [('blue',BLUE),('ink',INK),('second',SECOND),('muted',MUTED)]:
   self.parts.append(f'<marker id="arrow-{n}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto" markerUnits="strokeWidth"><path d="M1,1 L7,4 L1,7" fill="none" stroke="{c}" stroke-width="1.3"/></marker>')
  self.parts.append('</defs>')
 def text(self,x,y,t,size=27,color=INK,weight=400,anchor='start'):
  self.n+=1;self.parts.append(f'<text id="text-{self.n}" x="{x}" y="{y}" fill="{color}" font-family="{FONT}, sans-serif" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{html.escape(str(t))}</text>')
 def line(self,x1,y1,x2,y2,color=INK,width=3,dash=None,arrow=None):
  a=f' marker-end="url(#arrow-{arrow})"' if arrow else '';d=f' stroke-dasharray="{dash}"' if dash else ''
  self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"{d}{a}/>')
 def path(self,d,color=INK,width=3,arrow=None,fill='none',dash=None):
  a=f' marker-end="url(#arrow-{arrow})"' if arrow else '';da=f' stroke-dasharray="{dash}"' if dash else ''
  self.parts.append(f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"{da}{a}/>')
 def rect(self,x,y,w,h,fill='none',stroke=None,r=0,sw=2):
  self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '')+'/>')
 def circle(self,x,y,r,fill=BG,stroke=None,sw=2):
  self.parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '')+'/>')
 def image(self,path,x,y,w,h):
  raw=base64.b64encode(Path(path).read_bytes()).decode();self.parts.append(f'<image x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid meet" xlink:href="data:image/png;base64,{raw}"/>')
 def header(self,title,sub):
  self.text(56,58,title,32,weight=700);self.text(56,100,sub,23,MUTED)
 def footer(self,*lines):
  for i,l in enumerate(lines):self.text(56,self.h-28-(len(lines)-1-i)*34,l,22,MUTED)
 def save(self,name,pages,kind,source_ids,required_caption,notes='',official=[]):
  svg=OUT/(name+'.svg'); svg.write_text('\n'.join(self.parts+['</svg>']))
  png=OUT/(name+'.png'); subprocess.run(['inkscape',str(svg),'--export-type=png',f'--export-filename={png}','--export-width=1800'],check=True,capture_output=True)
  manifest.append(dict(id=name,svg=svg.name,png=png.name,dimensions_svg=[self.w,self.h],dimensions_png=list(Image.open(png).size),title=self.title,description=self.desc,pages=pages,evidence_class=kind,source_ids=source_ids,required_adjacent_caption=required_caption,designer_notes=notes,official_asset_ids=official,contains_genuine_product_image=bool(official),rights_status='unverified_for_public_republication' if official else 'original_explanatory_diagram',background=BG,ink=INK,accent=BLUE,comparison=SECOND))

# 01: Genuine product evidence. Markers sit outside the image; screenshot pixels remain untouched.
s=SVG(1620,980,'Waves H-Delay：真实界面与控件键','完整官方产品图，带四组外部文字索引。截图为 DUAL/BPM，120 BPM，左 1/8D、右 1/2，不是教程的 Ping Pong/HOST 试听设置。')
s.header('Waves H-Delay · 控件定位','真实官方产品图；原图保留，未改动按钮、旋钮或读数')
s.image(ROOT/'assets/source/h-delay-official-product.png',60,180,1499,545)
for n,xx,y in [('1',475,149),('2',1095,149),('3',1458,149)]:
 s.circle(xx,y,18,BG,BLUE,2);s.text(xx,y+8,n,23,BLUE,700,'middle');s.line(xx,y+19,xx,177,BLUE,2)
s.circle(1010,756,18,BG,BLUE,2);s.text(1010,764,'4',23,BLUE,700,'middle');s.line(1010,725,1010,737,BLUE,2)
for x,n,t,d in [(60,'1','DELAY','时间位置'),(435,'2','FEEDBACK','后续重复'),(810,'3','DRY/WET','干湿混合'),(1185,'4','HiPASS / LoPASS','延迟声部的音色')]:
 s.text(x,824,n+'  '+t,26,BLUE,700);s.text(x,862,d,25,INK)
s.text(60,915,'图中为 DUAL / BPM 状态，仅用于定位控件；图中参数不是本教程设置。',25,MUTED)
s.text(60,951,'界面图：Waves H-Delay 官方产品页。© Waves Audio Ltd. · 公开转载许可未核实。',22,MUTED)
s.save('01_official_control_map',[1],'official',['S0','S1'],'Waves 官方界面，仅用于定位控件；图中参数不是本教程设置。','Use complete genuine image; do not call screenshot Ping Pong active or HOST synced. External numbered markers do not alter the image.',official=['A01'])

# 02: Insert routing with plugin-internal dry path and feedback loop.
s=SVG(1200,690,'低 Wet 插入路由','人声先进入 H-Delay 边界，内部拆为干声支路和 Delay 支路，由 Dry/Wet 混合后输出到混音。Feedback 仅从 Delay 输出回送 Delay 输入。')
s.header('插入：在 H-Delay 内部混合','人声 → H-Delay → 混音')
s.rect(212,155,779,407,stroke=GRID,r=14);s.text(235,194,'H-Delay 内部',24,MUTED,600)
s.text(56,333,'人声',28,weight=700);s.line(121,323,259,323,INK,3,arrow='ink');s.circle(270,323,5,INK)
s.path('M270,323 V245 H828 V286',INK,3,arrow='ink');s.text(494,232,'干声支路',27,INK,600,'middle')
s.path('M270,323 V391 H381',BLUE,3,arrow='blue');s.circle(356,391,4,BLUE)
s.rect(393,349,227,86,fill=BG,stroke=BLUE,r=6);s.text(506.5,402,'Delay 支路',28,BLUE,600,'middle')
s.line(620,391,764,391,BLUE,3);s.circle(658,391,5,BLUE);s.path('M764,391 H828 V360',BLUE,3,arrow='blue')
s.path('M658,391 V492 H356 V394',BLUE,3,arrow='blue');s.text(506,530,'Feedback：取一部分回送',24,BLUE,600,'middle')
s.circle(828,323,34,BG,INK,2.5);s.text(828,335,'+',34,INK,600,'middle');s.text(862,279,'Dry/Wet',26,INK,600)
s.line(865,323,1043,323,INK,3,arrow='ink');s.text(1080,333,'混音',28,weight=700)
s.footer('单声道人声要左右输出：选 M>S；立体声轨选 Stereo。','功能路由示意，非精确 DSP 电路；Dry/Wet 5 不能直接当作电平比或响度比。')
s.save('02_insert_signal_path',[2],'conceptual',['S1','S3','S4'],'功能路由示意，不是插件内部精确 DSP 电路。','The dry bypass is inside H-Delay only. Feedback loop must stay on the Delay branch.')

# 03: Parallel send route is separate to avoid accidental insert bypass.
s=SVG(1200,560,'发送与返回的路由','原人声直接进入混音；发送支路经 H-Delay（Dry/Wet 100）返回混音，以发送量或返回推子控制多少。')
s.header('发送：原人声直达混音','效果轨只返回处理后的信号；用发送量或返回推子调多少')
s.text(56,221,'人声',28,weight=700);s.line(128,211,982,211,INK,3,arrow='ink');s.circle(259,211,5,INK)
s.text(1080,221,'混音',28,weight=700);s.circle(1012,211,28,BG,INK,2.5);s.text(1012,222,'+',31,INK,600,'middle');s.line(1041,211,1060,211,INK,3)
s.path('M259,211 V370 H458',BLUE,3,arrow='blue');s.text(315,348,'发送量',25,BLUE,600)
s.rect(474,314,264,114,fill=BG,stroke=BLUE,r=6);s.text(606,354,'H-Delay 效果轨',26,BLUE,600,'middle');s.text(606,395,'Dry/Wet 100',26,BLUE,600,'middle')
s.line(740,370,977,370,BLUE,3,arrow='blue');s.text(846,348,'返回推子',25,BLUE,600,'middle');s.path('M991,370 H1012 V248',BLUE,3,arrow='blue')
s.footer('常规发送路由：效果轨 Dry/Wet 设为 100，避免额外返回干声。','功能路由示意；此图与低 Wet 插入是两种不同用法。')
s.save('03_send_signal_path',[2],'conceptual',['S1','S3','S4'],'功能路由示意，不是插件内部精确 DSP 电路。','Optional secondary figure. Do not combine the send dry route with the insert diagram.')

# 04: Shared zero baseline and millisecond scale.
s=SVG(1200,660,'普通音符的时长比较','120 BPM：1/8 为 250 ms、1/16 为 125 ms。160 BPM：1/8 为 187.5 ms、1/16 为 93.75 ms。四组使用共同毫秒轴。')
s.header('同一音符，速度越快，时长越短','普通时值 · 四分音符为一拍 · 固定速度 · 共用毫秒轴')
x=lambda v:288+v*2.82
for t in range(0,251,50):
 s.line(x(t),150,x(t),493,GRID,1.5);s.text(x(t),532,str(t),23,MUTED,anchor='middle')
s.text(1118,532,'ms',23,MUTED)
for bpm,ys in [(120,[201,271]),(160,[389,459])]:
 s.text(56,sum(ys)/2-2,str(bpm),40,weight=700);s.text(58,sum(ys)/2+31,'BPM',22,MUTED)
 row=next(r for r in DATA['tempo_comparison']['rows'] if r['bpm']==bpm)
 for note,key,y,c in [('1/8','eighth_ms',ys[0],BLUE),('1/16','sixteenth_ms',ys[1],SECOND)]:
  v=row[key];s.text(252,y+9,note,27,c,600,'end');s.line(x(0),y,x(v),y,c,12);s.circle(x(0),y,4,BG);s.circle(x(v),y,6,c);s.text(x(v)+20,y+9,f'{v:g} ms',27,c,600)
s.text(56,589,'120 → 160 BPM：同一音符时长缩短 25%',28,BLUE,600)
s.text(56,634,'1/8 = 60,000 ÷ BPM ÷ 2',23,MUTED);s.text(626,634,'1/16 = 60,000 ÷ BPM ÷ 4',23,MUTED)
s.save('04_tempo_duration',[3],'calculated',['S1','S5'],'按固定速度计算，四分音符为一拍。','Never align the source screenshot 120 BPM / 1/8D with these ordinary-note values as if it showed our settings.')

# 05: Dotted warning is independent from the primary four rows.
s=SVG(1200,390,'普通 1/8 与 1/8D 的时长','固定 160 BPM，普通 1/8 为 187.5 ms；附点 1/8D 为 281.25 ms，是普通时值的 1.5 倍。')
s.header('确认普通 1/8，别漏看 D 后缀','160 BPM · D = 附点 · 附点时值为普通时值的 1.5 倍')
x=lambda v:330+v*2.35
for v in [0,100,200,300]:
 s.line(x(v),142,x(v),277,GRID,1.5);s.text(x(v),314,v,22,MUTED,anchor='middle')
for label,val,y,c in [('普通 1/8',187.5,181,BLUE),('1/8D（附点）',281.25,252,SECOND)]:
 s.text(56,y+9,label,27,c,600);s.line(x(0),y,x(val),y,c,10);s.text(x(val)+18,y+9,f'{val:g} ms',25,c,600)
s.footer('按固定速度计算。H-Delay 手册默认时值为 1/8D；加载预设后也要复核。')
s.save('05_ordinary_vs_dotted',[3],'calculated',['S1','S5'],'固定 160 BPM；附点为普通时值的 1.5 倍。','Secondary warning; keep ordinary and dotted durations visibly distinct.')

# 06: No waveforms or amplitude coding. Equal-size event markers only.
s=SVG(1200,650,'Ping Pong 的左右交替时序','160 BPM 普通 1/8，单次短输入。延迟信号在 187.5、375、562.5、750 ms 依次落于左、右、左、右。干声在 0 ms，原有声像不变。')
s.header('交替的是延迟声部','160 BPM · 普通 1/8 · 单次短输入 · 从左开始')
x=lambda v:200+v*1.17
for v in [0,187.5,375,562.5,750]:
 s.line(x(v),179,x(v),459,GRID,1.4);s.text(x(v),500,f'{v:g}',25,MUTED,anchor='middle')
for label,y,c in [('L 左',247,BLUE),('干声',325,INK),('R 右',403,SECOND)]:
 s.text(56,y+10,label,28,c,600)
 if label!='干声':s.line(173,y,1125,y,GRID,2)
s.circle(x(0),325,10,INK);s.text(x(0)+22,334,'0 ms',23,INK)
for ev in DATA['pingpong_timeline']['repeats']:
 y=247 if ev['channel']=='L' else 403;c=BLUE if ev['channel']=='L' else SECOND
 s.circle(x(ev['time_ms']),y,11,c);s.text(x(ev['time_ms']),y-26,f'第 {ev["repeat"]} 次',26,c,600,'middle')
s.path(f'M{x(187.5)},187 V165 H{x(562.5)} V187',BLUE,2);s.text((x(187.5)+x(562.5))/2,148,'同侧间隔 375 ms',24,BLUE,600,'middle')
s.text(56,559,'相邻重复间隔 187.5 ms',28,weight=600);s.text(1125,543,'时间 / ms',23,MUTED,anchor='end')
s.footer('干声保持原有声像；等大事件点不编码振幅。','单次输入、等间隔时序示意，非音频实测；左右起点可互换。')
s.save('06_pingpong_timeline',[4],'calculated',['S1','S3'],'单次输入、等间隔时序示意，非音频实测。左右起点可互换。','Equal event markers intentionally do not encode amplitude. Dry shown as a separate event, not necessarily a center-panned signal.')

# 07: Ideal-model amplitude comparison. Shared scale 0..100.
s=SVG(1200,715,'Feedback 理想模型中的振幅衰减','首个延迟信号振幅统一为 100。模型 g=0.3：100,30,9,2.7。g=0.6：100,60,36,21.6。第 4 次相差 8 倍振幅，并非响度比或插件读数。')
s.header('Feedback 影响后续重复的衰减','相对振幅：第 1 次 = 100 · 两组同一纵轴尺度')
base=485;scale=2.25
for bx,c,ser in [(121,SECOND,DATA['feedback_decay']['series'][0]),(714,BLUE,DATA['feedback_decay']['series'][1])]:
 s.text(bx-56,151,f'模型 g = {ser["g"]:g}',28,c,700);s.text(bx-56,184,f'每次回送 {ser["g"]*100:g}% 振幅',23,MUTED)
 for v in [0,50,100]:
  y=base-v*scale;s.line(bx-27,y,bx+357,y,GRID,1.3);s.text(bx-43,y+7,v,22,MUTED,anchor='end')
 for i,p in enumerate(ser['points']):
  xx=bx+i*108;yy=base-p['relative_amplitude']*scale;s.line(xx,base,xx,yy,c,11);s.circle(xx,yy,6,c);s.text(xx,yy-16,f'{p["relative_amplitude"]:g}',27,c,600,'middle');s.text(xx,529,f'第 {i+1} 次',23,MUTED,anchor='middle')
s.text(56,590,'第 4 次：21.6 ÷ 2.7 = 8 倍振幅',29,weight=700)
s.footer('理想线性模型：第 n 次振幅 = 100 × g⁽ⁿ⁻¹⁾，不含滤波和饱和。','不是 H-Delay 旋钮读数或实测；振幅倍数不等于响度倍数。')
s.save('07_feedback_decay',[5],'calculated',['S1','S3'],'理想线性模型：相对振幅，不是 H-Delay 旋钮读数、实测或响度倍数。','Keep model coefficient g explicitly separate from H-Delay FEEDBACK display values.')

# 08: Log-frequency positions, no fabricated response curve or slope.
s=SVG(1200,660,'延迟声部的滤波方向','对数频率标尺从 20 Hz 到 20 kHz。HiPASS 200 Hz、LoPASS 6 kHz 为试听起点；低频仍浑时试 300 Hz，齿音突出时试 4 kHz。仅示意方向。')
s.header('只给延迟声部滤波','HiPASS 200 Hz · LoPASS 6 kHz · 试听起点')
x=lambda f:88+(math.log10(f)-math.log10(20))/3*1024
hp=x(200);lp=x(6000);y=338
s.text(88,163,'高通：减少低频',26,BLUE,600);s.text(1112,163,'低通：收暗高频',26,BLUE,600,'end')
s.line(hp-8,193,90,193,BLUE,3,arrow='blue');s.line(lp+8,193,1110,193,BLUE,3,arrow='blue')
s.text(88,230,'向低频侧逐渐衰减',23,MUTED);s.text(1112,230,'向高频侧逐渐衰减',23,MUTED,anchor='end')
s.line(88,y,1112,y,INK,3)
for f in [20,100,1000,10000,20000]:
 xx=x(f);s.line(xx,y-7,xx,y+9,INK,2);s.text(xx,382,{20:'20',100:'100',1000:'1k',10000:'10k',20000:'20k'}[f],24,MUTED,anchor='middle')
for f,lab in [(200,'HiPASS · 200 Hz'),(6000,'LoPASS · 6 kHz')]:
 xx=x(f);s.line(xx,286,xx,y,BLUE,3);s.circle(xx,y,6,BLUE);s.text(xx,274,lab,26,BLUE,700,'middle')
s.text(1112,420,'对数频率 / Hz',22,MUTED,anchor='end')
s.line(hp,442,x(300),442,BLUE,3,arrow='blue');s.text(56,488,'低频仍浑：200 → 300 Hz',25,BLUE,600)
s.line(lp,442,x(4000),442,BLUE,3,arrow='blue');s.text(684,488,'齿音突出：6 → 4 kHz',25,BLUE,600)
s.text(56,548,'一次只改一个截止点；太薄或太暗，就往回调。',27,weight=600)
s.footer('仅示意滤波方向；截止点外逐渐衰减，不是完全切除。','没有虚构 dB 数值、斜率或实测频响；这里不改动主唱干声的 EQ。')
s.save('08_filter_direction',[6],'audition_proposal',['S1','S2','S6'],'试听起点；仅示意滤波方向，不是实测频响。','Use exact logarithmic positions. Arrows show the affected side or proposed trial direction, never a response slope.')

# 09: Non-skeuomorphic recipe ledger, explicitly a proposal.
s=SVG(1200,695,'H-Delay 试听起点清单','M>S 或 Stereo；PING PONG 开；HOST 普通 1/8；Feedback 20；Dry/Wet 5；HiPASS 200 Hz；LoPASS 6 kHz。Analog OFF、LoFi 关、Depth 0、ØL/ØR 关。不是官方预设。')
s.header('试听起点 · 按显示值记录','独立参数清单，不是插件截图或官方预设')
rows=[('组件','M>S / Stereo','单声道输入 / 立体声输入'),('PING PONG','开','确认左右输出'),('同步 / 音符','HOST · 普通 1/8','无 D / T 后缀'),('FEEDBACK / DRY/WET','20 / 5','插件显示值'),('HiPASS / LoPASS','200 Hz / 6 kHz','一次只改一个截止点')]
for i,(lab,val,note) in enumerate(rows):
 y=160+i*76;s.line(56,y+36,1144,y+36,GRID,1);s.text(56,y,lab,25,MUTED,500);s.text(433,y,val,28,BLUE,700);s.text(845,y,note,22,MUTED)
s.text(56,564,'减少变量',25,weight=700);s.text(260,564,'ANALOG OFF · LoFi 关 · MODULATION DEPTH 0',25,INK)
s.text(260,603,'ØL / ØR 关',25,INK)
s.footer('整组为试听起点；留意输出峰值，避免削波。')
s.save('09_audition_recipe',[7],'audition_proposal',['S1','S6'],'整组为试听起点，不是官方预设。数字按 H-Delay 显示值记录。','Do not paste these values onto the genuine product screenshot or simulate a preset UI.')

# 10: Controlled audition sequence, not a numerical control-scale chart.
s=SVG(1200,535,'分步试听 Dry/Wet、音符与 Feedback','带伴奏循环同一段，固定其他参数比较 Dry/Wet 显示值 0,3,5,8；选定后比较普通 1/8 与 1/16；最后根据延续调整 Feedback。')
s.header('固定其他参数，每次只听一件事','带伴奏循环同一段 · 不按数字大小预设优劣')
s.text(56,172,'1',31,BLUE,700);s.text(108,172,'先比较 Dry/Wet',27,weight=600)
for i,(xx,val) in enumerate(zip([556,718,880,1042],[0,3,5,8])):
 s.circle(xx,162,33,BG,BLUE,2);s.text(xx,173,val,31,BLUE,700,'middle')
 if i<3:s.line(xx+49,162,xx+112,162,GRID,2,arrow='muted')
s.line(56,231,1144,231,GRID,1)
s.text(56,299,'2',31,BLUE,700);s.text(108,299,'选好混合后，比音符',27,weight=600);s.text(578,299,'普通 1/8  ↔  1/16',31,BLUE,600)
s.line(56,358,1144,358,GRID,1)
s.text(56,422,'3',31,BLUE,700);s.text(108,422,'最后听后续延续',27,weight=600);s.text(578,422,'从 Feedback 20 小幅调整',27,BLUE,600)
s.footer('0 / 3 / 5 / 8 为插件显示值；等大选项不表示电平比、响度比或推荐排名。')
s.save('10_audition_sequence',[7],'audition_proposal',['S1'],'这是试听对照，数字为 H-Delay 显示值，不是干湿电平比例。','Candidate circles are categorical choices, not knob simulation or a numerical spacing claim.')

# 11: Problem-to-control map with actionable priority.
s=SVG(1200,650,'问题与控制项的诊断对应','延迟太抢耳先调 Dry/Wet；后续重复太久先调 Feedback；重复挤住咬字比较 1/8 和 1/16 并检查反馈；低频浑和高频刺分别调 HiPASS/LoPASS。')
s.header('听到什么，就先检查对应的控制项','带伴奏判断；每次只改变一个条件')
rows=[('延迟声部太抢耳','Dry/Wet','先收小干湿混合'),('后续重复拖太久','Feedback','先减少反馈'),('重复挤住咬字','1/8 / 1/16','比较时间，再检查反馈'),('低频浑 / 高频刺','HiPASS / LoPASS','分别调整，别同时改')]
for i,(a,b,c) in enumerate(rows):
 y=171+i*101;s.text(56,y,a,28,weight=600);s.line(390,y-10,500,y-10,BLUE,2.5,arrow='blue');s.text(545,y,b,30,BLUE,700);s.text(545,y+39,c,23,MUTED)
 if i<3:s.line(56,y+65,1144,y+65,GRID,1)
s.footer('诊断顺序是试听建议；没有音频实测，不能保证固定设置一定更宽或更清楚。')
s.save('11_diagnostic_map',[8],'audition_proposal',['S2','S8'],'诊断顺序为试听建议，结果需结合完整伴奏判断。','No fabricated width, LUFS, correlation, waveform, or before/after measurements.')

# 12: Mono fold-down is L+R, never only the left speaker.
s=SVG(1200,520,'单声道检查需要合并左右声道','左声道和右声道一起进入单声道折叠，再听音色、音量和平衡。实际折叠增益由工程或工具决定。只听左声道不是单声道兼容检查。')
s.header('单声道检查：合并 L + R 再听','尽量匹配开关前后的响度，检查音色、音量和平衡')
s.text(93,206,'L',35,BLUE,700);s.text(93,351,'R',35,SECOND,700)
s.path('M151,194 H446 V238',BLUE,3,arrow='blue');s.path('M151,339 H446 V294',SECOND,3,arrow='second')
s.circle(446,266,27,BG,INK,2.5);s.text(446,277,'+',32,INK,600,'middle')
s.line(479,266,699,266,INK,3,arrow='ink');s.text(577,242,'折叠为单声道',24,MUTED,anchor='middle')
s.rect(723,215,315,104,fill=BG,stroke=GRID,r=8);s.text(880,278,'试听整首歌的平衡',28,INK,600,'middle')
s.footer('这不是只听左声道；折叠增益以所用工程或工具为准。','功能示意，未绘制或暗示单声道兼容性实测结果。')
s.save('12_mono_fold_check',[8],'conceptual',['S8'],'L 与 R 合并为单声道；不是只听左声道。','Do not assign an arbitrary fold-down gain or claim guaranteed mono compatibility.')

# 13–16: Genuine UI crops with explicit state warnings.
s=SVG(1200,530,'真实时间显示与同步按钮','官方图原样裁切，显示 120 BPM、L 1/8D、R 1/2。BPM 亮起，HOST 未亮，不是 160 BPM 普通 1/8 设置。')
s.header('真实控件参考 · 时间与同步','辨认字符与按钮，不能将图片读数当作本教程参数')
s.image(ROOT/'assets/derived/h-delay-time-sync.png',64,145,420,294)
s.text(565,207,'图中读数',25,MUTED);s.text(565,255,'120 BPM · L 1/8D · R 1/2',29,weight=600);s.text(565,318,'BPM 亮起；HOST 未亮',27,BLUE,600);s.text(565,375,'原图为 DUAL 模式',24,MUTED)
s.footer('界面局部：Waves H-Delay 官方产品图 A02；仅裁切，未修改参数。','© Waves Audio Ltd. · 图中参数不是本教程设置；公开转载许可未核实。')
s.save('13_ui_time_reference',[3],'official',['S0','S1'],'图中为 120 BPM / 1/8D / 1/2，仅用于辨认字符，不是本教程设置。','Exact crop A02; preserve all depicted values.',official=['A02'])

s=SVG(1200,350,'真实 PING PONG 按钮参考','从官方产品图裁切的 PING PONG 按钮，仅定位控件，不宣称按钮已开启。')
s.header('真实控件参考 · PING PONG','只作位置与标签参考，不代表已经开启')
s.image(ROOT/'assets/derived/h-delay-pingpong-button.png',64,156,322.5,127.5)
s.text(474,191,'启用时选 Stereo 或 M>S',28,weight=600);s.text(474,238,'手册要求 Feedback 显示值 > 1',26,BLUE,600)
s.footer('界面局部：Waves 官方产品图 A03。原图非教程设置；© Waves Audio Ltd.')
s.save('14_ui_pingpong_reference',[4],'official',['S0','S1'],'真实 PING PONG 按钮定位图，不宣称该图按钮已开启。','The > 1 threshold is H-Delay display value, not model coefficient g. Publication rights remain unverified.',official=['A03'])

s=SVG(1200,650,'真实 FEEDBACK 与 DRY/WET 控件','两个官方图裁切并列，保留原始旋钮与刻度。Feedback 控制反馈，Dry/Wet 控制混合；图中旋钮位置不是教程起点。')
s.header('真实控件参考 · 两个旋钮，两个问题','FEEDBACK 管反馈延续；DRY/WET 管干湿混合')
s.image(ROOT/'assets/derived/h-delay-feedback.png',145,148,325.6,343.2)
s.image(ROOT/'assets/derived/h-delay-drywet.png',799,151,253.5,241.5)
s.text(306,535,'FEEDBACK',30,BLUE,700,'middle');s.text(306,575,'后续重复拖太久时检查',24,MUTED,anchor='middle')
s.text(926,450,'DRY/WET',30,BLUE,700,'middle');s.text(926,490,'整个延迟声部太明显时检查',24,MUTED,anchor='middle')
s.footer('界面局部：Waves 官方产品图 A04 / A05。仅裁切，未修改旋钮；© Waves Audio Ltd.')
s.save('15_ui_feedback_drywet',[5],'official',['S0','S1'],'图中旋钮位置不是本教程起点；模型 g 也不是 FEEDBACK 旋钮读数。','Maintain disclaimer adjacent if combined with the model chart. Publication rights remain unverified.',official=['A04','A05'])

s=SVG(1200,440,'真实滤波控件参考','官方图裁切 HiPASS / LINK / LoPASS，未改变旋钮位置。控制对象是延迟声部，不是干声 EQ。')
s.header('真实控件参考 · HiPASS / LoPASS','保留官网图的原始位置，不是 200 Hz / 6 kHz 试听起点的截图')
s.image(ROOT/'assets/derived/h-delay-filters.png',70,153,586.3,260)
s.text(733,214,'HiPASS：高通',28,BLUE,600);s.text(733,259,'LoPASS：低通',28,BLUE,600);s.text(733,319,'处理延迟信号的音色',24,MUTED)
s.text(733,369,'© Waves Audio Ltd.',21,MUTED)
s.save('16_ui_filter_reference',[6],'official',['S0','S1'],'界面局部：Waves 官方产品图 A06；图中旋钮位置不是本教程设置。','Attribution must stay adjacent. Exact crop A06; public republication license unverified.',official=['A06'])

# Deterministic validation before design.
checks={}
checks['tempo_formula']=all(abs(r['eighth_ms']-60000/r['bpm']/2)<1e-9 and abs(r['sixteenth_ms']-60000/r['bpm']/4)<1e-9 for r in DATA['tempo_comparison']['rows'])
checks['tempo_25_percent_shorter']=abs(187.5/250-0.75)<1e-9
checks['pingpong_equal_intervals']=all(abs(e['time_ms']-e['repeat']*187.5)<1e-9 for e in DATA['pingpong_timeline']['repeats'])
checks['feedback_formula']=all(abs(p['relative_amplitude']-100*s['g']**(p['repeat']-1))<1e-9 for s in DATA['feedback_decay']['series'] for p in s['points'])
checks['fourth_repeat_amplitude_ratio_8']=abs(21.6/2.7-8)<1e-9
checks['dotted_1_5']=abs(281.25/187.5-1.5)<1e-9
checks['original_image_hash_unchanged']=hashlib.sha256((ROOT/'assets/source/h-delay-official-product.png').read_bytes()).hexdigest()==next(a['sha256'] for a in SOURCES['assets'] if a['asset_id']=='A01')
checks['all_crop_pixels_exact']=all(Image.open(ROOT/a['file']).tobytes()==Image.open(ROOT/'assets/source/h-delay-official-product.png').crop(a['crop_box_xyxy']).tobytes() for a in SOURCES['assets'] if 'crop_box_xyxy' in a)
checks['no_prohibited_delay_translation']=all('回声' not in (OUT/a['svg']).read_text() for a in manifest)
checks['eight_pages_covered']=set(range(1,9))==set(p for a in manifest for p in a['pages'])
checks['all_svg_png_pairs_exist']=all((OUT/a['svg']).exists() and (OUT/a['png']).exists() for a in manifest)
# Inkscape gives rendered text bounds; any out-of-canvas text is a blocker.
text_overflows=[]
text_overlaps=[]
for a in manifest:
 result=subprocess.run(['inkscape',str(OUT/a['svg']),'--query-all'],capture_output=True,text=True,check=True)
 W,H=a['dimensions_svg']; boxes=[]
 for l in result.stdout.splitlines():
  bits=l.split(',')
  if len(bits)==5 and bits[0].startswith('text-'):
   xx,yy,ww,hh=map(float,bits[1:]); boxes.append((bits[0],xx,yy,ww,hh));
   if xx < -0.1 or yy < -0.1 or xx+ww > W+0.1 or yy+hh > H+0.1:text_overflows.append({'asset':a['id'],'text_id':bits[0],'bounds':[xx,yy,ww,hh]})
 for i,b in enumerate(boxes):
  for c in boxes[i+1:]:
   iw=min(b[1]+b[3],c[1]+c[3])-max(b[1],c[1]); ih=min(b[2]+b[4],c[2]+c[4])-max(b[2],c[2]);
   if iw>1 and ih>1:text_overlaps.append({'asset':a['id'],'text_ids':[b[0],c[0]],'overlap':[iw,ih]})
checks['all_text_inside_canvas']=not text_overflows
checks['no_text_collisions']=not text_overlaps
validation={'checks':checks,'text_overflows':text_overflows,'text_overlaps':text_overlaps,'status':'passed' if all(checks.values()) else 'needs_revision','not_audio_measured':True,'not_final_page_layout':True}
(OUT/'validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2))

# Asset contact sheet only, not an eight-page composition.
tile_w=740;col_gap=36;row_gap=48;margin=36;title_h=38
font=ImageFont.truetype(REG,20);tiles=[]
for a in manifest:
 im=Image.open(OUT/a['png']).convert('RGB');im=im.resize((tile_w,round(im.height*tile_w/im.width)),Image.Resampling.LANCZOS);tiles.append((a['id'],im))
row_heights=[max(tiles[i][1].height,tiles[i+1][1].height if i+1<len(tiles) else 0)+title_h for i in range(0,len(tiles),2)]
sheet=Image.new('RGB',(2*tile_w+col_gap+2*margin,sum(row_heights)+row_gap*(len(row_heights)-1)+2*margin),'#f1f2f4');d=ImageDraw.Draw(sheet);yy=margin
for r,rh in enumerate(row_heights):
 for col in range(2):
  i=r*2+col
  if i>=len(tiles):continue
  name,im=tiles[i];xx=margin+col*(tile_w+col_gap);d.text((xx,yy),name,font=font,fill=INK);sheet.paste(im,(xx,yy+title_h))
 yy+=rh+row_gap
sheet.save(OUT/'contact_sheet.png')
full={'version':'3.0','created_date':'2026-10-09','purpose':'Independent modular visual assets for eight-page tutorial. No final page design.','design_constraints':{'background':BG,'ink':INK,'accent':BLUE,'comparison':SECOND,'no_giant_color_blocks':True,'no_warm_paper':True},'source_files':['../research_and_story.md','../diagram_data.json','../term-map.json','../page-plan.json','../assets.json'],'assets':manifest,'screenshot_rights':'Official Waves product image and exact crops. Public republication permission is unverified; these are attributed product-specific commentary assets, not licensed stock.','contact_sheet':'contact_sheet.png','validation':'validation.json','rebuild':'python build_visuals.py'}
(OUT/'manifest.json').write_text(json.dumps(full,ensure_ascii=False,indent=2))
lines=['# v3 explanatory visualization assets','','16 independent SVG + PNG pairs for the eight-page story. These are reusable source figures, not final social-card layouts.','',f'Palette: white {BG}, ink {INK}, blue {BLUE}, subtle comparison {SECOND}. Editable SVG text uses Noto Sans CJK SC; rendered PNGs are 1800 px wide.','','## Usage rules','','- Keep every required caption and assumption with its figure. Never relabel calculated or conceptual data as audio measurement.','- Official image is DUAL/BPM at 120 BPM, with L 1/8D and R 1/2. It is not our Ping Pong/HOST recipe.','- Official screenshot pixels are unchanged. Numbered markers in 01 sit outside its image rectangle. UI crops are exact.','- Original diagram rights do not grant Waves image rights. Public republication permission for Waves material has not been verified. Preserve attribution and review before external publication.','- Never translate Delay as 回声. Use Delay / 延迟信号 / 延迟声部 as appropriate.','- The 0/3/5/8 choices are categorical audition trials. Model g is an amplitude feedback fraction and is not the H-Delay display scale.','- No fabricated waveforms, response curves, dB slopes, audio measures, UI settings, or preset screenshots.','','## Page coverage','']
for page in range(1,9):lines.append(f'- Page {page}: '+', '.join(a['id'] for a in manifest if page in a['pages']))
lines+=['','## Asset notes','']
for a in manifest:lines.extend([f'### {a["id"]}',f'- Title: {a["title"]}',f'- Evidence: {a["evidence_class"]}; sources: {", ".join(a["source_ids"])}',f'- Required caption: {a["required_adjacent_caption"]}',f'- Notes: {a["designer_notes"]}',''])
lines+=['## Validation','',json.dumps(validation,ensure_ascii=False,indent=2)]
(OUT/'manifest.md').write_text('\n'.join(lines))
print(json.dumps({'asset_count':len(manifest),'validation':validation,'contact_sheet':str(OUT/'contact_sheet.png')},ensure_ascii=False,indent=2))
