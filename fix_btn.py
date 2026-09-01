import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# PHONE
# Replace onKeyDown
text = text.replace(
    "onKeyDown={e => { if (e.key === 'Enter') handleSaveContact(); if (e.key === 'Escape') { setEditingContactField(null); setContactErrorMsg(null); } }} className=\"bg-transparent outline-none text-sm px-2 w-full text-black placeholder-gray-300\" placeholder=\"Ej: +34 600...\" tabIndex={editingContactField === 'phone' ? 0 : -1}",
    "onKeyDown={e => { if (e.key === 'Enter') { setActiveContactBtn(true); setTimeout(() => setActiveContactBtn(false), 150); handleSaveContact(); } if (e.key === 'Escape') { setEditingContactField(null); setContactErrorMsg(null); } }} className=\"bg-transparent outline-none text-sm px-2 w-full text-black placeholder-gray-300\" placeholder=\"Ej: +34 600...\" tabIndex={editingContactField === 'phone' ? 0 : -1}"
)

# Replace button
text = text.replace(
    "<button onClick={handleSaveContact} className={`rounded-full px-3 py-1 text-xs font-bold whitespace-nowrap transition-colors duration-200 ${!isValidPhone(editContactData.phone) ? 'bg-red-500 text-white' : 'bg-[#CCFF00] text-black hover:bg-[#b3e600]'}`} tabIndex={editingContactField === 'phone' ? 0 : -1}>OK</button>",
    "<button onClick={handleSaveContact} className={`rounded-full px-3 py-1 text-xs font-bold whitespace-nowrap transition-all duration-150 ${!isValidPhone(editContactData.phone) ? 'bg-red-500 text-white' : 'bg-[#CCFF00] text-black hover:bg-[#b3e600]'} ${activeContactBtn && editingContactField === 'phone' ? 'scale-90 opacity-80' : 'active:scale-90 active:opacity-80'}`} tabIndex={editingContactField === 'phone' ? 0 : -1}>OK</button>"
)


# EMAIL
# Replace onKeyDown
text = text.replace(
    "onKeyDown={e => { if (e.key === 'Enter') handleSaveContact(); if (e.key === 'Escape') { setEditingContactField(null); setContactErrorMsg(null); } }} className=\"bg-transparent outline-none text-sm px-2 w-full text-black placeholder-gray-300\" placeholder=\"tu@email.com\" tabIndex={editingContactField === 'email' ? 0 : -1}",
    "onKeyDown={e => { if (e.key === 'Enter') { setActiveContactBtn(true); setTimeout(() => setActiveContactBtn(false), 150); handleSaveContact(); } if (e.key === 'Escape') { setEditingContactField(null); setContactErrorMsg(null); } }} className=\"bg-transparent outline-none text-sm px-2 w-full text-black placeholder-gray-300\" placeholder=\"tu@email.com\" tabIndex={editingContactField === 'email' ? 0 : -1}"
)

# Replace button
text = text.replace(
    "<button onClick={handleSaveContact} className={`rounded-full px-3 py-1 text-xs font-bold whitespace-nowrap transition-colors duration-200 ${!isValidEmail(editContactData.email) ? 'bg-red-500 text-white' : 'bg-[#CCFF00] text-black hover:bg-[#b3e600]'}`} tabIndex={editingContactField === 'email' ? 0 : -1}>OK</button>",
    "<button onClick={handleSaveContact} className={`rounded-full px-3 py-1 text-xs font-bold whitespace-nowrap transition-all duration-150 ${!isValidEmail(editContactData.email) ? 'bg-red-500 text-white' : 'bg-[#CCFF00] text-black hover:bg-[#b3e600]'} ${activeContactBtn && editingContactField === 'email' ? 'scale-90 opacity-80' : 'active:scale-90 active:opacity-80'}`} tabIndex={editingContactField === 'email' ? 0 : -1}>OK</button>"
)


with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated successfully")

