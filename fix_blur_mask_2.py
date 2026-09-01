import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target_style = """    <style>"""
replacement_style = """    <style>
        .top-blur-mask {
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
text = text.replace(target_style, replacement_style)

target_app = """                <BackgroundAnimation />
                <div className="relative z-10 min-h-screen flex flex-col items-center">"""
replacement_app = """                <BackgroundAnimation />
                <div className="top-blur-mask"></div>
                <div className="relative z-10 min-h-screen flex flex-col items-center">"""
text = text.replace(target_app, replacement_app)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Added blur mask!")

