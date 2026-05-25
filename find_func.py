import os
path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "let shadowCast" in line:
        # print backwards to find function definition
        for j in range(i, -1, -1):
            if "function" in lines[j]:
                print(f"Enclosing function: {lines[j].strip()}")
                break
        break
