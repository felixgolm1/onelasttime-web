import re

files = [
    'c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/index.html',
    'c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html'
]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        txt = f.read()

    txt = txt.replace('Hagamos de tu cena,<br>', 'Hagamos de tu cena<br>')
    txt = txt.replace('la mejor que hayas tenido nunca.</span>', 'la mejor que hayas tenido nunca</span>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(txt)

print("Text updated")
