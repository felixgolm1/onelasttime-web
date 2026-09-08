import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

search = """          // Efecto de intensificar luces
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

replacement = """          // Ocultar formulario sutilmente
          var formContainer = document.getElementById('vip-form-container');
          if (formContainer) {
              formContainer.style.transition = 'opacity 0.4s ease';
              formContainer.style.opacity = '0';
          }
          
          // Efecto de intensificar luces (explosion)
          if (window.triggerEmberExplosion) window.triggerEmberExplosion();
          
          // Redirigir a la landing real
          setTimeout(function() {
              window.location.href = '3d-test.html';
          }, 1400);"""

if search in content:
    content = content.replace(search, replacement)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed index.html redirection logic")
else:
    print("Could not find the target string in index.html")
