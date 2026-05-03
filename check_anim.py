import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web-produccion\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(3989, 4030):
    print(lines[i].strip())
