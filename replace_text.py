import os

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

target = """          // Anti-deformación del texto: contrarrestamos la escala del padre
          const faceLeftSpan = mainDeck.querySelector('.face-left span');
          if (faceLeftSpan) {
              // Al estar rotado 90deg, la X del span corresponde a la Y del padre, y viceversa.
              faceLeftSpan.style.transform = otate(90deg) scaleX() scaleY();
          }"""

replacement = """          // Anti-deformación del texto: contrarrestamos la escala del padre pero aplicamos un aumento proporcional
          const faceLeftSpan = mainDeck.querySelector('.face-left span');
          if (faceLeftSpan) {
              let textScale = 1;
              if (transP >= 0.4) {
                  let tScaleText = Math.max(0, Math.min(1, (transP - 0.4) / 0.45));
                  textScale = 1 + (1.2 * tScaleText); // Crece hasta un 2.2x de su tamaño original
              }
              // Al estar rotado 90deg, la X del span corresponde a la Y del padre, y viceversa.
              faceLeftSpan.style.transform = otate(90deg) scaleX() scaleY();
          }"""

# Handle encoding issues with 'ó'
target_latin1 = target.replace('ó', '')
target_utf8_1 = target.replace('ó', 'Ã³')

if target in content:
    content = content.replace(target, replacement)
    print("Replaced exact UTF-8 target.")
elif target_latin1 in content:
    content = content.replace(target_latin1, replacement)
    print("Replaced Latin1 target.")
elif target_utf8_1 in content:
    content = content.replace(target_utf8_1, replacement)
    print("Replaced mojibake target.")
else:
    # Let's do a substring replace
    part1 = "const faceLeftSpan = mainDeck.querySelector('.face-left span');"
    part2 = "faceLeftSpan.style.transform ="
    idx1 = content.find(part1)
    if idx1 != -1:
        idx2 = content.find("}", idx1)
        if idx2 != -1:
            content = content[:idx1] + replacement[replacement.find("const faceLeftSpan"):] + content[idx2+1:]
            print("Replaced using substring logic.")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
