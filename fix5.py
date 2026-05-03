import os
import re

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the ID_CARD_B64 loading block
content = re.sub(r'// Carga nuestro prisma/carta local.*?ID_CARD_B64 not found - skipping 3D card mesh\'\);\s*\}', '', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Python phase 5 done")
