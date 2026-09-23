import re

files = ['terminos.html', 'privacidad.html', 'garantia.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Add position: sticky; top: 0; z-index: 100; back
    text = text.replace('position: relative; z-index: 10; background: transparent;', 'position: sticky; top: 0; z-index: 100; background: transparent;')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Updated {file}')
