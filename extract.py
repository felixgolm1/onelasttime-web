import os
import re

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

scripts = re.findall(r'<script.*?>\s*(.*?)\s*</script>', content, flags=re.DOTALL | re.IGNORECASE)

for i, script in enumerate(scripts):
    with open(f'script_{i}.js', 'w', encoding='utf-8') as f:
        f.write(script)
