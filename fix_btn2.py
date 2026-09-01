import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Replace button for phone
text = text.replace(
    "<button onClick={handleSaveContact} className={`rounded-full px-3 py-1 text-xs font-bold whitespace-nowrap transition-colors duration-200 ${!phoneValid ? 'bg-red-500 text-white' : 'bg-[#CCFF00] text-black hover:bg-[#b3e600]'}`} tabIndex={editingContactField === 'phone' ? 0 : -1}>OK</button>",
    "<button onClick={handleSaveContact} className={`rounded-full px-3 py-1 text-xs font-bold whitespace-nowrap transition-all duration-150 ${!phoneValid ? 'bg-red-500 text-white' : 'bg-[#CCFF00] text-black hover:bg-[#b3e600]'} ${activeContactBtn && editingContactField === 'phone' ? 'scale-90 opacity-80' : 'active:scale-90 active:opacity-80'}`} tabIndex={editingContactField === 'phone' ? 0 : -1}>OK</button>"
)

# Replace button for email
text = text.replace(
    "<button onClick={handleSaveContact} className={`rounded-full px-3 py-1 text-xs font-bold whitespace-nowrap transition-colors duration-200 ${!emailValid ? 'bg-red-500 text-white' : 'bg-[#CCFF00] text-black hover:bg-[#b3e600]'}`} tabIndex={editingContactField === 'email' ? 0 : -1}>OK</button>",
    "<button onClick={handleSaveContact} className={`rounded-full px-3 py-1 text-xs font-bold whitespace-nowrap transition-all duration-150 ${!emailValid ? 'bg-red-500 text-white' : 'bg-[#CCFF00] text-black hover:bg-[#b3e600]'} ${activeContactBtn && editingContactField === 'email' ? 'scale-90 opacity-80' : 'active:scale-90 active:opacity-80'}`} tabIndex={editingContactField === 'email' ? 0 : -1}>OK</button>"
)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated successfully")
