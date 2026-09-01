import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = "Te las encontrarás en la mesa al llegar"
replacement = "Te las encontrarás en el restaurante al llegar"

if target in text:
    text = text.replace(target, replacement)
    with open("arbol.html", "w", encoding="utf-8") as f:
        f.write(text)
    print("Replaced text!")
else:
    print("Target not found exactly.")

