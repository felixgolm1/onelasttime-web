import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target_notas = """                                    {globalData.logistics?.direccion && (
                                    <div className="mb-6">
                                        <strong className="text-gray-800 block mb-2">
                                            ¿Quieres que tengamos algo en cuenta para la entrega?
                                        </strong>
                                        <div className="mt-1 flex flex-col gap-1">
                                            <div className={`flex items-center transition-all duration-300 ease-out ${editingContactField === 'notas' ? 'h-[36px]' : 'h-[24px]'}`}>
                                                <div className="relative flex-1 h-full">"""

replacement_notas = """                                    {globalData.logistics?.direccion && (
                                    <div className="mb-6 text-sm flex flex-col gap-1">
                                        <div className={`flex items-start sm:items-center flex-col sm:flex-row transition-all duration-300 ease-out ${editingContactField === 'notas' ? 'min-h-[36px]' : 'min-h-[24px]'}`}>
                                            <strong className="text-gray-800 mr-2 mb-1 sm:mb-0">
                                                ¿Quieres que tengamos algo en cuenta para la entrega?
                                            </strong>
                                            <div className="relative flex-1 h-full w-full sm:w-auto mt-1 sm:mt-0">"""
text = text.replace(target_notas, replacement_notas)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated notes format!")

