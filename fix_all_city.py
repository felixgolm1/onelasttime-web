import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Fix in lines 3660, 3664
text = text.replace("globalData.logistics?.ciudad ||", "globalData.logistics?.ciudad_entrega || globalData.logistics?.ciudad_restaurante ||")

# Fix in line 3798 (Stripe metadata tracking)
text = text.replace("globalData.logistics?.ciudad || 'N/A'", "globalData.logistics?.ciudad_entrega || globalData.logistics?.ciudad_restaurante || 'N/A'")


with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated ALL remaining city fields!")

