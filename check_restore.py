import os

prod_path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web-produccion\3d-test.html"
dev_path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"

with open(prod_path, "r", encoding="utf-8") as f:
    prod_lines = f.readlines()

with open(dev_path, "r", encoding="utf-8") as f:
    dev_lines = f.readlines()

print("Prod lines length:", len(prod_lines))
print("Dev lines length:", len(dev_lines))
