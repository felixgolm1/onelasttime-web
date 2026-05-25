import os

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(
    "let shadowCast = mainDeck.querySelector('.box-shadow-cast');",
    "let shadowCast = document.getElementById('mainDeck').querySelector('.box-shadow-cast');"
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("shadowCast fixed.")
