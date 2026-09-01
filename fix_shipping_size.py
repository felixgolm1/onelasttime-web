import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Make the shipping cost text large
text = text.replace(
    "<span className={`font-medium whitespace-nowrap ${shipping.costColor}`}>{shipping.costText}</span>",
    "<span className={`text-lg font-bold whitespace-nowrap ${shipping.costColor}`}>{shipping.costText}</span>"
)


with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated shipping text size!")

