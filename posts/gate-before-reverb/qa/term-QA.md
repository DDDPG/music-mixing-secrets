# 术语与事实双轮 QA
2026-10-16
- 渲染前逐项核对 Gate（门限器）与 Threshold（阈值），未把二者混用。
- Pro-G 真实截图包含 THRESHOLD / RANGE / ATTACK / HOLD / RELEASE；没有虚构 Hysteresis 控件。
- Hysteresis 条件明确为已开门后的下降过程；−27 dBFS 并非独立开门电平。
- 关闭条件、Hold、Release 区分，120+40=160 ms，160+80=240 ms；示例不预测 Pro-G 的实际时间包络。
- −40 dBFS 经最大20 dB衰减为−60 dBFS；增益差使用 dB，不写成 dBFS。没有把这个差值推导成混响输出实测变化。
- Gate 位于Send/Return支路、Reverb前；Dry未穿过Gate。后级Gate案例明确在Wet输出。
- Sidechain/detector EQ只用于检测说明，不宣称改变进入混响的音色。
- 每页与PDF核对：图形、术语与小红书正文一致；比例与横轴为构造示例。
- BibTeX作者 {Kangdi, Wang}；仓库为 DDDPG/music-mixing-secrets；无虚构专题链接或DOI。
- 真实截图具体版本未标注；不称最新版本，不将显示参数当推荐预设。

已修正：首轮第4页溢出独立一页，缩短标题后重新渲染；第5页改为单行标题、精简上部留白，时间图恢复936px并将说明加大至32px；第8页引用块压缩非文字间距避免页脚冲突；第4页版权说明上移20px，第7页诊断面板缩减内边距确保页脚间隔。字体未靠缩小到不可读解决卡片正文。

最终来源复查：当前 Ableton Live 12 Gate 章节为29.20，已更正资料和报告中的章节号；#gate直达锚点不变。
