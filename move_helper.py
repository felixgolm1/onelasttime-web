import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

helper_fn = """                        const formatRestaurante = () => {
                let restName = globalData.logistics?.restaurante || '';
                let ciudad = globalData.logistics?.ciudad_restaurante || '';
                if (!restName) return 'tu restaurante';
                
                const commaIdx = restName.indexOf(',');
                if (commaIdx > -1) {
                    const name = restName.substring(0, commaIdx).trim();
                    const addr = restName.substring(commaIdx + 1).trim();
                    if (ciudad && !addr.toLowerCase().includes(ciudad.toLowerCase())) {
                        return `${name} (${addr}, ${ciudad})`;
                    } else {
                        return `${name} (${addr})`;
                    }
                } else {
                    if (ciudad) {
                        return `${restName} (${ciudad})`;
                    }
                    return restName;
                }
            };\n\n"""

# Remove helper from current location
text = text.replace(helper_fn, "")

# Insert helper before `let dondeLasUsaras`
target = "            let dondeLasUsaras = '';"
text = text.replace(target, helper_fn.strip() + "\n\n" + target)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Moved helper function!")

