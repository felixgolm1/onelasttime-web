import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(len(lines)):
    if 'img.style.transform = scale();' in lines[i]:
        lines[i] = '             img.style.transform = scale();\n'
    if 'img.style.filter =  rightness();' in lines[i]:
        lines[i] = '             img.style.filter = rightness();\n'

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print("Lines replaced via python script.")
