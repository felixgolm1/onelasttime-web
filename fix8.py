import os
import re

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Delete placeIdCard completely
content = re.sub(r'function placeIdCard\(gltf\) \{.*?\}(?=\s*function placeWineGlass)', '', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Python phase 8 done")
