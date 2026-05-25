import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace edge glow logic in smoothScrollLoop and requestAnimationFrame
edge_glow_logic = """
          // ─ Edge glow: matemáticamente atado a prog
          const eg = document.getElementById('edge-glow');
          if (eg) {
            let startP = 1.54;
            let endP = 2.19;
            
            if (prog >= startP && prog <= endP) {
              let glowP = mapRange(prog, startP, endP, 0, 1);
              if (glowP < 0.3) eg.style.opacity = glowP / 0.3;
              else eg.style.opacity = 1 - ((glowP - 0.3) / 0.7);
            } else {
              eg.style.opacity = 0;
            }
          }
"""

content = re.sub(
    r"// \u2500 Edge glow: matemáticamente atado a prog \(y apoyado por transition CSS\)\s*if \(typeof glowTSwap !== 'undefined' && glowTSwap > 0\) \{\s*const eg = document\.getElementById\('edge-glow'\);\s*if \(eg\) \{\s*let swapProg = glowTSwap / \(scrollTl\.duration\(\) / 2\.2\);\s*let startP = Math\.max\(0, swapProg - 0\.20\);\s*let endP = swapProg \+ 0\.05;\s*if \(prog >= startP && prog <= endP\) \{\s*let glowP = mapRange\(prog, startP, endP, 0, 1\);\s*if \(glowP < 0\.3\) eg\.style\.opacity = glowP / 0\.3;\s*else eg\.style\.opacity = 1 - \(\(glowP - 0\.3\) / 0\.7\);\s*\} else \{\s*eg\.style\.opacity = 0;\s*\}\s*\}\s*\}",
    edge_glow_logic.strip(),
    content
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
