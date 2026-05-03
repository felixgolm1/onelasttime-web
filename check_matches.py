import re

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web-produccion\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r"const rev1 = document\.getElementById\('review-panel-1'\);.*?const rev2 = document\.getElementById\('review-panel-2'\);"
matches = list(re.finditer(pattern, content, re.DOTALL))
print("Number of matches:", len(matches))
if len(matches) > 0:
    for i, m in enumerate(matches):
        print(f"Match {i} length:", m.end() - m.start())
