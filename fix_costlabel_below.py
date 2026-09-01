import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                                        <div className="text-right">
                                            <div className={`flex flex-col items-end ${shipping.costColor}`}>
                                                <div className="flex items-baseline justify-end gap-1 text-right flex-wrap">
                                                    <span className="text-lg font-bold whitespace-nowrap leading-none">{shipping.costText}</span>
                                                    {shipping.costLabel && <span className="text-[10px] font-bold leading-tight max-w-[140px] whitespace-normal">{shipping.costLabel}</span>}
                                                </div>
                                            </div>
                                            {shipping.cost > 0 && <p className="text-[10px] text-gray-400 mt-1 whitespace-nowrap leading-none">IVA incluido</p>}
                                        </div>"""

replacement = """                                        <div className="text-right flex flex-col items-end">
                                            <span className={`text-lg font-bold whitespace-nowrap leading-none block ${shipping.costColor}`}>{shipping.costText}</span>
                                            {shipping.costLabel && <span className={`text-[10px] font-bold leading-tight max-w-[130px] mt-1 whitespace-normal text-right ${shipping.costColor}`}>{shipping.costLabel}</span>}
                                            {shipping.cost > 0 && <p className="text-[10px] text-gray-400 mt-1 whitespace-nowrap leading-none">IVA incluido</p>}
                                        </div>"""
text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated costLabel below price!")

