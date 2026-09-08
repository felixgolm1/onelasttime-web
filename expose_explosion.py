import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Exponer funcion para explosion
search_target = "let explosionActive = false;"
replacement = "let explosionActive = false;\n        window.triggerEmberExplosion = function() { explosionActive = true; window._ctaHoverActive = true; };"

if search_target in content:
    content = content.replace(search_target, replacement)
    
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Exposed triggerEmberExplosion in 3d-test.html")
else:
    print("Could not find explosionActive in 3d-test.html")

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
if search_target in content:
    content = content.replace(search_target, replacement)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Exposed triggerEmberExplosion in index.html")
