import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Replace the wrapper
text = text.replace(
    '<div className="mt-1 space-y-2">',
    '<div className="mt-1 flex flex-col gap-1">'
)

# Replace phone row
text = text.replace(
    '<div className="flex items-center min-h-[36px]">',
    '<div className={`flex items-center transition-all duration-300 ease-out ${editingContactField === \'phone\' ? \'h-[36px]\' : \'h-[24px]\'}`}>',
    1
)

# Replace email row
text = text.replace(
    '<div className="flex items-center min-h-[36px]">',
    '<div className={`flex items-center transition-all duration-300 ease-out ${editingContactField === \'email\' ? \'h-[36px]\' : \'h-[24px]\'}`}>',
    1
)

# Replace internal relative wrappers to inherit height perfectly
text = text.replace(
    '<div className="relative flex-1 h-[36px]">',
    '<div className="relative flex-1 h-full">'
)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated spacing and heights!")
