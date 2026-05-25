import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

content = re.sub(
    r'\n\s*romper el preserve-3d\.',
    r' romper el preserve-3d.',
    content
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Fixed rogue line break.")
