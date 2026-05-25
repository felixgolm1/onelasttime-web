with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_bg = "url('assets/img/modelo-sin-fondo.png') center 15% / 250% no-repeat, #06020F"
new_bg = "url('assets/img/modelo-sin-fondo.png') center 15% / 250% no-repeat; background-color: #06020F"

if old_bg in text:
    text = text.replace(old_bg, new_bg)
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Split bg ok')
else:
    print('Not found')
