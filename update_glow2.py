import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the specific block with a more stable plateau
new_logic = """
            if (prog >= startP && prog <= endP) {
              if (prog < startP + 0.10) {
                // Fade in (0.10 units)
                eg.style.opacity = mapRange(prog, startP, startP + 0.10, 0, 1);
              } else if (prog > endP - 0.10) {
                // Fade out (0.10 units)
                eg.style.opacity = mapRange(prog, endP - 0.10, endP, 1, 0);
              } else {
                // Plateau (100% visible in the middle)
                eg.style.opacity = 1;
              }
            } else {
              eg.style.opacity = 0;
            }
"""

content = re.sub(
    r"if \(prog >= startP && prog <= endP\) \{\s*let glowP = mapRange\(prog, startP, endP, 0, 1\);\s*if \(glowP < 0\.3\) eg\.style\.opacity = glowP / 0\.3;\s*else eg\.style\.opacity = 1 - \(\(glowP - 0\.3\) / 0\.7\);\s*\} else \{\s*eg\.style\.opacity = 0;\s*\}",
    new_logic.strip(),
    content
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
