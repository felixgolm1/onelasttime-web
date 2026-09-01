import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                        {/* COLUMNA DERECHA: RESUMEN */}
                        <div className="space-y-8 bg-white rounded-[2rem] p-6 md:p-8 border border-gray-200 shadow-[0_20px_50px_rgba(0,0,0,0.05)] h-fit md:sticky md:top-[128px] self-start">"""

replacement = """                        {/* COLUMNA DERECHA: RESUMEN */}
                        <div className="space-y-8 bg-white rounded-[2rem] p-6 md:p-8 border border-gray-200 shadow-[0_20px_50px_rgba(0,0,0,0.05)] h-fit md:sticky md:top-[128px] self-start max-h-[calc(100vh-160px)] overflow-y-auto custom-scrollbar">"""
text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Added max-h and overflow!")

