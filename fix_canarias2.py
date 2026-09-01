import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """            if (!isDigital && globalData.logistics) {
                let cityField = globalData.logistics.ciudad_entrega || globalData.logistics.ciudad_restaurante || globalData.logistics.punto_recogida || '';
                let str = (cityField + ' ' + (globalData.logistics.direccion || '')).toLowerCase();
                if (str.includes("balears") || str.includes("baleares") || str.includes("ceuta") || str.includes("melilla") || str.match(/\\b(07|51|52)\\d{3}\\b/) || str.includes("palma de mallorca") || str.includes("ibiza") || str.includes("menorca")) {
                    isBalearesCeutaMelilla = true;
                }
                if (str.includes("canarias") || str.includes("las palmas") || str.includes("tenerife") || str.match(/\\b(35|38)\\d{3}\\b/)) {
                    isCanarias = true;
                }
            }"""

replacement = """            if (!isDigital && globalData.logistics) {
                let cityField = globalData.logistics.ciudad_entrega || globalData.logistics.ciudad_restaurante || globalData.logistics.punto_recogida || '';
                let str = (cityField + ' ' + (globalData.logistics.direccion || '')).toLowerCase();
                if (globalData.logistics.place_details && globalData.logistics.place_details.address_components) {
                    str += ' ' + JSON.stringify(globalData.logistics.place_details.address_components).toLowerCase();
                }
                if (globalData.logistics.cityFieldDetails && globalData.logistics.cityFieldDetails.address_components) {
                    str += ' ' + JSON.stringify(globalData.logistics.cityFieldDetails.address_components).toLowerCase();
                }
                if (globalData.logistics.restaurante_details && globalData.logistics.restaurante_details.address_components) {
                    str += ' ' + JSON.stringify(globalData.logistics.restaurante_details.address_components).toLowerCase();
                }
                
                if (str.includes("balears") || str.includes("baleares") || str.includes("ceuta") || str.includes("melilla") || str.includes("palma de mallorca") || str.includes("ibiza") || str.includes("menorca") || str.match(/\\b(07|51|52)\\d{3}\\b/)) {
                    isBalearesCeutaMelilla = true;
                }
                if (str.includes("canarias") || str.includes("las palmas") || str.includes("tenerife") || str.includes("fuerteventura") || str.includes("lanzarote") || str.includes("la palma") || str.includes("la gomera") || str.includes("el hierro") || str.match(/\\b(35|38)\\d{3}\\b/)) {
                    isCanarias = true;
                }
            }"""
text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated isCanarias logic in Checkout")

