from pathlib import Path
from html import escape
import math,json,hashlib
P=Path(__file__).parent
header='''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="620" viewBox="0 0 960 620"><defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10" fill="none" stroke="#0066cc" stroke-width="1.4"/></marker></defs><rect width="960" height="620" fill="white"/><g font-family="Noto Sans SC, sans-serif" fill="#1d1d1f">'''
def t(x,y,s,size=28,color='#1d1d1f',weight=400):return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}">{escape(s)}</text>'
def box(x,y,w,h,s,sub=None):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="#f5f5f7" stroke="#dce3e9"/>'+t(x+20,y+44,s,30,weight=600)+(t(x+20,y+82,sub,25,'#697887') if sub else '')
def line(x,y,xx,yy):return f'<path d="M{x},{y} L{xx},{yy}" stroke="#0066cc" stroke-width="3" fill="none" marker-end="url(#arrow)"/>'
def save(name,s): (P/'assets/svg'/name).write_text(header+s+'</g></svg>',encoding='utf-8')
s=t(30,45,'并行效果链 · 信号流示意',30,weight=600)
s+=box(30,98,205,105,'人声轨','Dry 直达')+line(235,148,730,148)+box(750,98,180,105,'混音汇合')
s+=f'<path d="M130,203 V280 H225" stroke="#0066cc" stroke-width="3" fill="none" marker-end="url(#arrow)"/>'+t(38,255,'Send',28,'#0066cc')
s+=box(245,228,300,105,'Reverb / Delay','常规并行：100% Wet')+line(545,280,620,280)+box(640,228,290,105,'M/S EQ','处理生成后的湿声')
s+=f'<path d="M790,333 V398 H945 V148 H935" stroke="#0066cc" stroke-width="3" fill="none" marker-end="url(#arrow)"/>'+t(520,395,'Return 输出',28,'#0066cc')
s+=t(30,492,'EQ 在效果器后，定位到湿声的 Side 频段。',31)+t(30,548,'共享 Return 上的其他声源也会一起改变。',28,'#697887')
save('routing.svg',s)
s=t(30,48,'先听原因，再选处理 · 诊断示意',30,weight=600)
for y,a,b in [(95,'湿声整体过多','先试降低 Return 电平'),(230,'Mid / Side 都厚','先试 Stereo EQ 或减少湿声'),(365,'主要 Side 中频过满','再试 Side 频段衰减')]:s+=box(30,y,375,95,a)+line(415,y+47,480,y+47)+box(500,y,430,95,b)
s+=t(30,552,'若主要是 Mid 厚，检查湿声 Mid 与干声叠加。',28,'#697887')
save('diagnosis.svg',s)
s=t(30,48,'M/S 是左右声道的另一种表示',32,weight=600)
s+=box(30,100,420,118,'M = (L + R) / 2','左右的和')+box(510,100,420,118,'S = (L − R) / 2','左右的差')
s+=line(240,220,240,290)+line(720,220,720,290)+box(30,310,420,100,'Mid 保持不变')+box(510,310,420,100,'仅处理 Side 目标频段')
s+=t(90,475,'L′ = M + S′',37,'#0066cc')+t(550,475,'R′ = M − S′',37,'#0066cc')
s+=t(30,560,'教学约定：1/2 编码；不是插件内部缩放声明。',27,'#697887')
save('matrix.svg',s)
s=t(30,48,'独立计算例 · 幅度 ≠ 宽度',33,weight=600)+t(30,105,'目标频率 Side：−3 dB → 幅度 × 0.708',30,'#0066cc')
for y,label,f,color in [(190,'Mid 保持',1,'#697887'),(310,'Side 原幅度',1,'#697887'),(430,'Side 衰减后',10**(-3/20),'#0066cc')]:
 s+=t(30,y+34,label,28)+f'<rect x="245" y="{y}" width="550" height="45" rx="5" fill="#f5f5f7"/><rect x="245" y="{y}" width="{550*f}" height="45" rx="5" fill="{color}"/>'+t(810,y+34,f'{f*100:.1f}%',27,color)
s+=t(30,544,'共用幅度尺度；各条以本身处理前幅度为 100%。',26,'#697887')+t(30,590,'10^(−3/20) = 0.7079；非实测、非宽度百分比。',26,'#697887')
save('attenuation.svg',s)
s=t(30,48,'Mono 检查：Side 的变化可能听不到',32,weight=600)
s+=t(50,145,'L′ = M + H(S)',42,'#0066cc')+t(50,225,'R′ = M − H(S)',42,'#0066cc')
s+=f'<path d="M40,270 H920" stroke="#dce3e9" stroke-width="2"/>'+t(50,350,'(L′ + R′) / 2 = M',48,weight=600)
s+=t(50,424,'Side 相消；Mid 保留。',34)
s+=t(30,510,'限理想纯 Side 处理，无额外增益、非线性或后级变化。',25,'#697887')+t(30,564,'Mono 检查不能单独证明“去糊成功”。',28,'#697887')
save('mono-check.svg',s)
a=json.loads((P/'assets.json').read_text())
for f in (P/'assets/svg').glob('*.svg'):
 a.append({'asset_id':f.name,'path':str(f.relative_to(P)),'entity':'Original educational mechanism diagram','version':'1.0','component':'Not plugin UI','source_page':None,'asset_url':None,'retrieved_at':None,'dimensions':[960,620],'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'rights_status':'original_created_for_user','rights_basis':'Original vector authored from stated routing/algebra; no copied product interface','attribution':'原创教学示意 / 计算示意','modifications':'none','used_on_pages':{'routing.svg':[1,3],'diagnosis.svg':[2],'matrix.svg':[4],'attenuation.svg':[6],'mono-check.svg':[7]}[f.name]})
(P/'assets.json').write_text(json.dumps(a,ensure_ascii=False,indent=2))
print('5 editable SVG diagrams ready')
