import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

old_logic = """                if (isDigital) {
                    return {
                        title: `Envío digital a ${editContactData.email || globalData.contact?.email || ''}`,
                        cost: 0,
                        costText: '',
                        costColor: 'text-black'
                    };
                }"""

new_logic = """                if (isDigital) {
                    return {
                        title: `Envío de enlace al WhatsApp ${editContactData.phone || globalData.contact?.phone || ''}`,
                        cost: 0,
                        costText: '',
                        costColor: 'text-black'
                    };
                }"""

if old_logic in text:
    text = text.replace(old_logic, new_logic)
    with open("arbol.html", "w", encoding="utf-8") as f:
        f.write(text)
    print("Logic replaced")
else:
    print("Old logic not found")
