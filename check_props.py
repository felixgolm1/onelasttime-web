import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

match = re.search(r'<LogisticsForm.*?>', text, flags=re.DOTALL)
if match:
    print(match.group(0))

