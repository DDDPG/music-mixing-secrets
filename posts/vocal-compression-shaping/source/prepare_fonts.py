from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools import subset
from fontTools.varLib.instancer import instantiateVariableFont
P=Path(__file__).resolve().parents[1]
text=''.join(p.read_text() for p in P.rglob('*') if p.suffix in ['.md','.txt','.html','.json','.svg','.css'])+''.join(chr(x) for x in range(32,127))
for weight in [400,600]:
 font=TTFont(P/'assets/fonts/NotoSansSC-Variable.ttf')
 instantiateVariableFont(font,{'wght':weight},inplace=True)
 options=subset.Options();options.layout_features='*';options.name_IDs=['*'];options.name_legacy=True;options.name_languages=['*']
 sub=subset.Subsetter(options=options);sub.populate(text=text);sub.subset(font)
 font.save(P/f'assets/fonts/NotoSansSC-{weight}.ttf')
 print('Prepared',weight)
