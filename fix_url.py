import re

for file in ['terminos.html', 'privacidad.html']:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Find the bad string
    text = text.replace('url(\\\'assets/img/logo%20one%20last%20time.png\\\')', 'url(assets/img/logo%20one%20last%20time.png)')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Fixed {file}')
