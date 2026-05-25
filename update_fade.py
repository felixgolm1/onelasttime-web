import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the fade duration in the edge-glow logic
new_logic = """
            if (prog >= startP && prog <= endP) {
              if (prog < startP + 0.03) {
                // Fade in rápido (0.03 unidades)
                eg.style.opacity = mapRange(prog, startP, startP + 0.03, 0, 1);
              } else if (prog > endP - 0.03) {
                // Fade out rápido (0.03 unidades)
                eg.style.opacity = mapRange(prog, endP - 0.03, endP, 1, 0);
              } else {
                // Plateau (100% visible)
                eg.style.opacity = 1;
              }
            } else {
              eg.style.opacity = 0;
            }
"""

content = re.sub(
    r"if \(prog >= startP && prog <= endP\) \{\s*if \(prog < startP \+ 0\.10\) \{\s*// Fade in \(0\.10 units\)\s*eg\.style\.opacity = mapRange\(prog, startP, startP \+ 0\.10, 0, 1\);\s*\} else if \(prog > endP - 0\.10\) \{\s*// Fade out \(0\.10 units\)\s*eg\.style\.opacity = mapRange\(prog, endP - 0\.10, endP, 1, 0\);\s*\} else \{\s*// Plateau \(100% visible in the middle\)\s*eg\.style\.opacity = 1;\s*\}\s*\} else \{\s*eg\.style\.opacity = 0;\s*\}",
    new_logic.strip(),
    content
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
