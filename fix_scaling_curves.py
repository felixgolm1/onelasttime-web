import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Make tX slower and tY faster
new_logic = """
             // Sincronización visual: X más lento al principio, Y más rápido al principio
             let tX = Math.pow(tScale, 1.3); // Ease-in suave para frenar izquierda/derecha
             let tY = 1 - Math.pow(1 - tScale, 2); // Ease-out para acelerar arriba/abajo
"""

content = re.sub(
    r"// Mismo ease-out cuadrǭtico para ambos ejes para una expansin 100% sincronizada\s*let tX = 1 - Math\.pow\(1 - tScale, 2\);\s*let tY = tX;",
    new_logic.strip(),
    content
)

# Also support matching just the code if the comment encoding failed
if new_logic.strip() not in content:
    content = re.sub(
        r"let tX = 1 - Math\.pow\(1 - tScale, 2\);\s*let tY = tX;",
        new_logic.strip(),
        content
    )

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
