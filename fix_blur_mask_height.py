import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """        .top-blur-mask {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 140px;
            z-index: 35;
            pointer-events: none;
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            mask-image: linear-gradient(to bottom, black 40%, transparent 100%);
            -webkit-mask-image: linear-gradient(to bottom, black 40%, transparent 100%);
        }"""

replacement = """        .top-blur-mask {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 180px;
            z-index: 35;
            pointer-events: none;
            background: linear-gradient(to bottom, rgba(0,0,0,0.95) 25%, rgba(0,0,0,0) 100%);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            mask-image: linear-gradient(to bottom, black 50%, transparent 100%);
            -webkit-mask-image: linear-gradient(to bottom, black 50%, transparent 100%);
        }"""
text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated blur mask!")

