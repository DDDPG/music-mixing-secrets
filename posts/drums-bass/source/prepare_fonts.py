"""Rebuild self-contained OFL font subsets from the original variable font."""
from pathlib import Path
import json
from fontTools.ttLib import TTFont
from fontTools import subset
from fontTools.varLib.instancer import instantiateVariableFont
R=Path(__file__).resolve().parent
spec=json.loads((R/'production_spec.json').read_text())
text=''.join(e['text'] for p in spec['pages'] for e in p['elements'] if e['type']=='text')
for weight in [400,600]:
 font=TTFont(R/'assets/fonts/NotoSansSC-Variable.ttf')
 instantiateVariableFont(font,{'wght':weight},inplace=True)
 options=subset.Options();options.layout_features='*';options.name_IDs=['*'];options.name_legacy=True;options.name_languages=['*']
 sub=subset.Subsetter(options=options);sub.populate(text=text);sub.subset(font)
 font.save(R/f'assets/fonts/NotoSansSC-{weight}.ttf')
 print('Prepared weight',weight)
