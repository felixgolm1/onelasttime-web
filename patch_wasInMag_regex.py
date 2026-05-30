import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Usamos regex para ignorar diferencias en espacios en blanco
pattern = re.compile(
    r'(if\s*\(window\.wasInMagazine\)\s*\{\s*window\.wasInMagazine\s*=\s*false;\s*if\s*\(volume\)\s*volume\.style\.transform\s*=\s*\'\';\s*mainDeck\.style\.transform\s*=\s*\'\';\s*mainDeck\.style\.opacity\s*=\s*\'\';\s*mainDeck\.style\.filter\s*=\s*\'\';\s*gsap\.set\(scBoard,\s*\{\s*y:\s*\'0vh\'\s*\}\);\s*scrollTl\.progress\(0\);\s*scrollTl\.progress\(Math\.min\(1,\s*prog\s*/\s*2\.2\)\);\s*)(\})',
    re.MULTILINE
)

replacement = r"\1\n            let hiddenFaces = document.getElementById('mainDeck').querySelectorAll('.box-flap, .tuck-lip, .dust-flap, .face-back, .face-front, .face-bottom, .interior-card, .face-right');\n            hiddenFaces.forEach(f => f.style.display = '');\n          \2"

if pattern.search(content):
    content_new = pattern.sub(replacement, content)
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content_new)
    print("Regex Replace OK")
else:
    print("Regex Target not found")
