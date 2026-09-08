import re

files = ['3d-test.html', 'index.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # _scLarge calculation
    content = content.replace(
        "const _scLarge = globalGlbCard._baseScaleFact * _GS_SC * 0.90;",
        "const _scLarge = globalGlbCard._baseScaleFact * _GS_SC * (window.innerWidth <= 768 ? 0.765 : 0.90);"
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
