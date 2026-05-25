import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Make tX and tY use the same ease-out curve
new_logic = """
             // Mismo ease-out cuadrático para ambos ejes para una expansión 100% sincronizada
             let tX = 1 - Math.pow(1 - tScale, 2);
             let tY = tX;
"""

content = re.sub(
    r"// Ease-out cuadrǭtico para X\s*let tX = 1 - Math\.pow\(1 - tScale, 2\);\s*// Lineal para Y\s*let tY = tScale;",
    new_logic.strip(),
    content
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
