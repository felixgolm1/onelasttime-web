with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()
lines = text.split('\n')
for i, line in enumerate(lines):
    if 'portalP' in line:
        print(f'{i}: {line.strip()}')
