import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

idx1 = content.find('(function startIntroAnim() {')
idx2 = content.find('(function startIntroAnim() {', idx1 + 10)
print(f"First startIntroAnim at {idx1}")
print(f"Second startIntroAnim at {idx2}")

# Let's find the start of the duplicate block
# We can look for the window.onload or whatever the very first line of the main script is
script_start = content.find('// 🎛️ CONTROLES GLOBALES & ESTADO SCROLL 🎛️')
script_start_2 = content.find('// 🎛️ CONTROLES GLOBALES & ESTADO SCROLL 🎛️', script_start + 10)
print(f"First // CONTROLES GLOBALES at {script_start}")
print(f"Second // CONTROLES GLOBALES at {script_start_2}")

