from pathlib import Path
import json,math,html,subprocess
P=Path(__file__).parent;D=P/'assets/diagrams';D.mkdir(exist_ok=True)
BLUE='#0066cc';GRAY='#697887';DARK='#1d1d1f'
def tx(x,y,s,size=25,c=DARK,anchor='start'):
 return f'<text x="{x}" y="{y}" font-size="{size}" fill="{c}" text-anchor="{anchor}">{html.escape(s)}</text>'
def line(x1,y1,x2,y2,c=GRAY,width=2,dash=''):
 return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{width}" '+(f'stroke-dasharray="{dash}" ' if dash else '')+'/>'
def rect(x,y,w,h,c='#f5f5f7',r=10):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{c}"/>'
def path(points,c=BLUE,width=3,dash=''):
 return '<polyline points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in points)+f'" fill="none" stroke="{c}" stroke-width="{width}" '+(f'stroke-dasharray="{dash}" ' if dash else '')+'/>'
def save(name,body,h=620):
 s=f'<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{h}" viewBox="0 0 960 {h}"><rect width="960" height="{h}" fill="white"/><g font-family="Noto Sans CJK SC, Noto Sans SC, sans-serif">'+body+'</g></svg>'
 (D/(name+'.svg')).write_text(s)
 subprocess.run(['inkscape',str(D/(name+'.svg')),'--export-type=png','--export-filename='+str(D/(name+'.png'))],capture_output=True,check=True)
data={'disclaimer':'Original computed or conceptual diagrams. No recorded audio, no fake plugin UI. All amplitudes illustrative.','diagrams':{}}
# Rhythm timeline
b=tx(36,45,'落点、延续、推进：三种任务',31)+tx(36,82,'120 BPM · 4/4 · 一小节 2000 ms · 编曲示意',22,GRAY)
x0=185;scale=700/2000
for ms in [0,500,1000,1500,2000]:
 x=x0+ms*scale;b+=line(x,122,x,442,'#dfe3e8')+tx(x,478,str(ms),21,GRAY,'middle')
b+=tx(855,515,'ms',22,GRAY)
for label,y in [('Kick',155),('Bass',260),('Snare',365)]:b+=tx(35,y+25,label,27)
for ms in [0,1000]:b+=rect(x0+ms*scale,145,32,52,BLUE)
for start,end in [(150,900),(1150,1900)]:b+=rect(x0+start*scale,250,(end-start)*scale,52,'#697887')
for ms in [500,1500]:b+=rect(x0+ms*scale,355,32,52,'#1d1d1f')
b+=tx(36,570,'示意：每条声音有自己的任务，不要求每条都占满。',25)
save('foundation-timeline',b)
data['diagrams']['foundation-timeline']={'bpm':120,'meter':'4/4','quarter_ms':500,'eighth_ms':250,'bar_ms':2000,'kick_onsets_ms':[0,1000],'bass_intervals_ms':[[150,900],[1150,1900]],'snare_onsets_ms':[500,1500],'note':'Blocks show illustrative musical events, not measured sound envelopes; Kick/Snare block widths have no acoustic decay meaning.'}
# sum amplitudes as bars, explicitly numeric
b=tx(36,45,'叠加后的峰值，需要重新检查',31)+tx(36,85,'计算例：两个完全相同、同相正弦，各自峰值 −12 dBFS',23,GRAY)
vals=[('A',-12),('B',-12),('A + B',-12+20*math.log10(2))]
for k in [0,-6,-12,-18]:
 y=155+(-k)*14;b+=line(180,y,850,y,'#e0e4e8')+tx(155,y+8,str(k),23,GRAY,'end')
for i,(label,v) in enumerate(vals):
 x=270+i*215;y=155-v*14;b+=rect(x-40,y,80,407-y,BLUE if i==2 else GRAY,0)+tx(x,452,label,27,DARK,'middle')+tx(x,y-18,f'{v:.2f} dBFS' if i==2 else '−12 dBFS',23,DARK,'middle')
b+=tx(36,510,'振幅相加：0.251 + 0.251 = 0.502',27)+tx(36,552,'峰值增加 6.02 dB；不是“任意两件乐器相加”的规则。',23,GRAY)
save('headroom-sum',b)
data['diagrams']['headroom-sum']={'unit':'dBFS sample peak, normalized full scale=1','input_peak_dbfs':[-12,-12],'input_amplitude':10**(-12/20),'output_amplitude':2*10**(-12/20),'output_peak_dbfs':-12+20*math.log10(2),'assumptions':'identical coherent sine waves, exactly in phase, no processor'}
# time vs polarity mathematical distinction
b=tx(36,43,'上下翻转 ≠ 向后移动',31)+tx(36,80,'蓝实线：原正弦   灰虚线：延后 5 ms · 振幅归一化',22,GRAY)
for n,f in enumerate([50,100]):
 mid=180+n*180
 b+=tx(36,mid-45,f'{f} Hz',29)+tx(36,mid,f'{360*f*.005:.0f}°',25,GRAY)+line(190,mid,890,mid,'#dfe3e8')
 pts=[];delay=[]
 for k in range(401):
  t=k/10000;xx=190+t/.04*700
  pts.append((xx,mid-52*math.sin(2*math.pi*f*t)));delay.append((xx,mid-52*math.sin(2*math.pi*f*(t-.005))))
 b+=path(pts)+path(delay,GRAY,3,'8 6')
for ms in [0,10,20,30,40]:b+=tx(190+ms/.04/1000*700,465,str(ms),22,GRAY,'middle')
b+=tx(878,500,'ms',22,GRAY)+tx(36,535,'Polarity：x(t) → −x(t)；所有采样符号反转。',26)+tx(36,578,'Delay：x(t) → x(t−5 ms)；相位变化随频率而变。',26)
save('polarity-time',b)
data['diagrams']['polarity-time']={'frequencies_hz':[50,100],'delay_seconds':.005,'time_axis_ms':[0,40],'normalized_peak':1,'phase_shift_degrees':[90,180],'formula':'phase_lag_deg=360*f*delay; x=sin(2*pi*f*t), delayed=sin(2*pi*f*(t-delay))','interpretation':'100 Hz shifted half-cycle is same as inversion for that sine only; 50 Hz is not.'}
# harmonic sticks true log axis
b=tx(36,45,'同一个音，向上延伸的纹理',31)+tx(36,85,'A1 = 55 Hz · 例示前 4 阶谐波，振幅人为设定',23,GRAY)
xmin,xmax=45,300
fx=lambda f:110+math.log(f/xmin)/math.log(xmax/xmin)*770
for f in [50,100,200,300]:
 x=fx(f);b+=line(x,150,x,420,'#e0e4e8')+tx(x,457,str(f),23,GRAY,'middle')
b+=line(105,420,890,420,GRAY)+tx(36,145,'相对振幅',22,GRAY)
for i,(f,a) in enumerate(zip([55,110,165,220],[1,.62,.4,.26])):
 x=fx(f);b+=line(x,420,x,420-220*a,BLUE if i==0 else GRAY,12)+tx(x,420-220*a-22,str(f)+' Hz',25,DARK,'middle')+tx(x,494,str(i+1)+' 阶',23,GRAY,'middle')
b+=tx(36,548,'横轴：对数频率。换音时，基频与谐波一起移动。',24)+tx(36,585,'低频层保留重量；上层帮助听清轮廓，不必各自抢主角。',23,GRAY)
save('harmonic-ladder',b)
data['diagrams']['harmonic-ladder']={'fundamental_hz':55,'harmonics':[{'n':i+1,'frequency_hz':f,'illustrative_amplitude':a} for i,(f,a) in enumerate(zip([55,110,165,220],[1,.62,.4,.26]))],'x_axis':'log frequency from 45 to 300 Hz','y_axis':'linear illustrative relative amplitude','a4_hz':440,'e1_hz':440*2**((28-69)/12)}
# Actual explanatory routing not plugin UI
b=tx(36,45,'Snare：本体与空间各自可控',31)+tx(36,85,'常规并行 Reverb 路由示意',23,GRAY)
for x,y,w,h,label in [(35,175,175,80,'Snare'),(365,125,215,85,'主路 / Dry'),(310,340,270,85,'Reverb · 100% Wet'),(665,340,245,85,'Return EQ'),(715,125,195,85,'鼓组／混音')]:
 b+=rect(x,y,w,h)+tx(x+w/2,y+h/2+9,label,26,DARK,'middle')
b+=line(210,210,285,210,BLUE,4)+line(285,210,285,167,BLUE,4)+line(285,167,365,167,BLUE,4)+line(580,167,715,167,BLUE,4)
b+=line(285,210,285,382,GRAY,4)+line(285,382,310,382,GRAY,4)+line(580,382,665,382,GRAY,4)+line(813,340,813,210,GRAY,4)
# visible arrowheads without reversed flows
for x,y in [(365,167),(715,167),(310,382),(665,382)]: b+=f'<path d="M {x-12} {y-7} L {x} {y} L {x-12} {y+7}" fill="none" stroke="{GRAY}" stroke-width="3"/>'
b+=f'<path d="M 806 222 L 813 210 L 820 222" fill="none" stroke="{GRAY}" stroke-width="3"/>'
b+=tx(120,316,'Send',25,GRAY)+tx(36,503,'先调发送量与尾长，再判断返回通道是否需要 EQ。',25)+tx(36,553,'只处理返回通道，不会直接削去主路的击打本体。',24,GRAY)
save('snare-routing',b)
data['diagrams']['snare-routing']={'edges':[['snare','dry_main'],['dry_main','mix'],['snare_send','reverb_100wet'],['reverb_100wet','return_eq'],['return_eq','mix']],'notes':'Illustrative parallel reverb; send tap intentionally unspecified. Return EQ only affects wet branch. No gain values claimed.'}
# Hierarchy not quantitative frequency map
b=tx(36,45,'让亮度服从节奏层次',31)+tx(36,85,'操作顺序示意；不是规定好的电平大小',23,GRAY)
steps=[('01','先调推子','整段是否一直太突出？'),('02','再找刺点','哪一次击打、哪一段频率？'),('03','选处理方式','整段太亮：静态；偶尔刺：可试动态'),('04','回到合奏','与人声、Snare 和高潮一起判断')]
for i,(n,t,sub) in enumerate(steps):
 y=135+i*105;b+=tx(35,y+25,n,31,BLUE)+tx(115,y+22,t,29)+tx(115,y+62,sub,23,GRAY)
 if i<3:b+=line(50,y+45,50,y+98,'#ccd6e1',2)
save('role-hierarchy',b)
data['diagrams']['role-hierarchy']={'type':'qualitative decision flow','steps':[s[1:] for s in steps],'numeric_levels':False}
b=tx(36,45,'四次复核，把改动放回音乐',31)
for i,(label,q) in enumerate([('低音量','节奏骨架还清楚吗？'),('Mono','有没有异常变薄？'),('换段落','换音、重击、高潮也成立吗？'),('匹配响度旁通','真的更清楚，还是只是更响？')]):
 y=115+i*115;b+=tx(36,y,str(i+1).zfill(2),30,BLUE)+tx(120,y,label,30)+tx(120,y+42,q,25,GRAY)
save('verification-path',b)
data['diagrams']['verification-path']={'type':'editorial listening checklist','measurements':False}
(P/'diagram-data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
assets=json.loads((P/'assets.json').read_text())
assets['assets']=[a for a in assets['assets'] if not a['asset_id'].startswith('D_')]
import hashlib
from PIL import Image
for f in D.glob('*.svg'):
 assets['assets'].append({'asset_id':'D_'+f.stem,'file':str(f.relative_to(P)),'preview_file':str(f.with_suffix('.png').relative_to(P)),'entity':'Original explanatory diagram','version':'1','component':'Not product UI','source_page':None,'asset_url':None,'retrieved_at':None,'dimensions':list(Image.open(f.with_suffix('.png')).size),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'rights_status':'original_created_for_user','rights_basis':'Original geometry and code; no third-party imagery','attribution':'Calculation / conceptual illustration, not measured audio','modifications':'Editable SVG generated by build_diagrams.py','used_on_pages':[p for p,stem in [(1,'foundation-timeline'),(2,'headroom-sum'),(3,'polarity-time'),(5,'harmonic-ladder'),(6,'snare-routing'),(7,'role-hierarchy'),(8,'verification-path')] if f.stem==stem],'data_source':'diagram-data.json'})
(P/'assets.json').write_text(json.dumps(assets,ensure_ascii=False,indent=2))
print('7 SVGs + 7 PNG previews and data created. No final page layout or render performed.')
