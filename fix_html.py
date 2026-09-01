import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# I will find `<div className="mb-6">\n                                            <strong className="text-gray-800 block mb-2">\n                                                {isDigital ? 'Información de contacto para la entrega:' : 'Información de contacto para el seguimiento del envío:'}`
# and inject the missing `                                        </div>\n                                    </div>\n` before it.

idx = text.find("                                  <div className=\"mb-6\">\n                                            <strong className=\"text-gray-800 block mb-2\">\n                                                {isDigital ? 'Información")
if idx == -1:
    print("Could not find the broken tag.")
else:
    text = text[:idx] + "                                        </div>\n                                    </div>\n" + text[idx:].replace('                                  <div className="mb-6">', '                                    <div className="mb-6">')
    with open("arbol.html", "w", encoding="utf-8") as f:
        f.write(text)
    print("Fixed missing divs!")

