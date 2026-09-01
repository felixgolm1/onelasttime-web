import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update `dondeLasUsaras`
target_donde = """            if (globalData.formatId?.includes('otro')) {
                dondeLasUsaras = globalData.formatCustomPlace || 'Otro lugar';
            } else if (globalData.formatId?.includes('reserva') || globalData.formatId?.includes('restaurante')) {
                dondeLasUsaras = globalData.logistics?.restaurante ? `En el restaurante ${globalData.logistics.restaurante}` : 'En un restaurante';
            } else if (formatNode) {"""
            
replacement_donde = """            if (globalData.formatId?.includes('otro')) {
                dondeLasUsaras = globalData.formatCustomPlace || 'Otro lugar';
            } else if (globalData.formatId?.includes('reserva') || globalData.formatId?.includes('restaurante')) {
                let restName = globalData.logistics?.restaurante || '';
                let restCity = globalData.logistics?.ciudad_restaurante || '';
                if (restName && restCity) {
                    dondeLasUsaras = `En el restaurante ${restName} (${restCity})`;
                } else if (restName) {
                    dondeLasUsaras = `En el restaurante ${restName}`;
                } else {
                    dondeLasUsaras = 'En un restaurante';
                }
            } else if (formatNode) {"""

text = text.replace(target_donde, replacement_donde)

# 2. Update shipping.title block
target_shipping = """                if (isReservationMade) {
                    const restName = globalData.logistics?.restaurante || 'tu restaurante';
                    const resName = globalData.logistics?.reserva || 'tu nombre';
                    title = (
                        <div className="flex flex-col">
                            <span>Las cartas te estarán esperando en tu mesa del restaurante {restName} el {fecha}</span>
                            <span className="text-gray-500 text-xs mt-1 font-medium">Nombre de la reserva: {resName}</span>
                        </div>
                    );
                } else if (isRestaurantDelivery) {
                    const restName = globalData.logistics?.restaurante || 'tu restaurante';
                    title = (
                        <div className="flex flex-col">
                            <span>Las cartas te estarán esperando en el restaurante {restName} el {fecha}.</span>
                            <span className="text-gray-500 text-xs mt-1 font-medium">Pregunta por ellas al o la camarerx con la confimación de tu pedido</span>
                        </div>
                    );"""

replacement_shipping = """                if (isReservationMade) {
                    let restName = globalData.logistics?.restaurante || 'tu restaurante';
                    if (globalData.logistics?.restaurante && globalData.logistics?.ciudad_restaurante) {
                        restName = `${globalData.logistics.restaurante} (${globalData.logistics.ciudad_restaurante})`;
                    }
                    const resName = globalData.logistics?.reserva || 'tu nombre';
                    title = (
                        <div className="flex flex-col">
                            <span>Las cartas te estarán esperando en tu mesa del restaurante {restName} el {fecha}</span>
                            <span className="text-gray-500 text-xs mt-1 font-medium">Nombre de la reserva: {resName}</span>
                        </div>
                    );
                } else if (isRestaurantDelivery) {
                    let restName = globalData.logistics?.restaurante || 'tu restaurante';
                    if (globalData.logistics?.restaurante && globalData.logistics?.ciudad_restaurante) {
                        restName = `${globalData.logistics.restaurante} (${globalData.logistics.ciudad_restaurante})`;
                    }
                    title = (
                        <div className="flex flex-col">
                            <span>Las cartas te estarán esperando en el restaurante {restName} el {fecha}.</span>
                            <span className="text-gray-500 text-xs mt-1 font-medium">Pregunta por ellas al o la camarerx con la confimación de tu pedido</span>
                        </div>
                    );"""

text = text.replace(target_shipping, replacement_shipping)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated text logic for restaurant parenthesis!")

