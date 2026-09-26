import re

file_path = "3d-test.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the specific scaling logic lines
content = content.replace(
    "let magH = magScene ? magScene.offsetHeight * 0.77 : 532.1;",
    "let magH = magScene ? magScene.offsetHeight * 0.77 : 532.1;\n             if (window._cIsMobile) { magW *= 1.10; magH *= 1.10; }"
)

# Replace the transform line
old_transform = "mainDeck.style.transform = `translateX(${shiftX}px) scaleX(${boxScaleX}) scaleY(${boxScaleY})`;"
new_transform = """
          let shiftY = 0;
          if (window._cIsMobile) {
             let vh = window.innerHeight;
             let yMain = (0.46 * vh) - 127 + (275.18 / 2);
             let yRecuadro = (0.50 * vh) - (0.056 * vh);
             let deltaY = yRecuadro - yMain;
             let tY = transP <= 0.85 ? (transP / 0.85) : 1;
             shiftY = deltaY * tY;
          }
          mainDeck.style.transform = `translate(${shiftX}px, ${shiftY}px) scaleX(${boxScaleX}) scaleY(${boxScaleY})`;"""

content = content.replace(old_transform, new_transform)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done.")
