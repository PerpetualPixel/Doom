#!/usr/bin/env python3
"""Regenerate assets.js: the sprite sheets and gun art as data URIs.

Run from the repo root after changing anything in sprites/ or Guns/:
    python3 tools/embed_assets.py
"""
import base64, os, json
out = ['// Generated: the sprite sheets and gun art inlined as data URIs.',
       '// Why: when index.html is opened straight from the files (file://),',
       '// the browser forbids reading pixels back from images loaded off',
       '// disk, so the sheet slicing and background keying silently fail',
       '// and the game falls back to its procedural placeholder art.',
       '// Data URIs are exempt, so the real art works everywhere.',
       '// Rebuild with: python3 tools/embed_assets.py',
       'window.EMBEDDED_ASSETS = {']
for folder in ('sprites', 'Guns/My Guns', 'Guns/GunsNoBackground'):
    for name in sorted(os.listdir(folder)):
        path = f'{folder}/{name}'
        mime = 'image/jpeg' if name.lower().endswith(('.jpg', '.jpeg')) else 'image/png'
        data = base64.b64encode(open(path, 'rb').read()).decode()
        out.append(f'{json.dumps(path)}: "data:{mime};base64,{data}",')
out.append('};')
open('assets.js', 'w').write('\n'.join(out))
print('assets.js regenerated')
