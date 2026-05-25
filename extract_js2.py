import re

with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'r', encoding='utf-8', errors='replace') as f:
    html = f.read()

scripts = re.findall(r'<script.*?>\s*(.*?)\s*</script>', html, re.DOTALL | re.IGNORECASE)

with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/extracted_scripts.js', 'w', encoding='utf-8') as f:
    for i, s in enumerate(scripts):
        f.write(f"\n/* --- SCRIPT {i} --- */\n")
        f.write(s)
