import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace let explosionActive = false; with the exposed function
search = re.compile(r"(let explosionActive = false;)")
replacement = r"\1\n        window.triggerEmberExplosion = function() { explosionActive = true; window._ctaHoverActive = true; for (let i = 0; i < 100; i++) { particles.push(new Particle()); } };"

if search.search(content):
    content = search.sub(replacement, content)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Injected triggerEmberExplosion in index.html")
else:
    print("Could not find the target string in index.html")
