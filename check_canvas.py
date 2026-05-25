import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('3d-test.html', 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

# Find canvas#c
for i, line in enumerate(lines):
    if 'id="c"' in line or "id='c'" in line:
        print(f'L{i+1}: {line.strip()[:100]}')

# Also check if tablewareset_base64.js is being referenced right
for i, line in enumerate(lines):
    if 'tablewareset_base64' in line or 'base64.js' in line:
        print(f'L{i+1}: {line.strip()[:100]}')
