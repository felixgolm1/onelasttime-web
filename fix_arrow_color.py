import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Current class: "w-12 h-12 rounded-full border-2 border-black flex items-center justify-center text-black hover:bg-black hover:text-[#CCFF00] transition-colors active:scale-95 shadow-sm"
# New class: "w-12 h-12 rounded-full flex items-center justify-center bg-black text-white hover:bg-[#1a1a1a] hover:text-[#CCFF00] transition-colors active:scale-95 shadow-md"

old_cls = 'className="w-12 h-12 rounded-full border-2 border-black flex items-center justify-center text-black hover:bg-black hover:text-[#CCFF00] transition-colors active:scale-95 shadow-sm"'
new_cls = 'className="w-12 h-12 rounded-full flex items-center justify-center bg-black text-white hover:bg-[#1a1a1a] hover:text-[#CCFF00] hover:shadow-[0_4px_12px_rgba(204,255,0,0.15)] transition-all duration-300 active:scale-95 shadow-md"'

text = text.replace(old_cls, new_cls)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated arrow button colors!")

