import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update ObjectiveScreen handleInspire
old_handle_1 = """            const handleInspire = () => {
                setPlaceholderIndex((prev) => (prev + 1) % examples.length);
                setIsAnimatingPlaceholder(true);
            };"""
new_handle_1 = """            const handleInspire = (direction = 'next') => {
                if (direction === 'next') {
                    setPlaceholderIndex((prev) => (prev + 1) % examples.length);
                } else {
                    setPlaceholderIndex((prev) => (prev - 1 + examples.length) % examples.length);
                }
                setIsAnimatingPlaceholder(true);
            };"""
text = text.replace(old_handle_1, new_handle_1)

# 2. Update CustomizationN4 handleInspire
old_handle_2 = """            const handleInspire = () => {
                setPlaceholderIndex((prev) => (prev + 1) % examplesDetalles.length);
            };"""
new_handle_2 = """            const handleInspire = (direction = 'next') => {
                if (direction === 'next') {
                    setPlaceholderIndex((prev) => (prev + 1) % examplesDetalles.length);
                } else {
                    setPlaceholderIndex((prev) => (prev - 1 + examplesDetalles.length) % examplesDetalles.length);
                }
            };"""
text = text.replace(old_handle_2, new_handle_2)

# 3. Replace the JSX buttons
old_btn = """                                <button 
                                    onClick={handleInspire}
                                    className="btn-black w-full uppercase text-sm tracking-wider"
                                >
                                    Siguiente ejemplo
                                </button>"""

new_btn = """                                <div className="flex justify-center items-center gap-6 w-full">
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

text = text.replace(old_btn, new_btn)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated arrows!")

