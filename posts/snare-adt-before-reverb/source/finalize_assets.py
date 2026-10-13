from pathlib import Path
import json,hashlib,fitz
from weasyprint import HTML
R=Path(__file__).resolve().parents[1]
A=[a for a in json.loads((R/'assets/assets.json').read_text()) if not a['path'].startswith('assets/diagrams/')]
usage={'reel-adt-official-product':[1,'research'],'reel-adt-position':[3,'research'],'reel-adt-src':[4],'reel-adt-adt':[4],'reel-adt-lfo':[3,'research'],'reel-adt-monitor':[],'manual-interface':['research verification']}
for a in A:a['used_on_pages']=usage.get(a['asset_id'],[])
for path in sorted((R/'assets/diagrams').glob('*.svg')):
 A.append({'asset_id':path.stem,'entity':'原创解释示意','version':'final','component':'conceptual diagram, not product UI','path':str(path.relative_to(R)),'source_page':'research/RESEARCH_REPORT.md','asset_url':None,'retrieved_at':None,'dimensions':[1080,1440] if path.stem.startswith('page-') else [936,520],'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'rights_status':'original_diagram_with_corresponding_source','rights_basis':'依据所引官方功能说明和独立计算制作的原创教学图形；不包含厂商像素。HTML/SVG导出骨架按AGPL-3.0提供。','attribution':'Kangdi Wang','modifications':'editable source','used_on_pages':['research'] if not path.stem.startswith('page-') else [int(path.stem.split('-')[1])],'limitations':'示意或明确假设下的数学模型，非音频实测。'})
 if path.stem.startswith('page-'):continue
 svg=path.read_text();css="@font-face{font-family:'Noto Sans SC';src:url('assets/fonts/NotoSansSC-Variable.ttf')}@page{size:936px 520px;margin:0}html,body{margin:0}"
 blob=HTML(string='<html><style>'+css+'</style><body>'+svg+'</body></html>',base_url=str(R)).write_pdf();d=fitz.open(stream=blob,filetype='pdf');d[0].get_pixmap(matrix=fitz.Matrix(4/3,4/3)).save(path.with_suffix('.png'))
(R/'assets/assets.json').write_text(json.dumps(A,ensure_ascii=False,indent=2)+'\n')
# The final page plan reflects the independent content-led split into eight pages.
spec=json.loads((R/'design/production_spec.json').read_text());plan=[]
for p in spec['pages']:
 plan.append({'page':p['page'],'title':p['title'],'author':'Kangdi Wang','design_spec':'design/production_spec.json','elements':[e['id'] for e in p['elements']],'narrative_role':['对象与目标','并联路由','时间与LFO真控件','Pan与Level真控件','共用时间轴','混响输入结构','完整链路试听与Mono风险','GitHub与BibTeX引用'][p['page']-1]})
(R/'story/page-plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
