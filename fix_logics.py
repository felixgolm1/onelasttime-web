import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. isCanarias logic
target_canarias = """            if (!isDigital && globalData.logistics) {
                let str = ((globalData.logistics.ciudad || '') + ' ' + (globalData.logistics.direccion || '')).toLowerCase();"""

replacement_canarias = """            if (!isDigital && globalData.logistics) {
                let cityField = globalData.logistics.ciudad_entrega || globalData.logistics.ciudad_restaurante || globalData.logistics.punto_recogida || '';
                let str = (cityField + ' ' + (globalData.logistics.direccion || '')).toLowerCase();"""
text = text.replace(target_canarias, replacement_canarias)

# 2. Date lowercasing
target_date = """const days = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];"""
replacement_date = """const days = ['domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado'];"""
text = text.replace(target_date, replacement_date)

# 3. derivedNotas fallback
target_notas = """const derivedNotas = globalData.contact?.notas_entrega || '';"""
replacement_notas = """const derivedNotas = globalData.contact?.notas_entrega || globalData.logistics?.notas_entrega || '';"""
text = text.replace(target_notas, replacement_notas)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated logics!")

