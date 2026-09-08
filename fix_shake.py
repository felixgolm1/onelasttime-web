import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

search = """        var shakeKeys = [
            { transform: 'translateX(-8px)' },
            { transform: 'translateX(8px)' },
            { transform: 'translateX(-8px)' },
            { transform: 'translateX(8px)' },
            { transform: 'translateX(0)' }
        ];
        err.animate(shakeKeys, { duration: 400 });
        input.animate(shakeKeys, { duration: 400, composite: 'add' });"""

replacement = """        var shakeKeys = [
            { transform: 'translateX(0)', offset: 0 },
            { transform: 'translateX(-8px)', offset: 0.2 },
            { transform: 'translateX(8px)', offset: 0.4 },
            { transform: 'translateX(-8px)', offset: 0.6 },
            { transform: 'translateX(8px)', offset: 0.8 },
            { transform: 'translateX(0)', offset: 1.0 }
        ];
        var shakeOpts = { duration: 400, easing: 'ease-in-out' };
        err.animate(shakeKeys, shakeOpts);
        input.animate(shakeKeys, Object.assign({}, shakeOpts, { composite: 'add' }));"""

if search in content:
    content = content.replace(search, replacement)
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed 3d-test.html")
else:
    print("Could not find the target string in 3d-test.html")

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
if search in content:
    content = content.replace(search, replacement)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed index.html")
else:
    print("Could not find the target string in index.html")
