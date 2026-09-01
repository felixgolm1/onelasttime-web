import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Undo neon green in Gratis
target_costColor = """                    costColor: cost === 0 ? 'text-[#CCFF00]' : 'text-gray-900'"""
replacement_costColor = """                    costColor: cost === 0 ? 'text-green-600' : 'text-gray-900'"""
text = text.replace(target_costColor, replacement_costColor)

# Revert neon green in shipping details (reservation made)
target_reserva = """                        <div className="flex flex-col gap-1">
                            <span className="mb-2 text-[#CCFF00] font-bold drop-shadow-sm">Las cartas te estarán esperando en tu mesa antes de que llegues</span>"""
replacement_reserva = """                        <div className="flex flex-col gap-1">
                            <strong className="mb-2 text-gray-800">Las cartas te estarán esperando en tu mesa antes de que llegues</strong>"""
text = text.replace(target_reserva, replacement_reserva)

# Revert neon green in shipping details (no reservation)
target_no_reserva = """                        <div className="flex flex-col gap-1">
                            <span className="mb-2 text-[#CCFF00] font-bold drop-shadow-sm">Las cartas te estarán esperando en el restaurante antes de que llegues</span>"""
replacement_no_reserva = """                        <div className="flex flex-col gap-1">
                            <strong className="mb-2 text-gray-800">Las cartas te estarán esperando en el restaurante antes de que llegues</strong>"""
text = text.replace(target_no_reserva, replacement_no_reserva)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Reverted colors!")

