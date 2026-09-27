with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

target_fase1 = "isTrack.style.transform = (window.innerWidth <= 768) ? 'translateX(0px)' : 'translateX(0.5cm)';"
rep_fase1 = "isTrack.style.transform = 'translateX(0.5cm)';"

target_fase2 = "isTrack.style.transform = 'translateX(' + (-ssp * maxScroll) + 'px)';"
rep_fase2 = "isTrack.style.transform = 'translateX(calc(0.5cm - ' + (ssp * maxScroll) + 'px))';"

content = content.replace(target_fase1, rep_fase1)
content = content.replace(target_fase2, rep_fase2)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
