import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find("let dondeLasUsaras = '';")
end_idx = text.find("const derivedNotas", idx)
print(text[idx:end_idx])

