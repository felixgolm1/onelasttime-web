import re

files = ['3d-test.html', 'index.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change introState initialization
    content = re.sub(
        r"let introState = \{ scaleMult: 1\.5 \};",
        r"let introState = { scaleMult: window.innerWidth <= 768 ? 1.0 : 1.5 };",
        content
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
