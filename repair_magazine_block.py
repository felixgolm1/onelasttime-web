# -*- coding: utf-8 -*-
import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find the broken section - from the corrupted comment at 4917 to the end of the duplicate block
# We need to find what was BEFORE the corruption (the box scaling logic)
# and restore the magazine if block cleanly

# The broken block starts at the comment that got merged:
# '// El magazine-scene tiene un scale(0.85)           // Obtener la posicion real'
# and continues until end of the duplicate overlay block

old_broken = re.search(
    r'// El magazine-scene tiene un scale\(0\.85\)           // Obtener la posicion real del recuadro en pantalla\n'
    r'           const magContent = magazineScene\.querySelector\(\'\.magazine-content\'\);[\s\S]*?'
    r'}\n            \} // 0 to 1 smooth\n'
    r'            \n'
    r'            const baseW = window\.innerWidth > 768 \? 466 : window\.innerWidth \* 0\.9;\n'
    r'            const baseH = window\.innerWidth > 768 \? 626 : window\.innerWidth \* 1\.3;',
    text
)

if old_broken:
    print(f'Found broken block at chars {old_broken.start()} to {old_broken.end()}')
    print('Length:', len(old_broken.group(0)))
else:
    print('Pattern not found, trying simpler search')
    idx = text.find('// El magazine-scene tiene un scale(0.85)           // Obtener la posicion real')
    print(f'Simple find index: {idx}')
    if idx >= 0:
        print('Context:', repr(text[idx:idx+200]))
