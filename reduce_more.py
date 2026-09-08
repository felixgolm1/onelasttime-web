import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update _scSmall
content = content.replace(
    "const _scSmall = globalGlbCard._baseScaleFact * (window.matchMedia('(max-width: 768px)').matches ? 0.75 : 0.65);",
    "const _scSmall = globalGlbCard._baseScaleFact * (window.matchMedia('(max-width: 768px)').matches ? 0.5 : 0.65);"
)

# 2. Update introState
content = content.replace(
    "let introState = { scaleMult: window.matchMedia('(max-width: 768px)').matches ? 1.333333 : 1.5 };",
    "let introState = { scaleMult: window.matchMedia('(max-width: 768px)').matches ? 2.0 : 1.5 };"
)

# 3. Update _snapScale
content = content.replace(
    "? (globalGlbCard._baseScaleFact * (window.matchMedia('(max-width: 768px)').matches ? 0.75 : (_gSY2 * 0.90)))",
    "? (globalGlbCard._baseScaleFact * (window.matchMedia('(max-width: 768px)').matches ? 0.5 : (_gSY2 * 0.90)))"
)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done reducing card size on table by another 50%.")
