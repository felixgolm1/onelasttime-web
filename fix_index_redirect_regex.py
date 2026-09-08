import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

search_regex = re.compile(r"// Efecto de intensificar luces\s*if \(window\.triggerEmberExplosion\).*?window\._ctaHoverActive = false;\s*\}, 800\);", re.DOTALL)

replacement = """// Ocultar formulario sutilmente para disfrutar de la explosion
        var formContainer = document.getElementById('vip-form-container');
        if (formContainer) {
            formContainer.style.transition = 'opacity 0.4s ease';
            formContainer.style.opacity = '0';
        }
        
        // Efecto de intensificar luces
        if (window.triggerEmberExplosion) window.triggerEmberExplosion();
        
        // Redirigir a la landing page despues de ver la explosion 1.5s
        setTimeout(function() {
            window.location.href = '3d-test.html';
        }, 1500);"""

if search_regex.search(content):
    content = search_regex.sub(replacement, content)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed index.html redirection logic using regex")
else:
    print("Regex failed in index.html")
