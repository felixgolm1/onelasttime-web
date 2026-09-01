import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Add `notas_entrega` to derived state in Checkout
text = text.replace(
    "const [editContactData, setEditContactData] = useState({ phone: derivedPhone, email: derivedEmail });",
    "const derivedNotas = globalData.contact?.notas_entrega || '';\n            const [editContactData, setEditContactData] = useState({ phone: derivedPhone, email: derivedEmail, notas_entrega: derivedNotas });"
)

# 2. Update handleSaveContact
text = text.replace(
    "phone: editContactData.phone, email: editContactData.email }",
    "phone: editContactData.phone, email: editContactData.email, notas_entrega: editContactData.notas_entrega }"
)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated state logic!")

