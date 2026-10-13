"""Build a self-contained, explicit-allowlist publication package."""
from pathlib import Path
import hashlib,json,shutil,zipfile
P=Path(__file__).resolve().parents[1];D=P/'public';D.mkdir(exist_ok=True)
base=['README.md','RESEARCH_REPORT.md','RESEARCH_REPORT.html','RIGHTS_AND_SOURCES.md','THIRD_PARTY_NOTICES.txt','LICENSE-AGPL-3.0.txt','CITATION.bib','public_caption.txt','index.html','assets.json',
'research/sources.md','research/sources.json','research/facts.json','research/term-map.json','research/diagram_data.json','research/model_samples.csv','research/page-plan.json','research/STORY.md',
'design/production_spec.json','design/design-plan.md','design/visual-qa.md','qa/QA_REPORT.md','qa/verification.json',
'source/prepare_fonts.py','source/generate_visuals.py','source/build_carousel.py','source/render_carousel.py','source/render_report.py','source/package_public.py','source/seed-editorial.html',
'assets/source/fabfilter-pro-c-3-official.jpg','assets/derived/compressor-controls.png','assets/derived/attack-release.png','assets/derived/gain-controls.png',
'assets/diagrams/attack-model.svg','assets/diagrams/release-model.svg','assets/diagrams/tempo-spacing.svg','assets/diagrams/syllable-concept.svg',
'assets/fonts/NotoSansSC-Variable.ttf','assets/fonts/NotoSansSC-400.ttf','assets/fonts/NotoSansSC-600.ttf','assets/fonts/NotoSans-Regular.ttf','assets/fonts/OFL.txt','assets/fonts/NotoSans-OFL-copyright.txt']
base += [f'assets/diagrams/page-{i:02}-geometry.svg' for i in range(1,10)]
files=base+['output/RESEARCH_REPORT.pdf','output/vocal-compression-shaping.pdf','output/contact-sheet.png']+[f'output/xhs-{i:02}.png' for i in range(1,10)]+[f'phone-preview/xhs-{i:02}-360.png' for i in range(1,10)]
for f in files:
 src=P/f;assert src.is_file(),src;dst=D/f;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dst)
archive=P/'output/vocal-compression-shaping-editable-source.zip'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for f in base:z.write(P/f,'vocal-compression-shaping/'+f)
with zipfile.ZipFile(archive) as z:assert z.testzip() is None;assert len(z.namelist())==len(base)
shutil.copyfile(archive,D/'output'/archive.name);files.append('output/'+archive.name)
manifest=[dict(path=f,size=(D/f).stat().st_size,sha256=hashlib.sha256((D/f).read_bytes()).hexdigest()) for f in sorted(files)]
(D/'SHA256SUMS').write_text('\n'.join(f'{m["sha256"]}  {m["path"]}' for m in manifest)+'\n')
manifest.append(dict(path='SHA256SUMS',size=(D/'SHA256SUMS').stat().st_size,sha256=hashlib.sha256((D/'SHA256SUMS').read_bytes()).hexdigest()))
(P/'PUBLIC_FILELIST.json').write_text(json.dumps({'publication_root':'public','file_count':len(manifest),'files':manifest},ensure_ascii=False,indent=2))
# Do not include raw caches, extracted source material, tool logs, or build history.
actual={str(p.relative_to(D)) for p in D.rglob('*') if p.is_file()};assert actual==set(m['path'] for m in manifest)
print('Public allowlist',len(manifest),'files; source ZIP',archive.stat().st_size,'bytes')
print('ZIP SHA256',hashlib.sha256(archive.read_bytes()).hexdigest())
