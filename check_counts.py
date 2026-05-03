import re

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web-produccion\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

print("Occurrences of 'review-panel-1' in prod:", content.count("review-panel-1"))
print("Occurrences of 'startIntroAnim' in prod:", content.count("startIntroAnim"))
