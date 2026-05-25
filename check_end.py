import os
path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

open_c = 0
found = False
for i in range(2692, len(lines)):
    open_c += lines[i].count('{')
    open_c -= lines[i].count('}')
    if i == 3668:
        print(f"At updateBoxState (line 3668), open braces from setupScrollAnim: {open_c}")
    if open_c == 0:
        print(f"setupScrollAnim ends at {i}")
        break
