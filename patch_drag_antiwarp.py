import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_code = """          // Actualizar targetProg para que el loop lo alcance suavemente
          let scrollPercent = newY / maxMove;
          targetProg = scrollPercent * maxProg;"""

new_code = """          // Actualizar targetProg para que el loop lo alcance suavemente
          let scrollPercent = newY / maxMove;
          let fakeMax = maxProg - 7.42;
          let fakeProg = scrollPercent * fakeMax;
          targetProg = fakeProg > 2.2 ? fakeProg + 7.42 : fakeProg;"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Reemplazo exitoso.")
else:
    print("No se encontró el texto a reemplazar.")
