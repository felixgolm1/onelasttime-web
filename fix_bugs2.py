import os

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Add crossfade for mainDeck
old_transform = "mainDeck.style.transform = `translateX(${shiftX}px) scaleX(${boxScaleX}) scaleY(${boxScaleY})`;"
new_transform = """mainDeck.style.transform = `translateX(${shiftX}px) scaleX(${boxScaleX}) scaleY(${boxScaleY})`;
        
        // CROSS-FADE SUAVE: Evita el corte brusco fundiendo la caja con la revista de forma progresiva
        let boxOpacity = transP < 0.85 ? 1 : mapRange(transP, 0.85, 0.95, 1, 0);
        let boxBlur = transP < 0.85 ? 0 : mapRange(transP, 0.85, 0.95, 0, 20);
        mainDeck.style.opacity = boxOpacity.toString();
        mainDeck.style.filter = `blur(${boxBlur}px)`;"""

content = content.replace(old_transform, new_transform)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
