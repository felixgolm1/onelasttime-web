import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Replace the text
text = text.replace('<li><strong className="text-gray-800">¿Dónde las usarás?:</strong> {dondeLasUsaras}</li>', 
                    '<li><strong className="text-gray-800">Lugar donde las vas a usar:</strong> {dondeLasUsaras}</li>')

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated label text!")

