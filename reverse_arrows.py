import re

for file in ['terminos.html', 'privacidad.html']:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # 1. Top CTA
    text = text.replace('padding-right: 44px;', 'padding-left: 44px;')
    text = text.replace('right: 6px;', 'left: 6px;')
    
    # 2. Bottom CTA
    text = text.replace('padding-right: 62px;', 'padding-left: 62px;')
    text = text.replace('right: 10px;', 'left: 10px;')
    
    # 3. Rotate SVG
    text = re.sub(r'(<div class="cta-arrow-pill".*?>\s*)<svg', r'\1<svg style="transform: rotate(180deg);" ', text)
    
    # 4. Media query
    text = text.replace('padding-right: 40px !important;', 'padding-left: 40px !important;')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(text)
