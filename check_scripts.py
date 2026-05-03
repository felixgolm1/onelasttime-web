import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

count = 0
idx = 0
while True:
    idx = content.find('<script>', idx)
    if idx == -1: break
    end_idx = content.find('</script>', idx)
    print(f"Script at {idx} length {end_idx - idx}")
    idx = end_idx
