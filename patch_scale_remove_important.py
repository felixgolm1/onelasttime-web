import re

files = ['3d-test.html', 'index.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove !important
    content = content.replace(
        "#card-morph-group, .sc-card { transform: scale(0.80) !important; transform-origin: center center; }",
        "#card-morph-group, .sc-card { transform: scale(0.80); transform-origin: center center; }"
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
