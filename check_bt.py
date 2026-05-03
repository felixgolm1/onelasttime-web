import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

script_idx = content.rfind('<script>')
end_idx = content.rfind('</script>')
script_body = content[script_idx:end_idx]

backticks = script_body.count('')
print("Backticks in main script:", backticks)
