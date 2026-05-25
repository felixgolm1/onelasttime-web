import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

content = re.sub(
    r"let divisor = 900;\s*if \(targetProg < 0\.50\) divisor = 6000;",
    "let divisor = 900;\n        if (targetProg < 2.20) divisor = 6000;",
    content
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
