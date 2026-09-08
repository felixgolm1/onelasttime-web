import re

files = ['3d-test.html', 'index.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. GSAP init for morphGroup
    content = content.replace(
        "gsap.set(morphGroup, { x: 0, y: 0, scaleX: 1, scaleY: 1, rotation: 0 });",
        "gsap.set(morphGroup, { x: 0, y: 0, scaleX: window.innerWidth <= 768 ? 0.85 : 1, scaleY: window.innerWidth <= 768 ? 0.85 : 1, rotation: 0 });"
    )
    
    # 2. _scSmall calculation
    content = content.replace(
        "const _scSmall = globalGlbCard._baseScaleFact * 0.65;",
        "const _scSmall = globalGlbCard._baseScaleFact * (window.innerWidth <= 768 ? 0.5525 : 0.65);"
    )
    
    # 3. CSS for .sc-card in mobile media query
    if '.sc-card {' not in content.split('@media screen and (max-width: 768px) {')[1]:
        content = content.replace(
            '@media screen and (max-width: 768px) {',
            '@media screen and (max-width: 768px) {\n  .sc-card { transform: scale(0.85); transform-origin: center center; }\n'
        )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
