import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Buscamos donde inicializa el script del VIP:
script_start = content.find('<script>\n// Mantener el efecto de luces siempre activo')
if script_start == -1:
    print("Could not find start of VIP script")
    exit(1)

# Añadimos la comprobación inicial
check_code = """
    if (sessionStorage.getItem('olt_vip_unlocked') === 'true') {
        var ov = document.getElementById('vip-overlay');
        if(ov) ov.style.display = 'none';
        document.body.style.overflow = 'auto';
    } else {
        document.body.style.overflow = 'hidden';
    }
"""

# Añadimos check_code al principio del script
content = content[:script_start + 8] + check_code + content[script_start + 8:]

# Buscamos donde oculta el overlay tras acertar
success_code = "overlay.style.transition = 'opacity 0.8s ease';"
success_idx = content.find(success_code)
if success_idx != -1:
    content = content[:success_idx] + "sessionStorage.setItem('olt_vip_unlocked', 'true');\n        document.body.style.overflow = 'auto';\n        " + content[success_idx:]
    print("Injected success logic")
else:
    print("Could not find success logic")
    exit(1)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("VIP persistence fixed")
