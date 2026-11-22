#!/usr/bin/env bash
# Regenera TODO (5 idiomas): historias, posts y panel. Requiere playwright (node) y python3.
set -e; cd "$(dirname "$0")"
rm -rf html ../stories ../posts ../profile-grid/{fr,de,es,pt,en}
python3 build_stories.py >/dev/null; python3 build_extra.py; python3 build_grid.py
node render.js
python3 - <<'P'
from PIL import Image
import os
base='../profile-grid'
for l in ['fr','de','es','pt','en']:
    im=Image.open(f'{base}/{l}/_full.png').convert('RGB')
    for i,(r,c) in enumerate([(2,3),(2,2),(2,1),(1,3),(1,2),(1,1)],1):
        im.crop(((c-1)*1080,(r-1)*1440,c*1080,r*1440)).save(f'{base}/{l}/subir-{i}_fila{r}-col{c}.jpg',quality=95,subsampling=0)
    im.resize((1080,960),Image.LANCZOS).save(f'{base}/{l}/_vista-previa.jpg',quality=90); os.remove(f'{base}/{l}/_full.png')
P
