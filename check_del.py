import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web-produccion\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(5142, len(lines)):
    if 'function ' in lines[i]:
        print(lines[i].strip())
