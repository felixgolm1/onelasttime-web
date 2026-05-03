import sys

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

depth = 0
for i in range(1296, 1403):
    line = lines[i]
    depth += line.count('<div') - line.count('</div')
    print(f"L{i+1} [depth={depth}]: {line.strip()}")
