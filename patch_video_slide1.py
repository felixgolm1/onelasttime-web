import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = '<img src="assets/img/annacartes.jpg" style="width: 100%; height: 100%; object-fit: cover; border-radius: 4px;">'
new = '<video src="assets/img/Anna Felix cena.mp4" autoplay loop muted playsinline style="width: 100%; height: 100%; object-fit: cover; border-radius: 4px;"></video>'

if old in content:
    content = content.replace(old, new)
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("OK: video inyectado en slide 1")
else:
    print("ERROR: no se encontro el texto exacto")
