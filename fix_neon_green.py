import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update text and color for the first line of shipping details (reservation made)
target_reserva = """                        <div className="flex flex-col gap-1">
                            <span className="mb-2">Las cartas te estarán esperando en tu mesa</span>
                            <span><strong className="text-gray-800">Nombre del restaurante:</strong> {restName}</span>"""
replacement_reserva = """                        <div className="flex flex-col gap-1">
                            <span className="mb-2 text-[#CCFF00] font-bold drop-shadow-sm">Las cartas te estarán esperando en tu mesa antes de que llegues</span>
                            <span><strong className="text-gray-800">Nombre del restaurante:</strong> {restName}</span>"""
text = text.replace(target_reserva, replacement_reserva)

# 2. Update text and color for the first line of shipping details (restaurant delivery, no reservation)
target_no_reserva = """                        <div className="flex flex-col gap-1">
                            <span className="mb-2">Las cartas te estarán esperando en el restaurante</span>
                            <span><strong className="text-gray-800">Nombre del restaurante:</strong> {restName}</span>"""
replacement_no_reserva = """                        <div className="flex flex-col gap-1">
                            <span className="mb-2 text-[#CCFF00] font-bold drop-shadow-sm">Las cartas te estarán esperando en el restaurante antes de que llegues</span>
                            <span><strong className="text-gray-800">Nombre del restaurante:</strong> {restName}</span>"""
text = text.replace(target_no_reserva, replacement_no_reserva)

# 3. Update Gratis color to #CCFF00
target_costColor = """                    costColor: cost === 0 ? 'text-green-600' : 'text-gray-900'"""
replacement_costColor = """                    costColor: cost === 0 ? 'text-[#CCFF00]' : 'text-gray-900'"""
text = text.replace(target_costColor, replacement_costColor)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated shipping text and cost colors!")

