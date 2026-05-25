import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

content = re.sub(
    r'const PAN\s*=\s*0\.20;\s*\n\s*const HOLD\s*=\s*0\.10;',
    'const PAN  = 0.80;\n      const HOLD = 0.40;',
    content
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
