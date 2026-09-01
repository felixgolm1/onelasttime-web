import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Fix goBackPhase logic
old_logic = "if (globalData.formatId && prev.globalData.formatId !== globalData.formatId) {"
new_logic = "if (globalData.formatId && prev.globalData.formatId && prev.globalData.formatId !== globalData.formatId) {"

text = text.replace(old_logic, new_logic)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated goBackPhase condition!")

