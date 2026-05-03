import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS for review-quote-fg
old_css = 'clip-path: inset(0% 0% 0% 100%);'
new_css = '-webkit-mask-image: linear-gradient(to right, black 50%, transparent 50%); -webkit-mask-size: 200% 100%; -webkit-mask-position: 100% 0%; transform: translateZ(0);'
content = content.replace(old_css, new_css)

# 2. Update JS to use webkitMaskPosition and opacity instead of clipPath and filter
old_js = '''          // 3. Texto iluminado de derecha a izquierda
          if (rev1._quoteFg) {
             let textP = mapRange(pRev, 0.2, 0.5, 100, 0); // inset right de 100 a 0
             textP = Math.max(0, Math.min(100, textP));
             rev1._quoteFg.style.clipPath = inset(0% 0% 0% %);
          }

          // 4. Imagen se agranda 30% y se ilumina
          if (rev1._img) {
             let imgP = mapRange(pRev, 0.1, 0.6, 0, 1);
             imgP = Math.max(0, Math.min(1, imgP));
             let scale = 1.0 + (0.3 * imgP);
             let brightness = 0.3 + (0.7 * imgP);
             rev1._img.style.transform = scale() translateZ(0); // translateZ forces GPU acceleration
             rev1._img.style.filter = rightness();
          }'''

new_js = '''          // 3. Texto iluminado de derecha a izquierda (Mask Position = ultra fast)
          if (rev1._quoteFg) {
             let textP = mapRange(pRev, 0.2, 0.5, 100, 0); 
             textP = Math.max(0, Math.min(100, textP));
             rev1._quoteFg.style.webkitMaskPosition = ${textP}% 0%;
          }

          // 4. Imagen se agranda 30% y se ilumina (Opacity = ultra fast)
          if (rev1._img) {
             let imgP = mapRange(pRev, 0.1, 0.6, 0, 1);
             imgP = Math.max(0, Math.min(1, imgP));
             let scale = 1.0 + (0.3 * imgP);
             let brightness = 0.3 + (0.7 * imgP);
             rev1._img.style.transform = scale() translateZ(0);
             rev1._img.style.opacity = brightness.toString(); // Faster than filter!
          }'''

content = content.replace(old_js, new_js)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Applied extreme performance fixes.")
