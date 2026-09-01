import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                                <div className="mt-5 bg-gray-50 rounded-xl p-3.5 border border-gray-100 flex items-start gap-3 text-left">
                                    <span className="text-lg leading-none mt-0.5">🤝</span>
                                    <p className="text-[13px] text-gray-600 leading-snug">
                                        <strong className="text-gray-900 font-bold">Garantía 100% libre de riesgo:</strong> Si la experiencia no cumple tus expectativas, te devolvemos el dinero sin preguntas.
                                    </p>
                                </div>"""

replacement = """                                <div className="text-center mt-4">
                                    <p className="text-[13px] text-gray-900 font-bold leading-snug">
                                        Garantía 100% libre de riesgo: Si no te gustan, te devolvemos el dinero sin preguntas
                                    </p>
                                </div>"""
text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated guarantee text!")

