import os
path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(4831, -1, -1):
    if "function" in lines[i]:
        print(f"Line 4831 is inside: {lines[i].strip()}")
        break
