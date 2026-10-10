# 独立设计方案：人声效果返回的 M/S EQ

## 设计依据
已阅读完整文章、逐页故事、术语表、事实、来源和素材清单，并目视检查 V3 最终手机预览、官方 Pro-Q 4 原图／裁切及解释素材。首要基准为已批准 V3，非新模板。
维持白／浅灰、深色正文、克制蓝、Noto Sans SC 400/600。正文36–40px，标题58–60px，无超大字、无大色块。克制细节只用于阅读：细运行线、统一数字对齐、图表线宽、少量浅灰分组。
Guizang cf4b810 仅补充 expression-first、每页单一解释任务、手机 QA；不采用其巨型字号、Swiss/Editorial强制字体或机械密度评分。
所有坐标为1080×1440像素，文字左上角为行框；左右安全线72/1008。production_spec.json 内含逐项文案、图形、坐标与样式，为执行依据。
## 全套叙事与页间节奏
不复制单一模板：封面插画 → 诊断／关系 → 路由／数学 → 官方对象 → 定量解释 → 验收。文字围绕图解删繁就简，扩展语境保留原完整文章。
## 素材与权属
官方原色、原比例、不改UI文字、不修选中状态。FabFilter 图片仍为有待核实公开发布范围的教学审阅草稿；必须携带原 assets.json/source 信息。封面 AI 图有紧邻可见标识，不能称为声场测量、真实产品或器材实拍。解释图按数据重排成页面元素，不把960×620整张含字SVG缩小。

## 第 01 页 · 人声一加空间，中频就糊了？
解释任务：Open with the audible problem; return diagnosis before Side treatment.
构图：concept-cover
底色：#ffffff
重点载体与文案坐标：
- series：人声空间 · M/S EQ；28px / 行高38；框[72, 48, 770, 40]
- page：01 / 07；28px / 行高38；框[884, 48, 124, 40]
- title：人声一加空间， / 中频就糊了？；60px / 行高76；框[72, 124, 936, 160]
- dek：先查效果返回，再决定要不要收窄。；38px / 行高54；框[72, 304, 936, 64]
- 图像 ai-vocal：../shared_concept_art/vocal_stereo_ai_concept.png；框[162, 398, 756, 504]；contain，原比例、无重绘。
- art-label：AI 概念插画 · 不是声场测量；28px / 行高38；框[72, 918, 936, 44]
- lead：静音 Reverb / Delay 返回后， / 臃肿感明显减轻？先从湿声查起。；38px / 行高54；框[72, 1000, 936, 108]
- takeaway：“臃肿”不等于“宽度过大”。；40px / 行高56；框[72, 1192, 936, 60]
- condition：只有多余中频主要在 Side，才考虑收一点。；32px / 行高46；框[72, 1274, 936, 58]
- source_footer：诊断为试听建议 · 机制与操作见后页；26px / 行高32；框[72, 1386, 936, 36]
验收：主标题→主体图／分支→操作或限制→来源顺序明确；所有单位、箭头和限制语在360px预览可读。

## 第 02 页 · 先分清：多了，还是宽了？
解释任务：A simple level test precedes a conditional three-way decision.
构图：diagnostic-ladder
底色：#ffffff
重点载体与文案坐标：
- series：人声空间 · M/S EQ；28px / 行高38；框[72, 48, 770, 40]
- page：02 / 07；28px / 行高38；框[884, 48, 124, 40]
- title：先分清：多了，还是宽了？；58px / 行高76；框[72, 124, 936, 82]
- lead：先静音／恢复 Return，再降低返回电平。 / 已经清楚，就不必强行加入 M/S。；38px / 行高54；框[72, 230, 936, 112]
- section：仍然偏厚？用 Mid / Side 辅助定位；38px / 行高54；框[72, 402, 936, 60]
- hear0：Mid 和 Side 都厚；36px / 行高50；框[72, 506, 420, 112]
- try0：先试 Stereo EQ / 或减少湿声；36px / 行高50；框[592, 506, 416, 116]
- hear1：主要是 Mid 厚；36px / 行高50；框[72, 722, 420, 112]
- try1：检查湿声 Mid / 与干声的叠加；36px / 行高50；框[592, 722, 416, 116]
- hear2：Side 中频铺得太满；36px / 行高50；框[72, 938, 420, 112]
- try2：再试 Side / 频段衰减；36px / 行高50；框[592, 938, 416, 116]
- takeaway：Solo 只帮助定位，决定要回到整段混音。；36px / 行高52；框[72, 1198, 936, 64]
- caveat：Pro-Q 的 Band Solo 不等于全频 Mid / Side Solo。；28px / 行高40；框[72, 1280, 936, 82]
- source_footer：试听诊断 · FabFilter Pro-Q 4 Help：Solo；26px / 行高32；框[72, 1386, 936, 36]
参考机制资产：assets/svg/diagnosis.svg；实际用本spec最终坐标重建。
验收：主标题→主体图／分支→操作或限制→来源顺序明确；所有单位、箭头和限制语在360px预览可读。

## 第 03 页 · EQ 放在效果器之后
解释任务：Dry bypasses the effect branch; EQ follows the generated stereo wet signal.
构图：parallel-routing
底色：#ffffff
重点载体与文案坐标：
- series：人声空间 · M/S EQ；28px / 行高38；框[72, 48, 770, 40]
- page：03 / 07；28px / 行高38；框[884, 48, 124, 40]
- title：EQ 放在效果器之后；58px / 行高76；框[72, 124, 936, 82]
- lead：干声直达混音；只处理生成后的湿声。；38px / 行高54；框[72, 230, 936, 64]
- diagram-label：常规并行效果链 · 信号流示意；30px / 行高42；框[72, 346, 936, 46]
- vocal：人声轨；36px / 行高50；框[92, 448, 220, 52]
- vocal-sub：Dry 直达；30px / 行高42；框[92, 502, 220, 90]
- mix：混音汇合；36px / 行高50；框[756, 448, 232, 52]
- send-label：Send；32px / 行高44；框[72, 604, 160, 44]
- fx：Reverb / Delay；36px / 行高50；框[320, 632, 368, 52]
- fx-sub：100% Wet；30px / 行高42；框[320, 686, 368, 90]
- eq：M/S EQ；36px / 行高50；框[320, 882, 368, 52]
- eq-sub：只处理目标 Side 频段；30px / 行高42；框[320, 936, 368, 90]
- return-label：Return；32px / 行高44；框[744, 976, 250, 48]
- one：放在效果器前的 EQ， / 不保证等价于处理最终湿声。；36px / 行高50；框[72, 1070, 936, 108]
- caveat：共享 Return 会一起改变其他声源。 / 需要只改人声时，使用独立返回。；30px / 行高42；框[72, 1230, 936, 96]
- source_footer：路由：Ableton Live 12 Manual · 常规并行 Wet 100%；26px / 行高32；框[72, 1386, 936, 36]
参考机制资产：assets/svg/routing.svg；实际用本spec最终坐标重建。
验收：主标题→主体图／分支→操作或限制→来源顺序明确；所有单位、箭头和限制语在360px预览可读。

## 第 04 页 · Side 不是“两边的乐器”
解释任务：Demystify M/S with two matched formula lanes and a single affected branch.
构图：matrix-parallel-lanes
底色：#ffffff
重点载体与文案坐标：
- series：人声空间 · M/S EQ；28px / 行高38；框[72, 48, 770, 40]
- page：04 / 07；28px / 行高38；框[884, 48, 124, 40]
- title：Side 不是“两边的乐器”；58px / 行高76；框[72, 124, 936, 82]
- lead：Mid 是左右的和，Side 是左右的差。；38px / 行高54；框[72, 230, 936, 60]
- m-label：MID · 和信号；36px / 行高50；框[72, 354, 444, 54]
- s-label：SIDE · 差信号；36px / 行高50；框[564, 354, 444, 54]
- m-encode：M = (L + R) / 2；38px / 行高54；框[72, 446, 444, 64]
- s-encode：S = (L − R) / 2；38px / 行高54；框[564, 446, 444, 64]
- m-hold：Mid 保持不变；36px / 行高50；框[92, 690, 404, 52]
- s-eq：只处理 Side；36px / 行高50；框[584, 690, 404, 52]
- s-eq-sub：目标频段衰减；30px / 行高42；框[584, 744, 404, 90]
- decode-label：重新解码；30px / 行高42；框[72, 870, 936, 46]
- decode-l：L′ = M + S′；40px / 行高56；框[72, 938, 444, 64]
- decode-r：R′ = M − S′；40px / 行高56；框[564, 938, 444, 64]
- takeaway：减少该段左右差分，常可让这一段更收拢。 / 不代表提取或单独处理“两侧的乐器”。；36px / 行高50；框[72, 1100, 936, 110]
- caveat：本文用 1/2 编码约定，并非插件内部缩放声明。 / 实际听感还取决于原始 M/S 比例、相位与素材。；28px / 行高40；框[72, 1270, 936, 92]
- source_footer：M/S 定义参考 Voxengo MSED · 公式为教学约定；26px / 行高32；框[72, 1386, 936, 36]
参考机制资产：assets/svg/matrix.svg；实际用本spec最终坐标重建。
验收：主标题→主体图／分支→操作或限制→来源顺序明确；所有单位、箭头和限制语在360px预览可读。

## 第 05 页 · Pro-Q 4：选中这个 Side
解释任务：Identify the real product and exact menu option without pretending the official image is configured.
构图：official-object-and-target
底色：#ffffff
重点载体与文案坐标：
- series：人声空间 · M/S EQ；28px / 行高38；框[72, 48, 770, 40]
- page：05 / 07；28px / 行高38；框[884, 48, 124, 40]
- title：Pro-Q 4：选中这个 Side；58px / 行高76；框[72, 124, 936, 82]
- lead：在立体声 Return 建立 Bell， / 打开频段右侧的 stereo placement 菜单。；36px / 行高50；框[72, 226, 936, 112]
- 图像 pro-q-4-official-full.jpg：assets/source/pro-q-4-official-full.jpg；框[72, 366, 400, 240.2]；contain，原比例、无重绘。
- full-caption：FabFilter Pro-Q 4 / 官方示例界面；32px / 行高46；框[514, 398, 494, 96]
- full-caveat：原图参数、频谱不是 / 推荐设置或本文实测。；28px / 行高40；框[514, 514, 494, 88]
- 图像 pro-q-4-controls-crop.png：assets/derived/pro-q-4-controls-crop.png；框[72, 658, 936, 253.25]；contain，原比例、无重绘。
- controls-caption：频段控制区：FREQ · GAIN · Q · stereo placement；28px / 行高40；框[72, 932, 936, 46]
- 图像 stereo-options.jpg：assets/source/stereo-options.jpg；框[72, 990, 234, 360]；contain，原比例、无重绘。
- side-choice：这里选择 Side；38px / 行高54；框[354, 1024, 654, 60]
- menu-caveat：图中当前选中 Right； / 箭头仅定位 Side，未显示已设置。；28px / 行高40；框[354, 1106, 654, 90]
- scope：这是单频段范围， / 不是整条返回的全频 Width。；32px / 行高46；框[354, 1218, 654, 94]
- mono：Mono 实例没有这些立体声选项。；26px / 行高36；框[354, 1320, 654, 42]
- source_footer：© FabFilter · 官方 Press Area / Pro-Q 4 Help；26px / 行高32；框[72, 1386, 936, 36]
Menu native234×360 placed234×360 at72,990. Side label center native y231 maps1221; end arrow at300,1220, near right menu edge306. Pointer must not obscure Side text or selected Right dot.
At360px preview product full only identifies object; controls and external labels carry detail. The external Side label and adjacent state disclaimer must remain readable; preserve the original menu, do not redraw UI.
验收：主标题→主体图／分支→操作或限制→来源顺序明确；所有单位、箭头和限制语在360px预览可读。

## 第 06 页 · 先小幅削，不要一刀切
解释任务：Separate an audition recipe from a different, explicitly independent mathematical example.
构图：settings-and-amplitude
底色：#ffffff
重点载体与文案坐标：
- series：人声空间 · M/S EQ；28px / 行高38；框[72, 48, 770, 40]
- page：06 / 07；28px / 行高38；框[884, 48, 124, 40]
- title：先小幅削，不要一刀切；58px / 行高76；框[72, 124, 936, 82]
- lead：试听起点，不是官方推荐或最佳值。；36px / 行高50；框[72, 230, 936, 60]
- recipe-label：Side · Bell；38px / 行高54；框[104, 366, 872, 58]
- recipe-numbers：400 Hz     −2 dB     Q 1.0；42px / 行高58；框[104, 442, 872, 70]
- search：按素材移动频点、改变带宽与衰减量。；36px / 行高50；框[72, 578, 936, 58]
- calc-title：另一个计算例：Side 衰减 −3 dB；36px / 行高50；框[72, 716, 936, 60]
- bar-label0：Mid 保持；32px / 行高46；框[72, 822, 244, 60]
- pct0：100.0%；32px / 行高46；框[886, 822, 122, 55]
- bar-label1：Side 处理前；32px / 行高46；框[72, 932, 244, 60]
- pct1：100.0%；32px / 行高46；框[886, 932, 122, 55]
- bar-label2：Side 处理后；32px / 行高46；框[72, 1042, 244, 60]
- pct2：70.8%；32px / 行高46；框[886, 1042, 122, 55]
- scale：各条以自身处理前幅度为 100%；共用幅度尺度。；28px / 行高40；框[72, 1156, 936, 48]
- caveat：10^(−3/20) ≈ 0.708；这是幅度，不是宽度。 / 此 −3 dB 计算例，与上方 −2 dB 试听设置不同。；28px / 行高40；框[72, 1242, 936, 96]
- source_footer：上方：试听建议 · 下方：独立计算示意，非实测；26px / 行高32；框[72, 1386, 936, 36]
参考机制资产：assets/svg/attenuation.svg；实际用本spec最终坐标重建。
验收：主标题→主体图／分支→操作或限制→来源顺序明确；所有单位、箭头和限制语在360px预览可读。

## 第 07 页 · 收窄之后，还要过三关
解释任务：Finish with practical listening and clarify why unchanged mono does not disprove Side processing.
构图：verification-and-mono-proof
底色：#ffffff
重点载体与文案坐标：
- series：人声空间 · M/S EQ；28px / 行高38；框[72, 48, 770, 40]
- page：07 / 07；28px / 行高38；框[884, 48, 124, 40]
- title：收窄之后，还要过三关；58px / 行高76；框[72, 124, 936, 82]
- check-number0：01；34px / 行高50；框[72, 256, 86, 60]
- check-label0：Stereo；38px / 行高54；框[176, 256, 832, 58]
- check-body0：字头更清楚吗？尾声仍自然吗？ / 没有更好，就撤回。；34px / 行高48；框[176, 326, 832, 104]
- check-number1：02；34px / 行高50；框[72, 478, 86, 60]
- check-label1：Mono；38px / 行高54；框[176, 478, 832, 58]
- check-body1：按 DAW 合并单声道； / 检查音色与平衡，不是只听左声道。；34px / 行高48；框[176, 548, 832, 104]
- check-number2：03；34px / 行高50；框[72, 700, 86, 60]
- check-label2：整段；38px / 行高54；框[176, 700, 832, 58]
- check-body2：主歌、副歌、句尾都复核； / 共享返回上的其他声源也要听。；34px / 行高48；框[176, 770, 832, 104]
- mono-label：为什么 Mono 可能听不出变化？；36px / 行高50；框[72, 964, 936, 60]
- proof：(L′ + R′) / 2 = M；42px / 行高60；框[72, 1040, 936, 66]
- ideal：理想纯 Side EQ 不改 Mid。 / 限无额外增益、非线性或后级变化。；30px / 行高42；框[72, 1136, 936, 92]
- closing：Mono 检查不能单独证明“去糊成功”。；36px / 行高50；框[72, 1284, 936, 58]
- source_footer：数学推导 + 听音验收 · 不构成实测效果承诺；26px / 行高32；框[72, 1386, 936, 36]
参考机制资产：assets/svg/mono-check.svg；实际用本spec最终坐标重建。
验收：主标题→主体图／分支→操作或限制→来源顺序明确；所有单位、箭头和限制语在360px预览可读。

## 编辑取舍
- Linear Phase paragraph remains in full article and sources; omitted from final page to protect the single verification task.
- Detailed Solo and normalization context remains in article; essential limits remain adjacent on pages.

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
## 渲染后修正
第5页 Side 箭头末端由x300移到x310，y1220不变，避免图片层遮住箭头尖端。全部字形与边界检查通过；7页全尺寸与7页360px手机图逐页实读完成。见qa/RENDER_QA.md。
