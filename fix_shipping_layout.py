import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                if (isReservationMade) {
                    const restName = formatRestaurante();
                    const resName = globalData.logistics?.reserva || 'tu nombre';
                    title = (
                        <div className="flex flex-col">
                            <span>Las cartas te estarán esperando en tu mesa del restaurante {restName} el {fecha}</span>
                            <span className="mt-1"><strong className="text-gray-800">Nombre de la reserva:</strong> {resName}</span>
                        </div>
                    );
                } else if (isRestaurantDelivery) {
                    const restName = formatRestaurante();
                    title = (
                        <div className="flex flex-col">
                            <span>Las cartas te estarán esperando en el restaurante {restName} el {fecha}.</span>
                            <span className="text-gray-500 text-xs mt-1 font-medium">Pregunta por ellas al o la camarerx con la confimación de tu pedido</span>
                        </div>
                    );"""

replacement = """                if (isReservationMade) {
                    const restName = formatRestaurante();
                    const resName = globalData.logistics?.reserva || 'tu nombre';
                    title = (
                        <div className="flex flex-col gap-1">
                            <span className="mb-2">Las cartas te estarán esperando en tu mesa</span>
                            <span><strong className="text-gray-800">Nombre del restaurante:</strong> {restName}</span>
                            <span><strong className="text-gray-800">Nombre de la reserva:</strong> {resName}</span>
                            <span><strong className="text-gray-800">Hora de la cena:</strong> {fecha}</span>
                        </div>
                    );
                } else if (isRestaurantDelivery) {
                    const restName = formatRestaurante();
                    title = (
                        <div className="flex flex-col gap-1">
                            <span className="mb-2">Las cartas te estarán esperando en el restaurante</span>
                            <span><strong className="text-gray-800">Nombre del restaurante:</strong> {restName}</span>
                            <span><strong className="text-gray-800">Hora de la cena:</strong> {fecha}</span>
                            <span className="text-gray-500 text-xs mt-2 font-medium">Pregunta por ellas al o la camarerx con la confimación de tu pedido</span>
                        </div>
                    );"""

text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated shipping layout for restaurants!")

