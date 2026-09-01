import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Top price
target_top = """                                    <div className="text-right">
                                        <p className="font-bold text-gray-900 text-lg whitespace-nowrap leading-none">{basePrice.toString().replace('.', ',')}€</p>
                                        <p className="text-[10px] text-gray-500 mt-0 whitespace-nowrap leading-none">IVA incluido</p>
                                    </div>"""

replacement_top = """                                    <div className="text-right">
                                        <p className="font-bold text-gray-900 text-lg whitespace-nowrap leading-none">{basePrice.toString().replace('.', ',')}€</p>
                                        <p className="text-[10px] text-gray-500 mt-1 whitespace-nowrap leading-none">IVA incluido</p>
                                    </div>"""
text = text.replace(target_top, replacement_top)

# 2. Shipping price
target_ship = """                                        <div className="text-right">
                                            <span className={`text-lg font-bold whitespace-nowrap leading-none block ${shipping.costColor}`}>{shipping.costText}</span>
                                            {shipping.cost > 0 && <p className="text-[10px] text-gray-400 mt-0.5 whitespace-nowrap leading-none">IVA incluido</p>}
                                        </div>"""

replacement_ship = """                                        <div className="text-right">
                                            <span className={`text-lg font-bold whitespace-nowrap leading-none block ${shipping.costColor}`}>{shipping.costText}</span>
                                            {shipping.cost > 0 && <p className="text-[10px] text-gray-400 mt-1 whitespace-nowrap leading-none">IVA incluido</p>}
                                        </div>"""
text = text.replace(target_ship, replacement_ship)

# 3. Total price
target_tot = """                                        <div className="text-right">
                                            <p className="leading-none">{price}</p>
                                            <p className="text-[10px] font-normal text-gray-500 mt-0.5 whitespace-nowrap leading-none">IVA incluido</p>
                                        </div>"""

replacement_tot = """                                        <div className="text-right">
                                            <p className="leading-none">{price}</p>
                                            <p className="text-xs font-normal text-gray-500 mt-1 whitespace-nowrap leading-none">IVA incluido</p>
                                        </div>"""
text = text.replace(target_tot, replacement_tot)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated IVA styles!")

