import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Replace the title text
text = text.replace(
    "<p className=\"text-sm text-black font-medium mt-2\">Experiencia con cartas ultra-personalizadas<br/>en versión {isDigital ? 'digital' : 'física'}</p>",
    "<p className=\"text-sm text-black font-medium mt-2\">Experiencia con cartas<br/>ultra-personalizadas<br/>en versión {isDigital ? 'digital' : 'física'}</p>"
)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated title text with two line breaks!")

