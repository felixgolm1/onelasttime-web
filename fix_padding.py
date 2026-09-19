import re

for file in ['terminos.html', 'privacidad.html']:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Remove padding from body
    text = re.sub(r'padding:\s*50px 20px;', 'padding: 0;', text)
    
    # Add horizontal padding to container inline style
    text = text.replace('<div class="container" style="padding-top: 40px;">', '<div class="container" style="padding: 40px 20px;">')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(text)
