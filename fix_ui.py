import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

old_ui = """                                </div>
                                                                <div className="space-y-2">
                                    <div className="flex justify-between text-sm text-gray-500">
                                        <span>{isDigital ? 'Envío Inmediato (Email/Web)' : `Envío a ${globalData.logistics?.ciudad || 'tu zona'}`}</span>
                                        <span className="text-green-600 font-medium">Gratis</span>
                                    </div>
                                    <div className="flex justify-between items-center text-2xl font-black pt-4 border-t border-gray-200 text-black">"""

new_ui = """                                </div>
                                
                                <div className="mt-8">
                                    <h3 className="font-bold text-lg text-gray-900 mb-4">Detalles del envío</h3>
                                    <div className="flex justify-between items-start text-sm text-gray-500 mb-6">
                                        <span className="pr-4">{shipping.title}</span>
                                        <span className={`font-medium whitespace-nowrap ${shipping.costColor}`}>{shipping.costText}</span>
                                    </div>
                                </div>

                                <div className="space-y-2">
                                    <div className="flex justify-between items-center text-2xl font-black pt-4 border-t border-gray-200 text-black">"""

if old_ui in text:
    text = text.replace(old_ui, new_ui)
    with open("arbol.html", "w", encoding="utf-8") as f:
        f.write(text)
    print("UI replaced")
else:
    print("Old UI block not found. Let's try matching with regex.")
    match = re.search(r'</div\s*>\s*<div\s+className="space-y-2">\s*<div\s+className="flex justify-between text-sm text-gray-500">\s*<span[^>]*>\{isDigital[^}]*\}</span\s*>\s*<span[^>]*>Gratis</span\s*>\s*</div\s*>\s*<div\s+className="flex justify-between items-center text-2xl font-black pt-4 border-t border-gray-200 text-black">', text)
    if match:
        text = text[:match.start()] + new_ui + text[match.end():]
        with open("arbol.html", "w", encoding="utf-8") as f:
            f.write(text)
        print("UI replaced via regex")
    else:
        print("Failed to find via regex too")

