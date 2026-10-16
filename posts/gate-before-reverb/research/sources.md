# 一手来源与适用范围
核验日期：2026-10-16。只以厂商资料作为产品事实依据；计算与路由推导另标。

S1 FabFilter Pro-G, Time controls, Style and Knee
https://www.fabfilter.com/help/pro-g/using/timecontrols
支持：内建 hysteresis；Attack/Release 的节目相关行为；Hold 最短全开定义；Lookahead。正文为释义，无长篇摘录。

S2 FabFilter Pro-G, Dynamic controls
https://www.fabfilter.com/help/pro-g/using/dynamiccontrols
支持：Threshold 依音频设定；Range 限制最大衰减。仅引用 Range 的20 dB例子并以独立算术解释，不把 Ratio 跨产品泛化。

S3 Ableton Live 12 Reference, 29.20 Gate
https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#gate
支持：Return 即 hysteresis；Hold/Release 顺序；侧链控制与音频路径区分；检测 EQ。产品实现差异与 Pro-G 分开描述。

S4 FabFilter Pro-G Overview
https://www.fabfilter.com/help/pro-g/using/overview
支持：界面区域与实际控件名。未断言媒体包截图属于当前软件版本。

S5 FabFilter Press Area
https://www.fabfilter.com/press
官方媒体包：https://www.fabfilter.com/downloads/press/fabfilter-pro-g.zip
实际取得官方截图，文件时间2015-12-14；媒体用途提供方式不等于明确通用再分发许可。仅作有实质评论的教学配图：比例缩放、明确厂商署名与来源、保留版权；不分发完整媒体包或独立原件。此为有限编辑使用评估，不是许可证或法律结论，权利仍保留。

D1 作者原创信号流推导
前级 Gate: y=R(g·x)；后级 Gate: y=g·R(x)。R 是有记忆的混响系统。两者一般不等价；此为机制解释，不是厂商测试结论。图中 gate 的 g 是控制增益而非混响衰减。

D2 作者构造分析例
开门 −24 dBFS，关门 −30 dBFS，相差6 dB；满足关闭条件120 ms，加Hold40 ms与Release80 ms，得到160/240 ms；无再触发、线性绘图示意，不代表产品时间响应。
