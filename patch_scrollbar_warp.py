import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Actualización visual de la barra (prog -> UI)
old_visual = """        if (scrollThumb && !window.isDraggingThumb) {
          const scrollPercent = Math.max(0, Math.min(1, prog / maxProg));
          // Asumimos un track de 100vh y thumb de 29vh, nos queda 71vh de recorrido libre
          scrollThumb.style.transform = `translateY(${scrollPercent * 71}vh)`;
        }"""
new_visual = """        if (scrollThumb && !window.isDraggingThumb) {
          let fakeProg = prog;
          if (prog >= 9.62) fakeProg = prog - 7.42;
          let fakeMax = maxProg - 7.42;
          const scrollPercent = Math.max(0, Math.min(1, fakeProg / fakeMax));
          // Asumimos un track de 100vh y thumb de 29vh, nos queda 71vh de recorrido libre
          scrollThumb.style.transform = `translateY(${scrollPercent * 71}vh)`;
        }"""
content = content.replace(old_visual, new_visual)

# 2. Arrastre de la barra (UI -> targetProg)
old_drag = """          // Actualizar targetProg para que el loop lo alcance suavemente
          let scrollPercent = newY / maxMove;
          targetProg = scrollPercent * maxProg;"""
new_drag = """          // Actualizar targetProg para que el loop lo alcance suavemente
          let scrollPercent = newY / maxMove;
          let fakeMax = maxProg - 7.42;
          let fakeProg = scrollPercent * fakeMax;
          targetProg = fakeProg > 2.2 ? fakeProg + 7.42 : fakeProg;"""
content = content.replace(old_drag, new_drag)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch anti-warp aplicado.")
