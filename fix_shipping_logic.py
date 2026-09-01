import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                let cost = 0;
                const isRestaurant = globalData.formatId?.includes('restaurante');
                const isPickup = globalData.logistics?.punto_recogida ? true : false;
                
                if (isBalearesCeutaMelilla) {
                    if (isRestaurant) cost = 3;
                    else if (isPickup) cost = 2;
                    else cost = 3;
                } else if (isCanarias) {
                    if (isRestaurant) cost = 3;
                    else if (isPickup) cost = 5;
                    else cost = 6;
                }
                
                const fecha = globalData.logistics?.fecha ? formatDate(globalData.logistics.fecha) : '';
                let title = '';
                
                if (isRestaurant) {
                    const restName = globalData.logistics?.restaurante || 'tu restaurante';
                    const dir = globalData.logistics?.direccion || globalData.logistics?.ciudad_entrega || globalData.logistics?.ciudad_restaurante || '';
                    title = `Envío garantizado antes del ${fecha} al restaurante ${restName} de la ${dir}`;
                } else if (isPickup) {
                    const pickup = globalData.logistics?.punto_recogida || '';
                    const dir = globalData.logistics?.direccion || globalData.logistics?.ciudad_entrega || globalData.logistics?.ciudad_restaurante || '';
                    title = `Envío garantizado antes del ${fecha} al punto de recogida ${pickup} de la ${dir}`;
                } else {
                    const dir = globalData.logistics?.direccion || '';
                    const info = globalData.logistics?.info_adicional_direccion ? ' ' + globalData.logistics.info_adicional_direccion : '';
                    const city = globalData.logistics?.ciudad_entrega || globalData.logistics?.ciudad_restaurante || '';
                    title = `Envío garantizado antes del ${fecha} a la ${dir}${info}, ${city}`;
                }"""

replacement = """                let cost = 0;
                const isReservationMade = globalData.formatId === 'cartas_fisicas_reserva_hecha';
                const isRestaurantDelivery = isReservationMade || (globalData.formatId === 'cartas_fisicas_reserva_no_hecha' && globalData.logistics?.restaurante);
                const isPickup = globalData.logistics?.punto_recogida ? true : false;
                
                if (isBalearesCeutaMelilla) {
                    if (isRestaurantDelivery) cost = 3;
                    else if (isPickup) cost = 2;
                    else cost = 3;
                } else if (isCanarias) {
                    if (isRestaurantDelivery) cost = 3;
                    else if (isPickup) cost = 5;
                    else cost = 6;
                }
                
                const fecha = globalData.logistics?.fecha ? formatDate(globalData.logistics.fecha) : '';
                let title = '';
                
                if (isReservationMade) {
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
                    );
                } else if (isPickup) {
                    const pickup = globalData.logistics?.punto_recogida || '';
                    const dir = globalData.logistics?.direccion || globalData.logistics?.ciudad_entrega || globalData.logistics?.ciudad_restaurante || '';
                    title = `Envío garantizado antes del ${fecha} al punto de recogida ${pickup} de la ${dir}`;
                } else {
                    const dir = globalData.logistics?.direccion || '';
                    const info = globalData.logistics?.info_adicional_direccion ? ' ' + globalData.logistics.info_adicional_direccion : '';
                    const city = globalData.logistics?.ciudad_entrega || globalData.logistics?.ciudad_restaurante || '';
                    title = `Envío garantizado antes del ${fecha} a la ${dir}${info}, ${city}`;
                }"""

if target in text:
    text = text.replace(target, replacement)
    with open("arbol.html", "w", encoding="utf-8") as f:
        f.write(text)
    print("Replaced getShippingDetails logic!")
else:
    print("Target block not found. Trying regex.")

