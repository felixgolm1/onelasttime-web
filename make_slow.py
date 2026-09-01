import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Replace duration-150 with duration-500 and duration-200 with duration-700 for the toggles.

text = re.sub(
    r'(<button[^>]*?onClick=\{\(\) => set(IsLivingTogether|Status)[^>]*?duration-)150([^>]*?>\s*<div[^>]*?duration-)200([^>]*?>)',
    r'\g<1>500\g<3>700\g<4>',
    text,
    flags=re.DOTALL
)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated toggle speeds to be very slow!")

