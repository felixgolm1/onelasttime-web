with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_bg = "url('assets/img/chica_sensibles.jpg') center/cover"
new_bg = "url('assets/img/modelo-sin-fondo.png') center/cover, #06020F"

if old_bg in text:
    text = text.replace(old_bg, new_bg)
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Sustituido con exito')
else:
    print('No se encontro el fondo antiguo')
