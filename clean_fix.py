# -*- coding: utf-8 -*-
import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Restore the simplest HTML for magazine-content
# Find any variant of magazine-content and replace it with the clean version
html_match = re.search(r'<div class="magazine-content"[\s\S]*?<!-- Fondo Oscurecido', text)
if html_match:
    clean_html = """<div class="magazine-content" style="background: url('assets/img/modelo-sin-fondo.png') center 15% / 250% no-repeat; background-color: #06020F; border: 12px solid #f9cc10; justify-content: flex-start; padding: 10px; position: relative; box-shadow: inset 0 0 0 2px #fff; width: 100%; height: 100%;">
          <!-- Fondo Oscurecido"""
    text = text.replace(html_match.group(0), clean_html)

# Also remove the mag-frame if it exists inside
text = re.sub(r'<!-- Marco y fondo que no se expande -->[\s\n]*<div class="mag-frame"[^>]*></div>[\s\n]*<!-- Contenedor interno[^>]*>', '', text)

# 2. Fix JS logic
js_match = re.search(r'const magContent = magazineScene\.querySelector\(\'\.magazine-content\'\);[\s\S]*?magContent\.style\.backgroundPosition = `center \$\{bgPos\}%`;\n           \}', text)

if js_match:
    new_js = """const magContent = magazineScene.querySelector('.magazine-content');
           if (magContent) {
              // 1. Expansion masiva del recuadro (hacia los lados y arriba como dibujaste)
              if (easeP > 0) {
                  magContent.style.position = 'fixed';
                  magContent.style.left = '50vw';
                  magContent.style.top = '50vh';
                  magContent.style.transform = 'translate(-50%, -50%)';
                  magContent.style.zIndex = '10000';
                  magContent.style.width = `${baseW + (window.innerWidth - baseW) * easeP}px`;
                  magContent.style.height = `${baseH + (window.innerHeight - baseH) * easeP}px`;
              } else {
                  magContent.style.position = 'relative';
                  magContent.style.left = 'auto';
                  magContent.style.top = 'auto';
                  magContent.style.transform = 'none';
                  magContent.style.zIndex = '2';
                  magContent.style.width = '100%';
                  magContent.style.height = '100%';
              }

              // Dejamos que los textos (.mag-ui) se estiren hacia los lados y desaparezcan
              // Solo el titulo se mantiene centrado para que sus letras puedan volar hacia arriba
              const titleContainer = magContent.querySelector('.mag-ui-title');
              if (titleContainer && easeP > 0) {
                  titleContainer.style.width = `${baseW}px`;
                  titleContainer.style.height = `${baseH}px`;
                  titleContainer.style.left = '50%';
                  titleContainer.style.top = '50%';
                  titleContainer.style.transform = 'translate(-50%, -50%)';
              } else if (titleContainer) {
                  titleContainer.style.width = '100%';
                  titleContainer.style.height = '100%';
                  titleContainer.style.left = '0';
                  titleContainer.style.top = '0';
                  titleContainer.style.transform = 'none';
              }

              // 2. Eliminamos el fondo negro para que la chica quede sobre el fondo verde de la web
              magContent.style.backgroundColor = `rgba(6, 2, 15, ${uiFade})`;
              
              // 3. Eliminamos el borde amarillo
              magContent.style.borderColor = `rgba(249, 204, 16, ${uiFade})`;
              magContent.style.boxShadow = `inset 0 0 0 2px rgba(255, 255, 255, ${uiFade})`;

              // Deshacemos las lineas blancas
              const svgLines = magazineScene.querySelectorAll('line');
              svgLines.forEach(line => {
                  line.style.strokeDasharray = '2000';
                  line.style.strokeDashoffset = `${2000 * easeP}`;
              });

              // 4. OCULTAMOS EL RESTO DEL CARRUSEL (las etiquetas del cerebro y otras cartas)
              // Buscamos todos los carousel-item
              const allItems = document.querySelectorAll('.carousel-item');
              allItems.forEach(item => {
                  // Si no es el que contiene nuestra revista, lo desvanecemos
                  if (!item.querySelector('.magazine-content')) {
                      item.style.opacity = uiFade;
                  }
              });

              // 5. Mantenemos el tamano de la chica estable o la crecemos un poco
              // 250% es el inicial. Queremos que termine en ~80% para que se vea enorme y majestuosa
              const bgSize = 250 - (170 * easeP); 
              const bgPos = 15 + (35 * easeP);
              magContent.style.backgroundSize = `${bgSize}%`;
              magContent.style.backgroundPosition = `center ${bgPos}%`;
           }"""
    text = text.replace(js_match.group(0), new_js)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Applied clean layout logic!")
