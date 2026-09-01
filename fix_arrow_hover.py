import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

old_cls = 'className="w-12 h-12 rounded-full flex items-center justify-center bg-black text-white hover:bg-[#1a1a1a] hover:text-[#CCFF00] hover:shadow-[0_4px_12px_rgba(204,255,0,0.15)] transition-all duration-300 active:scale-95 shadow-md"'
new_cls = 'className="w-12 h-12 rounded-full flex items-center justify-center bg-black text-white hover:bg-[#1a1a1a] hover:-translate-y-1.5 hover:shadow-[0_16px_32px_rgba(0,0,0,0.2)] transition-all duration-300 active:scale-95 shadow-md"'

text = text.replace(old_cls, new_cls)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated arrow hover effect!")

