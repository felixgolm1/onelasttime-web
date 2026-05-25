import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Instead of regex, let's just use string replace for the loop insertion
target = "          updateGlobalScenes();\n        }"
replacement = """          updateGlobalScenes();
        }

        // ─ Edge glow: matemáticamente atado a prog (y apoyado por transition CSS)
        if (typeof glowTSwap !== 'undefined' && glowTSwap > 0) {
          const eg = document.getElementById('edge-glow');
          if (eg) {
            let swapProg = glowTSwap / 4.80; // (10.57 / 2.2 = 4.80)
            let startP = Math.max(0, swapProg - 0.20);
            let endP = swapProg + 0.05;
            
            if (prog >= startP && prog <= endP) {
              let glowP = mapRange(prog, startP, endP, 0, 1);
              if (glowP < 0.3) eg.style.opacity = glowP / 0.3;
              else eg.style.opacity = 1 - ((glowP - 0.3) / 0.7);
            } else {
              eg.style.opacity = 0;
            }
          }
        }"""

content = content.replace(target, replacement, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
