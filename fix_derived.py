import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Add derivedPhone and derivedEmail just before editContactData
old_state = "const [editContactData, setEditContactData] = useState({ phone: globalData.contact?.phone || '', email: globalData.contact?.email || '' });"
new_state = """const derivedPhone = globalData.contact?.phone || globalData.logistics?.tu_whatsapp || '';
            const derivedEmail = globalData.contact?.email || globalData.logistics?.tu_email || '';
            const [editContactData, setEditContactData] = useState({ phone: derivedPhone, email: derivedEmail });"""

if old_state in text:
    text = text.replace(old_state, new_state)
else:
    print("Could not find state declaration")

# 2. Replace globalData.contact?.phone with derivedPhone in Checkout
# But ONLY inside Checkout. It's safer to just replace it generally where it says globalData.contact?.phone || ''
# Wait, the rendering is `{globalData.contact?.phone || 'No indicado'}`
text = text.replace("{globalData.contact?.phone || 'No indicado'}", "{derivedPhone || 'No indicado'}")
text = text.replace("{globalData.contact?.email || 'No indicado'}", "{derivedEmail || 'No indicado'}")

# 3. And in the onClick handlers for edit
text = text.replace("phone: globalData.contact?.phone || ''", "phone: derivedPhone")
text = text.replace("email: globalData.contact?.email || ''", "email: derivedEmail")

# 4. In getShippingDetails() for digital it says:
# const phone = editContactData.phone || globalData.contact?.phone || '';
# Replace it with derivedPhone
text = text.replace("const phone = editContactData.phone || globalData.contact?.phone || '';", "const phone = editContactData.phone || derivedPhone;")
text = text.replace("const email = editContactData.email || globalData.contact?.email || '';", "const email = editContactData.email || derivedEmail;")

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated references!")

