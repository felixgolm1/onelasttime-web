import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Remove mapRange from updateBoxState
content = re.sub(
    r"\s*function mapRange\(p, inMin, inMax, outMin, outMax\) \{\s*let t = Math\.max\(0, Math\.min\(1, \(p - inMin\) / \(inMax - inMin\)\)\);\s*return outMin \+ t \* \(outMax - outMin\);\s*\}",
    "",
    content
)

# Insert mapRange at the top of the main script block
content = content.replace(
    "const SC = 512;",
    "function mapRange(p, inMin, inMax, outMin, outMax) {\n      let t = Math.max(0, Math.min(1, (p - inMin) / (inMax - inMin)));\n      return outMin + t * (outMax - outMin);\n    }\n\n    const SC = 512;"
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
