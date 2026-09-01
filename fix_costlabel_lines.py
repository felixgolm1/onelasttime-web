import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target_logic = """                let costLabel = null;
                if (isIslandSupplement) {
                    costLabel = "(Suplemento islas. Gratis en península)";
                }"""

replacement_logic = """                let costLabel = null;
                if (isIslandSupplement) {
                    costLabel = (
                        <>
                            Suplemento islas<br />
                            (gratis en península)
                        </>
                    );
                }"""
text = text.replace(target_logic, replacement_logic)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated costLabel lines!")

