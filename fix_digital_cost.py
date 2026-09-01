import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Fix the empty costText for digital
old_logic = """                        title: (
                            <>
                                Envío de enlace al:<br/>
                                WhatsApp: {phone}<br/>
                                Email: {email}
                            </>
                        ),
                        cost: 0,
                        costText: '',"""

new_logic = """                        title: (
                            <>
                                Envío de enlace al:<br/>
                                WhatsApp: {phone}<br/>
                                Email: {email}
                            </>
                        ),
                        cost: 0,
                        costText: '0€',"""

if old_logic in text:
    text = text.replace(old_logic, new_logic)
    with open("arbol.html", "w", encoding="utf-8") as f:
        f.write(text)
    print("Updated digital cost text!")
else:
    print("Not found")

