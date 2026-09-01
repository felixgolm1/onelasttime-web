import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update Nombre de la reserva
target_reserva = """                            <span className="text-gray-500 text-xs mt-1 font-medium">Nombre de la reserva: {resName}</span>"""
replacement_reserva = """                            <span className="mt-1"><strong className="text-gray-800">Nombre de la reserva:</strong> {resName}</span>"""
text = text.replace(target_reserva, replacement_reserva)

# 2. Update Información de contacto
target_info = """                                    <div className="mb-6">
                                            <strong className="text-gray-800 block mb-2">
                                                {isDigital ? 'Información de contacto para la entrega:' : 'Información de contacto para el seguimiento del envío:'}
                                            </strong>"""
replacement_info = """                                    <div className="mb-6 text-sm">
                                            <strong className="text-gray-800 block mb-2">
                                                {isDigital ? 'Información de contacto para la entrega:' : 'Información de contacto para el seguimiento del envío:'}
                                            </strong>"""
text = text.replace(target_info, replacement_info)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated text sizing!")

