# 底鼓饱和与电平

十页中文图文与研究报告。作者 Kangdi, Wang，2026。

- index.html / style.css：可编辑图文，字体与图片本地加载
- output/：1080×1440 PNG、联系表、图文 PDF、研究报告 PDF
- phone-preview/：360×480 手机预览
- RESEARCH_REPORT.md / .html：完整研究文稿及图文版
- research/：事实、来源、术语、叙事、页计划与解析计算结果
- source/：生成、渲染、打包脚本
- assets.json / RIGHTS_AND_SOURCES.md：来源、版权边界与裁切记录

复现顺序：python source/generate_visuals.py；python source/build.py；python source/render_carousel.py；python source/render_report.py。依赖 Python、WeasyPrint 66、PyMuPDF、Pillow。渲染离线读取本地资产。SVG 标签使用随包 Noto 字体。所有数值是明示解析模型，未运行商业插件或音频实测。

官方产品像素版权保留，不因代码许可而获得再许可。源码压缩包不入公开 GitHub。根仓库：https://github.com/DDDPG/music-mixing-secrets
