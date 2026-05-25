import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

content = re.sub(
    r"\}\s*\n\s*// El efecto",
    "}\n        }\n\n        // El efecto",
    content
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
