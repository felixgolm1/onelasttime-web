import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                } else if (isPickup) {
                    const pickup = globalData.logistics?.punto_recogida || '';
                    title = (
                        <div className="flex flex-col gap-1">
                            <span><strong className="text-gray-800">Punto de recogida:</strong> {pickup}</span>
                            <span><strong className="text-gray-800">Entrega garantizada antes del</strong> {fecha}</span>
                        </div>
                    );
                }"""

replacement = """                } else if (isPickup) {
                    let pickup = globalData.logistics?.punto_recogida || '';
                    const cp = globalData.logistics?.punto_recogida_details?.postal_code;
                    
                    if (cp && pickup.includes(',') && !pickup.includes(cp)) {
                        const parts = pickup.split(',').map(s => s.trim());
                        if (parts.length >= 2) {
                            parts.splice(parts.length - 1, 0, cp);
                            pickup = parts.join(', ');
                        }
                    }

                    title = (
                        <div className="flex flex-col gap-4">
                            <span><strong className="text-gray-800">Punto de recogida:</strong> {pickup}</span>
                            <span><strong className="text-gray-800">Entrega garantizada antes del</strong> {fecha}</span>
                        </div>
                    );
                }"""

text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated pickup format with postal code and spacing!")

