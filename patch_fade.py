import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_logic = "if (magazineScene) {\n           magazineScene.style.opacity = 1;"
new_logic = """if (magazineScene) {
           magazineScene.style.opacity = 1;
           const uiFade = typeof prog !== 'undefined' ? (prog < 15.0 ? 1 : Math.max(0, 1 - (prog - 15.0) / 1.5)) : 1;
           const magUIs = magazineScene.querySelectorAll('.mag-ui');
           magUIs.forEach(el => el.style.opacity = uiFade);
           const magContent = magazineScene.querySelector('.magazine-content');
           if (magContent) {
              magContent.style.borderColor = gba(249, 204, 16, \);
              magContent.style.boxShadow = inset 0 0 0 2px rgba(255, 255, 255, \);
           }
"""

if old_logic in text:
    text = text.replace(old_logic, new_logic)
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fade logic patched!")
else:
    print("Pattern not found!")
