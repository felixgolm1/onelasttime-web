import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """            const getShippingDetails = () => {
                if (isDigital) {
                    const phone = editContactData.phone || derivedPhone;
                    const email = editContactData.email || derivedEmail;
                    return {
                        title: "Envío de enlace digital", 
                        cost: 0,
                        costText: '0€',
                        costColor: 'text-black'
                    };
                }

                let cost = 0;
                const isReservationMade = globalData.formatId === 'cartas_fisicas_reserva_hecha';
                const isRestaurantDelivery = isReservationMade || (globalData.formatId === 'cartas_fisicas_reserva_no_hecha' && globalData.logistics?.restaurante);
                const isPickup = globalData.logistics?.punto_recogida ? true : false;
                
                let isIslandSupplement = false;
                if (isBalearesCeutaMelilla) {
                    if (isRestaurantDelivery) cost = 3;
                    else {
                        if (isPickup) cost = 2;
                        else cost = 3;
                        isIslandSupplement = true;
                    }
                } else if (isCanarias) {
                    if (isRestaurantDelivery) cost = 3;
                    else {
                        if (isPickup) cost = 5;
                        else cost = 6;
                        isIslandSupplement = true;
                    }
                }
                
                let costLabel = null;
                if (isIslandSupplement) {
                    costLabel = (
                        <>
                            Suplemento islas<br />
                            (gratis en península)
                        </>
                    );
                }
                
                const fecha = globalData.logistics?.fecha ? formatDate(globalData.logistics.fecha) : '';"""

replacement = """            const getShippingDetails = () => {
                const fecha = globalData.logistics?.fecha ? formatDate(globalData.logistics.fecha) : '';
                
                if (isDigital) {
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
                }

                let cost = 0;
                const isReservationMade = globalData.formatId === 'cartas_fisicas_reserva_hecha';
                const isRestaurantDelivery = isReservationMade || (globalData.formatId === 'cartas_fisicas_reserva_no_hecha' && globalData.logistics?.restaurante);
                const isPickup = globalData.logistics?.punto_recogida ? true : false;
                
                let isIslandSupplement = false;
                if (isBalearesCeutaMelilla) {
                    if (isRestaurantDelivery) cost = 3;
                    else {
                        if (isPickup) cost = 2;
                        else cost = 3;
                        isIslandSupplement = true;
                    }
                } else if (isCanarias) {
                    if (isRestaurantDelivery) cost = 3;
                    else {
                        if (isPickup) cost = 5;
                        else cost = 6;
                        isIslandSupplement = true;
                    }
                }
                
                let costLabel = null;
                if (isIslandSupplement) {
                    costLabel = (
                        <>
                            Suplemento islas<br />
                            (gratis en península)
                        </>
                    );
                }"""
text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated digital title!")

