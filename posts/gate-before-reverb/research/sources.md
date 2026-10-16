# 一手来源与适用范围
核验日期：2026-10-16。只以厂商资料作为产品事实依据；计算与路由推导另标。

S1 FabFilter Pro-G, Time controls, Style and Knee
https://www.fabfilter.com/help/pro-g/using/timecontrols
支持：内建 hysteresis；Attack/Release 的节目相关行为；Hold 最短全开定义；Lookahead。正文为释义，无长篇摘录。

S2 FabFilter Pro-G, Dynamic controls
https://www.fabfilter.com/help/pro-g/using/dynamiccontrols
支持：Threshold 依音频设定；Range 限制最大衰减。本文以 20 dB 的 Range 说明最大衰减的计算。

S3 Ableton Live 12 Reference, 29.20 Gate
https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#gate
支持：Return 即 hysteresis；Hold/Release 顺序；侧链控制与音频路径区分；检测 EQ。产品实现差异与 Pro-G 分开描述。

S4 FabFilter Pro-G Overview
https://www.fabfilter.com/help/pro-g/using/overview
支持：界面区域与实际控件名。

S5 FabFilter Press Area
https://www.fabfilter.com/press
官方媒体包：https://www.fabfilter.com/downloads/press/fabfilter-pro-g.zip
界面配图 © FabFilter，文件日期 2015-12-14，具体版本及组件未注明。配图按比例缩放并裁切用于教学评论。未找到通用再分发许可，第三方图像版权保留；进一步复用应核对权利人许可。

D1 作者原创信号流推导
前级 Gate: y=R(g·x)；后级 Gate: y=g·R(x)。R 是有记忆的混响系统。两者一般不等价。图中 gate 的 g 表示控制增益，混响自身的衰减由 R 决定。

D2 作者构造分析例
开门 −24 dBFS，关门 −30 dBFS，相差6 dB；满足关闭条件120 ms，加Hold40 ms与Release80 ms，得到160/240 ms；以无再触发、线性关闭过程作图；具体时间行为依产品与音频内容调整。
