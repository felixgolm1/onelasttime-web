import re
import sys
with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

scripts = re.findall(r'<script.*?>([\s\S]*?)</script>', text)
script = scripts[19]
lines = script.split('\n')
open_b = 0
for i, line in enumerate(lines):
    l = re.sub(r'//.*', '', line)
    l = re.sub(r'".*?"', '""', l)
    l = re.sub(r"'.*?'", "''", l)
    l = re.sub(r"`.*?`", "``", l)
    open_b += l.count('{')
    open_b -= l.count('}')
    if 'function updateGlobalScenes' in line or 'function smoothScrollLoop' in line or open_b < 0:
        print(f'Line {i+1} [{open_b}]: {line.strip()[:80]}')
        
print(f'Final: {open_b}')
