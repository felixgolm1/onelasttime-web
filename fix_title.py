import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Replace the title text
text = text.replace(
    "<p className=\"text-sm text-black font-medium mt-2\">Experiencia con cartas en versión<br/>{isDigital ? 'digital' : 'física'} ultra-personalizada</p>",
    "<p className=\"text-sm text-black font-medium mt-2\">Experiencia con cartas ultra-personalizadas<br/>en versión {isDigital ? 'digital' : 'física'}</p>"
)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated title text!")

