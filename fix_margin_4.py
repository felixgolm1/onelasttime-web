import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                <div className="flex-1 py-12 px-6 flex flex-col items-center relative fade-in">
                    <div className="max-w-4xl w-full grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12 mt-24">"""

replacement = """                <div className="flex-1 py-12 px-6 flex flex-col items-center relative fade-in">
                    <div className="max-w-4xl w-full grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12 mt-32">"""
text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated margin to mt-32!")

