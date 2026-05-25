import sys
with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = list(re.finditer(r'targetProg\s*=', text))
with open('debug_targetProg.txt', 'w', encoding='utf-8') as out:
    for m in matches:
        out.write('targetProg: ' + text[m.start()-50:m.start()+150] + '\n\n')
