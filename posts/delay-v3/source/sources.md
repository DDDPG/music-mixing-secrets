# 来源、适用范围与真实配图 v3

核验日期：2026-10-09。正文为自主组织的教学释义，不复制厂商文段；计算与试听建议分别标注。公开文章只具体讨论 Waves H-Delay，其他产品文档仅作原理交叉核验，不把其功能移植到 H-Delay，也不加入无对应实图的产品讲解。

## S0｜Waves H-Delay Hybrid Delay 官方产品页与原图

- 页面：https://www.waves.com/plugins/h-delay-hybrid-delay
- 原始图片：https://media.wavescdn.com/images/products/plugins/max/h-delay-hybrid-delay.png
- 已下载原件：assets/source/h-delay-official-product.png，1499×545，PNG。
- 原图文件地址从官方页面的 H-Delay GUI 图片元素核对；不是搜索缩略图。
- 具体软件版本、Stereo/M>S 组件名未标注，不能凭外观猜为最新版。
- 已逐项观察：DUAL 和 BPM 呈选中显示，屏幕 120 BPM，左为 1/8D、右为 1/2。它用于展示控件，不代表本文 Ping Pong + HOST 普通 1/8 的设置。
- UI 关键拼写：DRY/WET、FEEDBACK、PING PONG、HiPASS、LoPASS、HOST。本图的 DELAY R 表示 DUAL 下选中右侧时间。
- A02–A07 仅作精确矩形裁切，未改字、数值、颜色、比例或按钮状态。坐标、尺寸、SHA-256、用途均见 assets.json。
- 相邻图片说明：Waves 官方界面，仅用于定位控件；图中参数不是本教程设置。

## S1｜Waves H-Delay User Guide

- 官方入口：https://www.waves.com/1lib/pdf/plugins/h-delay-hybrid-delay.pdf
- 当前官方 PDF 文件：https://assets.wavescdn.com/pdf/plugins/h-delay-hybrid-delay.pdf
- 留存核对文件：source_references/waves-h-delay-user-guide.pdf。
- 文件元数据：作者 Waves Audio Ltd.；创建 2024-04-25，修改 2024-05-16；手册正文未给明确插件版本号。元数据不是软件版本号。
- 印刷第 4 页：Ping Pong 交叉反馈；反馈显示值须大于 1；改变 Delay 时间的过渡音高行为。
- 第 5 页：Mono、Stereo、M>S 的输入输出配置。
- 第 6 页：插入与发送的干湿设置；高反馈电平累积提醒。
- 第 7 页：真实界面与控件索引。
- 第 8 页：HOST / BPM / MS，音符时值，默认 1/8D。
- 第 9–11 页：Dual、Depth、Ping Pong、Feedback、滤波和干湿混合。
- 重要边界：Ping Pong 选中后显示单一时值；不能引用 DUAL 的左右独立时值冒称 Ping Pong 可如此设置。手册用 Mix、HP、LP 等缩写，真实截图上的标签应写 DRY/WET、HiPASS、LoPASS。

## S2｜Waves：10 Delay Tips for Mixing Vocals

https://www.waves.com/delay-tips-for-mixing-vocals

第 2、3、5、6、10 节支持根据歌词密度选时间、滤波、避免重复累积、选择性发送和放回伴奏判断。第 7 节对 H-Delay 的独立左右时间/反馈描述与现行手册不一致，因此不采用该段的产品特定说法。本稿控制事实均按 S1。

## S3｜FabFilter Timeless 3 Help：Delay controls

https://www.fabfilter.com/help/timeless/using/delaycontrols

只核对一般反馈定义、干湿混合与左右交叉反馈概念。本文数学模型自行计算，不引用该产品 UI 或预设，也不把它的反馈刻度等同于 H-Delay。

## S4｜Ableton Live 12 Manual：Delay

https://www.ableton.com/en/manual/live-audio-effect-reference/#delay

用于核对不同干湿混合曲线的存在以及通用路由概念。不能仅按 Dry/Wet 数字推定跨插件的实际电平比；本文不介绍或要求使用另一插件。

## S5｜Ableton Learning Music：Beat and tempo

https://learningmusic.ableton.com/make-beats/beat-and-tempo.html

BPM 为每分钟拍数。本稿明确四分音符为一拍，再自行计算普通八分、十六分及附点八分音符的时长。

## S6｜Waves：4 Tips for Mixing 2021 Pop Vocals

https://www.waves.com/tips-for-mixing-2021-pop-vocals

第 3 节核对 H-Delay 的 HOST、滤波、反馈与 Analog Off 避免模拟模式噪声。文章范例是发送 throw，滤波更重；本教程 200 Hz / 6 kHz 等为自主提出的轻量试听起点，不归因于官方预设。

## S8｜iZotope：6 Tips for Using Ozone’s Utilities in Mixing and Mastering

https://www.izotope.com/community/blog/how-to-use-ozone-utilities

第 2、4 节支持尽量响度匹配的开关对比及单声道兼容检查。本文不要求该产品，不挪用范例中的测试结果。

## R1｜图片权利核查

https://www.waves.com/legal/waves-terms-of-use

本次可确认图片来自 Waves，不能确认存在允许通用公开转载的开放许可。页面条款保留知识产权，没有找到适用于此图的 CC 或媒体授权。素材只为产品相关教学评论准备有限引用，明确来源并保留完整对象图的品牌标记，不用其 logo 为作者或教程背书。

rights_status 保留 unverified_for_public_republication。这里不是关于特定司法辖区合理使用/适当引用是否成立的法律结论；不得将“已注明来源”写成“已获得版权授权”。外部发布前仍应核查该具体用途的授权或适用引用依据。本次仅制作并交付用户审阅，不代表已经对外发布。

请勿把 source_references 的整本手册或网页全文作为公众下载赠品。正式教程中仅保留实际讲解所需的界面图片与必要局部；不将官方原图单独当成可自由复用素材分发。

## 自主计算核对

- 普通 1/8：60,000 ÷ BPM ÷ 2；普通 1/16：60,000 ÷ BPM ÷ 4。
- 120 BPM：250 / 125 ms；160 BPM：187.5 / 93.75 ms。
- 187.5 ÷ 250 = 0.75：同一音符时长缩短 25%，不是说 BPM 增加 25%。
- 160 BPM 附点 1/8：187.5 × 1.5 = 281.25 ms。
- 理想左右交替：第 n 次时刻 n×187.5 ms，同侧重复间隔 375 ms。
- 相对振幅 100×g^(n−1)：g=.3 为 100/30/9/2.7；g=.6 为 100/60/36/21.6。
- 第四次振幅比 21.6/2.7=8；不是能量或主观响度比。

确定性断言已由 build_source_package.py 核对；详见 source_stage_validation.json。
