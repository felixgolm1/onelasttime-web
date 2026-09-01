import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Replace the "Seguir con las fisicas" button to have the lift hover effect
old_button = '<button type="button" onClick={() => setShowCrossSellModal(false)} className="px-6 py-2.5 bg-black text-white rounded-full font-semibold text-[10px] md:text-[11px] uppercase tracking-[0.1em] hover:bg-gray-800 transition-all active:scale-95 shadow-md">Seguir con las físicas</button>'
new_button = '<button type="button" onClick={() => setShowCrossSellModal(false)} className="px-6 py-2.5 bg-black text-white rounded-full font-semibold text-[10px] md:text-[11px] uppercase tracking-[0.1em] hover:bg-[#1a1a1a] hover:-translate-y-1.5 hover:shadow-[0_16px_32px_rgba(0,0,0,0.2)] transition-all duration-300 active:scale-95 shadow-md">Seguir con las físicas</button>'

# Also check for the other modal's button if it exists
old_modal2_button = '<button type="button" onClick={() => setShowModal(false)} className="px-6 py-2.5 bg-black text-white rounded-full font-semibold text-[10px] md:text-[11px] uppercase tracking-[0.1em] hover:bg-gray-800 transition-all active:scale-95 shadow-md">Seguir con las cartas físicas</button>'
new_modal2_button = '<button type="button" onClick={() => setShowModal(false)} className="px-6 py-2.5 bg-black text-white rounded-full font-semibold text-[10px] md:text-[11px] uppercase tracking-[0.1em] hover:bg-[#1a1a1a] hover:-translate-y-1.5 hover:shadow-[0_16px_32px_rgba(0,0,0,0.2)] transition-all duration-300 active:scale-95 shadow-md">Seguir con las cartas físicas</button>'


text = text.replace(old_button, new_button)
if old_modal2_button in text:
    text = text.replace(old_modal2_button, new_modal2_button)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated hover effects!")

