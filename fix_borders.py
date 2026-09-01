import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                                <div className="mt-6 pt-6 border-t-[1.5px] border-gray-200">
                                    <div className="flex justify-between items-start mb-4">
                                        <h3 className="font-bold text-lg text-gray-900">Detalles del envío</h3>"""
                                        
replacement = """                                <div className="mt-6">
                                    <div className="flex justify-between items-start mb-4">
                                        <h3 className="font-bold text-lg text-gray-900">Detalles del envío</h3>"""

text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Removed duplicate border!")

