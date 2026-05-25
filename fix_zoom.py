with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Buscamos la etiqueta actual de fondo
old_bg = "url('assets/img/modelo-sin-fondo.png') center/cover, #06020F"
# La cambiamos por un tamao ms grande y posicin ajustada. 
# Probemos con 150% de tamao y centrada hacia arriba (center 10%).
new_bg = "url('assets/img/modelo-sin-fondo.png') center 10% / 180% no-repeat, #06020F"

if old_bg in text:
    text = text.replace(old_bg, new_bg)
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Zoom ajustado a 180%")
else:
    # Quizas ya la cambie antes, busquemos usando regex
    import re
    match = re.search(r"url\('assets/img/modelo-sin-fondo\.png'\)[^;]+", text)
    if match:
        text = text.replace(match.group(0), "url('assets/img/modelo-sin-fondo.png') center 20% / 180% no-repeat, #06020F")
        with open('3d-test.html', 'w', encoding='utf-8') as f:
            f.write(text)
        print("Zoom ajustado con regex a 180%")
    else:
        print("No se encontr el fondo de la chica.")
