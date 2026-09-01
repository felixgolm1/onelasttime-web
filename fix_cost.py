import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                                <div className="mt-6 pt-6 border-t-[1.5px] border-gray-200">
                                    <h3 className="font-bold text-lg text-gray-900 mb-4">Detalles del envío</h3>
                                    <div className="flex justify-between items-start text-sm text-gray-500 mb-4">
                                        <div className="pr-4">{shipping.title}</div>
                                        <div className="text-right">
                                            <span className={`text-lg font-bold whitespace-nowrap leading-none block ${shipping.costColor}`}>{shipping.costText}</span>
                                            {shipping.cost > 0 && <p className="text-[10px] text-gray-400 mt-0.5 whitespace-nowrap leading-none">IVA incluido</p>}
                                        </div>
                                    </div>"""

replacement = """                                <div className="mt-6 pt-6 border-t-[1.5px] border-gray-200">
                                    <div className="flex justify-between items-start mb-4">
                                        <h3 className="font-bold text-lg text-gray-900">Detalles del envío</h3>
                                        <div className="text-right">
                                            <span className={`text-lg font-bold whitespace-nowrap leading-none block ${shipping.costColor}`}>{shipping.costText}</span>
                                            {shipping.cost > 0 && <p className="text-[10px] text-gray-400 mt-0.5 whitespace-nowrap leading-none">IVA incluido</p>}
                                        </div>
                                    </div>
                                    <div className="flex justify-between items-start text-sm text-gray-500 mb-4">
                                        <div className="pr-4">{shipping.title}</div>
                                    </div>"""

text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated HTML for cost alignment!")

