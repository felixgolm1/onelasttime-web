import re

for file in ['terminos.html', 'privacidad.html']:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Find the current width and height and replace them
    text = text.replace('width: 6.8em; height: 1.35em;', 'width: 7.8em; height: 1.55em;')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Updated {file}')
