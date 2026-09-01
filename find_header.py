import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find("const LogisticsForm =")
end_idx = text.find("const Checkout =", idx)
logistics = text[idx:end_idx]

for line in logistics.split("\n"):
    if "onBack" in line or "<button" in line or "svg" in line or "←" in line:
        pass # too much output
        
# Let's find the header
header_match = re.search(r'<div className="w-full max-w-2xl mx-auto flex items-center justify-center relative mb-12">.*?</div>', logistics, flags=re.DOTALL)
if header_match:
    print(header_match.group(0))

