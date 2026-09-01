import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

text = re.sub(
    r'if \(str\.includes\("canarias"\)(.*?)el hierro"\) \|\| str\.match\(/\\b\(35\|38\)\\d\{3\}\\b/\)\) \{',
    r'if (str.includes("canarias")\1el hierro") || str.includes("puertito de los molinos") || str.match(/\\b(35|38)\\d{3}\\b/)) {',
    text
)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated via regex")
