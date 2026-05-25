import re

with open("3d-test.html", "r", encoding="utf-8") as f:
    content = f.read()

old_js = r'''              // 3. CIENCIA - slide UP como "RISE" en Oryzo
              \{ const p = Math.min\(Math.max\(mapRange\(exitP, 0.05, 0.55, 0, 1\), 0\), 1\);
                const easeUp = 1 - Math.pow\(1 - p, 2\);
                applyExit\('mag-ciencia', 	ranslateY\(\$\{-60 \* easeUp\}px\),
                  Math.max\(0, 1 - mapRange\(p, 0.2, 1.0, 0, 1\)\)\); \}'''

new_js = '''              // 3. CIENCIA - slide UP escalonado
              { const baseP = Math.min(Math.max(mapRange(exitP, 0.05, 0.55, 0, 1), 0), 1);
                const globalOpacity = Math.max(0, 1 - mapRange(baseP, 0.2, 1.0, 0, 1));
                applyExit('mag-ciencia', '', globalOpacity);
                document.querySelectorAll('[id="mag-ciencia"]').forEach(container => {
                  container.querySelectorAll('.ciencia-letter').forEach((letter, idx) => {
                    const stagger = idx * 0.08;
                    const startP = stagger;
                    const endP = 0.5 + stagger;
                    const letterP = Math.min(Math.max(mapRange(exitP, startP, endP, 0, 1), 0), 1);
                    const easeUp = 1 - Math.pow(1 - letterP, 2);
                    letter.style.transform = 	ranslateY(px);
                  });
                });
              }'''

content = re.sub(old_js, new_js, content)

old_reset = r'''              \['mag-saber-mas','mag-natgeo','mag-ciencia','mag-col-left','mag-col-right','mag-bottom'\].forEach\(id => \{
                document.querySelectorAll\(\[id="\$\{id\}"\]\).forEach\(el => \{
                  el.style.transform = '';
                  el.style.opacity   = '';
                \}\);
              \}\);'''

new_reset = '''              ['mag-saber-mas','mag-natgeo','mag-ciencia','mag-col-left','mag-col-right','mag-bottom'].forEach(id => {
                document.querySelectorAll([id=""]).forEach(el => {
                  el.style.transform = '';
                  el.style.opacity   = '';
                });
              });
              document.querySelectorAll('.ciencia-letter').forEach(el => el.style.transform = '');'''

content = re.sub(old_reset, new_reset, content)

with open("3d-test.html", "w", encoding="utf-8") as f:
    f.write(content)