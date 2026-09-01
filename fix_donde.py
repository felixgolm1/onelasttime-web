import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Add the variable near the top of Checkout
idx = text.find("const Checkout = ({ globalData, setGlobalData, progress, onBack }) => {")
idx = text.find("const [editingContactField, setEditingContactField] = useState(null);", idx)

donde_logic = """
            let dondeLasUsaras = '';
            const formatNode = dbFormat.find(x => x.id === globalData.formatId);
            if (globalData.formatId?.includes('otro')) {
                dondeLasUsaras = globalData.formatCustomPlace || 'Otro lugar';
            } else if (globalData.formatId?.includes('reserva') || globalData.formatId?.includes('restaurante')) {
                dondeLasUsaras = 'En un restaurante';
            } else if (formatNode) {
                dondeLasUsaras = formatNode.label;
            }
"""

text = text[:idx] + donde_logic + "\n" + text[idx:]

# Add the UI element right below Formato de la experiencia
target = "<li><strong className=\"text-gray-800\">Formato de la experiencia:</strong> Cartas en versión {isDigital ? 'digital' : 'física'}</li>"
new_ui = target + "\n                                        {dondeLasUsaras && <li><strong className=\"text-gray-800\">¿Dónde las usarás?:</strong> {dondeLasUsaras}</li>}"

text = text.replace(target, new_ui)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Added Donde las usaras!")

