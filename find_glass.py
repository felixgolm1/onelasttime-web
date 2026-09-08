file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 2. Patch wine glass calls
idx = content.find('placeWineGlass(gltf, -3.0, +2.4)')
if idx > -1:
    print("Found wine glass at:", idx)
    print(repr(content[idx-80:idx+120]))
else:
    print("Not found, searching alternatives...")
    idx2 = content.find('placeWineGlass')
    print(repr(content[idx2:idx2+250]))
