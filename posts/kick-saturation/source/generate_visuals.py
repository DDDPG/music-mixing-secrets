from pathlib import Path
import math,json
P=Path(__file__).resolve().parents[1];D=P/'assets/diagrams'
def svg(name,body,h=460):
 (D/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="936" height="{h}" viewBox="0 0 936 {h}"><rect width="936" height="{h}" fill="#f5f5f7"/><g font-family="Noto Sans SC,sans-serif" font-size="30" fill="#1d1d1f">{body}</g></svg>')
def text(x,y,s,color='#1d1d1f',size=30):return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}">{s}</text>'
def line(x,y,X,Y,c='#697887',w=2):return f'<path d="M{x} {y}L{X} {Y}" stroke="{c}" stroke-width="{w}" fill="none"/>'
# Same axes transfer functions, normalized input and output
b=text(45,48,'瞬时输入 → 瞬时输出（归一化）')
for ox,title,non in [(60,'线性：y = x',False),(510,'饱和模型：y = x − 0.25x³',True)]:
 b+=text(ox,104,title,size=27)+line(ox+20,260,ox+350,260)+line(ox+185,125,ox+185,395)
 pts=[]
 for i in range(101):
  x=-1+i/50;y=x-.25*x**3 if non else x;pts.append(f'{ox+185+x*130:.2f},{260-y*130:.2f}')
 b+=f'<polyline points="{" ".join(pts)}" fill="none" stroke="#0066cc" stroke-width="6"/>'+text(ox+320,302,'+1',size=24)+text(ox+145,143,'+1',size=24)
svg('transfer.svg',b+text(40,440,'教学曲线；不代表 Saturn 2 的内部算法',size=25))
# harmonics vertical bars with exact relative level scale
b=text(40,50,'处理后解析频谱 / 相对基频 dB')
for db in [0,-10,-20,-30]:
 y=110-db*8;b+=line(110,y,860,y,'#d5dbe0')+text(35,y+10,str(db),size=26)
for hz,db in [(50,0),(150,20*math.log10(.0625/.8125))]:
 x=110+(hz/200)*750;y=110-db*8;b+=line(x,350,x,y,'#0066cc',22)+text(x-52,390,f'{hz} Hz')+text(x-65,y-15,f'{db:.1f} dB',size=28)
b+=text(450,435,'频率轴：线性；无其他分量',size=25);svg('harmonics.svg',b)
# peak/RMS calculations
r=math.sqrt((.8125**2+.0625**2)/2);comp=(1/math.sqrt(2))/r
metrics={'model':'x=sin(2*pi*50*t); y=x-0.25*x^3; full cycle analytic RMS; full scale amplitude=1','raw':{'peak_dbfs':0,'rms_dbfs':20*math.log10(1/math.sqrt(2))},'processed':{'peak_dbfs':20*math.log10(.75),'rms_dbfs':20*math.log10(r)},'rms_matched':{'gain_db':20*math.log10(comp),'peak_dbfs':20*math.log10(.75*comp),'rms_dbfs':20*math.log10(1/math.sqrt(2))}}
(P/'research/model-data.json').write_text(json.dumps(metrics,indent=2))
b=text(40,48,'同一 RMS 标尺下：峰值可以改变')
for x,label,peak,rms in [(220,'原始',0,-3.0103),(660,'RMS 匹配后',20*math.log10(.75*comp),-3.0103)]:
 b+=text(x-110,100,label)+line(x,350,x,140,'#c4cdd6',85)+line(x,350,x,140-peak*35,'#0066cc',85)+line(x-80,140-rms*35,x+80,140-rms*35,'#1d1d1f',4)+text(x-140,410,f'Peak {peak:.2f} dBFS',size=28)
svg('crest.svg',b+text(40,450,'黑线 RMS = −3.01 dBFS；满刻度幅度 = 1',size=26),480)
# alias fold
b=text(40,48,'48 kHz 采样率：Nyquist = 24 kHz')
b+=line(100,210,860,210,'#697887',3)
for f in [0,10,18,24,30,48]:
 x=100+f/48*760;b+=line(x,198,x,223)+text(x+12 if f==18 else x-25,265,str(f),size=28)
b+=text(800,305,'kHz')
for f,y,label in [(10,130,'输入 10'),(30,130,'三次 30'),(18,370,'折叠 18')]:
 x=100+f/48*760;b+=line(x,210,x,y,'#0066cc',6)+text(x+22 if f==18 else x-70,y-15,label,size=28)
b+=f'<path d="M575 105 Q480 10 385 105" stroke="#0066cc" stroke-width="4" fill="none"/><path d="M385 105L403 99M385 105L389 86" stroke="#0066cc" stroke-width="4" fill="none"/>'+text(45,435,'解析示例：假设 30 kHz 分量未被抗混叠滤除',size=26)
svg('aliasing.svg',b)
print(metrics)
