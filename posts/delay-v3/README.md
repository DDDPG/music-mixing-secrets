# 低 Wet 人声 Ping Pong Delay

2026 · 8 页 · 1080 × 1440 px · 中文混音教学

![成品缩略总览](source/output/vocal-delay-v3-contact-sheet.png)

## 阅读顺序

1. [详细图解研究报告](RESEARCH_REPORT.md)：问题拆解、公开证据、计算、素材解释与逐页决策。
2. [最终 PDF](source/output/vocal-delay-v3.pdf) · [最终 HTML](source/index.html) · [全尺寸 PNG](source/output/) · [手机预览](source/phone-preview/)
3. [发布文案](source/public_caption.txt) · [完整内容稿](source/research_and_story.md) · [设计方案](source/DESIGN_PLAN.md)
4. [公开来源](source/sources.md) · [素材记录](source/assets.json) · [术语映射](source/term-map.json) · [生产坐标与文字](source/production_spec.json)

## 如何复现

先打开 source/index.html 查看全部本地素材。Python 3.11+ 环境安装 source/requirements.txt 及 WeasyPrint 所需系统库；进入 source 目录运行 python build.py，再运行 python render.py。修改文字后可先运行 python prepare_fonts.py 重建随附 OFL 字体子集。完整字体、原始 SVG、版式几何、来源记录均保留在 source 下。原始教学图解生成器可能还需要 Inkscape；已渲染的 PNG/SVG 可直接使用，无需重新生成。运行 python package.py 可生成本帖独立 ZIP。

最终交付文件在本档案中保持原样。若重建，字体栅格化、依赖版本和 PDF 元数据可能造成不同输出；请先复制目录，在副本中修改。全局校验见 [PRESERVED_FINALS.json](../../PRESERVED_FINALS.json)。

## 证据与权利边界

没有真实音频测量或效果保证。计算图是数学或概念示意；试听值不是厂商预设。产品截图用于评论与控件说明，原图状态不等于教程设置。截图及商标属于相应厂商，公开可下载不等于取得无限制再许可。完整说明见 [权利说明](../../RIGHTS.md)、[原始权利记录](source/RIGHTS_AND_SOURCES.txt)。
