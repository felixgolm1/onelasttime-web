import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                if (isDigital) {
                    return {
                        title: (
                            <div className="flex flex-col gap-2">
                                <span>Envío de enlace a tu WhatsApp e email a la hora de la cena. Aunque las puedes recibir antes con un solo clic en caso de que os adelantéis.</span>
                                <span><strong className="text-gray-800">Hora de la cena:</strong> {fecha}</span>
                            </div>
                        ), 
                        cost: 0,
                        costText: '0€',
                        costColor: 'text-black'
                    };
                }"""

replacement = """                if (isDigital) {
                    return {
                        title: (
                            <div className="flex flex-col gap-3">
                                <span><strong className="text-gray-800">Tipo de envío:</strong> recibirás un enlace en tu WhatsApp e email</span>
                                <span><strong className="text-gray-800">Hora del envío:</strong> justo a la hora de la cena: {fecha}. Aunque las puedes recibir antes con un solo clic por si os avanzáis.</span>
                            </div>
                        ), 
                        cost: 0,
                        costText: '0€',
                        costColor: 'text-black'
                    };
                }"""
text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated digital title format!")

