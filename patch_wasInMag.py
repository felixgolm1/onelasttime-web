import sys

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = """          if (window.wasInMagazine) {
            window.wasInMagazine = false;
            if (volume) volume.style.transform = '';
            mainDeck.style.transform = '';
            mainDeck.style.opacity = '';
            mainDeck.style.filter = '';
            gsap.set(scBoard, { y: '0vh' });
            scrollTl.progress(0);
            scrollTl.progress(Math.min(1, prog / 2.2));
          }"""

replacement = """          if (window.wasInMagazine) {
            window.wasInMagazine = false;
            if (volume) volume.style.transform = '';
            mainDeck.style.transform = '';
            mainDeck.style.opacity = '';
            mainDeck.style.filter = '';
            gsap.set(scBoard, { y: '0vh' });
            scrollTl.progress(0);
            scrollTl.progress(Math.min(1, prog / 2.2));
            
            let hiddenFaces = document.getElementById("mainDeck").querySelectorAll('.box-flap, .tuck-lip, .dust-flap, .face-back, .face-front, .face-bottom, .interior-card, .face-right');
            hiddenFaces.forEach(f => f.style.display = '');
          }"""

# Normalizamos los saltos de línea para el replace
target_norm = target.replace('\r', '')
replacement_norm = replacement.replace('\r', '')
content_norm = content.replace('\r', '')

if target_norm in content_norm:
    content_norm = content_norm.replace(target_norm, replacement_norm)
    # Escribimos de vuelta
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content_norm)
    print("Replace OK")
else:
    print("Target not found")
