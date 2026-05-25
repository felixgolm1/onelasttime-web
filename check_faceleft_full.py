import os
path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for j in range(819, 830):
    print(f"Line {j+1}: {lines[j].strip()}")
