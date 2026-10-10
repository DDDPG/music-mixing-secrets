一点延迟，给人声加点空间

本文件夹包含 7 张小红书 3:4 卡片的可编辑 HTML 源文件。

打开 index.html 可预览并直接修改文字和排版。全部图片和字体保存在 assets 中，不依赖在线字体或远程脚本。请保留文件夹结构。

PNG 成品为每张 1080 × 1440。标题使用 Noto Sans SC Light，正文使用 Regular，遵循 Swiss IKB Blue 配色。封面为 AI 概念示意。

重新导出：在 Python 环境安装 weasyprint==66.0、PyMuPDF、Pillow，然后在本文件夹运行 python render.py。系统需要 WeasyPrint 所需的 Pango 字体库。PNG 与 PDF 将保存在 output。若只修改文案，也可直接使用浏览器打印为 1080×1440 px 页面。

本次导出使用 HTML→PDF→PNG；已逐页检查文字、安全边距、尺寸及对比度。未对真实音频做试听测试。

设计模板来源与技术参考见 SOURCES.md；上游模板 AGPL-3.0 许可证及字体 OFL 许可证随附。
