import re

for file in ['terminos.html', 'privacidad.html']:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Find the bad string
    bad_mask = r'<span style="display: inline-block; width: 6.8em; height: 1.35em; background-color: currentColor; -webkit-mask: url(\\\'assets/img/logo%20one%20last%20time.png\\\') no-repeat center / contain; mask: url(\\\'assets/img/logo%20one%20last%20time.png\\\') no-repeat center / contain; transform: translateY(-1px);"></span>'
    new_mask = '<span style="display: inline-block; width: 6.8em; height: 1.35em; background-color: currentColor; -webkit-mask: url(\'assets/img/logo%20one%20last%20time.png\') no-repeat center / contain; mask: url(\'assets/img/logo%20one%20last%20time.png\') no-repeat center / contain; transform: translateY(-1px);"></span>'
    
    text = re.sub(bad_mask, new_mask, text)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Fixed {file}')
