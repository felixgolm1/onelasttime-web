import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                    paymentElement.on('ready', () => setIsStripeReady(true));"""

replacement = """                    paymentElement.on('ready', () => { setIsStripeReady(true); window.scrollTo(0, 0); });"""
text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Added scrollTo on stripe ready!")

