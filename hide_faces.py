import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Add the logic to hide invisible faces when the box is perfectly rotated at 450deg
logic_to_insert = """
        // Esconder caras perpendiculares y solapas SÓLO cuando la caja ha alcanzado los 450 grados (prog > 10.02)
        // para evitar que sus bordes físicos de 1px sobresalgan durante la expansión 2D, sin usar opacidad para no 
romper el preserve-3d.
        let hiddenFaces = mainDeck.querySelectorAll('.box-flap, .tuck-lip, .dust-flap, .face-back, .face-front, 
.face-bottom');
        if (prog > 10.02) {
          hiddenFaces.forEach(f => f.style.display = 'none');
        } else {
          hiddenFaces.forEach(f => f.style.display = '');
        }
"""

content = content.replace(
    "// FASE 1: (0 a 0.4) El flip de la caja se detiene exactamente a los 450 grados.",
    logic_to_insert + "\n          // FASE 1: (0 a 0.4) El flip de la caja se detiene exactamente a los 450 grados."
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
