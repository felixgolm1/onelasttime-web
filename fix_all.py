import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'style.transform' in line and 'ranslate' in line:
        print(f"Line {i}: {repr(line)}")
        lines[i] = '          rev1.style.transform = 	ranslateY(px);\n'
    if 'style.transform' in line and 'scale()' in line:
        print(f"Line {i}: {repr(line)}")
        lines[i] = '             img.style.transform = scale();\n'

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print("Done fixing all powershell escapes.")
