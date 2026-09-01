import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

new_btn = """<div className="flex justify-center items-center gap-6 w-full">
                                    <button 
                                        onClick={() => handleInspire('prev')}
                                        className="w-12 h-12 rounded-full border-2 border-black flex items-center justify-center text-black hover:bg-black hover:text-[#CCFF00] transition-colors active:scale-95 shadow-sm"
                                    >
                                        <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 19l-7-7 7-7" /></svg>
                                    </button>
                                    <button 
                                        onClick={() => handleInspire('next')}
                                        className="w-12 h-12 rounded-full border-2 border-black flex items-center justify-center text-black hover:bg-black hover:text-[#CCFF00] transition-colors active:scale-95 shadow-sm"
                                    >
                                        <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 5l7 7-7 7" /></svg>
                                    </button>
                                </div>"""

pattern = r'<button\s*onClick=\{handleInspire\}\s*className="btn-black w-full uppercase text-sm tracking-wider"\s*>\s*Siguiente ejemplo\s*</button>'

text = re.sub(pattern, new_btn, text)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated second button!")

