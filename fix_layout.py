import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update comma in address info
target_home = """                } else {
                    const dir = globalData.logistics?.direccion || '';
                    const info = globalData.logistics?.info_adicional_direccion ? ' ' + globalData.logistics.info_adicional_direccion : '';"""

replacement_home = """                } else {
                    const dir = globalData.logistics?.direccion || '';
                    const info = globalData.logistics?.info_adicional_direccion ? ', ' + globalData.logistics.info_adicional_direccion : '';"""
text = text.replace(target_home, replacement_home)

# 2. Update layout of notas to put input on next line
target_notas = """                                    <div className="mb-6 text-sm flex flex-col gap-1">
                                        <div className={`flex items-start sm:items-center flex-col sm:flex-row transition-all duration-300 ease-out ${editingContactField === 'notas' ? 'min-h-[36px]' : 'min-h-[24px]'}`}>
                                            <strong className="text-gray-800 mr-2 mb-1 sm:mb-0">
                                                ¿Quieres que tengamos algo en cuenta para la entrega?
                                            </strong>
                                            <div className="relative flex-1 h-full w-full sm:w-auto mt-1 sm:mt-0">"""

replacement_notas = """                                    <div className="mb-6 text-sm flex flex-col gap-1">
                                        <div className={`flex flex-col transition-all duration-300 ease-out`}>
                                            <strong className="text-gray-800 mb-1">
                                                ¿Quieres que tengamos algo en cuenta para la entrega?
                                            </strong>
                                            <div className={`relative w-full ${editingContactField === 'notas' ? 'h-[36px]' : 'h-[24px]'}`}>"""
text = text.replace(target_notas, replacement_notas)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated address comma and notes layout!")

