import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace _scSmall calculation
content = content.replace(
    "const _scSmall = globalGlbCard._baseScaleFact * 0.65;",
    "const _scSmall = globalGlbCard._baseScaleFact * (window.matchMedia('(max-width: 768px)').matches ? 1.0 : 0.65);"
)

# Replace _scLarge calculation
content = content.replace(
    "const _scLarge = globalGlbCard._baseScaleFact * _GS_SC * 0.90;",
    "const _scLarge = globalGlbCard._baseScaleFact * _GS_SC * (window.matchMedia('(max-width: 768px)').matches ? (1.0/_GS_SC) : 0.90);"
)

# Replace _snapScale calculation
content = content.replace(
    "? (globalGlbCard._baseScaleFact * _gSY2 * 0.90)",
    "? (globalGlbCard._baseScaleFact * (window.matchMedia('(max-width: 768px)').matches ? 1.0 : (_gSY2 * 0.90)))"
)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done patching JS scales for mobile.")
