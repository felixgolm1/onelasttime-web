import re

files = ['terminos.html', 'privacidad.html', 'garantia.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Replace padding: 1.45rem 2rem !important; with padding: 1.3rem 2rem !important;
    text = text.replace('padding: 1.45rem 2rem !important;', 'padding: 1.3rem 2rem !important;')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Updated {file}')
