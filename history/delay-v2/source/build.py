from pathlib import Path
import re,sys,html,shutil,json,math
R=Path(__file__).resolve().parent
from fontTools.ttLib import TTFont
from fontTools import subset
from fontTools.varLib.instancer import instantiateVariableFont
seed_path=R/'seed-editorial.html'
if not seed_path.exists(): raise FileNotFoundError('Missing packaged seed-editorial.html')
seed=seed_path.read_text()
seed=re.sub(r'<link\b[^>]*>', '', seed)
seed=re.sub(r'<script\b[^>]*>[\s\S]*?</script>', '', seed)
seed=seed.replace('[必填] 替换为社交卡组标题 · Social Card Set','给人声一点空间 · 低 Wet Ping Pong Delay')
PAPER='#F7F4EE'; INK='#263335'; MUTED='#596762'; RULE='#D6DAD1'; TEAL='#177D78'; CORAL='#C86451'
posters=[]; visual_text=[]
def tx(text,x=72,y=0,size=32,w=936,weight=400,color=INK,lh=1.45,align='left',role='body'):
    visual_text.append(text)
    return f'<div class="copy {role}" style="left:{x}px;top:{y}px;width:{w}px;font-size:{size}px;font-weight:{weight};color:{color};line-height:{lh};text-align:{align}">{html.escape(text).replace(chr(10),"<br>")}</div>'
def st(text,x,y,size=30,color=INK,weight=400,anchor='start'):
    visual_text.append(text)
    return f'<text x="{x}" y="{y}" font-family="Noto Sans SC, sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}">{html.escape(text)}</text>'
def ln(x1,y1,x2,y2,color=RULE,width=2,arrow=False,dash=None):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"'+(f' marker-end="url(#{"teal" if color==TEAL else "coral" if color==CORAL else "ink"})"' if arrow else '')+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
def path(d,color=INK,width=3,arrow=False):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linejoin="round"'+(f' marker-end="url(#{"teal" if color==TEAL else "coral" if color==CORAL else "ink"})"' if arrow else '')+'/>'
def circ(x,y,r=6,color=TEAL,stroke=None,sw=2):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"'+(f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '')+'/>'
def rect(x,y,w,h,fill='none',stroke=RULE,sw=2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def svg(shapes,name):
    defs='<defs>'+''.join(f'<marker id="{name}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto" markerUnits="userSpaceOnUse"><path d="M1,1 L7,4 L1,7" fill="none" stroke="{col}" stroke-width="1.6"/></marker>' for name,col in [('ink',INK),('teal',TEAL),('coral',CORAL)])+'<linearGradient id="low-fade"><stop offset="0" stop-color="'+TEAL+'" stop-opacity=".14"/><stop offset="1" stop-color="'+TEAL+'" stop-opacity="0"/></linearGradient><linearGradient id="high-fade"><stop offset="0" stop-color="'+CORAL+'" stop-opacity="0"/><stop offset="1" stop-color="'+CORAL+'" stop-opacity=".14"/></linearGradient></defs>'
    raw='<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1440" viewBox="0 0 1080 1440">'+defs+''.join(shapes)+'</svg>'
    standalone_style='<style>@font-face{font-family:Noto Sans SC;src:url(fonts/NotoSansSC-400.ttf);font-weight:100 499}@font-face{font-family:Noto Sans SC;src:url(fonts/NotoSansSC-600.ttf);font-weight:500 649}@font-face{font-family:Noto Sans SC;src:url(fonts/NotoSansSC-700.ttf);font-weight:650 900}</style>'
    (R/'assets'/f'{name}.svg').write_text(raw.replace('<defs>',standalone_style+'<defs>',1))
    return raw.replace('<svg ','<svg class="diagram" ',1)
def page(num,slug,kicker,title,body,source='',title_y=124,title_size=62):
    top=tx(kicker,y=76,size=24,color=MUTED,role='kicker')+tx(title,y=title_y,size=title_size,weight=700,lh=1.22,role='headline')
    footer=f'<footer class="foot"><span>{source}</span><span>{num:02} / 08</span></footer>'
    posters.append(f'<section class="poster xhs v2-{slug}" id="xhs-{num:02}" data-recipe="custom-independent-{slug}"><div class="content">{top}{body}{footer}</div></section>')
# 01: image-led cover, full picture contained without cropping.
body=tx('低 Wet · Ping Pong Delay',y=326,size=36)+'''<!-- Subject map: microphone centered; speaker cabinets at both lateral edges; the image is fully contained, and no content overlays the hardware. -->
<img class="hero" src="assets/hero.png" alt="麦克风与左右音箱的空间概念插画" style="object-position:center 50%">'''+tx('空间与左右位置的概念插画',y=1110,size=26,color=MUTED)+tx('先选时间，再收尾巴，最后调音色。',y=1152,size=34,weight=600)+tx('从一组可试听的参数讲起。',y=1210)+tx('让回声补空间，保留歌词的清楚程度。',y=1280,size=30)
page(1,'cover','人声混音 · 延迟','给人声\n一点空间',body,'概念插画 · 非实测',130,82)
# 02: insert topology and auxiliary send topology.
g=[]
g += [rect(276,374,550,250), st('延迟插件内部',295,408,26,MUTED), st('人声',72,503,32),ln(152,491,296,491,INK,3,True),circ(302,491,5,INK)]
g += [path('M302 491 V442 H732 V491',INK,3),path('M302 491 V549 H732 V491',TEAL,3),st('干声',480,432,32),st('延迟回声',443,593,32,TEAL),circ(744,491,16,PAPER,INK,2),st('+',744,502,28,INK,400,'middle'),st('Dry/Wet',744,606,30,INK,400,'middle'),ln(761,491,930,491,INK,3,True),st('混音',944,503,32)]
g += [st('人声',72,867,32),ln(152,855,908,855,INK,3,True),circ(250,855,5,INK),st('原声直通',500,842,28,MUTED),circ(924,855,14,PAPER,INK),st('+',924,865,26,INK,400,'middle'),ln(938,855,944,855,INK,3),st('混音',944,902,32)]
g += [path('M250 855 V998 H333',TEAL,3,True),st('发送量',287,973,30,TEAL,400,'middle'),ln(342,998,420,998,TEAL,3,True),st('效果轨',539,970,30,TEAL,400,'middle'),st('100% Wet',539,1035,34,TEAL,600,'middle'),ln(650,998,704,998,TEAL,3,True),st('返回推子',772,970,30,TEAL,400,'middle'),path('M833 998 H924 V871',TEAL,3,True)]
body=tx('先分清插入与发送。',y=218)+tx('插入：在插件里调 Dry/Wet',y=302,size=34,weight=600)+svg(g,'02-routing')+tx('干声与回声混合后，再进入混音。',y=680)+tx('发送：效果轨只返回回声',y=765,size=34,weight=600)+tx('单声道人声选 M>S；立体声轨选 Stereo。\n发送路由用发送量或返回推子控制多少。',y=1124)+tx('功能路由示意，不代表插件内部的精确 DSP 电路。',y=1252,size=26,color=MUTED)
page(2,'routing','人声延迟 / 路由','回声，在哪里混入？',body,'Waves H-Delay 手册 · 原理示意')
# 03: common absolute scale for all four durations.
g=[]
for value in [0,50,100,150,200,250]:
    x=236+2.52*value
    g += [ln(x,383,x,806,RULE,1.5),ln(x,844,x,859,MUTED,1.5),st(str(value),x,894,28,MUTED,400,'middle')]
g += [ln(236,852,866,852,MUTED,2),st('ms',956,894,28,MUTED,400,'end')]
g += [st('120',72,456,38,INK,600),st('BPM',72,492,28,MUTED),st('160',72,706,38,INK,600),st('BPM',72,742,28,MUTED)]
for dur,y,note,col in [(250,414,'1/8',TEAL),(125,520,'1/16',CORAL),(187.5,664,'1/8',TEAL),(93.75,770,'1/16',CORAL)]:
    end=236+2.52*dur
    g += [st(note,218,y+10,30,col,400,'end'),ln(236,y,end,y,col,10),circ(end,y,6,col),st(f'{dur:g} ms',end+16,y+12,34,col,600)]
body=tx('四分音符为一拍 · 固定速度',y=302,size=28,color=MUTED)+svg(g,'03-time')+tx('120 → 160 BPM，同一音符缩短 25%。',y=943,size=38,weight=600)+tx('1/8 = 60,000 ÷ BPM ÷ 2\n1/16 = 60,000 ÷ BPM ÷ 4',y=1020)+tx('HOST 会跟随工程速度。\n对比 1/8 与 1/16，听回声是否挤住下一字。',y=1142)+tx('缩短间隔后，仍要重新听反馈与咬字。',y=1270,size=26,color=MUTED)
page(3,'time','人声延迟 / 时间','同一个 1/8\n换首歌就变了',body,'Ableton 节拍定义 · 时长为计算值',120)
# 04: alternating discrete events, no amplitude encoding.
g=[]
g += [st('同侧两次：375 ms',565,385,32,INK,600,'middle'),path('M372.5 420 V403 H757.5 V420',TEAL,2),ln(180,520,980,520,RULE,2),ln(180,780,980,780,RULE,2),st('L 左',72,532,32,TEAL,600),st('R 右',72,792,32,CORAL,600),circ(180,650,9,INK),st('干声',208,662,30,INK)]
for n,t,y,col in [(1,187.5,520,TEAL),(2,375,780,CORAL),(3,562.5,520,TEAL),(4,750,780,CORAL)]:
    x=180+t*770/750
    g += [ln(x,y+16,x,885,RULE,1.5,dash='4 7'),circ(x,y,12,col),st(f'第 {n} 次',x,y-35,30,col,600,'middle')]
g += [ln(180,650,180,885,RULE,1.5,dash='4 7'),ln(180,890,950,890,MUTED,2)]
for t in [0,187.5,375,562.5,750]:
    x=180+t*770/750
    g += [ln(x,883,x,898,MUTED,1.5),st(f'{t:g}',x,933,28,MUTED,400,'middle')]
g += [st('时间 / ms',950,975,28,MUTED,400,'end')]
body=tx('160 BPM · 普通 1/8\n从左开始的单次输入示意',y=231,size=30)+svg(g,'04-pingpong')+tx('相邻回声，每隔 187.5 ms 出现一次。',y=985,size=34,weight=600)+tx('H-Delay：打开 Ping Pong，\n还要让 Feedback 显示值 > 1。',y=1085)+tx('可暂时提高 Mix 确认交替，再收回低 Wet。',y=1190,size=30)+tx('单次输入、等间隔时序示意，非音频实测。\n左右起点可以互换。',y=1270,size=26,color=MUTED)
page(4,'pingpong','人声延迟 / 左右','回声怎样左右交替？',body,'Waves H-Delay 手册 · 时间为计算值')
# 05: identical scales; normalized relative amplitude, not plugin control values.
g=[]
for xpos,color,text in [(86,TEAL,'每次回送 30% 振幅'),(599,CORAL,'每次回送 60% 振幅')]: g += [st(text,xpos,412,32,color,600)]
for base in [150,661]:
    for value in [0,50,100]:
        y=870-3.8*value
        g += [ln(base-18,y,base+334,y,RULE,1.5),st(str(value),base-30,y+10,28,MUTED,400,'end')]
for xs,vals,col in [([150,253,356,459],[100,30,9,2.7],TEAL),([661,764,867,970],[100,60,36,21.6],CORAL)]:
    for n,(x,v) in enumerate(zip(xs,vals),1):
        top=870-3.8*v
        g += [ln(x,870,x,top,col,8),circ(x,top,5,col),st(f'{v:g}',x,top-18,34,col,600,'middle'),st(f'第{n}次',x,923,28,MUTED,400,'middle')]
body=tx('理想线性模型 · 相对振幅 · 第 1 次 = 100',y=302,size=28,color=MUTED)+svg(g,'05-feedback')+tx('第 4 次：21.6 ÷ 2.7 = 8 倍振幅',y=968,size=36,weight=600)+tx('整片回声太抢耳 → 先减 Mix',y=1050)+tx('第一下合适、后面拖太久 → 先减 Feedback',y=1120)+tx('第 n 次 = 100 × g^(n−1)，假设回送比例固定。\n这里是相对振幅，不代表听感响度，\n也不是 H-Delay 某旋钮值的实测。',y=1226,size=26,color=MUTED)
page(5,'feedback','人声延迟 / 反馈','Feedback 越高\n尾巴越难收',body,'FabFilter / Ableton 反馈定义 · 理想模型',120)
# 06: logarithmic frequency windows, no invented response curve.
fx=lambda hz:104+872*math.log10(hz/20)/3
hp,lp=fx(200),fx(6000)
g=[rect(104,506,hp-104,144,'url(#low-fade)','none',0),rect(lp,506,976-lp,144,'url(#high-fade)','none',0),ln(104,650,976,650,MUTED,2),ln(hp,563,hp,650,TEAL,4),ln(lp,563,lp,650,CORAL,4),st('HP 高通',hp,403,32,TEAL,600,'middle'),st('200 Hz',hp,460,42,TEAL,600,'middle'),st('LP 低通',lp,403,32,CORAL,600,'middle'),st('6 kHz',lp,460,42,CORAL,600,'middle'),st('减少低频累积',104,520,32,TEAL),st('收暗高频重复',690,520,32,CORAL),ln(230,541,230,574,TEAL,2),ln(865,541,865,574,CORAL,2)]
for hz,label in [(20,'20'),(100,'100'),(200,'200'),(1000,'1k'),(6000,'6k'),(20000,'20k')]:
    x=fx(hz)
    g += [ln(x,644,x,662,MUTED,1.5),st(label,x,713,28,MUTED,400,'middle')]
g += [st('Hz',976,750,28,MUTED,400,'end'),ln(hp,779,fx(300),779,TEAL,3,True),st('200 → 300',hp,821,28,TEAL,400,'middle'),ln(lp,779,fx(4000),779,CORAL,3,True),st('6k → 4k',lp,821,28,CORAL,400,'middle')]
body=tx('试听起点 · 对数频率刻度',y=302,size=28,color=MUTED)+svg(g,'06-filter')+tx('低频仍浑',y=868,size=34,weight=600)+tx('HP：200 → 300 Hz，试着再减一点低频',y=918)+tx('齿音跟着重复',y=1014,size=34,weight=600)+tx('LP：6 → 4 kHz，试着收暗一点',y=1064)+tx('一次只改一项；回声太薄或太暗，就往回调。',y=1170)+tx('仅示意滤波方向，不是完整频响或实测曲线。\n截止点外逐渐衰减；实际坡度取决于滤波器。',y=1254,size=26,color=MUTED)
page(6,'filter','人声延迟 / 滤波','回声也要\n修低频、收高频',body,'Waves / Soundtoys · 参数为试听建议',120)
# 07: modest parameter ledger and actual audition sequence.
g=[ln(72,348,1008,348,RULE,2),ln(72,540,1008,540,RULE,2)]
for x,val,label in [(174,0,'先听原声'),(418,3,'少量加入'),(662,5,'继续对比'),(906,8,'再多一点')]:
    g += [circ(x,800,47,PAPER,TEAL,2),st(str(val),x,818,46,TEAL,600,'middle'),st(label,x,895,30,INK,400,'middle')]
for x1,x2 in [(229,363),(473,607),(717,851)]: g += [ln(x1,800,x2,800,MUTED,2,True)]
body=tx('带伴奏，循环同一段。',y=224)+tx('H-Delay · 单声道选 M>S，立体声选 Stereo',y=296,size=30)+svg(g,'07-audition')
for y,left,lv,right,rv in [(357,'Ping Pong','On','HOST','1/8'),(419,'Dry/Wet','5','Feedback','20'),(481,'HP','200 Hz','LP','6 kHz')]:
    body += tx(left,72,y,30,220)+tx(lv,335,y-4,36,170,600,TEAL)+tx(right,564,y,30,230)+tx(rv,827,y-4,36,181,600,TEAL)
body += tx('Analog / LoFi：Off · Modulation Depth：0\nPhase Reverse：Off',y=555,size=26,color=MUTED)+tx('1  先选回声的量',y=675,size=36,weight=600)+tx('2  选好量，再比较 1/8 与 1/16',y=956,size=34,weight=600)+tx('3  后面拖太久，Feedback 从 20 往下收。\n    想多一点延续，再小幅增加。',y=1062)+tx('整组为试听起点，不是官方预设。\nMix 按 0–100 刻度；Feedback 20 是显示值。\n固定其他参数，每次回放同一段，先确认输出不削波。',y=1220,size=26,color=MUTED)
page(7,'audition','人声延迟 / 试听','打开工程，从这组开始试',body,'Waves H-Delay 手册 · 本页为试听起点',title_size=60)
# 08: decisions mapped to controls, then real-mix checks.
g=[]; body=tx('听到什么，就先动对应的控制。',y=224)
for y,problem,answer in [(333,'回声整体太明显','先减 Mix'),(455,'后面重复拖太长','再减 Feedback'),(577,'歌词被回声挤住','比 1/8 与 1/16'),(716,'回声又浑又亮','分别检查 HP / LP')]:
    body += tx(problem,72,y,32,450)+tx('→',548,y,34,64,color=MUTED)+tx(answer,628,y,34,380,600,TEAL)
    if y==577: body+=tx('再重新听反馈',628,624,28,380,color=MUTED)
for y in [424,546,685,797]:g.append(ln(72,y,1008,y,RULE,1.5))
body += svg(g,'08-check')+tx('最后，做三次检查',y=850,size=36,weight=600)+tx('带伴奏：歌词和下一句还清楚吗？',y=919)+tx('开关对比：先尽量匹配响度。',y=986)+tx('切单声道：音色、音量、歌词\n是否异常改变？',y=1053)+tx('选让这首歌更舒服的设置。',y=1190,size=36,weight=600)+tx('人声已有足够空间，也可以不加。',y=1250)
page(8,'check','人声延迟 / 判断','回到伴奏里，决定留多少',body,'最终以完整混音与单声道回放判断',title_size=60)
css='''
/* Vocal-delay v2: independent approved content-specific layout. This task block intentionally overrides template typography, palette and recipes. */
@font-face {font-family:"Noto Sans SC";src:url("assets/fonts/NotoSansSC-400.ttf");font-weight:100 499}
@font-face {font-family:"Noto Sans SC";src:url("assets/fonts/NotoSansSC-600.ttf");font-weight:500 649}
@font-face {font-family:"Noto Sans SC";src:url("assets/fonts/NotoSansSC-700.ttf");font-weight:650 900}
@page {size:1080px 1440px;margin:0}
html,body {margin:0;padding:0;background:#F7F4EE;color:#263335;font-family:"Noto Sans SC",sans-serif}
*,*:before,*:after {box-sizing:border-box}
.sheet {display:block;margin:0;padding:0}
.poster,.poster.xhs {width:1080px;height:1440px;display:block;position:relative;overflow:hidden;border:0;border-radius:0;box-shadow:none;background:#F7F4EE;break-after:page;break-inside:avoid;margin:0;padding:0}
.poster:last-child {break-after:auto}
.poster:before,.poster:after,.grain {display:none}
.poster.xhs .content {display:flex;flex-direction:column;position:relative;width:1080px;height:1440px;padding:0;margin:0;z-index:1}
.copy {position:absolute;margin:0;padding:0;letter-spacing:0;white-space:nowrap;font-family:"Noto Sans SC",sans-serif}
.headline {letter-spacing:0}
.diagram {position:absolute;left:0;top:0;width:1080px;height:1440px;overflow:visible}
.hero {position:absolute;left:0;top:390px;width:1080px;height:720px;object-fit:contain;display:block}
.foot {position:relative;flex-shrink:0;display:flex;justify-content:space-between;margin:1360px 72px 0;padding:0;width:936px;height:35px;font-family:"Noto Sans SC",sans-serif;font-size:24px;line-height:1.3;letter-spacing:0;color:#596762;border:0}
.foot span:last-child {margin-left:auto}
figure {margin:0}
@media screen {body {padding:40px;background:#e8e7e3}.sheet {display:flex;flex-direction:column;gap:40px;align-items:center}.poster{flex-shrink:0}}
'''
output=seed.replace('</head>','<style>'+css+'</style></head>')
output=re.sub(r'<main class="sheet">[\s\S]*?</main>','<main class="sheet">\n<!-- POSTERS_HERE -->\n'+''.join(posters)+'</main>',output)
(R/'index.html').write_text(output)
# Complete current-set font subsets include all text from all scientific diagram labels.
font=TTFont(R/'assets/fonts/NotoSansSC-Variable.ttf')
opts=subset.Options();opts.layout_features=['*'];opts.name_IDs=['*'];opts.name_legacy=True;opts.name_languages=['*']
sub=subset.Subsetter(options=opts);sub.populate(text=''.join(visual_text)+re.sub('<[^>]+>','',output)+''.join(chr(i) for i in range(32,127)));sub.subset(font)
for weight in [400,600,700]:
    f=instantiateVariableFont(font,{'wght':weight},inplace=False);f.save(R/f'assets/fonts/NotoSansSC-{weight}.ttf')
(R/'visible-copy.txt').write_text('\n'.join(visual_text))
print('Built eight pages and seven page-native SVG assets.')
