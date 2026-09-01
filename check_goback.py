import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find("const goBackPhase =")
print(text[idx:idx+1500])

