import re

files = [
    'c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/index.html',
    'c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html'
]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        txt = f.read()

    txt = txt.replace('z-index:9999998', 'z-index:90000000')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(txt)

print("Updated embers-canvas z-index to 90000000")
