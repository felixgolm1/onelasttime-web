import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

replacement = """
          // Anti-deformación del texto: contrarrestamos la escala del padre pero aplicamos un aumento proporcional
          const faceLeftSpan = mainDeck.querySelector('.face-left span');
          if (faceLeftSpan) {
              let textScale = 1;
              if (transP >= 0.4) {
                  let tScaleText = Math.max(0, Math.min(1, (transP - 0.4) / 0.45));
                  textScale = 1 + (1.8 * tScaleText); // Crece hasta un 2.8x de su tamaño original
              }
              // Al estar rotado 90deg, la X del span corresponde a la Y del padre, y viceversa.
              faceLeftSpan.style.transform = otate(90deg) scaleX() scaleY();
          }
"""

content = re.sub(
    r'// Anti-deformaci[^\n]+\n\s*const faceLeftSpan = mainDeck\.querySelector\(\'\.face-left span\'\);\n\s*if \(faceLeftSpan\) \{\n\s*// Al estar rotado 90deg[^\n]+\n\s*faceLeftSpan\.style\.transform = otate\(90deg\) scaleX\(\$\{1/boxScaleY\}\) scaleY\(\$\{1/boxScaleX\}\);\n\s*\}',
    replacement.strip(),
    content
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated text scale logic.")
