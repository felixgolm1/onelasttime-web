import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Fix getShippingDetails()
old_city = "const city = globalData.logistics?.ciudad || '';"
new_city = "const city = globalData.logistics?.ciudad_entrega || globalData.logistics?.ciudad_restaurante || '';"
text = text.replace(old_city, new_city)

# Fix Checkout
old_checkout = "${globalData.logistics?.ciudad || ''}"
new_checkout = "${globalData.logistics?.ciudad_entrega || globalData.logistics?.ciudad_restaurante || ''}"
text = text.replace(old_checkout, new_checkout)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated city fields!")

