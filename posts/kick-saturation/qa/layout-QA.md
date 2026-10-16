# Historical pre-R3 layout QA

This prior review describes the version before R3 editorial cleanup. Current output is covered by editorial-r3-QA.md; visible AI labels and repetitive disclaimer text were removed.

# 布局与术语复核

2026-10-16。10 页，1080×1440；10 张 360×480 手机预览。WeasyPrint 66 → PDF → PyMuPDF；每页文字边界自动检查无越界。图表与数值另用解析及离散采样重算，误差小于 1e−12。

独立设计审阅已检查全部 10 页原尺寸和手机预览。修改：第 4 页改为更大的三列数值表；第 5 页降低完整对象图高度，为关键控件局部和限制语腾出空间；第 8 页移开 18 kHz 标签与竖线、加入折叠箭头、扩展到 48 kHz，并增加底部距离；第 10 页减少代码块间距以保留版权说明。

完整对象原色比例、局部控件、截图状态、三列 Peak/RMS、同 RMS 限制、相位/极性区分、8×/32×、48−30=18、引用 author={Kangdi, Wang} 均复核。概念插画已明确标为 AI，不作声学图或实测证据。8 页研究报告逐页图像检查，无缺字、表格溢出、异常空白页或图文叠压。

制作中发现并修复过分页溢出和研究 HTML 标题解析错误；交付仅保留最新十页轮播与八页报告。
