import os
path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(4780, 4820):
    print(f"Line {i+1}: {lines[i].strip()}")
