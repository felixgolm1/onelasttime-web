import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

search = re.compile(r"var overlay = document\.getElementById\('vip-overlay'\);\s*sessionStorage\.setItem\('olt_vip_unlocked', 'true'\);\s*document\.body\.style\.overflow = 'auto';\s*overlay\.style\.transition = 'opacity 0\.8s ease';\s*overlay\.style\.opacity = '0';\s*setTimeout\(function\(\) \{ overlay\.style\.display = 'none'; \}, 800\);\s*clearInterval\(vipEmberInterval\);\s*window\._ctaHoverActive = false;")

replacement = """var overlay = document.getElementById('vip-overlay');
        sessionStorage.setItem('olt_vip_unlocked', 'true');
        document.body.style.overflow = 'auto';
        
        // Efecto de intensificar luces
        if (window.triggerEmberExplosion) window.triggerEmberExplosion();
        
        setTimeout(function() {
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

if search.search(content):
    content = search.sub(replacement, content)
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Modified checkVipCode in 3d-test.html using regex")
else:
    print("Regex failed in 3d-test.html")
