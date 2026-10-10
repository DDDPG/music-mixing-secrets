# 混音术语表

版本 1.0.0 · 56 条 · 官方资料核验日期 2026-10-09

为混音教学、社交卡片和普通讨论提供专业英文标签与准确中文说明。

## 使用原则

1. 术语标签优先使用准确的专业英文；中文用于解释含义，不禁止普通讨论中准确的中文表达。
2. 插件名、模块名、按钮和旋钮按对应产品及版本的原始英文 UI 写法引用；中文说明另列，不编造界面标签。
3. Delay 保留为 Delay，可解释为延时，不把正式标签翻成回声；Echo 的听感描述和产品名按上下文分别处理。
4. 同一英文词可能随上下文改变含义。先确认处理对象、信号取样点、模式、单位、路由与产品版本，再解释参数。
5. 资料优先顺序：当前实际 UI 与该版本官方手册、官方标准、厂商技术教程。术语表是基线，不覆盖产品特有定义。
6. 正文可以通俗，但不能省掉改变结论的条件；推荐值必须写成起点或例子，不写成跨产品或跨素材的固定规则。
7. 数值保留单位、正负号和模式：ms、s、Hz、kHz、dB、dB/oct、dBFS、dBTP、LUFS、%、ratio、音符分值不可混换。

## 渲染前术语校对

- 从稿件提取标题、图注、模块名和参数名，对照 term ID 与 preferred_label；不机械替换正文中的准确中文解释。
- 建立产品语境：产品、版本、模式、原 UI 拼写、参数单位、信号路径、对应官方说明页。未核对时不画成真实界面。
- 逐项检查易混组：Delay/Echo/Reverb；Feedback/Delay Time/Wet；Insert/Send/Return/Bus；Pan/Balance/Width；Phase/Polarity；HPF/LPF；Compression/Limiter；Peak/True Peak/RMS/Loudness。
- 核对公式、比例、时间单位、滤波方向、路由箭头与参数解释；示例必须注明假设和适用条件。
- 锁定已经核对的文字层再渲染。文案变更后重做术语检查；来源无法验证的断言删除或明确保留意见。

## 渲染后术语校对

- 逐页对照锁定稿与实际导出图，检查完整英文拼写、大小写、符号、数值、单位及中文是否漏字、错字或被截断。
- 把 OCR 作为辅助，与人工逐项核对结合；重点检查 Ø、−、:、%、dBFS/dBTP、LUFS、1/4 和 1/8 等易错字符。
- 看图中位置与连线是否改变原意：参数对应的处理器、反馈回路、发送取样点、干湿支路、左右声道和 M/S 标签必须一致。
- 正式标签若把 Delay 换成回声、HPF/LPF 方向颠倒、Phase/Polarity 混用或单位变化，直接退回修改；不以版面好看放行。
- 最终缩略图和原尺寸都要看；改字、换字体、移动参数或重新生成图后，再查该页并回归相关页。

## 产品语义示例

- **Ableton Live 12 Delay / Echo**：Delay 与 Echo 是不同设备名称；Echo 是 modulation delay，不能仅按中文听感改名。（S01）
- **FabFilter Pro-C 3**：Wet Gain 指压缩后的补偿增益；Dry Gain 可加入未压缩输入；这不是 Reverb 湿声。（S13）
- **Logic Pro Gain 10.7**：界面写 Phase Invert；教学解释注明此控件执行极性反转，保留 UI 原文。（S04、S24）
- **FabFilter Pro-Q 4**：Low Cut 对应 HPF、High Cut 对应 LPF；Q 数值定义不能直接套到其他 EQ。（S09）
- **FabFilter Pro-L 2**：True Peak Metering 负责测量；True Peak Limiting 负责限幅，是不同功能。（S26、S27）
- **FabFilter Pro-R 2 / ChromaVerb**：Space、Decay Rate、Decay、Predelay 的对象与刻度分别查手册，不能按词面互换。（S19、S20）

## 词条


### 信号与路由

#### 01 Signal Flow
- ID：signal_flow
- 中文解释标签：信号流
- 准确含义：音频从输入，经处理、分支和汇合，到输出所经过的路径与顺序。
- 避免：不要把插件列表的视觉位置当成完整路由；并行支路和取样点也要核对。
- 来源：S03

#### 02 Gain
- ID：gain
- 中文解释标签：增益
- 准确含义：对信号电平施加的放大或衰减量，常用 dB 表示。
- 避免：不是固定等于录音输入音量，也不是主观响度本身。
- 语境：先说明 Input、Output、Clip 或某个处理阶段。
- 来源：S04

#### 03 Gain Staging
- ID：gain_staging
- 中文解释标签：增益分配
- 准确含义：协调信号链各级电平，兼顾余量、噪声与处理器的工作范围。
- 避免：不要规定所有轨道必须达到同一个 dBFS 数值，也不要只看总线表头。
- 来源：S06

#### 04 Headroom
- ID：headroom
- 中文解释标签：余量
- 准确含义：给信号峰值或电平增长留下的空间；必须说明相对于哪个工作电平、上限或处理阶段。
- 避免：不等于 Crest Factor，也没有适用于所有交付的固定余量。
- 语境：模拟系统常以名义电平到过载点定义；混音交付也常说当前峰值到上限的剩余空间。
- 来源：S07

#### 05 Fader
- ID：fader
- 中文解释标签：推子
- 准确含义：控制相应通道某个位置的信号电平，常用于混音平衡。
- 避免：不要默认推子会改变其前级插件的输入电平。
- 来源：S02、S03

#### 06 Pan
- ID：pan
- 中文解释标签：声像
- 准确含义：在立体声场中定位信号；实际控制方式取决于单声道、立体声及 Pan 模式。
- 避免：不等于 Stereo Width；立体声轨上的 Pan 不一定是两个声道共同平移。
- 语境：核对 Mono Pan、Balance、Dual/Split Stereo Pan，以及 Pan Law。
- 来源：S02

#### 07 Stereo Balance
- ID：stereo_balance
- 中文解释标签：左右平衡
- 准确含义：改变已有左右声道的相对电平。
- 避免：不要默认它会把左声道内容移动到右声道，或能替代双声道独立 Pan。
- 语境：具体增益曲线与 Pan Law 依产品。
- 检索别名：Balance（不是无条件替换规则）
- 来源：S04

#### 08 Insert
- ID：insert
- 中文解释标签：插入处理
- 准确含义：把处理器放入某条通道的信号路径，典型为串联：上一处理器的输出进入下一处理器。
- 避免：Insert 不是「只能处理干声」；插件内部也可带 Dry/Wet 或并行路径。
- 来源：S05

#### 09 Send
- ID：send
- 中文解释标签：发送
- 准确含义：把某取样点的信号按指定电平送到另一目的地，常用于并行效果或监听。
- 避免：Send 不是效果器本身；也不天然等于 Wet 比例。
- 来源：S02

#### 10 Return / Aux
- ID：return_aux
- 中文解释标签：返回或辅助通道
- 准确含义：接收发送或总线信号、进行处理并输出的通道，常用于共享效果或子混音。
- 避免：不要把 Return、Aux、Bus 当成所有软件中完全相同的对象。
- 语境：名称、可用输入与通道类型依 DAW。
- 来源：S02、S03

#### 11 Bus
- ID：bus
- 中文解释标签：总线
- 准确含义：承载并可汇合一路或多路信号的路由通道，用于子混音、发送、输出等。
- 避免：总线不必是 Master/Main，也不必装效果器。
- 来源：S03

#### 12 Pre-Fader / Post-Fader
- ID：pre_post_fader
- 中文解释标签：推子前或推子后
- 准确含义：描述发送信号在通道推子之前还是之后取出；Post-Fader 通常跟随该推子的变化。
- 避免：Pre-Fader 不自动等于 Pre-FX；是否跟随 Mute、Pan 要查该产品。
- 来源：S02、S03

#### 13 Automation
- ID：automation
- 中文解释标签：自动化
- 准确含义：保存并回放随时间变化的参数值，如电平、声像或效果参数。
- 避免：不是自动混音，也不是只能控制音量。
- 来源：S08


### 均衡与滤波

#### 14 EQ
- ID：eq
- 中文解释标签：均衡
- 准确含义：通过提升或衰减特定频段来调整频率平衡。
- 避免：不是把所有频段调成一样大；均衡曲线平直也不代表频谱必然平直。
- 检索别名：Equalization（不是无条件替换规则）
- 来源：S10

#### 15 Frequency
- ID：frequency
- 中文解释标签：频率
- 准确含义：每秒振动周期数，以 Hz 或 kHz 表示；EQ 中还需区分中心频率与截止频率。
- 避免：不要把频率、音高和电平写成同一个量。
- 检索别名：Freq（不是无条件替换规则）
- 来源：S10、S09

#### 16 High-Pass Filter (HPF)
- ID：hpf
- 中文解释标签：高通或低切
- 准确含义：主要让较高频率通过，衰减截止频率以下的成分。
- 避免：高通不是削高频；截止点以下通常是渐进衰减，不是一律完全消失。
- 检索别名：High Pass、HPF、Low Cut（不是无条件替换规则）
- 来源：S10

#### 17 Low-Pass Filter (LPF)
- ID：lpf
- 中文解释标签：低通或高切
- 准确含义：主要让较低频率通过，衰减截止频率以上的成分。
- 避免：低通不是削低频；不要把 High Cut 错认成 High Shelf。
- 检索别名：Low Pass、LPF、High Cut（不是无条件替换规则）
- 来源：S10

#### 18 Bell
- ID：bell
- 中文解释标签：钟形均衡
- 准确含义：围绕一个中心频率提升或衰减，影响范围由带宽等参数决定。
- 避免：不是只改变单个频率点，也不是 Shelf。
- 检索别名：Peak EQ、Peaking EQ（不是无条件替换规则）
- 来源：S09

#### 19 Shelf
- ID：shelf
- 中文解释标签：搁架均衡
- 准确含义：Low Shelf 调整低频一侧，High Shelf 调整高频一侧；远离过渡区后响应趋向设定增益。
- 避免：Shelf 衰减不等于 High/Low-Pass 的持续滚降。
- 检索别名：Low Shelf、High Shelf（不是无条件替换规则）
- 来源：S10

#### 20 Q / Bandwidth
- ID：q_bandwidth
- 中文解释标签：品质因数与带宽
- 准确含义：Bell 中通常 Q 越高，作用频段越窄；Bandwidth 表示受影响频段的宽度。
- 避免：Q 与带宽不是同一数值；不同 EQ 的 Q 刻度和滤波类型未必可直接照搬。
- 语境：Shelf 和截止滤波器的 Q 还可能改变共振或过渡形状。
- 来源：S09

#### 21 Slope
- ID：slope
- 中文解释标签：滤波斜率
- 准确含义：表示滤波响应变化的陡峭程度，常用 dB/oct，即每倍频程变化多少 dB。
- 避免：不是截止频率，也不是所有频率都以同一数值衰减。
- 来源：S09

#### 22 Resonance
- ID：resonance
- 中文解释标签：共振
- 准确含义：滤波器语境中指截止频率附近的共振强调或振铃特征。
- 避免：不等于回声、整体音量或必然的刺耳感。
- 语境：高 Resonance 能否自激、是否补偿电平，依电路或算法。
- 来源：S11


### 动态处理

#### 23 Compression
- ID：compression
- 中文解释标签：动态压缩
- 准确含义：常见向下压缩按检测信号降低较强部分的增益，以改变动态范围与包络。
- 避免：不是文件压缩；不保证自动变响，也不保证完全阻止所有峰值。
- 语境：此处主要描述 downward compression；其他模式需另行注明。
- 来源：S01

#### 24 Threshold
- ID：threshold
- 中文解释标签：阈值
- 准确含义：决定动态处理开始作用的检测电平区域；软拐点时会有过渡带。
- 避免：不是「把输出直接设为这个电平」，也不一定测量未滤波的主输入。
- 来源：S12

#### 25 Ratio
- ID：ratio
- 中文解释标签：压缩比
- 准确含义：在常见稳态、硬拐点向下压缩中，4:1 表示阈值以上输入增加 4 dB，输出约增加 1 dB。
- 避免：不等于总音量除以四；瞬态、软拐点和特殊模式不能照此机械推算。
- 来源：S12

#### 26 Attack
- ID：attack
- 中文解释标签：起效时间或速度
- 准确含义：压缩器建立增益衰减的响应速度；会影响瞬态通过量。
- 避免：不是先完全不动作、等到设定毫秒后才突然压缩。
- 语境：时间常数定义依产品；不要混用合成器或混响的 Attack 含义。
- 来源：S13

#### 27 Release
- ID：release
- 中文解释标签：恢复时间或速度
- 准确含义：压缩器从增益衰减恢复的响应速度。
- 避免：不是声音或混响尾音的长度；标称时间不一定等于完全恢复用时。
- 语境：Auto/Program-dependent 模式会随素材改变行为。
- 来源：S13

#### 28 Knee
- ID：knee
- 中文解释标签：拐点
- 准确含义：描述阈值附近从未压缩到压缩的过渡形状或范围。
- 避免：Soft Knee 不是慢 Attack；软硬拐点与响应时间是不同维度。
- 来源：S12

#### 29 Gain Reduction (GR)
- ID：gain_reduction
- 中文解释标签：增益衰减量
- 准确含义：处理器正在降低的增益量，通常以 dB 显示。
- 避免：不是输出电平，也不是响度减少的同义词；有些表头用正数表示衰减量。
- 检索别名：GR、Gain Reduction（不是无条件替换规则）
- 来源：S01

#### 30 Make-Up Gain
- ID：makeup_gain
- 中文解释标签：补偿增益
- 准确含义：在压缩后调整电平，用于补偿处理造成的电平变化。
- 避免：不是恢复被改变的动态；Auto Gain 也不保证精确响度匹配。
- 检索别名：Makeup Gain、Make-up Gain（不是无条件替换规则）
- 来源：S13

#### 31 Sidechain
- ID：sidechain
- 中文解释标签：侧链或检测支路
- 准确含义：用于触发或控制处理的信号路径，可来自主输入或外部信号。
- 避免：不是低频避让的专名；侧链 EQ 通常改变检测行为，不直接 EQ 主音频。
- 检索别名：Side Chain（不是无条件替换规则）
- 来源：S14

#### 32 Limiter
- ID：limiter
- 中文解释标签：限幅器
- 准确含义：以很高压缩比及峰值控制机制限制信号上限的动态处理器。
- 避免：不是任意 Compressor 的等价物，也不保证开启后所有后续处理和编码都不超限。
- 语境：区分 Sample Peak 与 True Peak 模式；核对 Ceiling、Lookahead 和后级处理。
- 来源：S01、S27

#### 33 Gate
- ID：gate
- 中文解释标签：噪声门或门控
- 准确含义：依检测条件让信号通过或衰减；关闭时的衰减深度常由 Range 决定。
- 避免：不是自动删除一切噪声，也不是永远开或关的理想硬开关。
- 来源：S15

#### 34 Transient
- ID：transient
- 中文解释标签：瞬态
- 准确含义：声音起始或其他快速变化中的短促成分，例如鼓的击打头部。
- 避免：不等于所有高频，也不只是波形中最高的一个采样点。
- 来源：S16


### 延时与空间

#### 35 Delay
- ID：delay
- 中文解释标签：延时
- 准确含义：把信号延后输出；可用于对齐、加厚、空间感或产生重复。
- 避免：禁止把 Delay 的正式标签直接替换成「回声」；并非所有 Delay 都能听成独立重复。
- 语境：标题、图中模块、插件名和控件保留 Delay；正文可准确解释「延时」。
- 来源：S17

#### 36 Echo
- ID：echo
- 中文解释标签：可分辨的重复声或回声
- 准确含义：描述可被感知为重复的声音；也可能是具体产品或设备的名称。
- 避免：不要与 Delay 或 Reverb 无条件互换，也不要给所有素材设一个固定可分辨毫秒界限。
- 语境：例如 Ableton Echo 是名为 Echo 的 modulation delay，必须保留产品原名。
- 来源：S17、S01

#### 37 Delay Time
- ID：delay_time
- 中文解释标签：延时时间
- 准确含义：信号在相应延时路径中被延后的时长，常以 ms 或节拍分值显示。
- 避免：不是 Feedback、重复次数或混响 Decay；多抽头路径未必只有一个重复间隔。
- 语境：Sync 数值需同时说明工程速度、音符分值及附点或三连音状态。
- 检索别名：Time（不是无条件替换规则）
- 来源：S17、S18

#### 38 Feedback
- ID：feedback
- 中文解释标签：反馈量
- 准确含义：将处理输出的一部分送回输入；在 Delay 中常影响重复的衰减和持续程度。
- 避免：不是重复次数，也不是 Wet 音量；高反馈可能累积电平或自激。
- 语境：百分比不是跨产品通用的尾音长度；还取决于环路中的滤波、增益与非线性。
- 来源：S01、S18

#### 39 Wet
- ID：wet
- 中文解释标签：湿声或处理后信号
- 准确含义：相对于所讨论的某个处理器或支路，经过该处理的信号。
- 避免：不要只解释为「带混响的声音」；压缩、失真、Delay 都有 Wet。
- 语境：Wet 可以是电平控制，也可以是混合比例，先看单位和信号图。
- 来源：S18、S13

#### 40 Dry
- ID：dry
- 中文解释标签：干声或未经过该处理的信号
- 准确含义：相对于当前处理器或支路，未经该项处理的信号。
- 避免：Dry 不表示这条音轨从未经过任何插件，也不等于完全没有空间声。
- 来源：S18、S13

#### 41 Dry/Wet
- ID：dry_wet
- 中文解释标签：干湿混合
- 准确含义：调节未处理与处理后信号的混合关系。
- 避免：50% 不保证听感各一半或总响度恒定；干湿电平也可能是两个独立旋钮。
- 语境：常规并行发送效果通常使用 100% Wet，避免重复叠加干声；特殊路由另论。
- 检索别名：Mix、Wet/Dry（不是无条件替换规则）
- 来源：S18、S01

#### 42 Reverb
- ID：reverb
- 中文解释标签：混响
- 准确含义：密集反射及其衰减形成的空间尾声，效果器通过算法或脉冲响应等方式生成。
- 避免：不等于离散重复的 Echo，也不是只调大 Wet 就能指定空间大小。
- 语境：产品的 Space、Size、Distance、Decay 未必一一对应物理房间参数。
- 来源：S19、S20

#### 43 Pre-Delay
- ID：pre_delay
- 中文解释标签：预延时
- 准确含义：在混响语境中，控制原声起点与混响开始之间的间隔。
- 避免：不是尾音衰减时长；不要默认每个产品都同样延后早期反射和后期混响。
- 语境：ChromaVerb 的 Predelay 具体参照早期反射到达时间。
- 检索别名：Predelay（不是无条件替换规则）
- 来源：S20

#### 44 Decay / RT60
- ID：decay_rt60
- 中文解释标签：衰减与混响时间
- 准确含义：Decay 控制尾声衰减；RT60 指混响电平下降 60 dB 所需时间。
- 避免：不能说 Decay 到时就绝对静音，也不能默认所有 Decay 旋钮都直接表示 RT60。
- 语境：衰减常随频率变化；比例式 Decay、Decay Rate 需按产品解释。
- 来源：S20、S21、S19


### 立体声与相位

#### 45 Stereo Width
- ID：stereo_width
- 中文解释标签：立体声宽度
- 准确含义：描述或调节左右声道共同形成的宽阔程度，具体算法可改变声道差异、M/S 比例等。
- 避免：不是左右声像位置；Width 100% 的含义不能跨插件照搬。
- 语境：加宽后检查单声道折叠；纯 M/S 增益不能凭空给完全相同的左右信号增加 Side。
- 来源：S22、S18

#### 46 Mid/Side (M/S)
- ID：mid_side
- 中文解释标签：和差信号
- 准确含义：Mid 来自 L+R，Side 来自 L−R；缩放系数依约定，可再解码回 L/R。
- 避免：Mid 不是「只含居中乐器」，Side 不是可单独提取的左右两侧乐器。
- 语境：常见约定 M=(L+R)/2、S=(L−R)/2；此时 L=M+S、R=M−S。
- 检索别名：M/S、Mid/Side（不是无条件替换规则）
- 来源：S23

#### 47 Phase
- ID：phase
- 中文解释标签：相位
- 准确含义：描述波形各频率成分的周期位置及彼此关系；相加时可能增强或抵消。
- 避免：不等于 Polarity；固定时间偏移对不同频率产生不同相位差。
- 语境：讨论相位问题时说明频率、参考信号和路由，不能只看一个波峰是否对齐。
- 来源：S24

#### 48 Polarity
- ID：polarity
- 中文解释标签：极性
- 准确含义：极性反转把信号正负号翻转，即 x 变为 −x，本身不把信号向后延时。
- 避免：不要把极性反转说成万能相位对齐；单一正弦的 180° 等效关系不能泛化为宽带统一时间位移。
- 语境：UI 可能写 Phase Invert 或 Ø；照录原名，并说明这里实际是极性反转。
- 来源：S24、S04

#### 49 Mono Compatibility
- ID：mono_compatibility
- 中文解释标签：单声道兼容性
- 准确含义：检查立体声合并为单声道后，重要内容、音色与平衡是否仍然可用。
- 避免：相关度短暂为负不自动等于不合格；仅听左声道也不等于检查 L+R 折叠。
- 语境：结合折叠试听和相关度读数，确认折叠增益规则。
- 来源：S22、S04


### 失真与电平计量

#### 50 Saturation
- ID：saturation
- 中文解释标签：饱和
- 准确含义：由非线性处理带来谐波和动态变化的一类失真，常模拟磁带、电子管等特性。
- 避免：不等于必然温暖、必然只加偶次谐波，或完全无失真。
- 来源：S25

#### 51 Clipping
- ID：clipping
- 中文解释标签：削波
- 准确含义：信号超过某阶段的可用范围，或被刻意限幅整形，使波形峰部改变。
- 避免：表头越过 0 dBFS 不代表每个浮点内部阶段都已不可逆削波；后级降电平也不能修复已发生的削波。
- 语境：区分内部浮点、固定点文件、转换器与专门的 Soft/Hard Clip 处理。
- 来源：S06、S07、S26

#### 52 Sample Peak
- ID：sample_peak
- 中文解释标签：采样峰值
- 准确含义：已记录或计算的采样点中的最大绝对幅度；数字电平通常以 dBFS 为参照。
- 避免：不等于重建波形的 True Peak，更不等于响度；dBFS 也可用于 RMS 电平，不能只理解为峰值单位。
- 检索别名：Peak（不是无条件替换规则）
- 来源：S26、S27

#### 53 True Peak
- ID：true_peak
- 中文解释标签：真峰值
- 准确含义：估计采样点之间重建波形可能达到的峰值，通常用 dBTP 表示。
- 避免：不是只取最高采样点；True Peak Metering 不等于已经开启 True Peak Limiting。
- 语境：不同合规实现可能有小幅读数差异，后续编码也可能改变峰值。
- 检索别名：TP、dBTP（不是无条件替换规则）
- 来源：S26、S27

#### 54 Loudness
- ID：loudness
- 中文解释标签：响度
- 准确含义：听感上的响亮程度；节目响度常依规定算法用 LUFS/LKFS 测量。
- 避免：不是推子位置、Peak 或 RMS 的同义词；不要把某一个 LUFS 目标当成所有平台的永久要求。
- 语境：必须注明 Integrated、Short-term 或 Momentary；EBU 模式分别为测量区间、3 s、400 ms。
- 检索别名：LUFS、LKFS（不是无条件替换规则）
- 来源：S28、S29

#### 55 RMS
- ID：rms
- 中文解释标签：均方根电平
- 准确含义：将一定时间窗口内的信号平方、平均后开方，反映该窗口的幅度能量特征。
- 避免：不是采样值的简单平均，也不是经过感知加权的 LUFS。
- 语境：显示偏置、时间窗口和校准方式会影响读数，需看仪表说明。
- 检索别名：Root Mean Square（不是无条件替换规则）
- 来源：S30、S31

#### 56 Crest Factor
- ID：crest_factor
- 中文解释标签：峰均比
- 准确含义：严格幅度定义为 Peak/RMS，换算为 dB 后为同一基准下峰值与 RMS 电平之差。
- 避免：不等于 Headroom；不能混用不同时间窗或校准的读数；True Peak−Integrated LUFS 应标明为 PLR，不与严格 Peak/RMS 定义混用。
- 语境：裸数学 RMS 下正弦为约 3.01 dB；部分音频仪表的正弦校准会改变显示差值。
- 来源：S31、S32

## 官方来源

全部链接于 2026-10-09 在线核验。条目为原创归纳，不是官方译文；旧版本资料仅支持所注明的概念或 UI 示例，操作步骤须重新核对当前版本。

- **S01** [Ableton Live 12 — Audio Effect Reference](https://www.ableton.com/en/manual/live-audio-effect-reference/)。官方产品手册；Delay、Echo、Compressor、Limiter 等章节。访问日期：2026-10-09。
- **S02** [Ableton Live 12 — Mixing](https://www.ableton.com/en/manual/mixing/)。官方产品手册；音量、声像、Send、Return、Pre/Post。访问日期：2026-10-09。
- **S03** [Ableton Live 12 — Routing and I/O](https://www.ableton.com/en/manual/routing-and-i-o/)。官方产品手册；信号流与内部路由。访问日期：2026-10-09。
- **S04** [Apple Logic Pro — Gain plug-in](https://support.apple.com/en-za/guide/logicpro/lgcef2d8c650/10.7/mac/11.0)。官方产品手册；Gain、Balance、Mono、Phase Invert 的 UI 示例；所链接为 10.7 版本。访问日期：2026-10-09。
- **S05** [Apple Logic Pro — Route audio via insert effects](https://support.apple.com/guide/logicpro/route-audio-via-insert-effects-lgcp8e838ae3/mac)。官方产品手册；Insert 与串联处理。访问日期：2026-10-09。
- **S06** [iZotope — Gain staging: what it is and how to do it](https://www.izotope.com/community/blog/gain-staging-what-it-is-and-how-to-do-it)。厂商技术教程；增益分配与不同处理阶段。访问日期：2026-10-09。
- **S07** [iZotope — Headroom: How to Set Your Levels in Mixing and Mastering](https://www.izotope.com/community/blog/headroom-how-to-set-levels-mixing-and-mastering)。厂商技术教程；Headroom、名义工作电平与 Clipping。访问日期：2026-10-09。
- **S08** [Ableton Live 12 — Automation](https://www.ableton.com/en/live-manual/12/automation/)。官方产品手册；自动化。访问日期：2026-10-09。
- **S09** [FabFilter Pro-Q 4 — Band controls](https://www.fabfilter.com/help/pro-q/using/bandcontrols)。官方产品手册；Bell、Q、Slope；不同 EQ 的 Q 定义可能不同。访问日期：2026-10-09。
- **S10** [FabFilter Learn — Introduction to EQ](https://prod.fabfilter.com/learn/equalization/introduction-to-eq)。厂商技术教程；EQ、HPF、LPF、Shelf、频率参数。访问日期：2026-10-09。
- **S11** [Apple Logic Pro — Filter cutoff and resonance overview](https://support.apple.com/en-ca/guide/logicpro/lgsi24401cc5/mac)。官方产品手册；滤波器截止频率与共振。访问日期：2026-10-09。
- **S12** [FabFilter Pro-C 3 — Dynamics controls](https://www.fabfilter.com/help/pro-c/using/dynamicscontrols)。官方产品手册；Threshold、Ratio、Knee。访问日期：2026-10-09。
- **S13** [FabFilter Pro-C 3 — Time controls](https://www.fabfilter.com/help/pro-c/using/timecontrols)。官方产品手册；Attack、Release、Make-up Gain、Auto Gain。访问日期：2026-10-09。
- **S14** [FabFilter Pro-C 3 — Side chain section](https://www.fabfilter.com/help/pro-c/using/sidechainsection)。官方产品手册；检测支路、内部与外部触发。访问日期：2026-10-09。
- **S15** [FabFilter Pro-G — Dynamic controls](https://prod.fabfilter.com/help/pro-g/using/dynamiccontrols)。官方产品手册；Gate、Threshold、Range。访问日期：2026-10-09。
- **S16** [iZotope — What is a Transient in Audio Production?](https://www.izotope.com/community/blog/what-is-a-transient-audio-production)。厂商技术教程；瞬态。访问日期：2026-10-09。
- **S17** [Apple Logic Pro — Delay effects](https://support.apple.com/guide/logicpro/delay-effects-overview-lgcec7e3312c/mac)。官方产品手册；Delay 的处理原理及用途。访问日期：2026-10-09。
- **S18** [FabFilter Timeless 3 — Delay controls](https://www.fabfilter.com/help/timeless/using/delaycontrols)。官方产品手册；Delay Time、Wet、Dry、Mix、反馈路由。访问日期：2026-10-09。
- **S19** [FabFilter Pro-R 2 — Main controls](https://www.fabfilter.com/help/pro-r/using/maincontrols)。官方产品手册；混响及产品特定 Space、Decay Rate 语义。访问日期：2026-10-09。
- **S20** [Apple Logic Pro for iPad — ChromaVerb main controls](https://support.apple.com/en-ca/guide/logicpro-ipad/lpipdc1fd692/ipados)。官方产品手册；Predelay、Decay。访问日期：2026-10-09。
- **S21** [Apple Logic Pro — GoldVerb reverb parameters](https://support.apple.com/en-mn/guide/logicpro/lgcef29694ff/mac)。官方产品手册；RT60 定义。访问日期：2026-10-09。
- **S22** [iZotope Ozone 8 — Imager](https://downloads.izotope.com/docs/ozone8/imager/index.html)。官方产品手册；Width 与单声道兼容；所链接为 Ozone 8，数值不泛化到其他产品。访问日期：2026-10-09。
- **S23** [FabFilter Pro-G — Mid/Side processing](https://www.fabfilter.com/help/pro-g/using/midsideprocessing)。官方产品手册；M/S 和差信号及可逆编码。访问日期：2026-10-09。
- **S24** [iZotope — What is phase in audio?](https://www.izotope.com/community/blog/5-ways-to-adjust-phase-after-recording)。厂商技术教程；相位、极性与时间对齐。访问日期：2026-10-09。
- **S25** [FabFilter Saturn 2 — About FabFilter Saturn 2](https://prod.fabfilter.com/help/saturn/intro/fabfiltersaturn)。官方产品手册；饱和与失真。访问日期：2026-10-09。
- **S26** [FabFilter Pro-L 2 — Metering](https://www.fabfilter.com/help/pro-l/using/metering)。官方产品手册；Sample Peak 与 True Peak 测量。访问日期：2026-10-09。
- **S27** [FabFilter Pro-L 2 — Input and output options](https://www.fabfilter.com/help/pro-l/using/outputoptions)。官方产品手册；输出上限、重建峰值、True Peak Limiting。访问日期：2026-10-09。
- **S28** [FabFilter Pro-L 2 — Loudness metering](https://www.fabfilter.com/help/pro-l/using/loudnessmetering)。官方产品手册；LUFS 与响度测量模式；不以文中平台目标值作永久规范。访问日期：2026-10-09。
- **S29** [EBU Tech 3343 — Guidelines for Production of Programmes](https://tech.ebu.ch/files/live/sites/tech/files/shared/tech/tech3343v3_0.pdf)。官方技术指南；Momentary 400 ms、Short-term 3 s、Integrated 起止区间。访问日期：2026-10-09。
- **S30** [iZotope — RMS levels defined](https://www.izotope.com/community/blog/rms-levels)。厂商技术教程；RMS 与峰值、响度的区别。访问日期：2026-10-09。
- **S31** [iZotope — What Is Crest Factor and Why Is It Important?](https://www.izotope.com/community/blog/what-is-crest-factor)。厂商技术教程；峰值与 RMS 的比值、仪表校准差异。访问日期：2026-10-09。
- **S32** [Youlean Loudness Meter — Measurements Explained](https://docs.youlean.co/youlean-loudness-meter/getting-started/measurements-explained)。官方产品文档；PLR 与 Integrated Loudness 的关系。访问日期：2026-10-09。

## 数据使用约定

MIXING_TERMINOLOGY.json 与本文件共享同一批词条。preferred_label 是术语基线，explanation_label_zh 是可用于正文解释的中文名；aliases 用于检索匹配，不授权把所有同形文本改写。source_ids 对应 sources 中的完整官方链接。特定产品的原始英文 UI 名称优先于通用拼写。
