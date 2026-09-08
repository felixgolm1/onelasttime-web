import re

files = ['3d-test.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Revert _scSmall logic
    content = content.replace(
        "const _scSmall = globalGlbCard._baseScaleFact * (window.matchMedia('(max-width: 768px)').matches ? 0.52 : 0.65);",
        "const _scSmall = globalGlbCard._baseScaleFact * 0.65;"
    )
    
    # Revert _scLarge logic
    content = content.replace(
        "const _scLarge = globalGlbCard._baseScaleFact * _GS_SC * (window.matchMedia('(max-width: 768px)').matches ? 0.765 : 0.90);",
        "const _scLarge = globalGlbCard._baseScaleFact * _GS_SC * 0.90;"
    )
    
    # Apply the 0.8 scale at the ROOT in loadCardModel
    content = content.replace(
        "const targetH   = vH * (basePxH / window.innerHeight);",
        "const targetH   = vH * (basePxH / window.innerHeight) * (window.matchMedia('(max-width: 768px)').matches ? 0.8 : 1.0);"
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
