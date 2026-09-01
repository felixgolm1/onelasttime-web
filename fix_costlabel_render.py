import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                                            <span className={`text-lg font-bold whitespace-nowrap leading-none block ${shipping.costColor}`}>{shipping.costText}</span>
                                            {shipping.cost > 0 && <p className="text-[10px] text-gray-400 mt-1 whitespace-nowrap leading-none">IVA incluido</p>}
                                        </div>"""

replacement = """                                            <span className={`text-lg font-bold whitespace-nowrap leading-none block ${shipping.costColor}`}>{shipping.costText}</span>
                                            {shipping.cost > 0 && <p className="text-[10px] text-gray-400 mt-1 whitespace-nowrap leading-none">IVA incluido</p>}
                                            {shipping.costLabel && <p className="text-[10px] text-gray-500 mt-1 leading-tight max-w-[150px] text-right ml-auto">{shipping.costLabel}</p>}
                                        </div>"""
text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Rendered costLabel!")

