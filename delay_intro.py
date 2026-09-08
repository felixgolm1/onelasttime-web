import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Buscamos donde se ejecuta _runIntroAnim
search_target = """  if (typeof window._runIntroAnim === 'function' && !animReady) {
    window._runIntroAnim();
    window._runIntroAnim = null;
  }"""

replacement = """  if (typeof window._runIntroAnim === 'function' && !animReady) {
    // Si la pasarela VIP ESTA ACTIVA (es decir, NO esta en session storage)
    // Entonces NO lanzamos la animacion ahora, la dejamos para que la lance checkVipCode()
    if (sessionStorage.getItem('olt_vip_unlocked') === 'true') {
        window._runIntroAnim();
        window._runIntroAnim = null;
    }
  }"""

if search_target in content:
    content = content.replace(search_target, replacement)
    
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Delayed _runIntroAnim in 3d-test.html")
else:
    print("Could not find the target string in 3d-test.html")

# Hacemos lo mismo en index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
if search_target in content:
    content = content.replace(search_target, replacement)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Delayed _runIntroAnim in index.html")
