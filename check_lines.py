import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'function smoothScrollLoop' in line:
        print(f"smoothScrollLoop at line {i+1}")
    if 'function init3DScene' in line:
        print(f"init3DScene at line {i+1}")
