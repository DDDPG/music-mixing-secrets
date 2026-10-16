from pathlib import Path
p=Path(__file__).parent/'assets/diagrams'
def svg(name,body,h=520):
 (p/(name+'.svg')).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="936" height="{h}" viewBox="0 0 936 {h}"><rect width="936" height="{h}" fill="#f5f5f7"/><style>text{{font-family:Noto Sans SC,sans-serif;fill:#1d1d1f;font-size:30px}} .blue{{fill:#0066cc}} .small{{font-size:26px}}</style>'+body+'</svg>')
def text(x,y,t,cl=''): return f'<text x="{x}" y="{y}" class="{cl}">{t}</text>'
def line(x1,y1,x2,y2,col='#697887',dash=''): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="3" stroke-dasharray="{dash}"/>'
def box(x,y,w,t,col='#0066cc'): return f'<rect x="{x}" y="{y}" width="{w}" height="78" rx="8" fill="white" stroke="{col}" stroke-width="3"/>'+text(x+20,y+50,t)
b=text(32,48,'同一原轨：Dry 保持完整，Send 单独处理','small')+box(32,120,190,'原始轨道')+line(222,159,280,159)+line(280,159,280,315)+line(280,159,700,159)+box(700,120,200,'Dry 主路','#697887')+text(300,265,'Send → Return','blue')+line(280,315,335,315)+box(335,276,180,'Gate')+line(515,315,565,315)+box(565,276,335,'Reverb · 纯 Wet')+text(32,442,'Gate 不在 Dry / Send 分流之前。','small')
svg('routing',b,500)
b=text(32,48,'检测包络 / dBFS · 原创假设示意','small')
for v in [-12,-24,-30,-40]:
 y=90+(abs(v)-12)*10;b+=line(120,y,895,y,'#d2d2d7')+text(32,y+10,str(v))
b+=line(120,210,895,210,'#0066cc','10 8')+line(120,270,895,270,'#697887','10 8')
b+='<polyline points="120,370 170,90 260,140 390,240 520,250 640,290 750,370 895,370" fill="none" stroke="#0066cc" stroke-width="7"/>'
b+=text(480,195,'开门 −24','blue')+text(692,263,'关门 −30')+text(283,438,'−27：仍开门')+text(605,438,'−32：可关闭')+text(32,495,'两条阈值差 6 dB；图形不是实测波形。','small')
svg('hysteresis',b,535)
b=text(32,48,'假设无再触发 · 线性示意，非插件测量','small')
for t in [0,80,120,160,240,320]:
 x=100+t*2.4;b+=line(x,95,x,325,'#d2d2d7')+text(x-20,367,str(t),'small')
b+=text(32,110,'开')+text(32,310,'关')+text(768,412,'时间 / ms','small')
b+='<polyline points="100,110 484,110 676,310 868,310" fill="none" stroke="#0066cc" stroke-width="7"/>'
b+=text(335,455,'120：满足关闭条件','small')+text(335,497,'160：Hold 40 ms 后开始 Release','small')+text(335,539,'240：Release 80 ms 后到达衰减量','small')
b=b.replace('x="335"','x="150"').replace('class="small"','style="font-size:32px"')
svg('timing',b,585)
