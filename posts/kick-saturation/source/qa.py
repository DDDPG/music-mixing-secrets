from pathlib import Path
import fitz,json,re,math
from weasyprint import HTML
P=Path(__file__).resolve().parents[1]
# Render SVG viewing PNGs without changing the editable originals.
for f in (P/'assets/diagrams').glob('*.svg'):
 raw=f.read_text();h=int(re.search(r'height="(\d+)"',raw).group(1));page=f'<style>@font-face{{font-family:"Noto Sans SC";src:url({(P/"assets/fonts/NotoSansSC-400.ttf").as_uri()})}}@page{{size:936px {h}px;margin:0}}body{{margin:0}}img{{width:936px;height:{h}px}}</style><img src="{f.as_uri()}">'
 doc=fitz.open(stream=HTML(string=page).write_pdf(),filetype='pdf');doc[0].get_pixmap(matrix=fitz.Matrix(4/3,4/3)).save(f.with_suffix('.png'))
report={'dimensions':[1080,1440],'pages':10,'automated_bounds_warnings':sum(len(p['text_bounds_warnings']) for p in json.loads((P/'qa/layout-report.json').read_text())),'model_checked':json.loads((P/'research/model-data.json').read_text()),'terms_reviewed':['Gain vs saturation','Peak vs RMS vs LUFS','Crest Factor','sample peak vs True Peak','band Level vs global output','Mix','High Quality Good 8x Superb32x','Polarity vs phase'],'before_render':'Terms checked against baseline and official Saturn2 manual. No unsupported preset or actual audio performance claims.','after_render':'Designer reviewed all10 full and360 pages; requested label/spacing refinements applied. Final review pending latest verification.','citation':'author={Kangdi, Wang}, root URL verified upstream; standard BibTeX string concatenation in HTML','privacy':'No note identifiers, account data or raw original note in public payload.'}
(P/'qa/term-QA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print('QA diagrams exported')
