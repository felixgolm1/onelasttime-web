import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """            let dondeLasUsaras = '';
            const formatNode = dbFormat.find(x => x.id === globalData.formatId);
            if (globalData.formatId?.includes('otro')) {
                dondeLasUsaras = globalData.formatCustomPlace || 'Otro lugar';
            } else if (globalData.formatId?.includes('reserva') || globalData.formatId?.includes('restaurante')) {
                dondeLasUsaras = 'En un restaurante';
            } else if (formatNode) {
                dondeLasUsaras = formatNode.label;
            }"""

replacement = """            let dondeLasUsaras = '';
            const formatNode = dbFormat.find(x => x.id === globalData.formatId);
            if (globalData.formatId?.includes('otro')) {
                dondeLasUsaras = globalData.formatCustomPlace || 'Otro lugar';
            } else if (globalData.formatId?.includes('reserva') || globalData.formatId?.includes('restaurante')) {
                dondeLasUsaras = globalData.logistics?.restaurante ? `En el restaurante ${globalData.logistics.restaurante}` : 'En un restaurante';
            } else if (formatNode) {
                dondeLasUsaras = formatNode.label;
            }"""

text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated logic!")

