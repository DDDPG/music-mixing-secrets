from pathlib import Path
import json, math, hashlib
from PIL import Image
P=Path(__file__).parent
D=lambda n,o:(P/n).write_text(json.dumps(o,ensure_ascii=False,indent=2),encoding='utf-8')
pages=[
 {'page':1,'title':'人声一加空间，\n中频就糊了？','kicker':'先查效果返回，再决定要不要收窄','body':['如果静音 Reverb / Delay 返回后，臃肿感明显减轻，问题可能在湿声。','只有当多余的中频主要落在 Side，才考虑用 M/S EQ 收一点。'],'takeaway':'“臃肿”是听感描述，不等于“宽度过大”。','visual':'概念信号图：干声与湿声汇合；不画伪造声波。','assets':['routing.svg'],'facts':['F01','F02']},
 {'page':2,'title':'先分清：多了，\n还是宽了？','body':['① 静音／恢复 Return：确认问题是否随湿声出现。','② 先降低 Return 电平试听：若已经清楚，不必强行 M/S。','③ 分别听 Mid / Side 辅助定位，回到整段混音作决定。'],'decision_rows':[{'hear':'Mid 和 Side 都厚','try':'先试 Stereo EQ 或减少湿声'},{'hear':'主要是 Mid 厚','try':'检查 Mid 与干声的叠加'},{'hear':'Side 中频铺得太满','try':'再试 Side 频段衰减'}],'takeaway':'Solo 只帮助定位；选不选、削多少，要在整段混音里判断。','visual':'三个诊断分支；不要做不带条件的疗效前后对比。','assets':['diagnosis.svg'],'facts':['F01','F02','F03']},
 {'page':3,'title':'EQ 放在\n效果器之后','body':['干声继续直达混音；Send 送往立体声效果返回。','在 Reverb / Delay 后插入 M/S EQ，处理已经生成的湿声。','常规并行效果链先确认效果器为 100% Wet，避免额外叠加干声。'],'takeaway':'共享 Return 会连同其他声源一起改变；需要只改人声时，使用独立返回。','visual':'双路线：Dry 直达；Send → Reverb / Delay → M/S EQ → Return → 汇合。','assets':['routing.svg'],'facts':['F04','F05']},
 {'page':4,'title':'Side 不是\n“两边的乐器”','body':['Mid 是左右声道的和；Side 是左右声道的差。','只削 Side 的某段频率，会降低该段左右差分成分；常可让这一段更收拢。','Mid 不等于“只有主唱”，Side 也不是可以单独提取的两侧乐器。'],'formula':['M = (L + R) / 2','S = (L − R) / 2','L = M + S','R = M − S'],'takeaway':'本图采用 1/2 编码约定。实际听感还取决于原始 M/S 比例、相位与素材。','visual':'编码→只处理 S→解码；公式固定一套归一化。','assets':['matrix.svg'],'facts':['F06','F07']},
 {'page':5,'title':'Pro-Q 4：\n选中这个 Side','body':['在立体声 Return 打开 FabFilter Pro-Q 4，建立 Bell。','打开频段控制区右侧的 stereo placement 菜单，选择 Side。','调整 FREQ、GAIN 与 Q；这是单个频段的处理范围，不是整条返回的全频 Width。'],'takeaway':'官方菜单图当前选中 Right；此处只定位 Side 选项，未展示本教程已设置状态。','caption':'FabFilter Pro-Q 4 官方界面局部。原图参数与频谱不是推荐值，也不是本文实测。','visual':'小幅完整产品图定位对象，大幅官方控制区裁切 + 菜单原图；引线指向 Side 行。','assets':['pro-q-4-official-full.jpg','pro-q-4-controls-crop.png','stereo-options.jpg'],'facts':['F08','F09']},
 {'page':6,'title':'先小幅削，\n不要一刀切','body':['试听起点：Side · Bell · 400 Hz · −2 dB · Q 1.0。','400 Hz 只是搜索起点；实际频点、带宽与衰减量跟着素材走。','反复旁路这一频段，尽量匹配整体听感响度，确认字头更清楚、尾音仍自然。'],'example':'计算例：若目标频率的 Side 衰减为 −3 dB，幅度约为原来的 70.8%。','takeaway':'−3 dB 的计算例不等于“宽度变成 70.8%”；它也不是上方 −2 dB 的试听设置。','visual':'M 保持 100%，S 从100%变70.8%的同尺度幅度条；标“计算示意”，不伪造插件曲线。','assets':['attenuation.svg'],'facts':['F10','F11']},
 {'page':7,'title':'收窄之后，\n还要过这三关','body':['① Stereo：字头更清楚吗？空间是否自然？没有更好就撤回。','② Mono：按 DAW 的单声道合并方式检查音色与平衡，不是只听左声道。','③ 整段：主歌、副歌、句尾都检查；共享返回上的其他声源也要听。'],'callout':'理想纯 M/S Side EQ 不改 Mid；因此 Mono 不一定听得出差别，也不能用它证明“已去糊”。','takeaway':'线性相位不是必选项：它可能增加延迟和前振铃。以旁路与实际听感验证。','visual':'三个听音检查节点 + 一行 Mono 推导。','assets':['mono-check.svg'],'facts':['F12','F13']}
]
D('page-plan.json',{'status':'content_and_assets_ready_for_independent_design_review','page_count':7,'audience':'有基础 Send / Return 经验的音乐制作人','learning_outcome':'先诊断湿声堆积，再对效果返回的目标 Side 频段做小幅 EQ，并验证整段与 Mono。','pages':pages})
full='''# 人声中频显得臃肿，先检查效果返回

人声加上 Reverb 或 Delay 后变厚、变糊，并不自动意味着干声需要削中频。先静音效果返回，再恢复：如果臃肿感随着湿声出现，才继续检查这条效果链。先试着把 Return 电平降一点。有时只是湿声整体过多，降低返回比增加复杂处理更直接。

如果仍需处理，区分 Mid 和 Side 只是帮助定位的一种办法。Mid、Side 都偏厚，可以先试 Stereo EQ 或减少湿声；主要是 Mid 堆积，就检查湿声 Mid 与干声的叠加；当 Side 的中频铺得太满，再考虑 Side EQ。不要仅凭 Solo 后某个频段听起来难听就削掉它，最终需要回到整段混音。

把 M/S EQ 插在立体声 Return 上、Reverb / Delay 后面，处理已经生成的湿声。常规并行链先确认效果器设为 100% Wet，避免重复叠加干声。共享 Return 的任何变化都会影响经过它的其他声源；只想改人声时，使用独立的效果返回更容易控制。放在效果器之前的 EQ 会先改变送入效果器的信号，不保证等价于对最终湿声做 Side EQ。

M/S 是信号的和差表示。本文统一采用 M=(L+R)/2、S=(L−R)/2；解码为 L=M+S、R=M−S。Mid 不是只包含居中主唱，Side 也不是“把左右两边的乐器取出来”。降低 Side 某段的幅度，意味着减少该频段的左右差分成分，常能让这段湿声更收拢；听感并非线性的“宽度百分比”，也无法保证消除所有臃肿。

以 FabFilter Pro-Q 4 为例，在立体声 Return 上建立 Bell，打开频段右侧的 stereo placement 菜单并选择 Side，然后调整 FREQ、GAIN、Q。Mono 实例没有相应立体声选项。官方图中的参数和频谱只是厂商的示例状态，不能当作本教程的设置或测量结果；菜单原图当前选中 Right，本教程指的是菜单中 Side 的位置。

可从 Side、Bell、400 Hz、−2 dB、Q 1.0 开始试听。这是教学给出的搜索起点，不是官方推荐，也不是已测得的最佳值。按素材移动频点、改变带宽和衰减量。在整段混音中反复旁路，尽量匹配整体听感响度，听字头是否更容易辨认、空间尾声是否仍自然；没有改善就撤回。

为理解量级，另举一个独立的数学例子：−3 dB 对应幅度乘以 10^(−3/20)，约为 0.708。目标频率的 Side 幅度剩 70.8%，不等于宽度剩 70.8%，也不等于响度降低 29.2%。这与上面的 −2 dB 试听设置不是同一个数值。

最后听 Stereo、Mono 和完整段落。理想纯 M/S Side EQ，且无额外增益、非线性和后级处理变化时，L′=M+H(S)、R′=M−H(S)，所以 (L′+R′)/2=M；Side EQ 不改变 Mid。Mono 检查可能几乎听不出差别，不应把它当成“去糊成功”的证明。真实工程仍可能有路由、增益、插件模式和后级非线性等差异，须实际检查。M/S EQ 也不必默认 Linear Phase；线性相位会引入延迟，可能产生前振铃。选能解决当前问题、且没有带来更大副作用的处理即可。
'''
(P/'article.md').write_text(full,encoding='utf-8')
(P/'publish-caption.txt').write_text('''标题首选：人声一加混响就糊？先查返回轨
标题备选：
1. 人声中频臃肿，M/S EQ 应该削哪里？
2. Side 收一点，空间不一定要全关
3. 别急着削干声：先听效果返回

发布正文：
人声加上 Reverb / Delay 后，中频突然变厚、变糊？先静音效果返回，确认问题是不是随湿声出现。

我的检查顺序：
① 先降一点 Return 电平，排除“湿声整体太多”。
② Mid / Side 辅助定位，回到整段混音判断。
③ 只有 Side 中频铺得太满时，才在效果器后用 Side EQ 小幅衰减。

Pro-Q 4 可建立 Bell，stereo placement 选 Side。400 Hz、−2 dB、Q 1.0 只是试听起点，频点和幅度都要按素材调整。

削 Side 是减少某段左右差分成分，不是万能去糊，也不能换算成固定宽度百分比。最后做旁路、Stereo / Mono 和整段检查，空间变干、字头没改善就撤回。

图中插件画面来自 FabFilter 官方资料，仅用于功能定位；原图参数并非教程设置或实测。资料来源：FabFilter Pro-Q 4 在线帮助（Stereo options、Band controls、Processing mode）与 Ableton Live 12 手册（Return Tracks）。

#混音 #人声混音 #MS处理 #EQ #音乐制作 #混响 #FabFilter
''',encoding='utf-8')
sources=[
('S01','FabFilter Pro-Q 4 Help — Stereo options','https://www.fabfilter.com/help/pro-q/using/stereo','Stereo options; Surround and mono operation','每频段 Stereo / Left / Right / Mid / Side；Mono 实例限制。'),
('S02','FabFilter Pro-Q 4 Help — Band controls','https://www.fabfilter.com/help/pro-q/using/bandcontrols','Band controls','Bell、Frequency/Gain/Q、stereo placement；Q 数值不宜跨产品直接套用。'),
('S03','FabFilter Pro-Q 4 Help — Processing mode','https://www.fabfilter.com/help/pro-q/using/processingmode','Linear Phase; Choosing a suitable processing mode','线性相位延迟与前振铃；并非默认更好。'),
('S04','Ableton Live 12 Manual — Mixing','https://www.ableton.com/en/live-manual/12/mixing/','18.4 Return Tracks and the Main track','Send 决定送入量、Return 可被多轨共享。'),
('S05','Voxengo MSED official product page','https://www.voxengo.com/product/msed/','Overview','M/S 编解码与独立 Mid/Side 调整。公式为本文选定且可逆的教学约定，不宣称 Pro-Q 内部归一化。'),
('S06','FabFilter Press Area','https://www.fabfilter.com/press','Download press kits','官方提供含高分辨率截图的 press kit；未发现覆盖此社交平台教学再发布的明确完整许可。'),
('S07','FabFilter Pro-Q 4 Help — Solo','https://www.fabfilter.com/help/pro-q/using/solo','Solo','Band Solo 为频段定位，不是直接听 EQ 处理结果。本文不把它等同全频 M/S Solo。')]
D('sources.json',[{'id':s[0],'title':s[1],'url':s[2],'section':s[3],'supports':s[4],'accessed':'2026-10-09'} for s in sources])
(P/'sources.md').write_text('# 来源与适用范围\n\n核验日期：2026-10-09。实际对象：FabFilter Pro-Q 4，立体声实例；不声称已运行插件或试听用户音频。\n\n'+'\n\n'.join(f'## {a} — {b}\n{c}\n章节：{d}\n用途：{e}' for a,b,c,d,e in sources)+'\n\n## 推导与试听建议\nF06/F07/F11/F12 为可复核的代数或 dB 计算，不是音频测量。F01/F02/F03/F10 是有条件的诊断与试听建议，不是厂商承诺。没有实际音频，因此不提供效果改善比例。\n\n## 图像权属\n原始来源为 FabFilter 官方 press kit / 帮助页。版权属于 FabFilter。限量教学说明、评论草稿使用；未核实适用于小红书再发布的完整许可，不标记为 cleared，不代表厂商背书。对外发布前复核许可或替换为有权使用的实际截图。\n',encoding='utf-8')
facts=[('F01','diagnostic_advice','静音返回后臃肿感减轻，提示湿声可能参与问题；不是唯一病因。',[],[1,2]),('F02','diagnostic_advice','Wet 总量、频率平衡与立体声差分需分别判断，收窄不是通用去糊。',[],[1,2]),('F03','diagnostic_advice','分开听 Mid/Side 仅作定位，回到整段混音决定；不要把 Pro-Q Band Solo 当作全频 M/S Solo。',['S07'],[2]),('F04','official_fact','Return 可接收多轨 Send；处理共享 Return 会影响其中所有声源。',['S04'],[3]),('F05','routing_advice','常规并行效果链用 100% Wet，后置 EQ 处理生成后的湿声；前置不保证等效。',['S04'],[3]),('F06','mathematical_definition','本文约定 M=(L+R)/2，S=(L−R)/2；解码 L=M+S，R=M−S。不是对插件内部缩放作声明。',['S05'],[4]),('F07','mathematical_inference','保持 Mid，衰减目标频率 Side，可降低该频率差分幅度；听感宽度并无一一线性换算。',['F06'],[4]),('F08','official_fact','Pro-Q 4 每频段可设 Side；stereo placement 在 band controls 右侧；Mono 实例无此选项。',['S01','S02'],[5]),('F09','observed_asset_state','官方菜单原图选中 Right，不是 Side。Press kit 全图显示示例 EQ，非本文设置。',['S06','S01'],[5]),('F10','audition_starting_point','Side Bell 400 Hz −2 dB Q1.0 为自拟试听起点，未测量、非官方推荐。',[],[6]),('F11','calculation','10^(−3/20)=0.7079457844；幅度70.8%，不是宽度或响度百分比。',[],[6]),('F12','mathematical_inference','L′=M+H(S)，R′=M−H(S)，故平均合并为 M；限理想纯Side处理且无额外增益、非线性、后级变化。',['F06'],[7]),('F13','official_fact','Linear Phase 可引入延迟和前振铃，不是所有 M/S EQ 都必须采用。',['S03'],[7])]
D('facts.json',[dict(id=a,type=b,claim=c,sources=d,pages=e) for a,b,c,d,e in facts])
terms=[('M/S','Mid/Side','和差信号；统一1/2编码约定'),('Mid','Mid','左右和信号；不是只含居中主唱'),('Side','Side','左右差信号；不是两侧乐器的独立提取'),('Send','Send','发送；不等于返回或效果器'),('Return','Return / Aux','效果返回通道；各 DAW 命名与路由不同'),('Reverb','Reverb','混响'),('Delay','Delay','延时；不将正式标签改成回声'),('Wet','Wet','效果处理支路'),('Dry','Dry','此并行链中未经过该空间效果的直达支路'),('Bell','Bell','钟形均衡'),('FREQ','FREQ','Pro-Q 4 UI 频率控件'),('GAIN','GAIN','Pro-Q 4 UI 增益控件；单位 dB'),('Q','Q','带宽相关参数；不是立体声宽度'),('stereo placement','stereo placement','每频段声道处理范围；菜单项保留 Side'),('Stereo Width','Stereo Width','立体声宽度；不能与 Pan 或幅度百分比互换'),('Mono','Mono','左右合并单声道，非只听左声道'),('Linear Phase','Linear Phase','线性相位；有延迟/前振铃取舍')]
D('term-map.json',{'baseline':'MIXING_TERMINOLOGY.md v1.0.0; 2026-10-09','product':'FabFilter Pro-Q 4','normalization':{'encode':['M=(L+R)/2','S=(L−R)/2'],'decode':['L=M+S','R=M−S']},'terms':[dict(term=a,label=b,meaning=c) for a,b,c in terms]})
D('calculation-data.json',{'kind':'calculation_not_measurement','audition_example':{'placement':'Side','shape':'Bell','frequency_hz':400,'gain_db':-2,'Q':1.0,'basis':'self-authored audition starting point'},'independent_amplitude_example':{'gain_db':-3,'factor':10**(-3/20),'percent':100*10**(-3/20),'formula':'10^(gain_dB/20)','not':'Not width percentage or loudness percentage'},'matrix_convention':'M=(L+R)/2; S=(L-R)/2; L=M+S; R=M-S'})
# Authentic crops, no content retouching.
im=Image.open(P/'assets/source/pro-q-4-official-full.jpg')
# original is 2400 x 1441; crop box derived from viewed full screenshot ratios
w,h=im.size
box=tuple(round(v) for v in (w*.305,h*.745,w*.707,h*.926))
im.crop(box).save(P/'assets/derived/pro-q-4-controls-crop.png')
assets=[]
for name,entity,source,url,used,state in [
('pro-q-4-official-full.jpg','FabFilter Pro-Q 4','https://www.fabfilter.com/press','https://www.fabfilter.com/downloads/press/fabfilter-pro-q.zip',[5],'Official press screenshot, factory demonstration state; not tutorial setting'),
('stereo-options.jpg','FabFilter Pro-Q 4 stereo placement menu','https://www.fabfilter.com/help/pro-q/using/stereo','https://www.fabfilter.com/help_pages/pro-q/images/stereooptions%402x.jpg',[5],'Right selected; Side visible but not selected'),
('stereo-display.jpg','FabFilter Pro-Q 4 stereo curves example','https://www.fabfilter.com/help/pro-q/using/stereo','https://www.fabfilter.com/help_pages/pro-q/images/stereodisplay%402x.jpg',[],'Official example; not measured and not tutorial setting'),
('band-controls.jpg','FabFilter Pro-Q 4 band controls','https://www.fabfilter.com/help/pro-q/using/bandcontrols','https://www.fabfilter.com/help_pages/pro-q/images/bandcontrols%402x.jpg',[],'Official help example; not tutorial setting')]:
 f=P/'assets/source'/name
 if not f.exists():continue
 im=Image.open(f)
 assets.append({'asset_id':name,'path':str(f.relative_to(P)),'entity':entity,'version':'Pro-Q 4; exact patch version of image unconfirmed','component':'Stereo example, official product/help context','source_page':source,'asset_url':url,'retrieved_at':'2026-10-09','dimensions':list(im.size),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'rights_status':'unverified_for_public_republication','rights_basis':'Officially distributed press/help material, retained for limited teaching commentary draft; no explicit general redistribution license found','attribution':'Screenshot © FabFilter. Source: official Pro-Q 4 materials.','modifications':'none','used_on_pages':used,'state_disclaimer':state})
f=P/'assets/derived/pro-q-4-controls-crop.png'
assets.append({'asset_id':f.name,'path':str(f.relative_to(P)),'derived_from':'pro-q-4-official-full.jpg','crop_box_px':box,'entity':'FabFilter Pro-Q 4 control area','version':'Pro-Q 4; exact patch unconfirmed','component':'Stereo example','source_page':'https://www.fabfilter.com/press','asset_url':'https://www.fabfilter.com/downloads/press/fabfilter-pro-q.zip','retrieved_at':'2026-10-09','dimensions':list(Image.open(f).size),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'rights_status':'unverified_for_public_republication','rights_basis':'same as source','attribution':'Screenshot © FabFilter; cropped for control identification.','modifications':'crop only; no relabeling or retouch','used_on_pages':[5],'state_disclaimer':'Stereo shown in band controls; menu example separately shows Right selected. Neither is tutorial Side setting.'})
D('assets.json',assets)
print('Content written; image size',w,h,'crop',box)
