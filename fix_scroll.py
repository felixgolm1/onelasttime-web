import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """        const Checkout = ({ globalData, setGlobalData, progress, onBack }) => {"""

replacement = """        const Checkout = ({ globalData, setGlobalData, progress, onBack }) => {
            useEffect(() => { window.scrollTo(0, 0); }, []);"""
text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Added scrollTo to Checkout!")

