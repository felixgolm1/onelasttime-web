import re

files = ['terminos.html', 'privacidad.html', 'garantia.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Remove position: sticky; top: 0;
    text = text.replace('position: sticky; top: 0; z-index: 100;', 'position: relative; z-index: 10;')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Updated {file}')
