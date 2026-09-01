import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                return {
                    title: title,
                    cost: cost,
                    costText: cost === 0 ? 'Gratis' : `${cost}€`,
                    costColor: cost === 0 ? 'text-green-600' : 'text-gray-900'
                };"""

replacement = """                return {
                    title: title,
                    cost: cost,
                    costText: cost === 0 ? 'Gratis' : `${cost}€`,
                    costColor: cost === 0 ? 'text-green-600' : 'text-gray-900',
                    costLabel: costLabel
                };"""
text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Returned costLabel properly!")

