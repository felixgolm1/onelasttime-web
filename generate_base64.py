import base64
print("Iniciando conversión a JS...")
with open("assets/models/forkspoonknifedish.glb", "rb") as f:
    data = f.read()
b64 = base64.b64encode(data).decode('utf-8')
with open("assets/models/glb_base64.js", "w") as f:
    f.write(f'const GLB_MODEL_B64 = "data:application/octet-stream;base64,{b64}";')
print("Convertido con éxito!")
