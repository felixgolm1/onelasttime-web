import re

files = ['index.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply the 0.8 scale at the ROOT in loadCardModel
    content = content.replace(
        "const targetH   = vH * (basePxH / window.innerHeight);",
        "const targetH   = vH * (basePxH / window.innerHeight) * (window.matchMedia('(max-width: 768px)').matches ? 0.8 : 1.0);"
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
