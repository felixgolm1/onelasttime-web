import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('divisor = 2700;', 'divisor = 5000;')
content = content.replace('divisorT = 1350;', 'divisorT = 2500;')

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
