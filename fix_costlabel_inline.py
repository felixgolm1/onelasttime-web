import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update the costLabel string
target_logic = """                let costLabel = null;
                if (isIslandSupplement) {
                    costLabel = "(Suplemento islas. Gratis en península)";
                }"""

replacement_logic = """                let costLabel = null;
                if (isIslandSupplement) {
                    costLabel = "+ suplemento islas ";
                }"""
text = text.replace(target_logic, replacement_logic)

# 2. Update the rendering
target_render = """                                        <div className="text-right">
                                            <span className={`text-lg font-bold whitespace-nowrap leading-none block ${shipping.costColor}`}>{shipping.costText}</span>
                                            {shipping.cost > 0 && <p className="text-[10px] text-gray-400 mt-1 whitespace-nowrap leading-none">IVA incluido</p>}
                                            {shipping.costLabel && <p className="text-[10px] text-gray-500 mt-1 leading-tight max-w-[150px] text-right ml-auto">{shipping.costLabel}</p>}
                                        </div>"""

replacement_render = """                                        <div className="text-right">
                                            <span className={`text-lg font-bold whitespace-nowrap leading-none block flex items-baseline justify-end gap-1 ${shipping.costColor}`}>
                                                {shipping.costLabel && <span className="text-[10px]">{shipping.costLabel}</span>}
                                                {shipping.costText}
                                            </span>
                                            {shipping.cost > 0 && <p className="text-[10px] text-gray-400 mt-1 whitespace-nowrap leading-none">IVA incluido</p>}
                                        </div>"""
text = text.replace(target_render, replacement_render)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated costLabel rendering!")

