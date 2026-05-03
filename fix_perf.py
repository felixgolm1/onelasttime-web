import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_js = '''          // 3. Texto iluminado de derecha a izquierda
          const quoteFg = rev1.querySelector('.review-quote-fg');
          if (quoteFg) {
             let textP = mapRange(pRev, 0.2, 0.5, 100, 0); // inset right de 100 a 0
             textP = Math.max(0, Math.min(100, textP));
             quoteFg.style.clipPath = inset(0% 0% 0% %);
          }

          // 4. Imagen se agranda 30% y se ilumina
          const img = rev1.querySelector('.review-img-col img');
          if (img) {
             let imgP = mapRange(pRev, 0.1, 0.6, 0, 1);
             imgP = Math.max(0, Math.min(1, imgP));
             let scale = 1.0 + (0.3 * imgP);
             let brightness = 0.3 + (0.7 * imgP);
             img.style.transform = scale();
             img.style.filter = rightness();
          }'''

new_js = '''          // Caching elements to avoid layout thrashing and slow querySelectors in 60fps loop
          if (!rev1._quoteFg) rev1._quoteFg = rev1.querySelector('.review-quote-fg');
          if (!rev1._img) { 
              rev1._img = rev1.querySelector('.review-img-col img');
              if (rev1._img) rev1._img.style.willChange = 'transform, filter';
          }

          // 3. Texto iluminado de derecha a izquierda
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

if old_js in content:
    content = content.replace(old_js, new_js)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Optimization applied!")
else:
    print("Warning: old_js not found!")
