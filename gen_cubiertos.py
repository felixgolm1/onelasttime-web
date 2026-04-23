import base64
print("Convirtiendo cubiertos...")
with open("assets/models/cutlery_set.glb", "rb") as f:
    data = f.read()
b64 = base64.b64encode(data).decode('utf-8')
with open("assets/models/cubiertos_base64.js", "w") as f:
    f.write('const CUBIERTOS_B64 = "data:application/octet-stream;base64,' + b64 + '";')
print("Listo! Actualizado cubiertos_base64.js")
