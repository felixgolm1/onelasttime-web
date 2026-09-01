import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Add IDs to the inputs
text = text.replace(
    "className=\"bg-transparent outline-none text-sm px-2 w-full text-black placeholder-gray-300\" placeholder=\"Ej: +34 600...\"",
    "id=\"edit-phone-input\" className=\"bg-transparent outline-none text-sm px-2 w-full text-black placeholder-gray-300\" placeholder=\"Ej: +34 600...\""
)

text = text.replace(
    "className=\"bg-transparent outline-none text-sm px-2 w-full text-black placeholder-gray-300\" placeholder=\"tu@email.com\"",
    "id=\"edit-email-input\" className=\"bg-transparent outline-none text-sm px-2 w-full text-black placeholder-gray-300\" placeholder=\"tu@email.com\""
)

# Update the focus logic
text = text.replace(
    "setTimeout(() => e.currentTarget.parentElement.querySelector('input[type=\"tel\"]')?.focus(), 50);",
    "setTimeout(() => document.getElementById('edit-phone-input')?.focus(), 50);"
)

text = text.replace(
    "setTimeout(() => e.currentTarget.parentElement.querySelector('input[type=\"email\"]')?.focus(), 50);",
    "setTimeout(() => document.getElementById('edit-email-input')?.focus(), 50);"
)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Focus logic updated!")

