import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                } else if (isPickup) {
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

replacement = """                } else if (isPickup) {
                    const pickup = globalData.logistics?.punto_recogida || '';
                    title = (
                        <div className="flex flex-col gap-1">
                            <span><strong className="text-gray-800">Punto de recogida:</strong> {pickup}</span>
                            <span><strong className="text-gray-800">Entrega garantizada antes del</strong> {fecha}</span>
                        </div>
                    );
                }"""

text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated pickup format again!")

