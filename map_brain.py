with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
total = len(lines)
print(f'Total lines: {total}')

# Find key boundaries
for i, line in enumerate(lines):
    if 'initBrainRenderer' in line or ('function initBrain' in line):
        print(f'initBrain at line {i+1}: {line[:80]}')
    if 'CSS2DRenderer' in line and 'src=' in line:
        print(f'CSS2DRenderer script at line {i+1}: {line[:80]}')
    if 'brain-canvas' in line and 'appendChild' in line:
        print(f'brain-canvas append at line {i+1}: {line[:80]}')
