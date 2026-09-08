import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. placeTableSet
content = re.sub(
    r'(const size = box\.getSize\(new THREE\.Vector3\(\)\);\s*)const targetWidth = 9\.0;\s*(const scale = targetWidth / Math\.max\(size\.x, size\.z\);)',
    r"\1const isMobile = window.matchMedia('(max-width: 768px)').matches;\n    const targetWidth = isMobile ? 9.0 * 1.3 : 9.0;\n    \2",
    content
)

# 2. placeWineGlass
content = re.sub(
    r'(const size = box\.getSize\(new THREE\.Vector3\(\)\);\s*)const targetH = 4\.16;\s*(const scale   = targetH / Math\.max\(size\.y, 0\.001\);)',
    r"\1const isMobile = window.matchMedia('(max-width: 768px)').matches;\n    const targetH = isMobile ? 4.16 * 1.3 : 4.16;\n    \2",
    content
)

# 3. buildAllCards
content = re.sub(
    r'(const w = buildCard\(cardData\[i\], p\.x, p\.z, p\.rY, p\.rZ, p\.yOffset\);\s*)(scene\.add\(w\);)',
    r"\1if (window.matchMedia('(max-width: 768px)').matches) { w.scale.setScalar(1.3); }\n        \2",
    content
)

# 4. polaroidMesh
content = re.sub(
    r'(// Escala final\s*)window\.polaroidMesh\.scale\.set\(0\.83, 0\.83, 0\.83\);',
    r"\1const polS = window.matchMedia('(max-width: 768px)').matches ? 0.83 * 1.3 : 0.83;\n      window.polaroidMesh.scale.set(polS, polS, polS);",
    content
)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated scaling logic")
