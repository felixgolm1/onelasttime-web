import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """            const showInput = isFocused || customInput.trim() !== '';"""
replacement = """            const showInput = customInput !== '';"""
text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated showInput logic!")

