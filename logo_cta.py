import re

for file in ['terminos.html', 'privacidad.html']:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # 1. Replace Top CTA Text
    # We look for: <span class="cta-text-span" ...>VOLVER A ONE LAST TIME</span>
    # Note: top CTA has padding-left: 44px; bottom has padding-left: 62px;
    
    replacement_top = r'<span class="cta-text-span" style="position:relative; z-index:2; text-align:center; display: inline-flex; align-items: center; justify-content: center; gap: 7px; padding-left: 44px;">VOLVER A <img src="assets/img/logo%20one%20last%20time.png" alt="One Last Time" style="height: 1.2em; width: auto; filter: brightness(0) invert(1); transform: translateY(-1px);"></span>'
    text = re.sub(r'<span class="cta-text-span" style="[^"]*padding-left:\s*44px;[^"]*">VOLVER A ONE LAST TIME</span>', replacement_top, text)
    
    replacement_bottom = r'<span class="cta-text-span" style="position:relative; z-index:2; text-align:center; display: inline-flex; align-items: center; justify-content: center; gap: 8px; padding-left: 62px;">VOLVER A <img src="assets/img/logo%20one%20last%20time.png" alt="One Last Time" style="height: 1.2em; width: auto; filter: brightness(0) invert(1); transform: translateY(-1px);"></span>'
    text = re.sub(r'<span class="cta-text-span" style="[^"]*padding-left:\s*62px;[^"]*">VOLVER A ONE LAST TIME</span>', replacement_bottom, text)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Updated {file}')
