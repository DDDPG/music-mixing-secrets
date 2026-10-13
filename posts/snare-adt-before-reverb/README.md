# 军鼓混响前的 ADT 拓宽

作者 Kangdi Wang

用一条独立的军鼓空间支路，解释 Waves Abbey Road Reel ADT 的真实控件、ADT 与 Predelay 的区别、混响输入结构及完整链路的 Mono 检查。八张1080×1440图文和六页插图研究报告互相补充；所有数值模型都明确标注假设，没有音频实测。

## 阅读

- `output/xhs-01.png` 至 `output/xhs-08.png`：按顺序阅读的图文
- `output/snare-adt-before-reverb.pdf`：八页整套PDF
- `research/RESEARCH_REPORT.pdf`：六页完整插图报告
- `research/RESEARCH_REPORT.md`：可编辑研究正文
- `story/public_caption.txt`：标题和小红书发布正文
- `phone-preview/`：360px宽度的手机预览

## 编辑与复现

`index.html` 是自包含本地资源的可编辑页面；`design/production_spec.json` 是最终文案与坐标。`assets/diagrams/` 保留原创SVG、查看PNG和数据，`assets/source/` 保留真实对象原件，`assets/derived/` 保留可追溯裁切。完整Noto字体和许可也在本包内，不依赖历史字符子集。

参考运行环境：Python 3.12，WeasyPrint 66.0，PyMuPDF 1.26.6，Pillow 12.3.0，fontTools 4.66.1及WeasyPrint要求的系统字体/排版库。

在本目录运行：

```sh
python source/build_carousel.py
python source/render_carousel.py
python source/render_report.py
```

若修改研究正文生成逻辑，可先运行 `python source/build_research.py`，再重渲报告与轮播；最后运行 `python source/finalize_assets.py` 刷新图片使用记录和最终页面计划。离线渲染不请求外网。PNG输出应为1080×1440，手机预览360×480；重新编辑后需重新做全尺寸和手机检查。

## 来源与权属

关键一手依据是Waves Reel ADT官方手册/产品页与FabFilter Pro-R 2官方帮助。完整链接、适用范围、数据、术语与事实记录在 `research/`。

Waves图片保持真实像素，截图数值不是本篇参数；厂商图片的公开再发布许可未核实，署名和公开可见不等于已取得许可。本包不授予厂商素材的无限制再利用权。详情见 `RIGHTS.md`、`assets/assets.json` 和 `source/THIRD_PARTY_NOTICES.txt`。

HTML导出骨架沿用Guizang固定版本cf4b810，相关对应源码和AGPL-3.0许可随包保留；Noto字体为SIL OFL。各类素材的权利不因仓库总许可证而改变。没有包含完整厂商手册、网页缓存或任何私人原始材料。

## 引用

仓库：https://github.com/DDDPG/music-mixing-secrets

使用 `CITATION.bib`。BibTeX作者字段为 `{Kangdi, Wang}`；人类可读署名为Kangdi Wang。仓库引用不能替代具体技术来源或图片许可。
