import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                                    <div className="flex justify-between items-start text-sm text-gray-600 mb-4">
                                        <p className="max-w-[70%]">{shipping.title}</p>
                                    </div>"""

replacement = """                                    <div className="flex justify-between items-start text-sm text-gray-600 mb-4">
                                        <div className="w-full pr-4">{shipping.title}</div>
                                    </div>"""
text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated shipping title container!")

