with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match2 = re.search(r"url\('assets/img/modelo-sin-fondo\.png'\)[^;]+", text)
if match2:
    text = text.replace(match2.group(0), "url('assets/img/modelo-sin-fondo.png') center 15% / 250% no-repeat, #06020F")
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Zoom ajustado a 250%")
