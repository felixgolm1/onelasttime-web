import base64
print("Convirtiendo tablewareset.glb (~21 MB)...")
with open("assets/models/tablewareset.glb", "rb") as f:
    data = f.read()
b64 = base64.b64encode(data).decode('utf-8')
with open("assets/models/tablewareset_base64.js", "w") as f:
    f.write('const TABLESET_B64 = "data:application/octet-stream;base64,' + b64 + '";')
print("Listo! Generado tablewareset_base64.js")
