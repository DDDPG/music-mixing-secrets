# 混响入口门限：图文与研究

- `output/xhs-01.png`–`xhs-08.png`：1080×1440 小红书图文。
- `output/gate-before-reverb.pdf`：整套图文。
- `phone-preview/`：360px手机预览。
- `research/RESEARCH_REPORT.md`、`.html`、`.pdf`：详细图解研究报告。
- `title-caption.txt`：标题与平台正文。
- `source/index.html`、`source/style.css`：可编辑图文；assets/diagrams为原创可编辑SVG。
- `research/facts.json`、`term-map.json`、`sources.md`、`assets.json`：事实、术语、出处与素材溯源。
- `RIGHTS.md`：第三方配图边界；不将项目源码许可套用到厂商图像。

## 重现
Python 3，WeasyPrint 66.0、PyMuPDF、Pillow、fontTools。全部渲染素材本地加载，渲染器拒绝外网URL。
本包已包含可直接编辑的 HTML/CSS、覆盖当前正文的本地 Noto Sans SC 字体子集与必要显示尺寸配图。从本目录运行 `python source/render.py`，重新导出图文 PDF、PNG、手机预览与研究报告 PDF；脚本自动创建输出目录，不需要原始媒体包。

编辑文字后先运行 `python source/check_fonts.py` 检查本地字体覆盖；新增字若不在子集中，需用 Noto Sans SC 原字体补充子集后重新导出。

可选：运行 `python source/build_diagrams.py` 重建原创 SVG，再运行 `python source/render_assets.py` 导出独立图表 PNG。修改正文请直接编辑 `source/index.html` 和 `research/RESEARCH_REPORT.html`；修改样式请编辑 `source/style.css`。

图表采用简化分析示例，正文保留对应前提；实际参数需结合音频调整。报告包含信号流推导、产品定义与试听步骤。

## R3 编辑清理
沿用 R2 主视觉与版式，移除封面生成方式标签及内页重复声明；来源与第三方图像使用说明集中在末页和研究报告末尾。门限、时序、最大衰减及产品差异等技术条件仍随解释保留。
