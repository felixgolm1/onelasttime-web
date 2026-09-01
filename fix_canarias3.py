import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                if (str.includes("canarias") || str.includes("las palmas") || str.includes("tenerife") || str.includes("fuerteventura") || str.includes("lanzarote") || str.includes("la palma") || str.includes("la gomera") || str.includes("el hierro") || str.match(/\b(35|38)\d{3}\b/)) {"""
replacement = """                if (str.includes("canarias") || str.includes("las palmas") || str.includes("tenerife") || str.includes("fuerteventura") || str.includes("lanzarote") || str.includes("la palma") || str.includes("la gomera") || str.includes("el hierro") || str.includes("puertito de los molinos") || str.match(/\\b(35|38)\\d{3}\\b/)) {"""
text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated isCanarias logic to include puertito de los molinos")
