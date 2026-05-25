import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Add logic to fade out .box-shadow-cast
logic_to_insert = """
        // Fade out the physical box shadow before it flattens into the magazine cover
        let shadowCast = mainDeck.querySelector('.box-shadow-cast');
        if (shadowCast) {
          if (prog > 9.62) {
            let sP = mapRange(prog, 9.62, 10.02, 0, 1);
            shadowCast.style.opacity = (1 - sP).toString();
          } else {
            shadowCast.style.opacity = '1';
          }
        }
"""

# Insert right before FASE 1 in updateBoxState
content = content.replace(
    "// FASE 1: (0 a 0.4) El flip de la caja se detiene exactamente a los 450 grados.",
    logic_to_insert + "\n          // FASE 1: (0 a 0.4) El flip de la caja se detiene exactamente a los 450 grados."
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
