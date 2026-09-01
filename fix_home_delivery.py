import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update Home Delivery format
target_home = """                } else {
                    const dir = globalData.logistics?.direccion || '';
                    const info = globalData.logistics?.info_adicional_direccion ? ' ' + globalData.logistics.info_adicional_direccion : '';
                    const city = globalData.logistics?.ciudad_entrega || globalData.logistics?.ciudad_restaurante || '';
                    title = `Envío garantizado antes del ${fecha} a la ${dir}${info}, ${city}`;
                }"""

replacement_home = """                } else {
                    const dir = globalData.logistics?.direccion || '';
                    const info = globalData.logistics?.info_adicional_direccion ? ' ' + globalData.logistics.info_adicional_direccion : '';
                    const city = globalData.logistics?.ciudad_entrega || globalData.logistics?.ciudad_restaurante || '';
                    
                    const fullAddress = `${dir}${info}, ${city}`.trim().replace(/^,|,$/g, '').trim();
                    
                    title = (
                        <div className="flex flex-col gap-4">
                            <span><strong className="text-gray-800">Dirección de envío:</strong> {fullAddress}</span>
                            <span><strong className="text-gray-800">Entrega garantizada antes del</strong> {fecha}</span>
                        </div>
                    );
                }"""
text = text.replace(target_home, replacement_home)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated home delivery format!")

