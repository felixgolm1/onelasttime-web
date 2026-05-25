import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's find the exact block and replace it using regex.
pattern = r"const faceLeftSpan = mainDeck\.querySelector\('\.face-left span'\);\s*if \(faceLeftSpan\).*?\}[ \t]*\n"

replacement = """const faceLeftSpan = mainDeck.querySelector('.face-left span');
          if (faceLeftSpan) {
              let textScale = 1;
              if (transP >= 0.4) {
                  let tScaleText = Math.max(0, Math.min(1, (transP - 0.4) / 0.45));
                  textScale = 1 + (1.2 * tScaleText); // Crece hasta un 2.2x de su tamaño original
              }
              // Al estar rotado 90deg, la X del span corresponde a la Y del padre, y viceversa.
              faceLeftSpan.style.transform = otate(90deg) scaleX() scaleY();
          }
"""

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed the faceLeftSpan syntax error.")
