import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web-produccion\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(2135, 2150):
    print(lines[i].strip())
