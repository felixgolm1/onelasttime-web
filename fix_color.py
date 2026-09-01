import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                                    <div className="flex justify-between items-start text-sm text-gray-500 mb-4">
                                        <div className="pr-4">{shipping.title}</div>
                                    </div>"""
replacement = """                                    <div className="flex justify-between items-start text-sm text-gray-600 mb-4">
                                        <div className="pr-4">{shipping.title}</div>
                                    </div>"""

text = text.replace(target, replacement)

# And also for the contact fields to be text-gray-600?
# They use `text-gray-900` for the value `derivedPhone` etc. So that's fine.

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated shipping title color!")

