# 独立设计方案：鼓与 Bass 的音量、时间、频率与层次

## 设计依据
已阅读完整文章、逐页故事、术语表、事实、来源和素材清单，并目视检查 V3 最终手机预览、官方 Pro-Q 4 原图／裁切及解释素材。首要基准为已批准 V3，非新模板。
维持白／浅灰、深色正文、克制蓝、Noto Sans SC 400/600。正文36–40px，标题58–60px，无超大字、无大色块。克制细节只用于阅读：细运行线、统一数字对齐、图表线宽、少量浅灰分组。
Guizang cf4b810 仅补充 expression-first、每页单一解释任务、手机 QA；不采用其巨型字号、Swiss/Editorial强制字体或机械密度评分。
所有坐标为1080×1440像素，文字左上角为行框；左右安全线72/1008。production_spec.json 内含逐项文案、图形、坐标与样式，为执行依据。
## 全套叙事与页间节奏
不复制单一模板：封面插画 → 诊断／关系 → 路由／数学 → 官方对象 → 定量解释 → 验收。文字围绕图解删繁就简，扩展语境保留原完整文章。
## 素材与权属
官方原色、原比例、不改UI文字、不修选中状态。FabFilter 图片仍为有待核实公开发布范围的教学审阅草稿；必须携带原 assets.json/source 信息。封面 AI 图有紧邻可见标识，不能称为声场测量、真实产品或器材实拍。解释图按数据重排成页面元素，不把960×620整张含字SVG缩小。

## 第 01 页 · 鼓与 Bass，先把地基搭稳
解释任务：Introduce instrument relationships with modest concept art and an original rhythm strip.
构图：concept-cover-with-rhythm-strip
底色：#ffffff
重点载体与文案坐标：
- series：鼓与 Bass · 混音基础；28px / 行高38；框[72, 48, 770, 40]
- page：01 / 08；28px / 行高38；框[884, 48, 124, 40]
- title：鼓与 Bass， / 先把地基搭稳；60px / 行高76；框[72, 124, 936, 160]
- dek：先关系，后音色。；40px / 行高56；框[72, 304, 936, 58]
- 图像 ai-kick-bass：../shared_concept_art/kick_bass_ai_concept.png；框[190, 390, 700, 466.67]；contain，原比例、无重绘。
- art-label：AI 概念插画；28px / 行高38；框[72, 866, 936, 42]
- roles：Kick 定落点 · Bass 接延续 · Snare 撑重音；34px / 行高48；框[72, 946, 936, 54]
- path：音量平衡 → 时间与极性 / 频率分工 → 前后层次；38px / 行高54；框[72, 1040, 936, 116]
- action：先只听这三个声部，找到歌曲的重心。；36px / 行高50；框[72, 1230, 936, 58]
- caveat：角色会随编曲改变，不规定固定音量排序。；28px / 行高40；框[72, 1306, 936, 44]
- source_footer：试听工作流 · 参考 iZotope：How to Mix Kick and Bass；26px / 行高32；框[72, 1386, 936, 36]
参考机制资产：assets/diagrams/foundation-timeline.svg；实际用本spec最终坐标重建。
Cover does not include foundation timeline to avoid competing with conceptual hero. The rhythm/role idea is carried in exact role caption; timing diagram source retained in editable asset archive, not forced onto a page.
验收：主标题→主体图／分支→操作或限制→来源顺序明确；所有单位、箭头和限制语在360px预览可读。

## 第 02 页 · 第一步：平衡先过关
解释任务：Relationship by ear first; equal-sine calculation explains why summed peaks must be checked.
构图：listening-sequence-and-headroom-chart
底色：#ffffff
重点载体与文案坐标：
- series：鼓与 Bass · 混音基础；28px / 行高38；框[72, 48, 770, 40]
- page：02 / 08；28px / 行高38；框[884, 48, 124, 40]
- title：第一步：平衡先过关；58px / 行高76；框[72, 124, 936, 82]
- lead：一个推子能解决的事，先不交给 EQ。；38px / 行高54；框[72, 230, 936, 62]
- sequence：Kick 留余量 → 慢慢加入 Bass → 再加 Snare；34px / 行高48；框[72, 344, 936, 60]
- question：同时出现时，落点与音符仍分得清吗？；36px / 行高50；框[72, 424, 936, 56]
- chart-title：叠加后的峰值，需要重新检查；36px / 行高50；框[72, 548, 936, 58]
- math-condition：计算例：两条完全相同、同相正弦；28px / 行高40；框[72, 616, 936, 48]
- tick0：0；28px / 行高40；框[72, 694, 76, 44]
- tick-6：-6；28px / 行高40；框[72, 802, 76, 44]
- tick-12：-12；28px / 行高40；框[72, 910, 76, 44]
- tick-18：-18；28px / 行高40；框[72, 1018, 76, 44]
- bar-value0：−12 dBFS；30px / 行高42；框[190, 870, 212, 48]
- bar-label0：A；32px / 行高44；框[206, 1060, 180, 48]
- bar-value1：−12 dBFS；30px / 行高42；框[458, 870, 212, 48]
- bar-label1：B；32px / 行高44；框[474, 1060, 180, 48]
- bar-value2：−5.98 dBFS；30px / 行高42；框[726, 761.6292, 212, 48]
- bar-label2：A + B；32px / 行高44；框[742, 1060, 180, 48]
- axis-label：Sample Peak / dBFS；28px / 行高38；框[72, 1108, 936, 42]
- calculation：振幅相加：0.251 + 0.251 = 0.502；32px / 行高46；框[72, 1172, 936, 52]
- caveat：本例增加 6.02 dB；任意两件乐器不固定增加此值。 / 检查轨道、处理器、总线；没有通用 Kick 峰值目标。；28px / 行高40；框[72, 1270, 936, 94]
- source_footer：计算示意，非实测 · Ableton Mixing / Shure Recording；26px / 行高32；框[72, 1386, 936, 36]
参考机制资产：assets/diagrams/headroom-sum.svg；实际用本spec最终坐标重建。
验收：主标题→主体图／分支→操作或限制→来源顺序明确；所有单位、箭头和限制语在360px预览可读。

## 第 03 页 · 低频变薄，先分清原因
解释任务：Show that delay has frequency-dependent phase shift; distinguish from polarity inversion.
构图：synchronized-two-frequency-waves
底色：#ffffff
重点载体与文案坐标：
- series：鼓与 Bass · 混音基础；28px / 行高38；框[72, 48, 770, 40]
- page：03 / 08；28px / 行高38；框[884, 48, 124, 40]
- title：低频变薄，先分清原因；58px / 行高76；框[72, 124, 936, 82]
- lead：难辨可能是遮蔽；重叠时低频明显减少， / 再检查极性与时间关系。；36px / 行高50；框[72, 230, 936, 108]
- definition1：Polarity：上下翻转 x(t) → −x(t)；36px / 行高50；框[72, 380, 936, 58]
- definition2：Delay：沿时间移动 x(t) → x(t−5 ms)；34px / 行高48；框[72, 450, 936, 58]
- legend：数学示意：蓝实线 原正弦 · 灰虚线 延后 5 ms；28px / 行高40；框[72, 562, 936, 46]
- freq0：50 Hz；32px / 行高46；框[72, 624, 130, 52]
- deg0：90°；30px / 行高42；框[72, 682, 130, 44]
- freq1：100 Hz；32px / 行高46；框[72, 862, 130, 52]
- deg1：180°；30px / 行高42；框[72, 920, 130, 44]
- time0：0；28px / 行高40；框[202.0, 1060, 56, 42]
- time10：10；28px / 行高40；框[396.5, 1060, 56, 42]
- time20：20；28px / 行高40；框[591.0, 1060, 56, 42]
- time30：30；28px / 行高40；框[785.5, 1060, 56, 42]
- time40：40；28px / 行高40；框[952, 1060, 56, 42]
- axis：共用时间轴 / ms · 振幅归一化；28px / 行高40；框[72, 1120, 936, 44]
- takeaway：一次反相，不等于全曲“相位对齐”。；36px / 行高52；框[72, 1192, 936, 60]
- caveat：实际 Kick / Bass 不是固定正弦。对比多个音符与鼓点； / 别为对齐一个波峰破坏 groove，也要检查尾长与编曲。；28px / 行高38；框[72, 1284, 936, 84]
- source_footer：定义：Shure / Ableton Utility · 角度为独立计算；26px / 行高32；框[72, 1386, 936, 36]
参考机制资产：assets/diagrams/polarity-time.svg；实际用本spec最终坐标重建。
验收：主标题→主体图／分支→操作或限制→来源顺序明确；所有单位、箭头和限制语在360px预览可读。

## 第 04 页 · 频率是线索，不是处方
解释任务：Use the authentic spectrum display as an object, not as drum/bass evidence.
构图：official-analyzer-with-listening-criteria
底色：#ffffff
重点载体与文案坐标：
- series：鼓与 Bass · 混音基础；28px / 行高38；框[72, 48, 770, 40]
- page：04 / 08；28px / 行高38；框[884, 48, 124, 40]
- title：频率是线索，不是处方；58px / 行高76；框[72, 124, 936, 82]
- lead：Kick 的重量不固定在 100 Hz； / 先听共振区域、尾长与击打轮廓。；36px / 行高50；框[72, 230, 936, 108]
- 图像 A01：assets/source/press-kit/FabFilter Pro-Q 4 Screen Shot@2x.jpg；框[72, 378, 936, 562.09]；contain，原比例、无重绘。
- state-caveat：官方示例：Guitar · Equalize 4。 / 曲线不是鼓／Bass 设置，频谱也不是本文实测。；28px / 行高40；框[72, 954, 936, 84]
- analyzer：Analyzer 帮助定位，频谱重叠不能单凭 / 画面判成遮蔽或相消。；36px / 行高50；框[72, 1080, 936, 108]
- notes：Bass 会换音：E1 ≈ 41.20 Hz · A1 = 55 Hz。 / 固定削减对一个音有效，也可能伤到另一个音。；30px / 行高42；框[72, 1230, 936, 88]
- tuning：A4 = 440 Hz · 十二平均律 · 中央 C 记为 C4；26px / 行高36；框[72, 1330, 936, 40]
- source_footer：© FabFilter · Pro-Q 4 Help：Analyzer / Piano display；26px / 行高32；框[72, 1386, 936, 36]
Official full image kept intact at936px wide; no invented highlighted curve and no claim about a selected frequency. Do not require tiny on-screen labels to teach the point.
Optional detailed Bell starting point 800Hz–2kHz, −1 to−2dB stays in full manuscript/caption; do not squeeze it into this page.
验收：主标题→主体图／分支→操作或限制→来源顺序明确；所有单位、箭头和限制语在360px预览可读。

## 第 05 页 · 让 Bass 在小音箱也有形
解释任务：Explain harmonics with a real numeric axis, then link to small-speaker listening.
构图：harmonic-ladder-and-layer-guidance
底色：#ffffff
重点载体与文案坐标：
- series：鼓与 Bass · 混音基础；28px / 行高38；框[72, 48, 770, 40]
- page：05 / 08；28px / 行高38；框[884, 48, 124, 40]
- title：让 Bass 在小音箱也有形；58px / 行高76；框[72, 124, 936, 82]
- lead：低频负责重量，谐波帮助辨认音高与轮廓。；36px / 行高50；框[72, 230, 936, 60]
- chart-label：A1 = 55 Hz · 前 4 阶谐波；36px / 行高50；框[72, 348, 936, 54]
- axis-y：相对振幅（人为设定）；28px / 行高40；框[72, 424, 936, 44]
- tick50：50；28px / 行高40；框[102.0, 840, 84, 46]
- tick100：100；28px / 行高40；框[436.24082545064397, 840, 84, 46]
- tick200：200；28px / 行高40；框[770.4816509012879, 840, 84, 46]
- tick300：300；28px / 行高40；框[924, 840, 84, 46]
- hz0：55 Hz；30px / 行高42；框[124.9592912805505, 460, 130, 48]
- order0：1 阶；30px / 行高42；框[139.9592912805505, 904, 100, 48]
- hz1：110 Hz；30px / 行高42；框[459.2001167311945, 562.0, 130, 48]
- order1：2 阶；30px / 行高42；框[474.2001167311945, 904, 100, 48]
- hz2：165 Hz；30px / 行高42；框[654.7184658299064, 634.0, 130, 48]
- order2：3 阶；30px / 行高42；框[669.7184658299064, 904, 100, 48]
- hz3：220 Hz；30px / 行高42；框[793.4409421818384, 673.0, 130, 48]
- order3：4 阶；30px / 行高42；框[808.4409421818384, 904, 100, 48]
- log-axis：横轴：对数频率 / Hz；28px / 行高40；框[72, 966, 936, 44]
- listen：换音时，基频与谐波一起移动。 / 听不清 Bass，别只继续推最底下。；36px / 行高50；框[72, 1042, 936, 108]
- layer：独立高频层先匹配起音与时值，再小声加入； / 用实际小音箱与全频监听来回检查。；32px / 行高46；框[72, 1188, 936, 96]
- caveat：非实测频谱；不保证任意小音箱可重放图中频率。；28px / 行高40；框[72, 1320, 936, 44]
- source_footer：谐波：FabFilter One Help · 聆听建议：iZotope low end；26px / 行高32；框[72, 1386, 936, 36]
参考机制资产：assets/diagrams/harmonic-ladder.svg；实际用本spec最终坐标重建。
验收：主标题→主体图／分支→操作或限制→来源顺序明确；所有单位、箭头和限制语在360px预览可读。

## 第 06 页 · Snare：本体与空间分开管
解释任务：Separate dry body from reverb return so tone and space can be adjusted independently.
构图：split-routing-with-frequency-search
底色：#ffffff
重点载体与文案坐标：
- series：鼓与 Bass · 混音基础；28px / 行高38；框[72, 48, 770, 40]
- page：06 / 08；28px / 行高38；框[884, 48, 124, 40]
- title：Snare：本体与空间分开管；58px / 行高76；框[72, 124, 936, 82]
- lead：先让本体站住，再决定空间需要多少。；38px / 行高54；框[72, 230, 936, 60]
- diagram-caption：常规并行 Reverb · 信号流示意；30px / 行高42；框[72, 350, 936, 46]
- snare：Snare；36px / 行高50；框[92, 470, 200, 52]
- dry：Dry 主路；36px / 行高50；框[428, 470, 240, 52]
- mix：鼓组／混音；36px / 行高50；框[804, 470, 184, 52]
- sendlabel：Send；32px / 行高44；框[72, 628, 180, 46]
- reverb：Reverb；36px / 行高50；框[324, 690, 282, 52]
- reverb-sub：100% Wet；30px / 行高42；框[324, 744, 282, 90]
- return：Return EQ；36px / 行高50；框[734, 690, 254, 52]
- body-label：本体；36px / 行高50；框[72, 904, 176, 54]
- body-search：约 300 Hz：搜索厚度 / 约 1 kHz 显硬／共振：再局部试削；34px / 行高48；框[278, 900, 730, 100]
- space-label：空间；36px / 行高50；框[72, 1070, 176, 54]
- space-search：先少送一点，或缩短尾声； / 再听 Return 的 2–3 kHz 是否拥挤。；34px / 行高48；框[278, 1066, 730, 100]
- caveat：以上是试听起点，并非所有 Snare 都要 Reverb。 / 抬 10 kHz 不能等价补回削去的击打清晰度。；28px / 行高40；框[72, 1262, 936, 96]
- source_footer：iZotope：How to EQ Drums · FabFilter Learn：Reverb；26px / 行高32；框[72, 1386, 936, 36]
参考机制资产：assets/diagrams/snare-routing.svg；实际用本spec最终坐标重建。
验收：主标题→主体图／分支→操作或限制→来源顺序明确；所有单位、箭头和限制语在360px预览可读。

## 第 07 页 · 亮，不必每一下都扎耳
解释任务：A fader-first fork chooses static versus dynamic response based on time behavior.
构图：conditional-decision-fork
底色：#ffffff
重点载体与文案坐标：
- series：鼓与 Bass · 混音基础；28px / 行高38；框[72, 48, 770, 40]
- page：07 / 08；28px / 行高38；框[884, 48, 124, 40]
- title：亮，不必每一下都扎耳；58px / 行高76；框[72, 124, 936, 82]
- lead：Hi-hat / Cymbal 先收一点推子， / 再听节奏是否仍然连贯。；38px / 行高54；框[72, 230, 936, 108]
- listen-question：刺耳是偶尔出现，还是持续整段？；38px / 行高54；框[72, 408, 936, 62]
- leftcase：整段太亮；38px / 行高54；框[72, 602, 444, 62]
- rightcase：只有重击刺耳；38px / 行高54；框[564, 602, 444, 62]
- leftaction：再考虑静态 EQ；36px / 行高50；框[72, 700, 444, 60]
- rightaction：可试 Dynamic EQ；36px / 行高50；框[564, 700, 444, 60]
- freq-note：5–8 kHz 只是可能的搜索区，先听出问题再处理。；30px / 行高42；框[72, 814, 936, 52]
- perc-title：大打击乐：体积也要服务高潮；38px / 行高54；框[72, 954, 936, 60]
- perc-copy：检查 1–3 kHz 的硬度、尾长与进入时机， / 别用无限加低频换气势。；36px / 行高50；框[72, 1046, 936, 108]
- takeaway：和人声、Snare 一起听，保留需要的身体感。；34px / 行高48；框[72, 1226, 936, 58]
- caveat：不设固定削减频率；避免高通过头后只剩尖锐边缘。；28px / 行高40；框[72, 1320, 936, 44]
- source_footer：条件性试听建议 · iZotope：How to EQ Drums；26px / 行高32；框[72, 1386, 936, 36]
参考机制资产：assets/diagrams/role-hierarchy.svg；实际用本spec最终坐标重建。
验收：主标题→主体图／分支→操作或限制→来源顺序明确；所有单位、箭头和限制语在360px预览可读。

## 第 08 页 · 最后，用一段音乐验收
解释任务：A spacious annotated checklist closes the workflow without invented measurements.
构图：four-stage-listening-scorecard
底色：#ffffff
重点载体与文案坐标：
- series：鼓与 Bass · 混音基础；28px / 行高38；框[72, 48, 770, 40]
- page：08 / 08；28px / 行高38；框[884, 48, 124, 40]
- title：最后，用一段音乐验收；58px / 行高76；框[72, 124, 936, 82]
- lead：整段通过，比某一击“巨大”更重要。；38px / 行高54；框[72, 230, 936, 62]
- number0：01；34px / 行高50；框[72, 350, 90, 60]
- label0：低音量；38px / 行高54；框[192, 350, 816, 58]
- body0：Kick 落点、Bass 音符、Snare 重音， / 都能跟住吗？；34px / 行高48；框[192, 418, 816, 100]
- number1：02；34px / 行高50；框[72, 554, 90, 60]
- label1：Mono；38px / 行高54；框[192, 554, 816, 58]
- body1：合并单声道后，低频与高频 Bass 层 / 有没有异常变薄？；34px / 行高48；框[192, 622, 816, 100]
- number2：03；34px / 行高50；框[72, 758, 90, 60]
- label2：换段落、换音符；38px / 行高54；框[192, 758, 816, 58]
- body2：主歌与高潮都稳定吗？ / 镲片有没有盖过主角？；34px / 行高48；框[192, 826, 816, 100]
- number3：04；34px / 行高50；框[72, 962, 90, 60]
- label3：匹配响度旁通；38px / 行高54；框[192, 962, 816, 58]
- body3：关系更清楚，还是只是更响？ / 最后再检查输出余量。；34px / 行高48；框[192, 1030, 816, 100]
- closing：一次只解决一个已听到的问题。；38px / 行高54；框[72, 1236, 936, 62]
- caveat：数值只用于解释与起步试听；本套没有工程音频实测。；28px / 行高40；框[72, 1324, 936, 44]
- source_footer：整段复核 · 参考 Ableton / FabFilter / iZotope；26px / 行高32；框[72, 1386, 936, 36]
参考机制资产：assets/diagrams/verification-path.svg；实际用本spec最终坐标重建。
验收：主标题→主体图／分支→操作或限制→来源顺序明确；所有单位、箭头和限制语在360px预览可读。

## 编辑取舍
- Optional Kick harshness Bell recipe stays in manuscript, not the already image-dominant page4.
- Bass 800Hz–2.5kHz search suggestion stays in manuscript; page5 prioritizes harmonic mechanism and actual speaker check.
- foundation timeline retained as editable research diagram but not rendered on cover; relationship caption carries its key point.

## 渲染器的 QA 与停止条件
- Render and inspect every full-size page and every 360px preview; do not rely on contact sheet alone.
- Essential labels ≥30px; body normally36–40px; limitations28px; no font shrinking to fix overflow.
- No text/images beyond x72–1008 except nonessential image breathing; footer bottom≤1420.
- Source-image caveat adjacent, not only footer. Preserve selected menu state and original colors/aspect ratio.
- Rebuild explanation diagrams at final coordinates. Never scale complete 960×620 SVG including its text into a small box.
- Use original data and formulas; same axes/scales for comparisons; state mathematical idealization adjacent.
- Check Chinese line endings, minus signs, primes, arrows, degree symbols, frequency units, product names against term-map.
- If layout requires change, preserve claim+caveat together; move optional detail to caption, not smaller type.
- 这是独立设计阶段，没有渲染最终成品，也没有宣称通过手机实读。渲染器发现空间或字体指标问题应重排局部，记录变化并重新导出受影响页面。
- 对纯图形可调位置改善对齐；不能静默改数值、删条件、改原图状态或将数据示意声称为实测。
- 所有标题、标签、图注、SVG、发布正文二次对照term-map。没有缺字、截断、重叠或错指的控件；PNG、PDF、手机预览一致后方可交付。