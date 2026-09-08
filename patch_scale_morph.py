import re

files = ['3d-test.html', 'index.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Revert targetH hack
    content = content.replace(
        "const targetH   = vH * (basePxH / window.innerHeight) * (window.matchMedia('(max-width: 768px)').matches ? 0.8 : 1.0);",
        "const targetH   = vH * (basePxH / window.innerHeight);"
    )
    
    # Apply CSS scale to #card-morph-group as well
    content = content.replace(
        ".sc-card { transform: scale(0.80); transform-origin: center center; }",
        "#card-morph-group, .sc-card { transform: scale(0.80) !important; transform-origin: center center; }"
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
