# 人声压缩怎样塑形

一套九页中文图文，解释 Attack 与 Release 怎样影响字头、字身和下一音节；附七页完整研究报告与可编辑源文件。

## 阅读

- `output/xhs-01.png` 至 `output/xhs-09.png`：1080 × 1440 图文
- `output/vocal-compression-shaping.pdf`：整套图文 PDF
- `phone-preview/`：360 × 480 手机预览
- `RESEARCH_REPORT.md`、`RESEARCH_REPORT.html`、`output/RESEARCH_REPORT.pdf`：完整图文研究报告
- `public_caption.txt`：小红书标题与发布正文
- `qa/QA_REPORT.md`：事实、术语、真实素材、数学与视觉检查摘要

## 编辑与复现

`design/production_spec.json` 是逐页文字和坐标的权威规格；`index.html` 是可直接查看和编辑的最终 HTML。`research/diagram_data.json` 与 `research/model_samples.csv` 保留模型假设及数值。`assets/` 保留原始官方截图、精确裁切、原创 SVG、完整字体与许可证。所有渲染素材均为本地文件。

参考依赖：Python、WeasyPrint 66.0、PyMuPDF 1.26.6、Pillow 12.3.0、fontTools 4.66.1，以及 WeasyPrint 所需系统库。已安装依赖后，在项目根目录运行：

    python source/generate_visuals.py
    python source/prepare_fonts.py
    python source/build_carousel.py
    python source/render_carousel.py
    python source/render_report.py

修改文字后重建字体子集，不能沿用旧中文子集猜测字形覆盖。图形可编辑，但公式、单位和坐标应同时复核。整套图文最后一页保留 HTML 渲染的 GitHub 引用；BibTeX 作者字段为 `{Kangdi, Wang}`。

## 解释边界与素材权利

数学曲线是明确假设的一阶 GR 模型，不是人声实测，也不是 FabFilter Pro-C 3 的算法复刻。模型时间常数 τ 与实际插件旋钮标称时间不可混用。示例毫秒值是练习对照，不是通用预设。

FabFilter 截图只用于解释真实产品及控件，厂商展示状态不是本篇人声设置。截图保留 © FabFilter 权利，不因公开可见、署名或存在 press kit 就取得无限制再发布或商用许可。完整权利边界见 `RIGHTS_AND_SOURCES.md`、`assets.json` 和 `THIRD_PARTY_NOTICES.txt`。HTML 导出骨架为 AGPL-3.0；Noto 字体为 SIL OFL；这些许可不覆盖厂商图片。

项目仓库：https://github.com/DDDPG/music-mixing-secrets
