import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# I will add a helper function `formatRestaurante` inside Checkout to handle this logic cleanly.
helper_fn = """            const formatRestaurante = () => {
                let restName = globalData.logistics?.restaurante || '';
                let ciudad = globalData.logistics?.ciudad_restaurante || '';
                if (!restName) return 'tu restaurante';
                
                const commaIdx = restName.indexOf(',');
                if (commaIdx > -1) {
                    const name = restName.substring(0, commaIdx).trim();
                    const addr = restName.substring(commaIdx + 1).trim();
                    if (ciudad && !addr.toLowerCase().includes(ciudad.toLowerCase())) {
                        return `${name} (${addr}, ${ciudad})`;
                    } else {
                        return `${name} (${addr})`;
                    }
                } else {
                    if (ciudad) {
                        return `${restName} (${ciudad})`;
                    }
                    return restName;
                }
            };"""

# Insert the helper function before `const getShippingDetails`
text = text.replace("const getShippingDetails = () => {", helper_fn + "\n\n            const getShippingDetails = () => {")

# Update `dondeLasUsaras` logic
target_donde = """            } else if (globalData.formatId?.includes('reserva') || globalData.formatId?.includes('restaurante')) {
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
replacement_donde = """            } else if (globalData.formatId?.includes('reserva') || globalData.formatId?.includes('restaurante')) {
                const formatted = formatRestaurante();
                dondeLasUsaras = formatted === 'tu restaurante' ? 'En un restaurante' : `En el restaurante ${formatted}`;
            } else if (formatNode) {"""
text = text.replace(target_donde, replacement_donde)

# Update `getShippingDetails` logic
target_shipping_1 = """                if (isReservationMade) {
                    let restName = globalData.logistics?.restaurante || 'tu restaurante';
                    if (globalData.logistics?.restaurante && globalData.logistics?.ciudad_restaurante) {
                        restName = `${globalData.logistics.restaurante} (${globalData.logistics.ciudad_restaurante})`;
                    }
                    const resName = globalData.logistics?.reserva || 'tu nombre';"""
replacement_shipping_1 = """                if (isReservationMade) {
                    const restName = formatRestaurante();
                    const resName = globalData.logistics?.reserva || 'tu nombre';"""
text = text.replace(target_shipping_1, replacement_shipping_1)

target_shipping_2 = """                } else if (isRestaurantDelivery) {
                    let restName = globalData.logistics?.restaurante || 'tu restaurante';
                    if (globalData.logistics?.restaurante && globalData.logistics?.ciudad_restaurante) {
                        restName = `${globalData.logistics.restaurante} (${globalData.logistics.ciudad_restaurante})`;
                    }
                    title = ("""
replacement_shipping_2 = """                } else if (isRestaurantDelivery) {
                    const restName = formatRestaurante();
                    title = ("""
text = text.replace(target_shipping_2, replacement_shipping_2)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated restaurant formatting logic!")

