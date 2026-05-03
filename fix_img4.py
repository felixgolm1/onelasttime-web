import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Brute force string replace
lines = content.split('\n')
for i in range(len(lines)):
    if 'scale();' in lines[i]:
        lines[i] = '             img.style.transform = scale();'
    if 'rightness();' in lines[i]:
        lines[i] = '             img.style.filter = rightness();'

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print("Brute force replaced.")
