import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Enhance the exposed function to add particles
search_target = "window.triggerEmberExplosion = function() { explosionActive = true; window._ctaHoverActive = true; };"
replacement = "window.triggerEmberExplosion = function() { explosionActive = true; window._ctaHoverActive = true; for (let i = 0; i < 100; i++) { particles.push(new Particle()); } };"

if search_target in content:
    content = content.replace(search_target, replacement)
    
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Enhanced triggerEmberExplosion in 3d-test.html")

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
if search_target in content:
    content = content.replace(search_target, replacement)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Enhanced triggerEmberExplosion in index.html")
