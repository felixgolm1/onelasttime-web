import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Update for reservation made
target_reserva = """                        <div className="flex flex-col gap-1">
                            <strong className="mb-2 text-gray-800">Las cartas te estarán esperando en tu mesa antes de que llegues</strong>
                            <span><strong className="text-gray-800">Nombre del restaurante:</strong> {restName}</span>
                            <span><strong className="text-gray-800">Nombre de la reserva:</strong> {resName}</span>
                            <span><strong className="text-gray-800">Hora de la cena:</strong> {fecha}</span>
                        </div>"""

replacement_reserva = """                        <div className="flex flex-col">
                            <strong className="mb-2 text-gray-800">Las cartas te estarán esperando en tu mesa antes de que llegues</strong>
                            <ul className="list-disc ml-4 space-y-1">
                                <li><strong className="text-gray-800">Nombre del restaurante:</strong> {restName}</li>
                                <li><strong className="text-gray-800">Nombre de la reserva:</strong> {resName}</li>
                                <li><strong className="text-gray-800">Hora de la cena:</strong> {fecha}</li>
                            </ul>
                        </div>"""

text = text.replace(target_reserva, replacement_reserva)


# Update for restaurant delivery (no reservation)
target_no_reserva = """                        <div className="flex flex-col gap-1">
                            <strong className="mb-2 text-gray-800">Las cartas te estarán esperando en el restaurante antes de que llegues</strong>
                            <span><strong className="text-gray-800">Nombre del restaurante:</strong> {restName}</span>
                            <span><strong className="text-gray-800">Hora de la cena:</strong> {fecha}</span>
                            <span className="text-gray-500 text-xs mt-2 font-medium">Pregunta por ellas al o la camarerx con la confimación de tu pedido</span>
                        </div>"""

replacement_no_reserva = """                        <div className="flex flex-col">
                            <strong className="mb-2 text-gray-800">Las cartas te estarán esperando en el restaurante antes de que llegues</strong>
                            <ul className="list-disc ml-4 space-y-1">
                                <li><strong className="text-gray-800">Nombre del restaurante:</strong> {restName}</li>
                                <li><strong className="text-gray-800">Hora de la cena:</strong> {fecha}</li>
                            </ul>
                            <span className="text-gray-500 text-xs mt-3 font-medium">Pregunta por ellas al o la camarerx con la confimación de tu pedido</span>
                        </div>"""

text = text.replace(target_no_reserva, replacement_no_reserva)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Added bullet points!")

