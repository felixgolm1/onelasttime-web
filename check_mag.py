with open('3d-test.html', 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

for i, line in enumerate(lines):
    if 'magazine-content' in line:
        print(f'{i+1}: {line.strip()}')
