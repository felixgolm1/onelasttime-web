import codecs
import re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# 1. Update HTML
html_pattern = r'<!-- Copy superior \(ahora debajo de la barra\) -->.*?</div>'
html_replacement = '''<!-- Copy superior (ahora debajo de la barra) -->
    <div id="envej-cta-container" style="display:none; position:relative; flex-direction:column; gap:4px; text-align:center; align-items:center; justify-content:center; margin-top:16px;">
      <button id="envej-final-cta" onclick="window.location.href='reservar-mi-cena.html'" style="background-color: #a3cc00; color: #111; border: none; border-radius: 100px; padding: 8px 20px; font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 700; text-align: center; line-height: 1.3; text-transform: uppercase; cursor: pointer; box-shadow: 0 4px 12px rgba(163,204,0,0.4); display: flex; flex-direction: column; align-items: center; justify-content: center; width: 100%;">
        <span style="display:block; letter-spacing: 0.05em;">No te dejes nada por decir</span>
        <span style="display:block; letter-spacing: 0.05em;">D&iacute;selo en la pr&oacute;xima cena</span>
      </button>
    </div>'''
content = re.sub(html_pattern, html_replacement, content, flags=re.DOTALL)

# 2. Update JS
js_pattern = r'window\.updateEnvejCopy = function\(pct\) \{.*?\};\s*window\.envejSeekByRange = function\(val\)'
js_replacement = '''window.updateEnvejCopy = function(pct) {
            const ctaContainer = document.getElementById('envej-cta-container');
            if (pct >= 0.99) {
               if (ctaContainer) ctaContainer.style.display = 'flex';
            } else {
               if (ctaContainer) ctaContainer.style.display = 'none';
            }
          };
          window.envejSeekByRange = function(val)'''
content = re.sub(js_pattern, js_replacement, content, flags=re.DOTALL)

with codecs.open('3d-test.html', 'w', 'utf-8') as f:
    f.write(content)

print("Done")
