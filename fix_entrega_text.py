import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

old_text = "Entrega con enlace por WhatsApp justo al inicio de la cena o cuando quieras a partir de 10 minutos con un solo click. Por si os adelantáis"
new_text = "Entrega con enlace por WhatsApp y email justo al inicio de la cena o cuando quieras a partir de 10 minutos con un solo click. Por si os adelantáis"

if old_text in text:
    text = text.replace(old_text, new_text)
    with open("arbol.html", "w", encoding="utf-8") as f:
        f.write(text)
    print("Replaced!")
else:
    print("Not found! Trying with special chars")
    # Might have encoding issues in the terminal output, let's just use regex
    text = re.sub(r'Entrega con enlace por WhatsApp justo al inicio de la cena o cuando quieras a partir de 10 minutos con un solo click\. Por si os adelant.is', new_text, text)
    with open("arbol.html", "w", encoding="utf-8") as f:
        f.write(text)
    print("Replaced via regex!")
