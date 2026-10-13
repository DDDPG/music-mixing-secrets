from pathlib import Path
import json,hashlib,shutil,zipfile
R=Path(__file__).resolve().parents[1];P=R/'publicsafe';P.mkdir(exist_ok=True)
base=['README.md','RESEARCH_REPORT.md','research-report.html','index.html','caption.txt','CITATION.bib','RIGHTS.md','THIRD_PARTY_NOTICES.txt','LICENSE-AGPL-3.0.txt','requirements.txt','assets.json','design/design-plan.md','design/production_spec.json','design/visual-qa.md','research/sources.md','research/facts.json','research/term-map.json','research/data.json','research/story.md','research/page-plan.json','research/imagegen-prompt.txt','source/build_assets.py','source/build_carousel.py','source/render_carousel.py','source/render_report.py','source/apply_qa_refinements.py','source/validate.py','source/package.py','qa/render.json','qa/research-checks.json','qa/validation.json','qa/visual-review.json','qa/report/render.json']
base+=sorted(str(p.relative_to(R)) for p in (R/'assets').rglob('*') if p.is_file())
output=[f'output/{i:02d}.png' for i in range(1,13)]+[f'phone-preview/{i:02d}.png' for i in range(1,13)]+['output/合成器的前后左右_图文.pdf','output/合成器的左右宽度与前后层次_研究报告.pdf']
all_files=sorted(set(base+output));assert len(all_files)==len(base+output)
for rel in all_files:
 src=R/rel;assert src.is_file(),rel;dst=P/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
sourcezip=P/'synth-placement-editable-source.zip'
with zipfile.ZipFile(sourcezip,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for rel in sorted(base):z.write(R/rel,arcname='synth-placement/'+rel)
assert zipfile.ZipFile(sourcezip).testzip() is None
all_files+=['synth-placement-editable-source.zip']
manifest={'slug':'synth-placement','title':'合成器的前后左右','carousel_pages':12,'report_pages':9,'cover':'output/01.png','carousel_pdf':'output/合成器的前后左右_图文.pdf','research_pdf':'output/合成器的左右宽度与前后层次_研究报告.pdf','caption':'caption.txt','source_zip':'synth-placement-editable-source.zip','editable_entrypoint':'index.html','publication_scope':'post-specific materials only; vendor screenshot rights limitations retained','source_zip_distribution':'Library delivery; GitHub may use expanded sources and omit ZIP','files':[]}
for rel in sorted(all_files):
 p=P/rel;manifest['files'].append({'path':rel,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(P/'public-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
(P/'SHA256SUMS').write_text('\n'.join(e['sha256']+'  '+e['path'] for e in manifest['files'])+'\n')
(R/'PUBLIC_DELIVERABLES.json').write_text(json.dumps({'public_root':str(P),'manifest':str(P/'public-manifest.json'),'file_count':len(manifest['files']),'source_zip_bytes':sourcezip.stat().st_size,'source_zip_sha256':hashlib.sha256(sourcezip.read_bytes()).hexdigest()},indent=2))
print((R/'PUBLIC_DELIVERABLES.json').read_text())
