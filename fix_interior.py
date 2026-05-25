import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

content = re.sub(
    r'\.face-back, \.face-front, \s*\.face-bottom',
    r'.face-back, .face-front, .face-bottom, .interior-card',
    content
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Added .interior-card to hiddenFaces.")
