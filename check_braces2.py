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

print(f'Final balance: {open_b}')
if open_b != 0:
    open_b = 0
    for i, line in enumerate(lines):
        l = re.sub(r'//.*', '', line)
        l = re.sub(r'".*?"', '""', l)
        l = re.sub(r"'.*?'", "''", l)
        l = re.sub(r"`.*?`", "``", l)
        open_b += l.count('{')
        open_b -= l.count('}')
        if open_b > 0 and i > len(lines) - 50:
            print(f'Line {i+1}: balance {open_b}')
