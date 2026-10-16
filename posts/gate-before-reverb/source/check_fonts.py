"""Verify bundled font coverage for the current editable HTML and SVG copy."""
from pathlib import Path
from html.parser import HTMLParser
from fontTools.ttLib import TTFont
import json
R=Path(__file__).resolve().parents[1]
class TextOnly(HTMLParser):
 def __init__(self):super().__init__();self.values=[]
 def handle_data(self,data):self.values.append(data)
def text_chars():
 chars=set(chr(i) for i in range(32,127))
 for p in [R/'source/index.html',R/'research/RESEARCH_REPORT.html',*(R/'source/assets/diagrams').glob('*.svg')]:
  parser=TextOnly();parser.feed(p.read_text());chars.update(''.join(parser.values))
 return {c for c in chars if c not in '\r\n\t'} | {' ', '\u00a0'}
if __name__=='__main__':
 chars=text_chars();results={}
 for weight in [400,600]:
  f=TTFont(R/f'source/assets/fonts/NotoSansSC-{weight}.ttf');cmap=f.getBestCmap();missing=sorted(c for c in chars if ord(c) not in cmap)
  results[str(weight)]={'required_characters':len(chars),'missing':missing}
 (R/'qa').mkdir(exist_ok=True)
 (R/'qa/font-coverage.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
 print(results)
 assert all(not result['missing'] for result in results.values())
