import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

target = """          updateFaceSwap();
          updateGlobalScenes();
  
            // ─ Edge glow: matemáticamente atado a prog"""

replacement = """          updateFaceSwap();
          updateGlobalScenes();
        }
  
        // ─ Edge glow: matemáticamente atado a prog"""

# Need to be careful of encoding for the em-dash
target_re = r"updateGlobalScenes\(\);\s*// \u2500 Edge glow: matemáticamente atado a prog"
replacement_re = "updateGlobalScenes();\n        }\n\n        // ─ Edge glow: matemáticamente atado a prog"

# Actually let's just search and replace ignoring exact spaces
content = re.sub(
    r"updateGlobalScenes\(\);\s*// \u2500 Edge glow: matemáticamente atado a prog",
    "updateGlobalScenes();\n        }\n\n        // ─ Edge glow: matemáticamente atado a prog",
    content
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
