import os
path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "function setupScrollAnim" in line:
        print(f"setupScrollAnim at {i}")
    if "function updateBoxState" in line:
        print(f"updateBoxState at {i}")
