import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Add the css class
css_target = """            .fade-out {
                animation: fadeOut 0.5s ease-out forwards;
            }"""

css_replacement = """            .fade-out {
                animation: fadeOut 0.5s ease-out forwards;
            }
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

# Add the element to the App component
app_target = """                <BackgroundAnimation />
                <div className="relative z-10 min-h-screen flex flex-col items-center">"""

app_replacement = """                <BackgroundAnimation />
                <div className="top-blur-mask"></div>
                <div className="relative z-10 min-h-screen flex flex-col items-center">"""
text = text.replace(app_target, app_replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Added blur mask!")

