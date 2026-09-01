import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Replace the toggle speeds. We only want to touch the toggles in TreeEngine (isLivingTogether, prometidos, casados)
# Specifically, we look for `duration-300` -> `duration-150` and `duration-400` -> `duration-200` in those buttons.
# A regex on the button tags:

text = re.sub(
    r'(<button[^>]*?onClick=\{\(\) => set(IsLivingTogether|Status)[^>]*?duration-)300([^>]*?>\s*<div[^>]*?duration-)400([^>]*?>)',
    r'\g<1>150\g<3>200\g<4>',
    text,
    flags=re.DOTALL
)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated toggle speeds!")

