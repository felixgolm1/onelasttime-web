import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                return {
                    title,
                    cost,
                    costText: cost > 0 ? `${cost}€` : 'Gratis',
                    costColor: cost > 0 ? 'text-gray-900' : 'text-green-600'
                };"""

replacement = """                return {
                    title,
                    cost,
                    costText: cost > 0 ? `${cost}€` : 'Gratis',
                    costColor: cost > 0 ? 'text-gray-900' : 'text-green-600',
                    costLabel
                };"""
text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Returned costLabel!")

