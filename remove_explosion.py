import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

search = re.compile(r"// Efecto de intensificar luces\s*if \(window\.triggerEmberExplosion\) window\.triggerEmberExplosion\(\);\s*// Redirigir a la landing page despues de ver la explosion 1\.5s\s*setTimeout\(function\(\) \{\s*window\.location\.href = '3d-test\.html';\s*\}, 1500\);", re.DOTALL)

replacement = """// Redirigir suavemente a la landing page
        setTimeout(function() {
            window.location.href = '3d-test.html';
        }, 600);"""

if search.search(content):
    content = search.sub(replacement, content)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Removed explosion and adjusted redirect in index.html")
else:
    print("Regex failed in index.html")
