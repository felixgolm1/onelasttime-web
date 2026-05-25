import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the specific block safely
content = re.sub(
    r"// Eliminados los tweens absolutos a 9\.62.*?scrollTl\.set\(\{\},\s*\{\},\s*10\.57\);",
    "// Eliminados los tweens absolutos a 9.62 que alargaban el scrollTl artificialmente.\n      // Permitimos que la duración sea su longitud natural para mapear suavemente a prog/2.2.",
    content,
    flags=re.DOTALL
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
