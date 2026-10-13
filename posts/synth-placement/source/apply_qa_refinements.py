from pathlib import Path
import json
R=Path(__file__).resolve().parents[1];p=R/'design/production_spec.json';s=json.loads(p.read_text())
def el(n,id):return next(x for x in s['pages'][n-1]['elements'] if x['id']==id)
el(1,'roles')['text']='主旋律要清楚 · 铺底要支撑 · 琶音要有位置'
el(4,'intro')['text']='湿声（Wet）相对更多，可能更退后，也可能更糊。\n还要听干声电平、频谱和起音。'
el(4,'condition')['text']='同源、同窗、同一标尺；RMS = 均方根'
for id in ['dryA','dryB']:el(4,id)['text']='Dry 干声';el(4,id)['box'][2]=154
for id in ['wetA','wetB']:el(4,id)['text']='Wet 湿声';el(4,id)['box'][2]=154
el(4,'caveat')['text']='非房间 DRR（直达/混响能量比），不能换算距离。\n也不能推断听感倍数；总 RMS 还受两路相关性影响。\n两个 dBFS 读数不能直接相加。'
el(4,'caveat')['box']=[72,1236,936,126]
el(5,'caveat')['text']=el(5,'caveat')['text'].replace('快速 Arp','快速琶音')
el(8,'post_label')['box']=[420,558,270,54]
s['qa_refinements']=['P1 Chinese role labels before English definitions on P9','P4 defines Dry/Wet/RMS/DRR while keeping scale and numerical caveats','P5 first-use Arp replaced by Chinese 琶音','P8 Send label moved left of the vertical path; unchanged text size']
p.write_text(json.dumps(s,ensure_ascii=False,indent=2))
