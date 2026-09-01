import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                                <div className="text-center mt-4">
                                    <p className="text-[13px] text-gray-900 font-bold leading-snug">
                                        Garantía 100% libre de riesgo: Si no te gustan, te devolvemos el dinero sin preguntas
                                    </p>
                                </div>"""

replacement = """                                <div className="text-center mt-4">
                                    <p className="text-[13px] text-gray-900 font-bold leading-snug">
                                        Si no te gustan, te devolvemos el dinero sin preguntas
                                    </p>
                                </div>"""
text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Removed prefix!")

