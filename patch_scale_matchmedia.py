import re

files = ['3d-test.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Cambiar window.innerWidth por matchMedia
    content = content.replace(
        "window.innerWidth <= 768",
        "window.matchMedia('(max-width: 768px)').matches"
    )
    
    # Bajarlo a 0.52 en vez de 0.5525 (20% en vez de 15% para que se note si o si)
    content = content.replace(
        "0.5525",
        "0.52"
    )
    
    # CSS a 0.80
    content = content.replace(
        "transform: scale(0.85);",
        "transform: scale(0.80);"
    )
    
    content = content.replace(
        "? 0.85 : 1",
        "? 0.80 : 1"
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
