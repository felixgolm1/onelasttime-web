import os

files = ['index.html', '3d-test.html']
search = "showVipError('Por favor, introduce un email v&aacute;lido.', false);"
replace = "showVipError('Introduce un email v&aacute;lido.', false);"

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    if search in content:
        content = content.replace(search, replace)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {file}")
