import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find("const TreeEngine =")
end_idx = text.find("return", idx + 200) + 500
print(text[idx:end_idx])

