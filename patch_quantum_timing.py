import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Buscamos el bloque y reemplazamos los 2.6 por 2.2
# targetProg > 2.6 && targetProg < 9.62
pattern = re.compile(
    r'(if\s*\(\s*targetProg\s*>\s*)2\.6(\s*&&\s*targetProg\s*<\s*9\.62\s*\)\s*\{\s*if\s*\(\s*prog\s*<=\s*)2\.6(\s*\)\s*\{\s*targetProg\s*=\s*9\.62;\s*prog\s*=\s*9\.62;\s*\}\s*else\s*\{\s*targetProg\s*=\s*)2\.6(;\s*prog\s*=\s*)2\.6(;\s*\}\s*\})'
)

if pattern.search(content):
    content_new = pattern.sub(r'\g<1>2.2\g<2>2.2\g<3>2.2\g<4>2.2\g<5>', content)
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content_new)
    print("Regex Replace OK")
else:
    print("Regex Target not found")
