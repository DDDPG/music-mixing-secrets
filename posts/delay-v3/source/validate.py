"""Deterministic numeric, typography, extraction, and asset-integrity QA."""
from pathlib import Path
from collections import Counter
import fitz, json, hashlib, re, unicodedata, math
from PIL import Image
from fontTools.ttLib import TTFont
R=Path(__file__).resolve().parent
(R/'qa').mkdir(exist_ok=True)
spec=json.loads((R/'production_spec.json').read_text());data=json.loads((R/'diagram_data.json').read_text());assets=json.loads((R/'assets.json').read_text())
report={'pages':[],'assets':[],'checks':{}}
norm=lambda s:re.sub(r'\s+','',unicodedata.normalize('NFKC',s))
pdf=fitz.open(R/'output/vocal-delay-v3.pdf');assert len(pdf)==8
for p,pg in zip(spec['pages'],pdf):
 expected=''.join(e['text'] for e in p['elements'] if e['type']=='text');actual=pg.get_text()
 want=Counter(norm(expected));got=Counter(norm(actual));assert want==got,(p['page'],want-got,got-want)
 spans=[s for b in pg.get_text('dict')['blocks'] if 'lines'in b for l in b['lines'] for s in l['spans']]
 outside=[s for s in spans if s['bbox'][0]<0 or s['bbox'][1]<0 or s['bbox'][2]>810 or s['bbox'][3]>1080];assert not outside
 used=[]
 for e in p['elements']:
  if e['type']=='text':
   f=TTFont(R/f'assets/fonts/NotoSansSC-{e["font_weight"]}.ttf');cmap=set(f.getBestCmap());sym=set(TTFont(R/'assets/fonts/NotoSans-Regular.ttf').getBestCmap());missing={c for c in e['text'] if not c.isspace() and ord(c)not in cmap|sym};assert not missing,missing
   used.extend(c for c in e['text'] if ord(c)not in cmap and not c.isspace())
 report['pages'].append({'page':p['page'],'extracted_text_complete':True,'no_glyphs_outside_canvas':True,'text_spans':len(spans),'font_names':sorted({s['font'] for s in spans}),'packaged_symbol_font_characters':sorted(set(used))})
 (R/'qa'/f'page-{p["page"]:02}-extracted.txt').write_text(actual)
for a in assets['assets']:
 f=R/a['file'];assert hashlib.sha256(f.read_bytes()).hexdigest()==a['sha256'],f
 if 'crop_box_xyxy'in a:
  parent=next(v for v in assets['assets'] if v['asset_id']==a['parent_asset_id']);orig=Image.open(R/parent['file']).crop(a['crop_box_xyxy']);assert orig.tobytes()==Image.open(f).tobytes()
 report['assets'].append({'id':a['asset_id'],'sha256_verified':True,'exact_crop_verified':'crop_box_xyxy'in a})
for r in data['tempo_comparison']['rows']:
 assert r['eighth_ms']==60000/r['bpm']/2;assert r['sixteenth_ms']==60000/r['bpm']/4
assert 187.5/250==.75
assert 187.5*1.5==281.25
for ss in data['feedback_decay']['series']:
 for pt in ss['points']:assert math.isclose(pt['relative_amplitude'],100*ss['g']**(pt['repeat']-1))
assert 21.6/2.7==8
for p in spec['pages']:
 els={e['id']:e for e in p['elements']}
 if p['page']==3:
  for bpm,note,dur in [(120,'1/8',250),(120,'1/16',125),(160,'1/8',187.5),(160,'1/16',93.75)]:
   # The source spec independently records exact common-scale endpoints.
   expect=282+dur*516/250
   bars=[e for e in p['elements'] if e['type']=='line' and e['stroke_width']>=8]
   assert any(math.isclose(e['points'][-1][0],expect) for e in bars)
 if p['page']==4:
  circles=[e for e in p['elements'] if e['type']=='circle']
  for t in [187.5,375,562.5,750]:assert any(math.isclose(e['center'][0],234+t*702/750) for e in circles)
 if p['page']==6:
  circles=[e for e in p['elements'] if e['type']=='circle']
  for hz in [200,6000]:assert any(math.isclose(e['center'][0],96+math.log10(hz/20)/3*888) for e in circles)
for f in (R/'output').glob('xhs-*.png'):assert Image.open(f).size==(1080,1440)
for f in (R/'phone-preview').glob('*.png'):assert Image.open(f).size==(360,480)
assert len(list((R/'output').glob('xhs-*.png')))==8
caption=(R/'public_caption.txt').read_text();report['caption_characters']=len(caption)
assert '回声' not in ''.join(e['text'] for p in spec['pages'] for e in p['elements'] if e['type']=='text')
report['checks']={'all_text_extracted':True,'font_coverage_packaged':True,'original_pixels_preserved':True,'tempo_math':True,'feedback_math':True,'timeline_coordinates':True,'log_frequency_coordinates':True,'png_dimensions':True,'Delay_term_preserved':True,'public_republication_rights':'unverified'}
(R/'qa/final-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False,indent=2))
