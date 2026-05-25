import re
import sys
with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

script = re.findall(r'<script.*?>([\s\S]*?)</script>', text)[19]
lines = script.split('\n')
open_b = 0
for i, line in enumerate(lines):
    l = re.sub(r'//.*', '', line)
    l = re.sub(r'".*?"', '""', l)
    l = re.sub(r"'.*?'", "''", l)
    l = re.sub(r"`.*?`", "``", l)
    open_b += l.count('{')
    open_b -= l.count('}')
    
    if i == 2746:
        print(f'Before updateGlobalScenes: {open_b}')
    if i == 2765:
        print(f'Before smoothScrollLoop: {open_b}')
        
