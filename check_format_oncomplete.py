import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split("\n")
print("\n".join(lines[4359:4372]))

