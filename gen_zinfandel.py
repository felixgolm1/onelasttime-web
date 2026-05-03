import base64
with open('assets/models/sm_zinfandel_glass.glb', 'rb') as f:
    data = f.read()
b64 = base64.b64encode(data).decode('utf-8')
with open('assets/models/sm_zinfandel_glass_base64.js', 'w') as f:
    f.write('const WINEGLASS_B64 = "data:application/octet-stream;base64,' + b64 + '";')
print('Listo!')
