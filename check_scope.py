import os
path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "function smoothScrollLoop" in line:
        print(f"smoothScrollLoop at {i}")
        for j in range(i, -1, -1):
            if "function initGSAP" in lines[j]:
                print(f"Inside initGSAP at {j}")
                break
        break
