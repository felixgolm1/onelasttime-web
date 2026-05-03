import re

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract script block
scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
for script in scripts:
    if 'function smoothScrollLoop' in script:
        # Check basic syntax logic
        print("Script length:", len(script))
