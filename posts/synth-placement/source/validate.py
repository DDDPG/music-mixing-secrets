from pathlib import Path
import json,re,hashlib,math,subprocess,shutil
from PIL import Image
from fontTools.ttLib import TTFont
import fitz
R=Path(__file__).resolve().parents[1]
spec=json.loads((R/'design/production_spec.json').read_text())
qa=json.loads((R/'qa/render.json').read_text());assert qa['pages']==12 and not qa['out_of_safe_area']
chars=set(''.join(e.get('text','') for p in spec['pages'] for e in p['elements'])+(R/'RESEARCH_REPORT.md').read_text())
cmap=set()
for p in (R/'assets/fonts').glob('*.ttf'):cmap.update(TTFont(p).getBestCmap())
missing=sorted(c for c in chars if not c.isspace() and ord(c) not in cmap);assert not missing,missing
crop_results=[]
for src,name,box in [('ableton-utility-official.png','utility-width-balance.png',(7,142,270,319)),('fabfilter-pro-r-2-maincontrols-official.jpg','pro-r-predelay-distance.png',(27,43,520,205)),('fabfilter-pro-r-2-maincontrols-official.jpg','pro-r-brightness-width-mix.png',(775,43,1270,205))]:
 im=Image.open(R/'assets/source'/src).crop(box);crop=Image.open(R/'assets/derived'/name);assert im.tobytes()==crop.tobytes();crop_results.append(name)
for a in json.loads((R/'assets.json').read_text()):assert hashlib.sha256((R/a['file']).read_bytes()).hexdigest()==a['sha256']
assert math.isclose(10**(6/20),1.9952623149688795)
assert 10*48000/1000==480 and 40*48000/1000==1920
bib=R/'qa/bibtex';bib.mkdir(exist_ok=True)
(bib/'check.aux').write_text('\\relax\n\\citation{wang2026musicmixingsecrets}\n\\bibstyle{check}\n\\bibdata{../../CITATION}\n')
(bib/'check.bst').write_text('ENTRY { author title year url } {} {}\nFUNCTION {misc} { author write$ newline$ title write$ newline$ year write$ newline$ url write$ newline$ }\nREAD\nITERATE {call.type$}\n')
subprocess.run(['bibtex','check'],cwd=bib,check=True,capture_output=True)
parsed=(bib/'check.bbl').read_text().splitlines();assert parsed==['Kangdi, Wang','Music Mixing Secrets','2026','https://github.com/DDDPG/music-mixing-secrets'],parsed
car=fitz.open(R/'output/合成器的前后左右_图文.pdf');rep=fitz.open(R/'output/合成器的左右宽度与前后层次_研究报告.pdf');assert len(car)==12 and len(rep)==9
alltext=''.join(p.get_text() for p in car)+''.join(p.get_text() for p in rep)
assert '\ufffd' not in alltext
assert not any(t in alltext for t in ['Apple Notes','笔记ID','来自笔记','原始笔记','source_note','20261013'])
for n in range(1,13):
 assert Image.open(R/f'output/{n:02d}.png').size==(1080,1440)
 assert Image.open(R/f'phone-preview/{n:02d}.png').size==(360,480)
endlinks=car[-1].get_links();assert any(l.get('uri')==parsed[-1] for l in endlinks)
post_bounds=[]
for b in car[7].get_text('dict')['blocks']:
 for l in b.get('lines',[]):
  for sp in l['spans']:
   if 'Post-Fader Send' in sp['text']:post_bounds.append(sp['bbox'][2]/.75)
assert post_bounds and max(post_bounds)<690,post_bounds
result={'status':'passed','carousel_pages':12,'report_pages':9,'full_and_phone_dimensions':'passed','safe_area':'passed','fonts_missing_chars':missing,'exact_crop_pixel_checks':crop_results,'all_asset_checksums':'passed','citation_parsed_fields':parsed,'citation_pdf_link':'passed','send_label_right_edge_css_px':max(post_bounds),'private_source_content_scan':'passed','no_audio_measurement_claimed':True,'vendor_general_republication_permission':'unverified; limited educational-commentary basis explicit'}
(R/'qa/validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False,indent=2))
