import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Top summary
text = text.replace(
    '<p className="font-bold text-gray-900 text-lg whitespace-nowrap">',
    '<p className="font-bold text-gray-900 text-lg whitespace-nowrap leading-none">'
)
text = text.replace(
    '<p className="text-[10px] text-gray-500 mt-0.5 whitespace-nowrap">IVA incluido</p>',
    '<p className="text-[10px] text-gray-500 mt-0 whitespace-nowrap leading-none">IVA incluido</p>'
)

# Shipping cost
text = text.replace(
    '<span className={`text-lg font-bold whitespace-nowrap ${shipping.costColor}`}>{shipping.costText}</span>',
    '<span className={`text-lg font-bold whitespace-nowrap leading-none block ${shipping.costColor}`}>{shipping.costText}</span>'
)
text = text.replace(
    '<p className="text-[10px] text-gray-400 mt-0.5 whitespace-nowrap">IVA incluido</p>',
    '<p className="text-[10px] text-gray-400 mt-0.5 whitespace-nowrap leading-none">IVA incluido</p>'
)

# Total cost
text = text.replace(
    '<span>{price}</span>\n                                            <p className="text-[10px] font-normal text-gray-500 mt-0.5 whitespace-nowrap">IVA incluido</p>',
    '<p className="leading-none">{price}</p>\n                                            <p className="text-[10px] font-normal text-gray-500 mt-0.5 whitespace-nowrap leading-none">IVA incluido</p>'
)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated margins and leading!")

