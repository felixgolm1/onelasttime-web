import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Add CSS
css_target = """        .font-poppins { font-family: Poppins, sans-serif; }"""
css_replacement = """        .font-poppins { font-family: Poppins, sans-serif; }
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
text = text.replace(css_target, css_replacement)

# Add to App return
app_target = """                <div className="w-full relative min-h-screen flex flex-col">
                    {transitionState.active && ("""
app_replacement = """                <div className="w-full relative min-h-screen flex flex-col">
                    <div className="top-blur-mask"></div>
                    {transitionState.active && ("""
text = text.replace(app_target, app_replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Added blur mask!")

