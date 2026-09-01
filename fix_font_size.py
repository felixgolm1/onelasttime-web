import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                                <div className="text-center mt-6">
                                    <p className="text-[10px] text-gray-500 leading-relaxed px-2">"""

replacement = """                                <div className="text-center mt-6">
                                    <p className="text-xs text-gray-500 leading-relaxed px-2">"""

text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated font size!")

