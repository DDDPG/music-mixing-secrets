给人声一点空间 · Editable source package

Start with index.html to view the eight editable 1080×1440 pages.
The final PNGs and PDF are in output/. Phone-size previews are in phone-preview/.
assets/ contains the conceptual cover, page-native SVGs, packaged fonts and font licenses.
source_diagrams/ contains the original explanatory SVGs before portrait reflow.
public_caption.txt is the publication caption. sources.txt identifies the factual references.
WORKFLOW.md and 图文制作流程.txt describe the reusable content-first production procedure.

Rebuild:
1. Run python build.py to regenerate HTML and SVGs.
2. Run python render.py to regenerate PDF, full-size PNGs, phone previews and contact sheet.

Dependencies: Python 3, WeasyPrint 66.0, PyMuPDF, Pillow, fontTools, and WeasyPrint system dependencies. This project does not install software automatically. Both scripts use local assets. render.py rejects external URLs. View the result again if rendering on a different platform or with different dependencies.

The inherited seed's theme/layout defaults are intentionally overridden by the project-specific design block. The copied source template and license are retained for transparency. See THIRD_PARTY_NOTICES.txt.
