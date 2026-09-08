import os

files = ['index.html', '3d-test.html']
search1 = "Introduce un email v&aacute;lido."
replace1 = "Introduce un email v&aacute;lido"

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    if search1 in content:
        content = content.replace(search1, replace1)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {file}")
