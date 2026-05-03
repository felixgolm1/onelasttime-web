import os
import re

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'img\.style\.transform = scale\(\);', r'img.style.transform = scale();', content)
content = re.sub(r'img\.style\.filter =\s*rightness\(\);', r'img.style.filter = rightness();', content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed via regex")
