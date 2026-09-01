import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update the costLabel string
target_logic = """                let costLabel = null;
                if (isIslandSupplement) {
                    costLabel = "+ suplemento islas ";
                }"""

replacement_logic = """                let costLabel = null;
                if (isIslandSupplement) {
                    costLabel = "(Suplemento islas. Gratis en península)";
                }"""
text = text.replace(target_logic, replacement_logic)

# 2. Update the rendering
target_render = """                                        <div className="text-right">
                                            <span className={`text-lg font-bold whitespace-nowrap leading-none block flex items-baseline justify-end gap-1 ${shipping.costColor}`}>
                                                {shipping.costLabel && <span className="text-[10px]">{shipping.costLabel}</span>}
                                                {shipping.costText}
                                            </span>
                                            {shipping.cost > 0 && <p className="text-[10px] text-gray-400 mt-1 whitespace-nowrap leading-none">IVA incluido</p>}
                                        </div>"""

replacement_render = """                                        <div className="text-right">
                                            <div className={`flex flex-col items-end ${shipping.costColor}`}>
                                                <div className="flex items-baseline justify-end gap-1 text-right flex-wrap">
                                                    <span className="text-lg font-bold whitespace-nowrap leading-none">{shipping.costText}</span>
                                                    {shipping.costLabel && <span className="text-[10px] font-bold leading-tight max-w-[140px] whitespace-normal">{shipping.costLabel}</span>}
                                                </div>
                                            </div>
                                            {shipping.cost > 0 && <p className="text-[10px] text-gray-400 mt-1 whitespace-nowrap leading-none">IVA incluido</p>}
                                        </div>"""
text = text.replace(target_render, replacement_render)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated costLabel inline after!")

