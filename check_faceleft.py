import os
path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if ".face-left {" in line:
        for j in range(max(0, i-5), min(len(lines), i+6)):
            print(f"Line {j+1}: {lines[j].strip()}")
        print("-" * 40)
