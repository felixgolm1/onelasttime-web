import sys

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Set the brainRenderer clear color to deep indigo (Oryzo background)
old_renderer = """    window.brainRenderer = new THREE.WebGLRenderer({ canvas: window.brainCanvasEl, antialias: true, alpha: true });
    window.brainRenderer.setPixelRatio(window.devicePixelRatio);
    window.brainRenderer.setSize(window.innerWidth, window.innerHeight);"""

new_renderer = """    window.brainRenderer = new THREE.WebGLRenderer({ canvas: window.brainCanvasEl, antialias: true, alpha: false });
    window.brainRenderer.setPixelRatio(window.devicePixelRatio);
    window.brainRenderer.setSize(window.innerWidth, window.innerHeight);
    window.brainRenderer.setClearColor(0x04010E, 1.0); // Deep indigo - Oryzo cold background"""

if old_renderer in text:
    text = text.replace(old_renderer, new_renderer)
    print("Renderer clear color set to deep indigo.")
else:
    # Try to find the renderer init and patch it
    import re
    # Find setClearColor if already there, update it
    if 'setClearColor' in text and 'brainRenderer' in text:
        text = re.sub(
            r'window\.brainRenderer\.setClearColor\(.*?\);',
            'window.brainRenderer.setClearColor(0x04010E, 1.0); // Deep indigo',
            text
        )
        print("Updated existing setClearColor.")
    else:
        # Add it after setSize
        text = text.replace(
            'window.brainRenderer.setSize(window.innerWidth, window.innerHeight);',
            'window.brainRenderer.setSize(window.innerWidth, window.innerHeight);\n    window.brainRenderer.setClearColor(0x04010E, 1.0); // Deep indigo - Oryzo cold'
        )
        print("Injected setClearColor after setSize.")

# 2. Also set CSS background on the canvas element itself as fallback
old_canvas_style = "transition:opacity 0.8s ease;"
new_canvas_style = "transition:opacity 0.8s ease; background-color: #04010E;"

text = text.replace(old_canvas_style, new_canvas_style, 1)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Done: Background set to deep indigo.")
