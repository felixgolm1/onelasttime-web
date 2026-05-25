import os
path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

import re
funcs = re.findall(r'function (\w+)\(', content)
print("Defined functions:")
print(set(funcs))
