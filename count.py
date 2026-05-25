import os
path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

count = content.count("// FASE 1: (0 a 0.4)")
print(f"Count of FASE 1: {count}")
