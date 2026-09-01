import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """<div className={`flex-1 flex flex-col w-full transition-opacity ease-in-out ${transitionState.bgOpacity === 1 ? 'opacity-0 duration-500' : 'opacity-100 duration-1000'}`} style={phase !== 'intro' ? { WebkitMaskImage: 'linear-gradient(to bottom, transparent 0px, transparent 86px, black 112px, black 100%)', maskImage: 'linear-gradient(to bottom, transparent 0px, transparent 86px, black 112px, black 100%)' } : {}}>"""
replacement = """<div className={`flex-1 flex flex-col w-full transition-opacity ease-in-out ${transitionState.bgOpacity === 1 ? 'opacity-0 duration-500' : 'opacity-100 duration-1000'}`}>"""
text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Removed old inline mask!")

