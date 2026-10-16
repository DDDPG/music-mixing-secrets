from pathlib import Path
from weasyprint import HTML
import fitz
from PIL import Image

p = Path(__file__).resolve().parents[1]
for folder in ('output', 'phone-preview', 'qa/report-preview'):
    (p / folder).mkdir(parents=True, exist_ok=True)
for name, out in [('index.html', 'carousel.pdf'), ('research-report.html', 'research-report.pdf')]:
    HTML(filename=str(p / name)).write_pdf(p / 'output' / out)
    with fitz.open(p / 'output' / out) as document:
        if name == 'index.html':
            for folder in ('output', 'phone-preview'):
                for old in (p / folder).glob('[0-9][0-9].png'):
                    old.unlink()
            for i, page in enumerate(document, 1):
                pix = page.get_pixmap(matrix=fitz.Matrix(4/3, 4/3), alpha=False)
                pix.save(p / f'output/{i:02d}.png')
                with Image.open(p / f'output/{i:02d}.png') as image:
                    image.resize((360, 480), Image.Resampling.LANCZOS).save(p / f'phone-preview/{i:02d}.png')
            sheet = Image.new('RGB', (1080, ((len(document) + 2) // 3) * 480), '#dddddd')
            for i in range(len(document)):
                with Image.open(p / f'phone-preview/{i+1:02d}.png') as image:
                    sheet.paste(image, ((i % 3) * 360, (i // 3) * 480))
            sheet.save(p / 'output/contact-sheet.jpg', quality=95)
        else:
            for old in (p / 'qa/report-preview').glob('*.png'):
                old.unlink()
            for i, page in enumerate(document, 1):
                page.get_pixmap(matrix=fitz.Matrix(.65, .65), alpha=False).save(p / f'qa/report-preview/{i:02d}.png')
            thumb_w, thumb_h = 248, 351
            sheet = Image.new('RGB', (thumb_w * 3, ((len(document) + 2) // 3) * thumb_h), '#dddddd')
            for i in range(len(document)):
                with Image.open(p / f'qa/report-preview/{i+1:02d}.png') as image:
                    sheet.paste(image.resize((thumb_w, thumb_h), Image.Resampling.LANCZOS), ((i % 3) * thumb_w, (i // 3) * thumb_h))
            sheet.save(p / 'qa/report-contact.jpg', quality=95)
        print(out, len(document), 'pages')
