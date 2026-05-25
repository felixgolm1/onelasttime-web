import re
import sys
with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

script = re.findall(r'<script.*?>([\s\S]*?)</script>', text)[19]
lines = script.split('\n')

open_b = 0
for i, line in enumerate(lines):
    # simple removal of strings/comments for this line
    l = re.sub(r'//.*', '', line)
    l = re.sub(r'".*?"', '""', l)
    l = re.sub(r"'.*?'", "''", l)
    l = re.sub(r"`.*?`", "``", l)
    open_b += l.count('{')
    open_b -= l.count('}')
    if i >= 4980 and i < 5050:
        sys.stdout.buffer.write(f'{i+1} [{open_b}]: {line.strip()[:60]}\n'.encode('utf-8'))
