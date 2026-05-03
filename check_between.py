import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web-produccion\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r"const rev1 = document\.getElementById\('review-panel-1'\);.*?const rev2 = document\.getElementById\('review-panel-2'\);"
match = re.search(pattern, content, re.DOTALL)
if match:
    print(match.group(0))
