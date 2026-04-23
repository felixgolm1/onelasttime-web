import base64
print("Convirtiendo plato...")
with open("assets/models/unhyun__white_porcelain_dish_a.glb", "rb") as f:
    data = f.read()
b64 = base64.b64encode(data).decode('utf-8')
with open("assets/models/plato_base64.js", "w") as f:
    f.write('const PLATO_B64 = "data:application/octet-stream;base64,' + b64 + '";')
print("Listo! Generado plato_base64.js")
