import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the scale from the pile of cards (which contains CSS3DObjects that crash Safari)
content = re.sub(
    r"if \(window\.matchMedia\('\(max-width: 768px\)'\)\.matches\) \{ w\.scale\.setScalar\(1\.3\); \}\n\s*scene\.add\(w\);",
    r"scene.add(w);",
    content
)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed scale from cards")
