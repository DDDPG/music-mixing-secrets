"""Export only explicitly approved public deliverable files; never copy cache trees."""
from pathlib import Path
import json,hashlib,shutil,zipfile
R=Path(__file__).resolve().parents[1];P=R/'public';P.mkdir(exist_ok=True)
files=['README.md','RIGHTS.md','CITATION.bib','metadata.json','index.html',
'research/RESEARCH_REPORT.md','research/RESEARCH_REPORT.html','research/RESEARCH_REPORT.pdf','research/facts.json','research/sources.json','research/sources.md','research/term-map.json',
'story/ARTICLE.md','story/page-plan.json','story/public_caption.txt',
'design/production_spec.json','design/design-plan.md','design/visual-qa.md',
'assets/assets.json','assets/diagram_data.json','assets/source/reel-adt-official-product.png','assets/source/reel-adt-manual-interface.jpeg',
'qa/FINAL_QA.md','qa/research-qa.md','qa/font-metrics.json','qa/bibtex-verification.txt','qa/reproduction-check.json',
'output/snare-adt-before-reverb.pdf','output/contact-sheet.png']
files += [f'assets/derived/reel-adt-{x}.png' for x in ['position','src','adt','lfo','monitor']]
files += [f'assets/fonts/{x}' for x in ['NotoSansSC-Variable.ttf','NotoSansSC-400.ttf','NotoSansSC-600.ttf','NotoSans-Regular.ttf','OFL.txt','NotoSans-OFL-copyright.txt']]
files += [f'assets/diagrams/{n}.{e}' for n in ['parallel-routing','time-reference','comb-response'] for e in ['svg','png']]
files += [f'assets/diagrams/page-{i:02}-geometry.svg' for i in range(1,9)]
files += [f'output/xhs-{i:02}.png' for i in range(1,9)]
files += [f'phone-preview/xhs-{i:02}-360.png' for i in range(1,9)]
files += [f'source/{x}' for x in ['build_research.py','build_carousel.py','render_report.py','render_carousel.py','finalize_assets.py','package_public.py','seed-editorial.html','LICENSE-AGPL-3.0.txt','THIRD_PARTY_NOTICES.txt']]
assert len(files)==len(set(files))
assert not any('private' in x or x.endswith('.blg') or x.startswith('repo_') for x in files)
for f in files:
 src=R/f;assert src.is_file(),src;dest=P/f;dest.parent.mkdir(parents=True,exist_ok=True);dest.unlink(missing_ok=True);shutil.copyfile(src,dest)
manifest=[{'path':f,'bytes':(P/f).stat().st_size,'sha256':hashlib.sha256((P/f).read_bytes()).hexdigest()} for f in sorted(files)]
(P/'SHA256SUMS').write_text(''.join(f'{r["sha256"]}  {r["path"]}\n' for r in manifest))
(P/'PUBLIC_MANIFEST.json').write_text(json.dumps({'author':'Kangdi Wang','allowed_files_only':True,'excluded':['full vendor manuals','cached webpages','private original inputs','execution logs','internal status'],'vendor_republication_clearance':'unverified','files':manifest},ensure_ascii=False,indent=2)+'\n')
zip_path=P/'snare-adt-editable-source.zip'
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for f in sorted(files+['SHA256SUMS','PUBLIC_MANIFEST.json']):z.write(P/f,'snare-adt-before-reverb/'+f)
with zipfile.ZipFile(zip_path) as z:assert z.testzip() is None
allfiles=sorted(files+['SHA256SUMS','PUBLIC_MANIFEST.json','snare-adt-editable-source.zip'])
final={'public_root':str(P),'author':'Kangdi Wang','status':'content_and_visual_qa_complete','vendor_republication_clearance':'unverified','files':[{'path':f,'absolute_path':str(P/f),'bytes':(P/f).stat().st_size,'sha256':hashlib.sha256((P/f).read_bytes()).hexdigest()} for f in allfiles]}
(R/'DELIVERY_MANIFEST.json').write_text(json.dumps(final,ensure_ascii=False,indent=2)+'\n')
print('Public files:',len(allfiles),'ZIP bytes:',zip_path.stat().st_size)
print('ZIP SHA256',hashlib.sha256(zip_path.read_bytes()).hexdigest())
