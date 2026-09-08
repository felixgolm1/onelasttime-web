import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

search1 = "btn.innerHTML = 'APUNTARME';"
replace1 = "btn.innerHTML = '<span style=\"position:relative; z-index:2; text-align:center; padding-right:40px;\">APUNTARME</span><div class=\"cta-arrow-pill\" style=\"right: 12px; width: 50px; height: 32px;\"><svg width=\"18\" height=\"18\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.5\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><line x1=\"5\" y1=\"12\" x2=\"19\" y2=\"12\"></line><polyline points=\"12 5 19 12 12 19\"></polyline></svg></div>';"

search2 = "btn.innerHTML = 'Entrar';"
replace2 = "btn.innerHTML = '<span style=\"position:relative; z-index:2; text-align:center; padding-right:40px;\">ENTRAR</span><div class=\"cta-arrow-pill\" style=\"right: 12px; width: 50px; height: 32px;\"><svg width=\"18\" height=\"18\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.5\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><line x1=\"5\" y1=\"12\" x2=\"19\" y2=\"12\"></line><polyline points=\"12 5 19 12 12 19\"></polyline></svg></div>';"

content = content.replace(search1, replace1)
content = content.replace(search2, replace2)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Done")
