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
Python 3，WeasyPrint 66.0、PyMuPDF、Pillow。全部渲染素材本地加载，渲染器拒绝外网URL。
本包已包含可直接编辑的 HTML/CSS 与必要显示尺寸配图。从本目录运行 `python source/render.py`，重新导出图文 PDF、PNG、手机预览与研究报告 PDF；不需要原始媒体包。

可选：运行 `python source/build_diagrams.py` 重建原创 SVG，再运行 `python source/render_assets.py` 导出独立图表 PNG。修改正文请直接编辑 `source/index.html` 和 `research/RESEARCH_REPORT.html`；修改样式请编辑 `source/style.css`。

图表数值为构造的分析示例，未做音频实测。报告区分信号流推导、厂商定义与试听建议。
