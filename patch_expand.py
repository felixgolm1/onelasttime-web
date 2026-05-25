with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

old_logic_match = re.search(r'const uiFade[\s\S]*?rgba\(255, 255, 255, \$\{uiFade\}\)\;\n           \}', text)

new_logic = '''const uiFade = typeof prog !== 'undefined' ? (prog < 15.0 ? 1 : Math.max(0, 1 - (prog - 15.0) / 1.5)) : 1;
           const expandP = 1 - uiFade;
           
           const magUIs = magazineScene.querySelectorAll('.mag-ui');
           magUIs.forEach(el => el.style.opacity = uiFade);
           
           const baseW = window.innerWidth > 768 ? 466 : window.innerWidth * 0.9;
           const baseH = window.innerWidth > 768 ? 626 : window.innerWidth * 1.3;
           const targetW = window.innerWidth;
           const targetH = window.innerHeight;
           
           // Apply ease in-out for smoother expansion
           const easeP = expandP * expandP * (3 - 2 * expandP);
           magazineScene.style.width = \\px\;
           magazineScene.style.height = \\px\;

           const magContent = magazineScene.querySelector('.magazine-content');
           if (magContent) {
              magContent.style.borderColor = \gba(249, 204, 16, \)\;
              magContent.style.boxShadow = \inset 0 0 0 2px rgba(255, 255, 255, \)\;
              magContent.style.backgroundColor = \gba(6, 2, 15, \)\;
              
              // Zoom effect: 250% down to 100%
              const bgSize = 250 - (150 * easeP);
              const bgPos = 15 - (15 * easeP);
              magContent.style.backgroundSize = \\%\;
              magContent.style.backgroundPosition = \center \%\;
           }'''

if old_logic_match:
    text = text.replace(old_logic_match.group(0), new_logic)
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Expansion logic patched!")
else:
    print("Pattern not found!")
