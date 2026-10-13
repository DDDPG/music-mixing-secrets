# 合成器的前后左右

作者：Kangdi Wang

本教程拆开 Pan、Stereo Width 与前后层次，解释混响与路由，并提供可复核的数字例子和单声道检查。它讨论普通双声道混音，不声称实际距离或音频实测。

## 交付文件

- RESEARCH_REPORT.md 与 output/合成器的左右宽度与前后层次_研究报告.pdf：独立可读的完整研究报告，含原理、构造数值、真实界面与局部、步骤、限制和一手来源。
- output/01.png 等：按序发布图；output/合成器的前后左右_图文.pdf：整套图文。
- phone-preview/：360×480 检查版。
- index.html、source/、assets/、research/、design/：可编辑内容、图解与制作依据。
- caption.txt：建议标题与发布正文。
- assets.json、RIGHTS.md、THIRD_PARTY_NOTICES.txt：来源、原始截图状态、裁切与许可边界。
- qa/：数值、术语、像素、页面和手机检查记录。

## 离线重建

建议 Python 3.12；WeasyPrint 66.0、PyMuPDF 1.26.6、Pillow 12.3.0、fontTools 4.66.1 及 WeasyPrint 所需系统组件。所有字体、图片和图解均为本地文件。

1. 在项目根目录执行 python source/build_assets.py，重建原创 SVG 和真图局部。
2. 执行 python source/build_carousel.py，重建可编辑 index.html。
3. 执行 python source/render_carousel.py，导出 PDF、1080×1440 PNG 与 360×480 预览。
4. 执行 python source/render_report.py，重建研究报告 HTML/PDF。
5. 阅读并重新执行 QA。换渲染器或字体后不能假定页面仍相同。

## 复用边界

代码保留 AGPL-3.0，对应源文件随包提供。字体保留 SIL OFL。原理图是原创示意；AI 插画不是测量证据。官方插件截图只作为必要的教育评论素材，并未获得一般性商业再许可或无条件转载许可。第三方图像不受本包开源代码许可覆盖。若发布目的地要求明确的图片授权，应先获得授权或移除图像并保留官方链接。

项目入口：https://github.com/DDDPG/music-mixing-secrets

引用作者字段须保持 {Kangdi, Wang}，见 CITATION.bib。
