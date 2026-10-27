import json
from pathlib import Path

d = json.loads(Path('power_bi/audit_layout.json').read_text(encoding='utf-8'))
def texts(x):
    if isinstance(x, dict):
        for k,v in x.items():
            if k == 'value' and isinstance(v,str): yield v
            else: yield from texts(v)
    elif isinstance(x,list):
        for v in x: yield from texts(v)
out=[]
for path,p in d.items():
    if not path.endswith('/page.json'): continue
    out.append('\nPAGE '+p['displayName'])
    prefix=path.rsplit('/',1)[0]+'/visuals/'
    for k,v in d.items():
        if not k.startswith(prefix): continue
        vis=v.get('visual',{})
        title=vis.get('visualContainerObjects',{}).get('title',[])
        out.append(json.dumps({'id':v['name'],'type':vis.get('visualType'),'position':v.get('position'),'title':title,'text':list(texts(vis.get('objects',{}))), 'fields':vis.get('query',{}).get('queryState'), 'filters':v.get('filterConfig'),'sort':vis.get('query',{}).get('sortDefinition')},ensure_ascii=False))
    out.append('INTERACTIONS '+json.dumps(p.get('visualInteractions',[])))
Path('power_bi/audit_visual_summary.txt').write_text('\n'.join(out),encoding='utf-8')
print('\n'.join(out))
