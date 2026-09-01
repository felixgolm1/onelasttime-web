import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Replace div px-4 pb-4
text = text.replace('<div className="px-4 pb-4">', '<div className="pb-4">')

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated div padding!")

