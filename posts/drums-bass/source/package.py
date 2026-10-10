"""Build a portable ZIP of this post without recursively including generated ZIPs."""
from pathlib import Path
import zipfile
R = Path(__file__).resolve().parent
with zipfile.ZipFile(R.parent / (R.parent.name + '-source.zip'), 'w', zipfile.ZIP_DEFLATED) as z:
    for f in sorted(R.rglob('*')):
        if f.is_file() and f.suffix != '.zip' and '__pycache__' not in f.parts:
            z.write(f, f.relative_to(R))
