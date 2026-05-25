import sys
with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fallback for placeIdCard just in case
if 'window.placeIdCard = function' not in text:
    text = text.replace('function placeIdCard(gltf)', 'window.placeIdCard = function(gltf) { placeIdCardImpl(gltf); }; function placeIdCardImpl(gltf)')

# 2. Make sure brainCanvasEl has a visible background when opacity=1 so we can debug
text = text.replace('z-index:10008;pointer-events:none;opacity:0;transition:opacity 0.8s ease;', 
                    'z-index:10008;pointer-events:none;opacity:0;transition:opacity 0.8s ease;') # I'll just leave it transparent

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)
