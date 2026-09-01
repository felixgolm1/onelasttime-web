import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find("const handleSaveContact = () => {")
end_idx = text.find("};", idx) + 2
print(text[idx:end_idx])

