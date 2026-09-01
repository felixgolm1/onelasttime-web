import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                                <div className="text-center mt-4">
                                    <p className="text-base text-gray-900 font-bold leading-snug">
                                        Si no te gustan, te devolvemos el dinero sin preguntas
                                    </p>
                                </div>"""

replacement = """                                <div className="text-center mt-4">
                                    <p className="text-base text-gray-900 font-bold leading-snug">
                                        Si no te gustan, te devolvemos el 100% del dinero sin preguntas
                                    </p>
                                </div>"""
text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Added 100%!")

