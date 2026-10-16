from pathlib import Path
import re,fitz
from weasyprint import HTML
R=Path(__file__).parent;D=R/'assets/diagrams'
for svg in D.glob('*.svg'):
 h=int(re.search(r'height="(\d+)"',svg.read_text()).group(1))
 html=f'<style>@font-face{{font-family:"Noto Sans SC";src:url({(R/"assets/fonts/NotoSansSC-400.ttf").as_uri()})}}@page{{size:936px {h}px;margin:0}}body{{margin:0}}img{{display:block;width:936px}}</style><img src="{svg.as_uri()}">'
 pdf=HTML(string=html,base_url=str(R)).write_pdf();d=fitz.open(stream=pdf,filetype='pdf');d[0].get_pixmap(matrix=fitz.Matrix(4/3,4/3),alpha=False).save(svg.with_suffix('.png'))
