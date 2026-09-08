import re

files = ['3d-test.html', 'index.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Revert introState scaleMult to 1.0 for mobile
    content = content.replace(
        "let introState = { scaleMult: window.innerWidth <= 768 ? 0.85 : 1.5 };",
        "let introState = { scaleMult: window.innerWidth <= 768 ? 1.0 : 1.5 };"
    )
    
    content = content.replace(
        "scaleMult: window.innerWidth <= 768 ? 0.85 : 1.0,",
        "scaleMult: 1.0,"
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
