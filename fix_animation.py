import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Add CSS
css_to_add = """
        .fade-fast { animation: fadeInFast 0.3s ease-out both; }
        @keyframes fadeInFast { from { opacity: 0; transform: translateY(5px); } to { opacity: 1; transform: none; } }
"""
text = text.replace('/* --- UTILIDADES GLOBALES --- */', '/* --- UTILIDADES GLOBALES --- */\n' + css_to_add)

# 2. Add key and class to ObjectiveScreen
old_p_1 = """                                    <p className="text-base md:text-lg font-medium leading-relaxed text-center text-gray-600 font-inter italic">
                                        {formatExampleText(currentPlaceholder)}
                                    </p>"""
new_p_1 = """                                    <p key={placeholderIndex} className="text-base md:text-lg font-medium leading-relaxed text-center text-gray-600 font-inter italic fade-fast">
                                        {formatExampleText(currentPlaceholder)}
                                    </p>"""
text = text.replace(old_p_1, new_p_1)

# 3. Add key and class to CustomizationN4
old_p_2 = """                                    <p className="text-base md:text-lg font-medium leading-relaxed text-center text-gray-600 font-inter italic">
                                        {formatExampleText(currentModalExample)}
                                    </p>"""
new_p_2 = """                                    <p key={placeholderIndex} className="text-base md:text-lg font-medium leading-relaxed text-center text-gray-600 font-inter italic fade-fast">
                                        {formatExampleText(currentModalExample)}
                                    </p>"""
text = text.replace(old_p_2, new_p_2)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Added animations!")

