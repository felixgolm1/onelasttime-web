import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

old_logic = """                if (isDigital) {
                    return {
                        title: `Envío de enlace al WhatsApp ${editContactData.phone || globalData.contact?.phone || ''}`,
                        cost: 0,
                        costText: '',
                        costColor: 'text-black'
                    };
                }"""

new_logic = """                if (isDigital) {
                    const phone = editContactData.phone || globalData.contact?.phone || '';
                    const email = editContactData.email || globalData.contact?.email || '';
                    return {
                        title: (
                            <>
                                Envío de enlace al:<br/>
                                WhatsApp: {phone}<br/>
                                Email: {email}
                            </>
                        ),
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
