import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find("const getShippingDetails = () => {")
end_idx = text.find("const shipping = getShippingDetails();", idx)
print(text[idx:end_idx])

