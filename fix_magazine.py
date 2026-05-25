# -*- coding: utf-8 -*-
import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. FIX HTML
html_match = re.search(r'<div class="magazine-content" style="background: url\(\'assets/img/modelo-sin-fondo\.png\'\) center 15% / 250% no-repeat; background-color: #06020F; border: 12px solid #f9cc10; justify-content: flex-start; padding: 10px; position: relative; box-shadow: inset 0 0 0 2px #fff;">', text)

if html_match:
    new_html = """<div class="magazine-content" style="background: url('assets/img/modelo-sin-fondo.png') center 15% / 250% no-repeat; position: relative; width: 100%; height: 100%;">
          <!-- Marco y fondo que no se expande -->
          <div class="mag-frame" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-color: #06020F; border: 12px solid #f9cc10; box-shadow: inset 0 0 0 2px #fff; z-index: 0; pointer-events: none;"></div>
          <!-- Contenedor interno para los textos para que queden sobre el fondo pero debajo de la chica si quisieramos, pero la chica es el bg del padre -->"""
    text = text.replace(html_match.group(0), new_html)

# 2. FIX JS
js_match = re.search(r'const magContent = magazineScene\.querySelector\(\'\.magazine-content\'\);[\s\S]*?magContent\.style\.backgroundPosition = `center \$\{bgPos\}%`;\n           \}', text)

if js_match:
    new_js = """const magContent = magazineScene.querySelector('.magazine-content');
           if (magContent) {
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

              // El marco y fondo se queda en su tamano original y hace fade out
              const magFrame = magContent.querySelector('.mag-frame');
              if (magFrame) {
                  magFrame.style.width = easeP > 0 ? `${baseW}px` : '100%';
                  magFrame.style.height = easeP > 0 ? `${baseH}px` : '100%';
                  magFrame.style.left = easeP > 0 ? '50%' : '0';
                  magFrame.style.top = easeP > 0 ? '50%' : '0';
                  magFrame.style.transform = easeP > 0 ? 'translate(-50%, -50%)' : 'none';
                  magFrame.style.opacity = uiFade;
              }

              // Anclamos los textos al centro para que no se estiren con el flexbox
              const magUIs = magContent.querySelectorAll('.mag-ui, .mag-ui-title');
              magUIs.forEach(el => {
                  if (easeP > 0) {
                      el.style.width = `${baseW}px`;
                      el.style.height = `${baseH}px`;
                      el.style.left = '50%';
                      el.style.top = '50%';
                      // el transform ya esta seteado por el scale o el translate
                      if (el.classList.contains('mag-ui')) {
                          el.style.transform = `translate(-50%, -50%) scale(${1 + expandP * 0.05})`;
                      } else {
                          el.style.transform = `translate(-50%, -50%)`;
                      }
                  } else {
                      el.style.width = '100%';
                      el.style.height = '100%';
                      el.style.left = '0';
                      el.style.top = '0';
                      if (el.classList.contains('mag-ui')) {
                          el.style.transform = `scale(1)`;
                      } else {
                          el.style.transform = `none`;
                      }
                  }
              });

              const svgLines = magazineScene.querySelectorAll('line');
              svgLines.forEach(line => {
                  line.style.strokeDasharray = '2000';
                  line.style.strokeDashoffset = `${2000 * easeP}`;
              });

              // Zoom effect de la foto
              const bgSize = 250 - (100 * easeP); // de 250% a 150% para que no se vea pequena
              const bgPos = 15 + (35 * easeP);
              magContent.style.backgroundSize = `${bgSize}%`;
              magContent.style.backgroundPosition = `center ${bgPos}%`;
           }"""
    text = text.replace(js_match.group(0), new_js)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Magazine fixed!")
