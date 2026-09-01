import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace('<span className="pr-4">{shipping.title}</span>', '<div className="pr-4">{shipping.title}</div>')

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Replaced span with div!")

