import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

search = """          var overlay = document.getElementById('vip-overlay');
          overlay.style.transition = 'opacity 0.8s ease';
          overlay.style.opacity = '0';
          setTimeout(function() { overlay.style.display = 'none'; }, 800);
          clearInterval(vipEmberInterval);
          window._ctaHoverActive = false;"""

replacement = """          var overlay = document.getElementById('vip-overlay');
          sessionStorage.setItem('olt_vip_unlocked', 'true');
          
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
          }, 800);"""

if search in content:
    content = content.replace(search, replacement)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed index.html")
else:
    print("Could not find the target string in index.html")
