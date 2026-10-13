from pathlib import Path
import json,hashlib,html,math,re,shutil
from PIL import Image
R=Path(__file__).resolve().parents[1]
D=R/'assets/diagrams'; D.mkdir(exist_ok=True)
def write(p,t): (R/p).write_text(t,encoding='utf-8')
def dump(p,x): write(p,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
sources=[
{'id':'S1','title':'Waves Abbey Road Reel ADT User Guide','url':'https://assets.wavescdn.com/pdf/plugins/reel-adt.pdf','scope':'第7–13页：组件、输入路由、SRC/ADT、ADT Position、Varispeed、LFO、Pan、Monitor。第9页 Quick Start 对象是人声，不是军鼓。'},
{'id':'S2','title':'Waves Abbey Road Reel ADT 官方产品页','url':'https://www.waves.com/plugins/reel-adt','scope':'标准产品名、原始产品界面。具体版本号未标注。'},
{'id':'S3','title':'FabFilter Pro-R 2 Main controls','url':'https://www.fabfilter.com/help/pro-r/using/maincontrols','scope':'Predelay、Stereo Width 的内部交叉馈送、Send 时 Mix=100%。用于说明不同混响的输入/输出结构会影响前置拓宽结果，不把该产品的百分比套用到其他混响。'},
{'id':'S4','title':'Waves Terms of Use','url':'https://www.waves.com/legal/waves-terms-of-use','scope':'版权及商标保留；未发现界面图可公开再分发的通用许可。'},
{'id':'S5','title':'Music Mixing Secrets','url':'https://github.com/DDDPG/music-mixing-secrets','scope':'本系列可编辑源码仓库。仓库引用不代替技术资料和图片许可。'}]
dump('research/sources.json',sources)
write('research/sources.md','# 一手来源\n\n'+'\n\n'.join(f'## {s["id"]} {s["title"]}\n\n{s["url"]}\n\n{s["scope"]}' for s in sources))
terms=[('Snare','军鼓','本文讨论独立军鼓信号；有串音的实录轨还要监听串音。'),('ADT','Artificial Double Tracking，人工双轨效果','由单一信号生成略有时间与音高差异的声部；不是另录一遍。'),('Waves Abbey Road Reel ADT','产品准确名称','Reel，不是 Real。'),('SRC','未调制的源声部','插件内部源声部可带磁带建模处理，不等于外部完全未处理干声。'),('ADT Position','ADT 声部的基准相对时间位置','相对 SRC，ms；不是混响 Predelay。'),('Varispeed','改变 ADT 时间位置的变速控制','会造成时间与音高变化。'),('LFO','低频振荡器','自动调制；Range 单位 ms，Rate 可为 Hz 或 Bars。'),('Pan','声像位置','Pan 决定声部位置，不等于整体 Stereo Width。'),('Stereo Width','立体声宽度','具体实现依插件而异。'),('Predelay','混响前延时','定义原声到混响开始之间的时间；与 ADT 相对偏移不同。'),('Send / Bus / Return','发送 / 总线 / 返回','本文并联路径：独立干声直达总线，Send 进入效果返回。'),('Wet','效果信号','混响返回设全 Wet，避免重复叠加不需要的直达声。'),('Mono','单声道','监听 L+R 合并结果，不是只听左声道。'),('Phase / Polarity','相位 / 极性','保留 UI 的 Phase 标签；极性翻转不是任意频率的时间对齐。')]
dump('research/term-map.json',[{'term':t,'zh':z,'scope':s} for t,z,s in terms])
facts=[
('F1','product','正式名称为 Waves Abbey Road Reel ADT，ADT 指 Artificial Double Tracking。','S1','p3,p7'),
('F2','product','SRC 与 ADT 分别是未调制声部与效果声部，可独立调整 Pan 和 Level。','S1','p7,p12–13'),
('F3','product','普通版本能相对 SRC 提前或滞后；Live 版本只提供滞后。','S1','p8,p11'),
('F4','product','Stereo 组件通过 Left、Right 或 L+R 选择输入；L+R 为左右相加后除以2。','S1','p8,p11'),
('F5','scope','手册第9页约±10–15 ms及LFO 3–8 ms为人声 Quick Start，不能宣称为军鼓标准参数。','S1','p9'),
('F6','product','Monitor 可切 Mono；LFO Range 选3表示±3 ms。','S1','p11'),
('F7','product','Pro-R 2 Stereo Width 涉及交叉馈送；50%时单边输入在两侧形成等量混响，100%时两侧独立。','S3','Stereo Width'),
('F8','product','Pro-R 2 作为 Send 效果时官方要求 Mix 100%。','S3','Mix'),
('F9','inference','把 ADT 放在独立混响返回的前端，可让直达军鼓绕开 ADT；效果是否更合适必须在编曲内检验。','original','routing'),
('F10','calculation','假设 ADT 固定晚12 ms、混响Predelay20 ms：两路送入相同混响的理想起始参考分别为20和32 ms。','original','time model'),
('F11','calculation','等幅同极性的原声与延迟副本相加时，梳状陷波为(2k+1)/(2τ)；τ=12 ms时首个为41.67 Hz，间隔83.33 Hz。','original','linear fixed-delay model'),
('F12','limitation','本项目没有运行音频实测，没有客观宽度提升值、推荐预设或保证单声道兼容的参数。','original','scope')]
dump('research/facts.json',[dict(id=i,type=t,claim=c,source=s,locator=l) for i,t,c,s,l in facts])
# Genuine pixel crops, no retouching
im=Image.open(R/'assets/source/reel-adt-official-product.png'); print('official image',im.size)
crops={'position':(0,0,1940,440),'src':(250,450,605,1669),'adt':(1360,450,1690,1669),'lfo':(605,1350,1380,1620),'monitor':(1690,1340,1940,1669)}
# use actual source dimensions, source is 1940 x 1669
for name,box in crops.items(): im.crop(box).save(R/f'assets/derived/reel-adt-{name}.png')
base={'entity':'Waves Abbey Road Reel ADT','version':'官方产品页图，具体版本未标注','component':'单 ADT 声部 Stereo 界面；有 Input Source Left/L+R/Right 与 Monitor','source_page':sources[1]['url'],'asset_url':'https://media.wavescdn.com/images/products/plugins/max/reel-adt.png','retrieved_at':'2026-10-13','copyright_owner':'Waves Audio Ltd. / relevant trademark owners','rights_status':'limited_educational_commentary_public_clearance_unverified','rights_basis':'真实界面用于对该产品控件的必要教学评论；未发现通用转载许可，不宣称已获厂商授权。公开再发布需另行核实权利或取得许可。','attribution':'Waves 官方产品图 © Waves Audio Ltd.；产品与商标归各自权利人。','limitations':'图中 19.98 ms、LFO ±05、2 Bars、L+R 等为厂商展示状态，非本文设置或实测。仅裁切或等比缩放；不改值、不补字、不仿制 UI。'}
assets=[]
for name,path,box in [('official-product','assets/source/reel-adt-official-product.png',None)]+[(n,f'assets/derived/reel-adt-{n}.png',b) for n,b in crops.items()]:
    p=R/path; a=dict(base); a.update(asset_id='reel-adt-'+name,path=path,dimensions=list(Image.open(p).size),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),modifications='none' if box is None else {'crop_px':list(box),'from':'reel-adt-official-product'},used_on_pages=[]); assets.append(a)
p=R/'assets/source/reel-adt-manual-interface.jpeg';a=dict(base);a.update(asset_id='manual-interface',path=str(p.relative_to(R)),source_page=sources[0]['url']+'#page=10',asset_url=sources[0]['url'],dimensions=list(Image.open(p).size),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),modifications='从官方PDF第10页提取未重编码嵌入JPEG；原图已包含厂商蓝色箭头标注。',used_on_pages=['research']);assets.append(a)
dump('assets/assets.json',assets)
# Original explanatory SVGs. They are conceptual diagrams, not UI or measured traces.
B='#0066cc';G='#697887';INK='#1d1d1f';LIGHT='#f5f5f7'
def svg(name,body,w=936,h=520):
    (D/(name+'.svg')).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><defs><marker id="arr" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8" fill="none" stroke="{B}" stroke-width="1.3"/></marker></defs><rect width="100%" height="100%" fill="white"/><g font-family="Noto Sans SC,sans-serif" fill="{INK}">{body}</g></svg>')
def tx(x,y,t,size=30,color=INK): return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}">{html.escape(t)}</text>'
def rect(x,y,w,h,label): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{LIGHT}" stroke="#d2d2d7"/>'+tx(x+20,y+h/2+10,label,30)
def ar(x1,y1,x2,y2):return f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="{B}" stroke-width="3" marker-end="url(#arr)"/>'
b=tx(0,38,'并联路径示意：干声绕开 ADT，空间单独处理',32)
b+=rect(0,85,170,80,'Snare')+ar(170,125,750,125)+rect(765,85,170,80,'Mix Bus')+tx(340,100,'Dry：居中',28,G)
b+=f'<path d="M110 165 L110 265 L175 265" fill="none" stroke="{B}" stroke-width="3" marker-end="url(#arr)"/>'+tx(0,220,'Send',28,B)
b+=rect(190,225,210,80,'Reel ADT')+ar(400,265,470,265)+rect(485,225,245,80,'Stereo Reverb')+tx(499,347,'100% Wet',28,B)
b+=f'<path d="M730 265 L850 265 L850 175" fill="none" stroke="{B}" stroke-width="3" marker-end="url(#arr)"/>'
b+=tx(0,430,'SRC + ADT 是混响的输入材料；最终返回只保留混响。',28)+tx(0,479,'假设 DAW 路由与延迟补偿正确；具体插件输入结构另核对。',25,G)
svg('parallel-routing',b)
b=tx(0,35,'理想时间模型：ADT 偏移与 Predelay 不是同一个量',31)
for y,label,t,color in [(125,'Dry',0,G),(235,'SRC → Reverb',20,B),(345,'ADT → Reverb',32,B)]:
 b+=tx(0,y-25,label,28,color)+f'<line x1="270" y1="{y}" x2="880" y2="{y}" stroke="#d2d2d7" stroke-width="2"/>'
 x=270+t*15;b+=f'<line x1="{x}" y1="{y-35}" x2="{x}" y2="{y+15}" stroke="{color}" stroke-width="5"/>'+tx(x+10,y-12,str(t)+' ms',27,color)
for n in [0,10,20,30,40]: b+=tx(260+n*15,411,str(n),25,G)
b+=tx(895,411,'ms',25,G)+tx(0,470,'假设：ADT +12 ms；Predelay 20 ms；忽略建模与调制。',27,G)
svg('time-reference',b)
# linear fixed-delay response, normalized equal amplitude sum
pts=[]
for i in range(701):
 f=i/700*350; mag=max(abs(math.cos(math.pi*f*.012)),.001); db=max(20*math.log10(mag),-36);x=100+f/350*780;y=90-db/36*300;pts.append(f'{x:.2f},{y:.2f}')
b=tx(0,34,'相加后的梳状结构：理想固定 Delay，非插件实测',31)
for db in [0,-12,-24,-36]:y=90-db/36*300;b+=f'<line x1="100" y1="{y}" x2="880" y2="{y}" stroke="#e5e5ea"/>'+tx(10,y+8,str(db)+' dB',22,G)
b+=f'<polyline points="{" ".join(pts)}" fill="none" stroke="{B}" stroke-width="3"/>'
for f in [0,100,200,300]:b+=tx(88+f/350*780,430,str(f),24,G)
b+=tx(845,430,'Hz',24,G)+tx(0,485,'τ = 12 ms；等幅、同极性；幅度按两路同相峰值归一化。',26,G)
svg('comb-response',b)
dump('assets/diagram_data.json',{'routing':{'dry_path':'Snare -> Mix Bus','send_path':'Snare -> Reel ADT (SRC+ADT) -> Stereo Reverb 100% Wet -> Mix Bus','type':'conceptual'},'time_model':{'type':'illustrative_not_measured','adt_relative_ms':12,'reverb_predelay_ms':20,'src_reverb_onset_ms':20,'adt_reverb_onset_ms':32,'assumptions':['fixed relative delay','LFO off for model','identical onset convention','not measured through actual plugin']},'comb_model':{'tau_s':.012,'model':'abs(cos(pi*f*tau)), normalized equal-amplitude same-polarity sum','first_null_hz':1/(2*.012),'null_spacing_hz':1/.012,'scope':'fixed delay without modulation, nonlinear saturation, filtering or reverb; not a Reel ADT response'}})
report='''# 军鼓混响前的 ADT 拓宽研究报告

作者 Kangdi Wang

## 结论与适用范围

想让军鼓周围的空间更有左右差异，可以把 Waves Abbey Road Reel ADT 放在独立混响返回的前端，让原始军鼓走居中的直达路径。这样能把“打击中心”和“空间处理”分开调整。它是一种值得比较的路由选择，不保证比直接送混响更宽，也不是所有军鼓都需要。

本文面向已经会建立 Send / Return 的混音学习者。讨论对象是单声道或中心明确的军鼓；目标是学会搭建路径、判断 ADT 改了什么，以及识别这条链路何时没有意义。没有载入音频进行试听或测量，所以不提供最佳预设、客观宽度增益或听感保证。所有图中的数值例子均为明确假设下的教学计算。

## 一 先认清实际产品

正确名称是 Waves Abbey Road Reel ADT，其中 Reel 指磁带卷盘。ADT 是 Artificial Double Tracking：由同一声源产生略有时间、音高和音色差异的声部，制造类似双轨的感觉。[S1][S2]

![Waves Reel ADT 官方完整产品图](../assets/source/reel-adt-official-product.png)

图1 真实官方产品图。具体版本未标注；这是单 ADT 声部并带 Input Source 与 Monitor 的 Stereo 界面。图内 19.98 ms、LFO ±05、2 Bars 和 L+R 是厂商展示状态，不是本文设置，更不是实测结果。原图像素未重绘。

SRC 是插件内部的未调制声部；ADT 是调制声部。SRC 虽未被 ADT 调制，仍处在插件的建模路径中，不能简单等同于外部完全未处理的干声。两声部各自有 Pan 与 Level。Pan 决定它们在左右的位置；宽度来自两路的差异和相对声像，不是一个叫“宽度”的万能旋钮。[S1，p7、p12–13]

普通 Reel ADT 可让 ADT 相对 SRC 提前或滞后；Live 组件只允许滞后。所谓“提前”是相对插件内部参照，不是让现实中的鼓点穿越时间；普通版本利用处理延迟来实现这个关系。[S1，p8]

## 二 路由先解决干声的归属

![并联军鼓空间路由示意](../assets/diagrams/parallel-routing.svg)

图2 原创信号流程示意，不是 DAW 截图。干声直达 Mix Bus；Send 经 Reel ADT，再进立体声混响，最终返回混音。

一个可控的起点是：军鼓直达路径居中，单独建立效果返回。在这个返回上按顺序放 Reel ADT → Stereo Reverb。混响设为全 Wet，效果强弱用发送量或返回推子调整。FabFilter Pro-R 2 的官方说明也明确建议 Send 使用时把 Mix 设为100%；其他混响要核对自己的 Mix / Wet 控件语义。[S3]

这里常见的误解是“并联效果都应该只剩 ADT 声部”。本例并非如此：Reel ADT 的 SRC 与 ADT 一起作为混响的输入材料，然后由后面的全 Wet 混响输出空间。Reel ADT 本身的 SRC 不会通过一个独立直通出口绕过后面的混响。若目标是只给偏移声部加混响，当然也能静音 SRC，但那已是另一种声源关系，需要重新判断两侧能量与返回音色。

这种路由让直达军鼓绕开 ADT，但不保证整个混音的瞬态或单声道结果毫无变化。返回信号仍会与直达声叠加，实录军鼓里的镲片串音也会被送进效果。检查 DAW 的发送位置、立体声通道、声像跟随方式和延迟补偿；不要把路由假设当成已验证的工程状态。

## 三 真界面里需要看哪里

![Reel ADT 时间区局部](../assets/derived/reel-adt-position.png)

图3 官方界面时间区原像素裁切。SRC 为时间参照；ADT Position 给出效果声部的基准相对位置。截图的19.98 ms仅用于识别位置。[S1，p11]

![Reel ADT LFO 区局部](../assets/derived/reel-adt-lfo.png)

图4 官方界面 LFO 区原像素裁切。LFO Range 的单位是ms；Rate 可用Hz，开启 Sync 后可用Bars。Range 选择3表示±3 ms，不是总共3 ms。图里的2 Bars不是2秒。[S1，p11–12]

先静态比较，再增加调制，比一次拧多个旋钮更容易知道哪里产生变化。可以先关闭 LFO，找到不让打击关系明显散开的相对时间和声部平衡，再增加少量调制并带伴奏判断。这是试听方法，不是厂商军鼓预设。

手册第9页的 Quick Start 明确以人声轨为例，其中±10–15 ms及LFO 3–8 ms不能直接改写成“军鼓推荐参数”。本文的+12 ms计算只是容易核算的示例，也不是建议照抄。SRC / ADT 的Drive会引入额外音色因素，初次比较时应把它们控制住，避免同时改变太多变量。

## 四 ADT 偏移不等于混响 Predelay

![ADT与混响前延时的时间参照](../assets/diagrams/time-reference.svg)

图5 理想事件时间模型，不是采样波形。假定源声部相对时刻为0，ADT固定晚12 ms，混响Predelay为20 ms，并暂时忽略调制、建模和算法建立过程。

在这个简化模型下，源声部驱动的混响起始参考位于20 ms，ADT声部驱动的参考位于32 ms。两者仍相差12 ms。ADT改的是送进混响的两份材料之间的关系；Predelay改的是混响相对各自输入的起始位置。把两种操作都叫“延迟”容易掩盖它们的不同任务。

这个算术不能预测真实混响的首个可闻反射。真实算法有内部扩散、建立时间和跨声道耦合，Reel ADT又有调制与磁带建模；普通组件的插件延迟、宿主补偿也必须单独考虑。因此20与32 ms用于理解信号流，不应写成导出文件必定出现的测量位置。

## 五 前置宽度能不能留到输出

“混响输出是立体声”并不等于“输入的左右差异会原样保留”。如果算法先把左右输入相加成单声道，前置的声像差异就已合并；此时后端仍可生成宽阔的立体声尾音，但其宽度主要由混响内部结构决定。ADT留下的时间与音色变化仍可能改变混响，不能据此说它完全没有作用。

一个可核验的例子来自 Pro-R 2：Stereo Width 不只是输出端的左右混合，它还控制内部交叉馈送；官方说明50%时单侧输入会在两侧形成等量混响，100%时两声道独立处理。[S3] 这证明应查具体算法，不应把“有Stereo插槽”当成统一保证。这些百分比只适用于Pro-R 2。

另外，Reel ADT 的 Stereo 组件本身也不是透明地保留一个已宽化输入：它可选择左声道、右声道或将L+R相加后除以2。[S1，p8、p11] 本文从独立单声道军鼓出发；若来源已经是立体声鼓组或宽化采样，先核对 Input Source，避免把整组左右信息意外折叠。不要把这里的前置ADT技巧泛化为整个鼓总线的默认处理。

实际判断可分三步：单独听混响返回；保持声部电平与混响设置不变，比较ADT不同Pan关系；再回到整首歌听中心、宽度和串音。如果只有音量变大，先尽量匹配响度再比较。如果算法的输入结构无法确认，就把结果写成该会话下的试听判断，不宣称普遍原理。

## 六 为什么必须听 Mono

![固定延迟叠加的理想梳状响应](../assets/diagrams/comb-response.svg)

图6 理想数学模型：等幅、同极性原声与固定延迟副本相加；横轴Hz，纵轴按同相峰值归一化的dB。它不是Reel ADT测得的频响，也不包含混响。

令两路为x(t)与x(t−τ)。归一化幅度是 |cos(πfτ)|，陷波发生在 f=(2k+1)/(2τ)。若τ=0.012 s，首个陷波为41.67 Hz，相邻陷波间隔83.33 Hz。例如125 Hz和208.33 Hz也在这一理想序列上。数值说明：短到听不成独立重复的时间差，也可能在合并时形成明显的频率选择性叠加。

真实军鼓不是稳定正弦，ADT也不是这个线性静态模型。LFO会让时间变化，电平不等会使陷波变浅，Drive、滤波和混响都会改变结果。因此不能用图6预测某个军鼓一定丢掉哪段频率。它解释的是风险来源，而非提供一条必须躲开的12 ms禁区。

用插件Monitor可检查ADT输出的Mono，但完整链路还应在后级监听整个混音的L+R合并。单听左声道不算Mono检查。听中心打击是否变空、返回音色是否明显塌陷、平衡是否改变；若有问题，先降低返回量或ADT声部、减少过度调制，再重新判断是否需要这条链路。UI 的 Phase 按钮执行极性翻转，不是任意频率的时间对齐，也不是万能修复；相位、时间和极性不是同一概念。

## 七 可复用的试听流程与停止条件

1. 先听原军鼓直接送同一混响，记住中心、尾音与串音。
2. 在返回前加Reel ADT，保持直达路径不动。先做静态声部关系，再加LFO；每次只比较一个变量。
3. 尽量匹配开关处理前后的主观响度，避免“更大声”被误判为“更宽、更好”。不要用插件截图上的推子位置冒充已匹配响度。
4. 依次听返回Solo、整首歌Stereo、整首歌Mono。手机的小扬声器检查可以补充，但不是标准化测量。
5. 如果空间更符合编曲而中心仍清楚，保留最低有效用量；如果只增加晃动、串音、拖尾或单声道问题，回退至直接送混响，或改用混响自身的宽度与声道选项。

停止条件不是把所有旋钮都用上，而是在相同监听条件下得到可接受的中心和空间关系。没有明确问题，就没有必须加ADT的理由。

## 图片真实性与发布权利

两份真实对象证据分别来自Waves官方产品原图和官方手册第10页的嵌入JPEG。产品图裁切只改变取景范围，没有重绘界面、替换数值、补字或改色；每项尺寸、裁切框和SHA-256在assets.json中逐项记录。完整手册缓存不进入对外交付包。

厂商图用于必要的产品教学评论。公开可见、注明来源、保留商标都不自动构成转载许可。未找到该图可公开再分发的通用许可，Waves条款保留相关权利。[S4] 因而素材状态是“公开再发布权利未核实”，不能标记为cleared或当作图库再授权；公开发布前需核实适用权利基础或取得许可。原创SVG为解释示意，不是音频实测或厂商界面。

## 参考资料

'''+ '\n\n'.join(f'[{s["id"]}] [{s["title"]}]({s["url"]})。{s["scope"]}' for s in sources)
write('research/RESEARCH_REPORT.md',report)
article='''# 军鼓的空间想更宽 先试试混响前的 ADT

想让军鼓周围多一点左右差异，可以在独立混响返回前加Waves Abbey Road Reel ADT。原军鼓仍走居中的直达路径，空间支路单独调整。它适合当作一次对照实验，不是每条军鼓都必须加的处理。

Reel ADT把信号分为SRC和ADT声部，用相对时间、调制与独立Pan制造差异。SRC是插件内部未调制声部，不代表完全没经过建模。让这两份材料先形成关系，再送进混响，是这条链路的核心。

搭建时：Snare直接送Mix Bus；另开Send，顺序为Reel ADT → Stereo Reverb → Mix Bus。最后的混响设100% Wet，效果大小用发送或返回量控制。Reel ADT内部可以保留SRC与ADT，因为二者还要一起送入混响；不要把“并联”误读为必须静音SRC。

先认三个区域：ADT Position看相对时间；SRC / ADT Pan与Level看左右和电平关系；LFO看随时间的变化。先静态比较，再加调制，一次只改一个变量。官方图上的数值不是本篇参数；手册人声Quick Start也不能当成军鼓标准预设。

ADT时间差和混响Predelay不一样。仅为计算示例：ADT晚12 ms、Predelay20 ms，两路驱动混响的理想时间参照是20与32 ms。这不是音频实测，也没计入算法扩散、磁带建模或宿主延迟。

还要确认混响怎样使用左右输入。立体声输出不保证保留输入的声像；有的处理会先合并，有的有内部跨声道馈送。Reel ADT的Stereo组件也能选择L、R或L+R，因此已有立体声的鼓源不能按单声道军鼓直接照搬。

最后听三遍：返回Solo、整首歌Stereo、整首歌Mono。短时间差合并后可能产生梳状叠加；先匹配响度，再听中心是否空、尾音是否乱、串音是否更突出。必要时降低返回量或减少ADT声部；若仍无收益，就回到直接送混响。

目标是清楚的中心和合适的空间。只用能听出价值的那一点处理。
'''
write('story/ARTICLE.md',article)
plans=[
{'page':1,'question':'想拓宽哪里','title':'军鼓的空间想更宽','takeaway':'在混响前试 ADT；让直达军鼓留在中心。','carrier':'完整官方插件图 + 两路概念速览','source_ids':['S1','S2'],'caveat':'路由建议，未经音频实测；官方图参数非推荐。'},
{'page':2,'question':'具体怎么接','title':'干声居中 空间走支路','takeaway':'Dry直达；Send → Reel ADT（SRC+ADT）→ Stereo Reverb 100% Wet → Mix Bus。','carrier':'全页信号流 + 为何保留SRC解释','source_ids':['S1','S3'],'caveat':'核对宿主延迟补偿和混响输入结构。'},
{'page':3,'question':'该看哪些真控件','title':'先静态比较 再加调制','takeaway':'时间、Pan/Level、LFO各有任务；手册人声Quick Start不是军鼓标准参数。','carrier':'真实时间区、SRC/ADT、LFO局部 + 对应标注','source_ids':['S1','S2'],'caveat':'截图状态为官方展示，不是本教程设置。'},
{'page':4,'question':'ADT与Predelay为何不同','title':'两种时间 两个任务','takeaway':'假设ADT晚12ms且Predelay20ms，理想混响起始参考20/32ms，间隔仍12ms。','carrier':'共用时间轴的原创示意','source_ids':['S1','S3'],'caveat':'计算例，不是实测或推荐值；忽略调制、扩散与宿主延迟。'},
{'page':5,'question':'前置宽度一定到达输出吗','title':'先查混响怎样吃进左右','takeaway':'Stereo输出不保证保留输入声像；Reel ADT自身也可折叠输入。','carrier':'保持分离 / 先合并的两种概念路径 + Pro-R2官方例证','source_ids':['S1','S3'],'caveat':'Pro-R2百分比只适用该产品；不引入第二产品截图假装已研究全套。'},
{'page':6,'question':'怎样判断是否值得留','title':'宽了之后 还要听 Mono','takeaway':'匹配响度；返回Solo→全曲Stereo→全曲Mono；听中心、尾音与串音。','carrier':'短数学风险例 + 试听检查路径','source_ids':['S1'],'caveat':'等幅固定Delay模型非Reel ADT实测；不承诺单声道兼容。'},
{'page':7,'question':'去哪复核与引用','title':'完整图文与可编辑源码','takeaway':'真实仓库URL + 简洁BibTeX，author精确Kangdi, Wang。','carrier':'主题收束与HTML GitHub引用末页','source_ids':['S1','S2','S3','S5'],'caveat':'仓库引用不代替技术一手来源或图片许可。'}]
dump('story/page-plan.json',plans)
write('story/public_caption.txt','''标题：军鼓混响前加 ADT，宽的是哪一层？

想让军鼓周围的空间多一点左右差异，可以试一条支路：
Snare Send → Waves Abbey Road Reel ADT → Stereo Reverb。

直达军鼓仍居中，最后的混响用全 Wet，空间大小用发送/返回量控制。Reel ADT 内部的 SRC 与 ADT 可以一起送入混响。

关键不在照抄毫秒数，而在三件事：
• 先静态比较，再加调制；ADT 偏移与混响 Predelay 是两个任务
• 确认混响如何处理左右输入，Stereo 输出不保证输入声像原样保留
• 匹配响度后，听返回 Solo、全曲 Stereo 和全曲 Mono

图中算术是教学示例，没有做音频实测；官方界面数值不是推荐预设。手册的人声 Quick Start 也不应变成军鼓标准参数。

资料：Waves Reel ADT 官方手册与产品页、FabFilter Pro-R 2 官方帮助。
源码仓库：https://github.com/DDDPG/music-mixing-secrets

#混音 #军鼓 #Snare #ReelADT #混响 #音乐制作
''')
write('RIGHTS.md','''# 权属与发布边界

Waves原图及原像素裁切用于对该产品的必要教学评论。未验证公开再发布许可；状态不等于cleared。来源、原件尺寸、哈希、裁切、展示参数与权利基础见assets/assets.json。Waves Terms of Use保留相关IP及商标权；本包不声称厂商背书或素材无限制再授权。

原创信号流、时间轴、数学模型均为明确假设下的解释图，没有音频实测。字体Noto Sans SC及Noto Sans按随附SIL OFL提供。HTML导出骨架继承Guizang固定版本cf4b810的AGPL-3.0，保留可编辑对应源码及LICENSE。独立故事、布局、图形与数据为本项目新增；混合权利不能被仓库总许可证覆盖。完整厂商手册与缓存网页只用于核对，不进入公开包。

公开发布前的未决项：确认厂商图在具体发布场景下的合法使用依据，或取得许可。不能将本包直接宣称为公开版权清零。
''')
write('source/THIRD_PARTY_NOTICES.txt','''Guizang social-card export scaffold: https://github.com/op7418/guizang-social-card-skill, pinned cf4b810. seed-editorial.html retained; derivative HTML/CSS supplied under AGPL-3.0 with corresponding source.
Noto Sans SC and Noto Sans: SIL OFL 1.1; complete original font and licenses supplied under assets/fonts.
Waves UI: genuine official product pixels and official manual excerpt; copyright and trademarks remain with relevant rights holders. No blanket republication license has been verified. See RIGHTS.md and assets/assets.json.
Original diagrams: conceptual signal flow and deterministic arithmetic, not measured evidence.
''')
# Simple flowing report HTML: independent-readable illustrated research, not carousel design.
def inline(s):
 s=html.escape(s)
 s=re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+)\)',r'<a href="\2">\1</a>',s)
 return s
blocks=[]
paras=report.split('\n\n')
skip=False
for pi,para in enumerate(paras):
 if skip:
  skip=False;continue
 if para.startswith('# '):blocks.append('<h1>'+inline(para[2:])+'</h1>')
 elif para.startswith('## '):blocks.append(('<h2 style="break-before:page">' if para.startswith('## 七 ') else '<h2>')+inline(para[3:])+'</h2>')
 elif para.startswith('!['):
  m=re.match(r'!\[(.*?)\]\((.*?)\)',para);caption=paras[pi+1] if pi+1<len(paras) and paras[pi+1].startswith('图') else '';skip=bool(caption);blocks.append(f'<figure><img src="{m[2]}" alt="{html.escape(m[1])}"><figcaption>'+inline(caption)+'</figcaption></figure>')
 else:blocks.append('<p>'+inline(para).replace('\n','<br>')+'</p>')
css='''@font-face{font-family:Noto;src:url('../assets/fonts/NotoSansSC-Variable.ttf')}@font-face{font-family:'Noto Sans SC';src:url('../assets/fonts/NotoSansSC-Variable.ttf')}@font-face{font-family:Formula;src:url('../assets/fonts/NotoSans-Regular.ttf')}@page{size:A4;margin:18mm 19mm 19mm;@bottom-center{content:counter(page);font-size:9pt;color:#697887}}body{font-family:Noto,Formula,sans-serif;color:#1d1d1f;font-size:10.6pt;line-height:1.65}h1{font-size:23pt;line-height:1.35;margin:0 0 8mm}h2{font-size:16pt;margin:9mm 0 3mm;break-after:avoid}p{margin:0 0 3.4mm;orphans:3;widows:3}a{color:#0066cc;text-decoration:none;overflow-wrap:anywhere}figure{margin:4mm 0;break-inside:avoid}img{max-width:100%;max-height:105mm;display:block;margin:auto}figcaption{font-size:9pt;line-height:1.6;color:#515154;margin-top:3mm}figure:has(img[src*="official-product"]) img{max-height:92mm}'''
write('research/RESEARCH_REPORT.html','<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>军鼓混响前的 ADT 拓宽研究报告</title><style>'+css+'</style><body>'+''.join(blocks)+'</body></html>')
dump('STATUS.json',{'state':'research_story_assets_ready_pending_independent_design','topic':'Snare ADT before reverb','publication_ready':False,'blocking_public_rights':'Waves UI republication clearance unverified','pages_proposed':7})
print('Built research, story, facts, terms, genuine crops, and 3 original diagrams')
