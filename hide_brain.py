with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Ocultar el UI del cerebro
text = text.replace("document.getElementById('brain-ui').style.opacity = 1;", "document.getElementById('brain-ui').style.opacity = 0;")
text = text.replace("if (brainCanvasEl) brainCanvasEl.style.opacity = brainOp;", "if (brainCanvasEl) brainCanvasEl.style.opacity = 0;")
text = text.replace("if (window.brainPivot) window.brainPivot.visible = true;", "if (window.brainPivot) window.brainPivot.visible = false;")
text = text.replace("brainCanvasEl.style.opacity = '1';", "brainCanvasEl.style.opacity = '0';")

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Brain hidden')
