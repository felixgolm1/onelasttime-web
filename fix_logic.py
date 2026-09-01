import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

old_logic = """            const isDigital = globalData.formatId?.includes('digital');
            const price = isDigital ? '8,99€' : '13,99€';
            const formatName = isDigital ? 'Edición Digital' : 'Edición Física';"""

new_logic = """            const isDigital = globalData.formatId?.includes('digital');
            const formatName = isDigital ? 'Edición Digital' : 'Edición Física';
            
            let isBalearesCeutaMelilla = false;
            let isCanarias = false;
            if (!isDigital && globalData.logistics) {
                let str = ((globalData.logistics.ciudad || '') + ' ' + (globalData.logistics.direccion || '')).toLowerCase();
                if (str.includes("balears") || str.includes("baleares") || str.includes("ceuta") || str.includes("melilla") || str.match(/\\b(07|51|52)\\d{3}\\b/) || str.includes("palma de mallorca") || str.includes("ibiza") || str.includes("menorca")) {
                    isBalearesCeutaMelilla = true;
                }
                if (str.includes("canarias") || str.includes("las palmas") || str.includes("tenerife") || str.match(/\\b(35|38)\\d{3}\\b/)) {
                    isCanarias = true;
                }
            }

            const getShippingDetails = () => {
                if (isDigital) {
                    return {
                        title: `Envío digital a ${editContactData.email || globalData.contact?.email || ''}`,
                        cost: 0,
                        costText: 'Gratis',
                        costColor: 'text-black'
                    };
                }

                let cost = 0;
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
                    const dir = globalData.logistics?.direccion || globalData.logistics?.ciudad || '';
                    title = `Envío garantizado antes del ${fecha} al restaurante ${restName} de la ${dir}`;
                } else if (isPickup) {
                    const pickup = globalData.logistics?.punto_recogida || '';
                    const dir = globalData.logistics?.direccion || globalData.logistics?.ciudad || '';
                    title = `Envío garantizado antes del ${fecha} al punto de recogida ${pickup} de la ${dir}`;
                } else {
                    const dir = globalData.logistics?.direccion || '';
                    const info = globalData.logistics?.info_adicional_direccion ? ' ' + globalData.logistics.info_adicional_direccion : '';
                    const city = globalData.logistics?.ciudad || '';
                    title = `Envío garantizado antes del ${fecha} a la ${dir}${info}, ${city}`;
                }
                
                return {
                    title: title,
                    cost: cost,
                    costText: cost === 0 ? 'Gratis' : `${cost}€`,
                    costColor: cost === 0 ? 'text-green-600' : 'text-gray-900'
                };
            };

            const shipping = getShippingDetails();
            const basePrice = isDigital ? 8.99 : 13.99;
            const totalPriceNum = basePrice + shipping.cost;
            const price = totalPriceNum.toFixed(2).replace('.', ',') + '€';"""

text = text.replace(old_logic, new_logic)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Logic injected")
