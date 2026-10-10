"""Verify preserved artifacts and embedded research-report illustrations without network access."""
from pathlib import Path
import hashlib, json, re
ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / 'PRESERVED_FINALS.json').read_text())
errors = []
for item in manifest['files']:
    path = ROOT / item['file']
    if not path.is_file():
        errors.append(f'Missing final artifact: {item["file"]}')
    elif hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
        errors.append(f'Changed final artifact: {item["file"]}')
reports = list((ROOT / 'posts').glob('*/RESEARCH_REPORT.md'))
for report in reports:
    for target in re.findall(r'!\[[^\]]*\]\(([^)]+)\)', report.read_text()):
        if not target.startswith(('http:', 'https:')) and not (report.parent / target).is_file():
            errors.append(f'Missing illustration in {report.relative_to(ROOT)}: {target}')
for path in ROOT.rglob('*.py'):
    try:
        compile(path.read_text(), str(path.relative_to(ROOT)), 'exec')
    except SyntaxError as error:
        errors.append(f'Invalid Python: {path.relative_to(ROOT)}: {error}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'OK: {len(manifest["files"])} original final artifacts; {len(reports)} reports; Python syntax checked.')
print('This does not execute a rebuild or verify external websites.')
