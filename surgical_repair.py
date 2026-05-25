import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# The issue: lines 4922 (index 4921) to 4951 (index 4950) are corrupted magazine code
# They should be replaced with the correct box code AND then the magazine block added AFTER line 4952 (end of if transP block)

# Line 4922 should be: '           shiftX = -44.87 * boxScaleX;\n'
# Lines 4923-4951 should be DELETED (they are orphaned magazine animation code)
# Then lines 4952+ should continue normally

# Build fixed version
new_lines = (
    lines[:4921] +                           # lines 1 to 4921 (including shiftX correction)
    ['        } else if (transP > 0.85) {\n',
     '           boxScaleX = 4.414;\n',
     '           boxScaleY = 1.615;\n',
     '           shiftX = -44.87 * boxScaleX;\n',
     '        }\n',
     '        mainDeck.style.transform = 	ranslateX(px) scaleX() scaleY();\n',
     '        \n',
     '        // CROSS-FADE SUAVE\n',
     '        let boxOpacity = transP < 0.85 ? 1 : mapRange(transP, 0.85, 0.95, 1, 0);\n',
     '        let boxBlur = transP < 0.85 ? 0 : mapRange(transP, 0.85, 0.95, 0, 20);\n',
     '        mainDeck.style.opacity = boxOpacity.toString();\n',
     '        mainDeck.style.filter = lur(px);\n',
     '\n',
     '        // Anti-deformacion del texto\n',
     '        const faceLeftSpan = mainDeck.querySelector(".face-left span");\n',
     '        if (faceLeftSpan) {\n',
     '            let uniformScale = 1 + ((boxScaleY - 1) * 4);\n',
     '            faceLeftSpan.style.transform = otate(90deg) scaleX() scaleY();\n',
     '        }\n',
     '\n',
     '        if (heroCta) {\n',
     '          let ctaOp = mapRange(transP, 0.0, 0.20, 1, 0);\n',
     '          heroCta.style.opacity = ctaOp;\n',
     '          heroCta.style.pointerEvents = ctaOp > 0 ? "auto" : "none";\n',
     '        }\n',
     '\n',
     '        // CAMERA FLASH\n',
     '        const cameraFlash = document.getElementById("camera-flash");\n',
     '        if (cameraFlash) {\n',
     '           if (transP < 0.80) cameraFlash.style.opacity = "0";\n',
     '           else if (transP < 0.85) cameraFlash.style.opacity = mapRange(transP, 0.80, 0.85, 0, 1);\n',
     '           else if (transP < 0.95) cameraFlash.style.opacity = mapRange(transP, 0.85, 0.95, 1, 0);\n',
     '           else cameraFlash.style.opacity = "0";\n',
     '        }\n',
     '\n',
     '        // MAGAZINE EXPANSION ANIMATION\n',
     '        if (magazineScene) {\n',
     '           magazineScene.style.opacity = 1;\n',
     '           const uiFade = typeof prog !== "undefined" ? (prog < 15.0 ? 1 : Math.max(0, 1 - (prog - 15.0) / 1.5)) : 1;\n',
     '           const expandP = 1 - uiFade;\n',
     '           const easeP = expandP * expandP * (3 - 2 * expandP);\n',
     '           const baseW = window.innerWidth > 768 ? 466 : window.innerWidth * 0.9;\n',
     '           const baseH = window.innerWidth > 768 ? 626 : window.innerWidth * 1.3;\n',
     '\n',
     '           // Ocultar siempre las etiquetas del cerebro\n',
     '           ["b-label-1","b-label-2","b-label-3"].forEach(id => {\n',
     '               const el = document.getElementById(id);\n',
     '               if (el) el.style.opacity = "0";\n',
     '           });\n',
     '\n',
     '           // RISE letters fly up staggered\n',
     '           const riseLetters = magazineScene.querySelectorAll(".rise-l, .rise-dot");\n',
     '           riseLetters.forEach((el, index) => {\n',
     '               const delay = index * 0.15;\n',
     '               const letterP = Math.max(0, Math.min(1, (expandP - delay) / (1 - delay)));\n',
     '               const letterEase = letterP * letterP;\n',
     '               el.style.transform = 	ranslateY(-vh);\n',
     '               el.style.opacity = 1 - letterEase;\n',
     '           });\n',
     '\n',
     '           // Other UI elements fade out\n',
     '           magazineScene.querySelectorAll(".mag-ui").forEach(el => {\n',
     '               el.style.opacity = uiFade;\n',
     '           });\n',
     '\n',
     '           const magContent = magazineScene.querySelector(".magazine-content");\n',
     '           const overlay = document.getElementById("mag-breakout-overlay");\n',
     '\n',
     '           if (easeP > 0 && magContent && overlay) {\n',
     '               // Recuadro centrado en pantalla -> crece a pantalla completa\n',
     '               const startL = (window.innerWidth - baseW) / 2;\n',
     '               const startT = (window.innerHeight - baseH) / 2;\n',
     '               const currentW = baseW + (window.innerWidth - baseW) * easeP;\n',
     '               const currentH = baseH + (window.innerHeight - baseH) * easeP;\n',
     '               const currentL = startL * (1 - easeP);\n',
     '               const currentT = startT * (1 - easeP);\n',
     '               const bgSize = 250 - (170 * easeP);\n',
     '               const bgPos = 15 + (35 * easeP);\n',
     '\n',
     '               overlay.style.display = "block";\n',
     '               overlay.style.left = currentL + "px";\n',
     '               overlay.style.top = currentT + "px";\n',
     '               overlay.style.width = currentW + "px";\n',
     '               overlay.style.height = currentH + "px";\n',
     '               overlay.style.background = url("assets/img/modelo-sin-fondo.png") center % / % no-repeat;\n',
     '               overlay.style.backgroundColor = gba(6, 2, 15, );\n',
     '               overlay.style.border = (12 * uiFade) + "px solid rgba(249, 204, 16, " + uiFade + ")";\n',
     '               magContent.style.opacity = "0";\n',
     '\n',
     '               // Hide all other carousel items\n',
     '               document.querySelectorAll(".carousel-item").forEach(item => {\n',
     '                   item.style.opacity = uiFade;\n',
     '               });\n',
     '           } else {\n',
     '               if (overlay) overlay.style.display = "none";\n',
     '               if (magContent) magContent.style.opacity = "1";\n',
     '               document.querySelectorAll(".carousel-item").forEach(item => {\n',
     '                   item.style.opacity = "";\n',
     '               });\n',
     '           }\n',
     '        }\n',
     '\n',
    ] +
    lines[4951:]  # resume from line 4952 onwards (the carousel-track-small logic etc)
)

print(f'Old lines: {len(lines)}, New lines: {len(new_lines)}')
print('Lines 4920-4960 after repair:')
for i in range(4918, 4960):
    print(f'{i+1}: {new_lines[i][:100]}')

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print('Surgical repair done!')
