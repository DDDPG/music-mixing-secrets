from pathlib import Path
import json,math,hashlib,shutil
from PIL import Image
P=Path(__file__).parent
D=P/'assets/diagrams'
def j(name,obj): (P/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2))
sources=[
('S01','Ableton Live 12 Manual — Mixing','https://www.ableton.com/en/manual/mixing/','18.1.1 Additional Mixer Features','Floating-point internal headroom is not a license to clip physical I/O or fixed-point export; no universal kick peak target.'),
('S02','Shure — Microphone Techniques for Recording','https://www.shure.com/en-US/docs/education/Microphone-Techniques-for-Recording','Phase; electrical output','Equal coherent sine sums; timing differences cause frequency-dependent phase relationships. Use definitions, not oversimplified broadband “180 degrees” phrasing.'),
('S03','FabFilter Pro-Q 4 Help — Spectrum analyzer','https://www.fabfilter.com/help/pro-q/using/analyzer','Spectrum analyzer','Pre/Post/external display; collision suggestion is not proof of audible masking; analyzer resolution and tilt change display.'),
('S04','FabFilter Pro-Q 4 Help — Piano display','https://www.fabfilter.com/help/pro-q/using/pianodisplay','Piano display','88-key A0=27.5 Hz through C8; note labels and frequencies are related, not fixed tonal recipes.'),
('S05','FabFilter One Help — Filter','https://prod.fabfilter.com/help/one/using/filter','Filter','Harmonics are multiples of fundamental in harmonic oscillator signals.'),
('S06','iZotope — How to Mix Kick and Bass','https://shopify.izotope.com/community/blog/how-to-mix-kick-and-bass','Unmask overlapping frequencies; sidechain; choose notes','Arrangement, envelope length, tonal choices and conditional dynamic ducking. Do not reproduce article’s overly broad 90% or fixed kick-wins statements.'),
('S07','iZotope — Mastering low end: essential processing tips and tools','https://shopify.izotope.com/community/blog/mastering-low-end','Harmonic support','Harmonics can preserve bass identity on restricted-bandwidth playback; not a universal 800–2500 Hz requirement.'),
('S08','iZotope — How to EQ Drums','https://www.izotope.com/community/blog/how-to-eq-drums','Snare; toms and percussion; hi-hats','Timbre and arrangement determine EQ; dynamic EQ can tame intermittent harshness. Do not adopt mandatory HPF recipe from article.'),
('S09','FabFilter Press Area','https://www.fabfilter.com/press','Download press kits','Official Pro-Q 4 editorial media kit; no blanket redistribution license discovered.'),
('S11','FabFilter Learn — How to use reverb?','https://www.fabfilter.com/learn/reverb/how-to-use-reverb','Auxiliary reverb workflow','Conventional parallel reverb uses 100% Wet; variable Send amounts control wet contribution.'),
('S10','Ableton Live 12 Manual — Live Audio Effect Reference','https://www.ableton.com/en/manual/live-audio-effect-reference/#utility','Utility','Left/right phase inversion controls; terminology distinction is explained separately.'),
]
(P/'sources.md').write_text('# Public research sources\n\nRetrieved 2026-10-09 UTC. All are manufacturer manuals or manufacturer educational publications. Numerical examples marked C are independently calculated; listening moves marked W are editorial starting points, not measurements.\n\n'+'\n\n'.join(f'## {x[0]} {x[1]}\n{x[2]}\nSection: {x[3]}\nScope: {x[4]}' for x in sources)+'\n\n## Image rights\nFabFilter official press kit provides screenshots for press use. This is a strong editorial-use signal, but not an explicit general license for commercial social redistribution or modified crops. No blanket clearance is claimed. Official manual illustrations also have no discovered reuse license. Assets are research/review material until scope is accepted or permission obtained. See assets.json.\n')
facts=[
('F01','product_fact','各级处理与输出都需留余量；单轨峰值不能替代总线检查。',['S01'],[2],'不承诺所有内部轨道一过 0 dBFS 就削波，也不推广“红灯无害”。'),
('F02','editorial_workflow','先辨认节奏主角，再用推子建立 Kick / Bass / Snare 的关系；没有跨曲风固定音量排序。',[],[1,2],'试听起点，不是标准。'),
('F03','definition','Polarity 反转是 x(t)→−x(t)；Delay 是 x(t)→x(t−τ)，两者不等价。',['S02','S10'],[3],'单一正弦在半周期时二者可能等效；宽频复杂信号不能混同。'),
('F04','calculation','5 ms 对 50 Hz 是 90°，对 100 Hz 是 180°。',[],[3],'Δφ=360°fτ；用稳定正弦说明，不是实际鼓波形测量。'),
('F05','calculation','两个同相同幅正弦相加，振幅 2 倍，20log10(2)=6.0206 dB；相反极性且完全相同则理想抵消。',['S02'],[2,3],'不意味着两条任意乐器相加固定 +6 dB。'),
('F06','product_fact','FabFilter Pro-Q 4 的 Analyzer 可显示 Pre/Post/外部频谱；Show Collisions 仅给潜在冲突提示。',['S03'],[4],'频谱重叠并不自动证明听觉遮蔽，也不等于相消。'),
('F07','calculation','在 A4=440 Hz 的十二平均律中，E1≈41.20 Hz，A1=55 Hz；A1 的前四阶谐波是 55/110/165/220 Hz。',['S04','S05'],[4,5],'音符八度命名以 C4 为中央 C；某些 DAW 八度标签不同，频率不变。'),
('F08','editorial_workflow','Kick 约 100 Hz 或 Bass 800 Hz–2.5 kHz 只能作有问题时的搜索区；先确认音色、音高与编曲角色。',['S06','S07'],[4,5],'不是必须提升，也不是每个素材的基频或唯一可听区域。'),
('F09','editorial_workflow','高频 Bass 层可由低频层的谐波感觉出发，匹配起音与时值，再判断音高和增益。',['S05','S07'],[5],'审美目标；不同音符或独立节奏也可有意成为两个声部。'),
('F10','editorial_workflow','Snare 的厚度、击打感、空间尾声分开判断；300 Hz、1 kHz、2–3 kHz、10 kHz 只是局部试听假设。',['S08'],[6],'削 2–3 kHz 后抬 10 kHz 无法等价恢复原来的击打清晰度。'),
('F11','editorial_workflow','Hi-hat / Cymbal 先降推子，再定位刺耳频段；只在重击刺耳时可试动态 EQ。',['S08'],[7],'不能一律低切到固定频率或削去整个 5–8 kHz。'),
('F12','calculation','120 BPM 的一拍为 500 ms；该速度的八分音符为 250 ms。',[],[1,8],'时间示意不规定实际 groove 或包络长度。'),
]
j('facts.json',{'retrieved_at':'2026-10-09','facts':[dict(zip(['id','type','claim','sources','pages','conditions'],f)) for f in facts]})
terms=[('Kick','底鼓'),('Bass','贝斯／低音声部'),('Snare','军鼓'),('Hi-hat','踩镲'),('Cymbal','镲片'),('Percussion','打击乐'),('Overheads','上方拾音话筒／轨道'),('Fader','推子'),('Gain','增益'),('Headroom','余量'),('Sample Peak','采样峰值'),('dBFS','数字满刻度相对电平'),('Polarity','极性'),('Phase','相位'),('Delay','延时'),('EQ','均衡'),('Bell','钟形均衡'),('Q','品质因数'),('Dynamic EQ','动态均衡'),('Analyzer','分析器'),('Spectrum','频谱'),('Pre','EQ 前频谱，UI 原名'),('Post','EQ 后频谱，UI 原名'),('SC/Ext','外部频谱选择，文档原名'),('Show Collisions','潜在频率冲突提示'),('Fundamental','基频'),('Harmonics','谐波'),('Reverb','混响'),('Send','发送'),('Return','返回通道'),('Dry','未经过该支路处理的信号'),('Wet','经过该支路处理的信号'),('Mono','单声道'),('Bypass','旁通'),('FabFilter Pro-Q 4','产品标准名')]
j('term-map.json',{'baseline':'MIXING_TERMINOLOGY.md v1.0.0','terms':[{'preferred_label':a,'explanation_zh':b} for a,b in terms],'guards':['Phase ≠ Polarity','EQ curve ≠ Spectrum','dB gain ≠ dBFS meter reading','SC screenshot label preserved; manual SC/Ext does not replace actual screenshot text','Delay formal label retained','Harmonic n*f0 only for harmonic components; acoustic drums can be inharmonic']})
pages=[
{'page':1,'title':'鼓与 Bass，先把地基搭稳','dek':'先关系，后音色。让低频有重量，让节奏有轮廓。','body':['先听一段主歌和一段高潮：谁负责落点，谁负责延续，谁负责推进？','沿着 4 条线排查：音量平衡 → 时间与极性 → 频率分工 → 前后层次。','不要一上来，把每件乐器都调得又大又亮。'],'visual':'foundation-timeline.svg','action':'先只听 Kick、Bass、Snare，找到歌曲的重心。','caveat':'图为 120 BPM 的节奏示意，非录音波形；不规定固定乐器音量排序。','sources':['S06']},
{'page':2,'title':'第一步：平衡先过关','dek':'一个推子能解决的事，先不交给 EQ。','body':['把 Kick 调到舒服、留有余量的位置，再慢慢加入 Bass；同时出现时，仍能分清落点与音符吗？','再加入 Snare。让它撑起节奏重音，但别默认所有歌都要 Snare > Kick。','检查轨道、处理器与总线的峰值。不存在通用的“Kick 必须 −10 dBFS”。'],'visual':'headroom-sum.svg','action':'以相近听感响度比较。整体太满，就回调相关轨道／组的电平，再检查前级处理器。','caveat':'两个完全相同、同相正弦相加才是 +6.02 dB；实际乐器叠加不固定增加这个值。','sources':['S01','S02']},
{'page':3,'title':'低频变薄，先分清原因','dek':'遮蔽、相消、尾音堆积，需要不同的处理。','body':['加入 Bass 后 Kick 难辨：可能是遮蔽。两者重叠时低频明显减少：再检查极性与时间关系。','Polarity 反转是上下翻转；Delay 是沿时间移动。一次反相不等于全曲“相位对齐”。','对比多个音符、多个鼓点；若只是某一击更大，别急着保留。先考虑音色、尾长与编曲避让。'],'visual':'polarity-time.svg','action':'保留让整段低频更稳定、节奏更自然的选择。避免为对齐一个波峰破坏 groove。','caveat':'数学示意：5 ms 对 50 Hz 是 90°，对 100 Hz 是 180°；实际 Kick / Bass 不是两条固定正弦。','sources':['S02','S06','S10']},
{'page':4,'title':'频率是线索，不是处方','dek':'先找到“它是什么”，再决定“让它往哪走”。','body':['Kick 的重量不固定在 100 Hz。先听基音／共振区域、尾长和击打轮廓，再决定保留哪一部分。','Bass 会换音：E1 ≈ 41.20 Hz，A1 = 55 Hz。对一个音有效的固定削减，可能伤到另一个音。','Analyzer 帮你定位；频谱重叠不能单凭画面判成遮蔽或相消。最终回到整段试听。'],'visual':'official-proq-object','action':'若 Kick 在 800 Hz–2 kHz 显硬，可先试约 −1 至 −2 dB 的宽 Bell，再匹配响度旁通比较；不硬就不削。','caveat':'官方 Pro-Q 4 图的轨道名为 Guitar，预设 Equalize 4；只解释界面，曲线不是鼓／Bass 推荐设置。','sources':['S03','S04','S06']},
{'page':5,'title':'让 Bass 在小音箱也有形','dek':'低频负责重量，谐波帮助辨认音高与轮廓。','body':['A1 的基频是 55 Hz；110、165、220 Hz 是它的第 2、3、4 阶谐波。音高变了，这组位置也跟着变。','小音箱听不清 Bass，别只继续推最底下。先判断已有谐波是否足够，也可在 800 Hz–2.5 kHz 寻找音符轮廓。','若有独立高频 Bass 层：先对齐音乐起音与时值，再从较小电平慢慢加入；听起来像同一声部的纹理即可。'],'visual':'harmonic-ladder.svg','action':'用实际小音箱复核，同时回到全频监听：轮廓增强了，低频是否仍自然？','caveat':'示意振幅人为设定；不是实测频谱，也不承诺任意小音箱能重放所列频率。','sources':['S05','S07']},
{'page':6,'title':'Snare 的厚度与空间，分开管','dek':'鼓的本体要站住，混响才有地方落。','body':['先听本体：约 300 Hz 可作厚度搜索起点；约 1 kHz 若显硬或有突出共振，再局部试削。','空间太抢时，先减少 Send 或缩短尾声，再检查 Reverb Return 的 2–3 kHz 是否拥挤。','削去击打区后，抬 10 kHz 只能改变另一段亮度，不能等价“补回”原来的清晰度。'],'visual':'snare-routing.svg','action':'用独立 Send / Return 管理 Snare 的 Reverb。主路保留本体，返回通道单独调音量与 EQ。','caveat':'频率均为试听起点；常规并行 Reverb 设为 100% Wet。不是所有 Snare 都要添加混响。','sources':['S08','S11']},
{'page':7,'title':'亮，不必每一下都扎耳','dek':'Hi-hat、Cymbal 与大打击乐，要服务歌曲层次。','body':['先把高频打击乐推子稍收，再听节奏是否仍连贯；不要把“能听见”变成“永远最突出”。','若只有重击刺耳，试动态 EQ；若整段都太亮，再考虑静态 EQ。5–8 kHz 只是可能的搜索区。','大打击乐要有体积，但别用无限加低频换气势；让 1–3 kHz 的硬度、尾长与进入时机配合高潮。'],'visual':'role-hierarchy.svg','action':'与人声、Snare 一起听。保留需要的身体感，避免高通削过头后只剩尖锐边缘。','caveat':'没有固定的镲片／打击乐削减频率；体积、亮度与情绪是整段关系。','sources':['S08']},
{'page':8,'title':'最后，用一段音乐验收','dek':'整段通过，比某一击“巨大”更重要。','body':['① 低音量听：Kick 落点、Bass 音符、Snare 重音都能跟住吗？','② Mono 听：合并为单声道后，低频与高频 Bass 层有没有异常变薄？','③ 换段落、换音符：处理是否稳定？高潮里镲片有没有盖过主角？','④ 匹配响度旁通：改善来自关系更清楚，还是只是更响？最后检查输出余量。'],'visual':'verification-path.svg','action':'一次只解决一个已听到的问题。没有问题的频段，不必按表动刀。','caveat':'本套数值用于说明与起步试听；没有工程音频，因此不构成实测结论。','sources':['S01','S03','S06','S08']}
]
j('page-plan.json',{'working_title':'鼓与 Bass，先把地基搭稳','audience':'能使用推子、EQ 与 Send 的混音初学者／中级自学者','outcome':'按音量、时间、频率和层次顺序建立稳定鼓与 Bass 基础','status':'CONTENT_AND_ASSETS_READY_FOR_INDEPENDENT_DESIGN_REVIEW','pages':pages})
(P/'manuscript.md').write_text('# 鼓与 Bass，先把地基搭稳\n\n'+ '\n\n'.join(f"## {p['page']:02d} {p['title']}\n\n{p['dek']}\n\n"+'\n\n'.join(p['body'])+f"\n\n操作：{p['action']}\n\n图注／限制：{p['caveat']}\n\n公开来源："+'、'.join(p['sources']) for p in pages))
(P/'caption.txt').write_text('标题：鼓与 Bass，先把地基搭稳\n\n低频有重量，不等于 Kick 和 Bass 都要更大；鼓组有气势，也不等于每件打击乐都要更亮。\n\n这套顺序可以直接带回工程：先用推子找关系，再排查时间与极性，接着看频率分工，最后安排 Snare 的空间与镲片的层次。\n\n记住两个边界：一次反相不等于全曲相位对齐；频率数字是搜索起点，不是统一处方。做完用低音量、Mono、不同段落和相近响度的旁通比较验收。\n\n图中的波形、节奏与谐波为计算／概念示意，非工程实测。真实产品图片来自 FabFilter；图片发布权范围仍需确认。公开资料与逐项条件见配套来源说明。\n\n#混音 #音乐制作 #鼓组 #Bass #EQ')
# Real object files: no pixel edits other than literal crops.
full=P/'assets/source/press-kit/FabFilter Pro-Q 4 Screen Shot@2x.jpg'
im=Image.open(full)
# Original press screenshot known dimensions, crop bottom control context retaining frequency scale & track state.
w,h=im.size
crop=(0,int(h*.72),w,h)
im.crop(crop).save(P/'assets/derived/proq-controls-context.png')
crop2=(int(w*.28),int(h*.71),int(w*.74),int(h*.94))
im.crop(crop2).save(P/'assets/derived/proq-band-controls.png')
assets=[]
def asset(id,file,page,source,url,rights,mods='',box=None):
 path=P/file
 if not path.exists(): return  # Optional unused reference images are not redistributed.
 img=Image.open(path)
 assets.append({'asset_id':id,'file':file,'entity':'FabFilter Pro-Q 4','version':'Pro-Q 4; exact screenshot build not stated','component':'Stereo shown in press screenshot; manual analyzer image component not verified','source_page':source,'asset_url':url,'retrieved_at':'2026-10-09','dimensions':list(img.size),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'rights_status':rights,'rights_basis':'Official media kit is supplied for press; no explicit general social/commercial redistribution or crop license found.' if 'press' in source else 'Official manual illustration, no reuse license found.','attribution':'Image © FabFilter. Official product image; no endorsement implied.','modifications':mods or 'None; original downloaded bytes.','crop_box_original_px':box,'used_on_pages':page,'state_warning':'Press screenshot: Equalize 4 preset, Guitar instance, Natural Phase, High, Analyzer: Pre+Post+SC; not drum/bass settings. Manual analyzer UI says SC; do not relabel it SC/Ext.'})
press='https://www.fabfilter.com/press';zipurl='https://www.fabfilter.com/downloads/press/fabfilter-pro-q.zip'
asset('A01','assets/source/press-kit/FabFilter Pro-Q 4 Screen Shot@2x.jpg',[4],press,zipurl,'editorial_press_basis_scope_unconfirmed')
asset('A02','assets/derived/proq-controls-context.png',[4],press,zipurl,'editorial_press_basis_scope_unconfirmed','Literal crop, no retouching, no recoloring, no text replacement',crop)
asset('A03','assets/derived/proq-band-controls.png',[4],press,zipurl,'editorial_press_basis_scope_unconfirmed','Literal crop, no retouching, no recoloring, no text replacement',crop2)
for name in ['analyzer','analyzersettings']:
 asset('REF_'+name,'assets/source/'+name+'.jpg',[],'https://www.fabfilter.com/help/pro-q/using/analyzer','https://www.fabfilter.com/help_pages/pro-q/images/'+name+'@2x.jpg','unknown_reference_only')
j('assets.json',{'publication_blocker':'Third-party image publishing scope requires decision or permission. Diagrams are original and cleared. Do not silently replace a required object photograph with fake UI.','assets':assets})
print('Wrote content, sources and image manifest. Original image',im.size,'crop',crop)