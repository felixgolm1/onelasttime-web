import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                } else if (isPickup) {
                    const pickup = globalData.logistics?.punto_recogida || '';
                    const dir = globalData.logistics?.direccion || globalData.logistics?.ciudad_entrega || globalData.logistics?.ciudad_restaurante || '';
                    title = `Envío garantizado antes del ${fecha} al punto de recogida ${pickup} de la ${dir}`;
                }"""

replacement = """                } else if (isPickup) {
                    const pickup = globalData.logistics?.punto_recogida || '';
                    title = (
                        <div className="flex flex-col">
                            <strong className="mb-2 text-gray-800">Envío garantizado a tu punto de recogida</strong>
                            <ul className="list-disc ml-4 space-y-1">
                                <li><strong className="text-gray-800">Punto de recogida:</strong> {pickup}</li>
                                <li><strong className="text-gray-800">Límite de entrega:</strong> {fecha}</li>
                            </ul>
                        </div>
                    );
                }"""

text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated pickup format!")

