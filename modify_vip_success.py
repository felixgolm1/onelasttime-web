import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

search_target = """        var overlay = document.getElementById('vip-overlay');
        overlay.style.transition = 'opacity 0.8s ease';
        overlay.style.opacity = '0';
        setTimeout(function() { overlay.style.display = 'none'; }, 800);
        clearInterval(vipEmberInterval);
        window._ctaHoverActive = false;"""

replacement = """        // Efecto de intensificar luces
        if (window.triggerEmberExplosion) window.triggerEmberExplosion();
        
        setTimeout(function() {
            var overlay = document.getElementById('vip-overlay');
            overlay.style.transition = 'opacity 1.2s ease';
            overlay.style.opacity = '0';
            setTimeout(function() { 
                overlay.style.display = 'none'; 
                // Secuencia de carga de la landing page (letras, etc)
                if (typeof window._runIntroAnim === 'function') {
                    window._runIntroAnim();
                    window._runIntroAnim = null;
                }
            }, 1200);
            if (typeof vipEmberInterval !== 'undefined' && vipEmberInterval) clearInterval(vipEmberInterval);
            window._ctaHoverActive = false;
        }, 800); // Dar 800ms para que se vea la explosion antes de hacer fade out"""

if search_target in content:
    content = content.replace(search_target, replacement)
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Modified checkVipCode in 3d-test.html")
else:
    print("Could not find the target string in 3d-test.html")

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
if search_target in content:
    content = content.replace(search_target, replacement)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Modified checkVipCode in index.html")
