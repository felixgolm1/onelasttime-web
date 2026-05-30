import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(
    r'(scrollTl\.to\(scBoard,\s*\{\s*rotationY:\s*335,\s*rotationX:\s*0,\s*duration:\s*0\.35,\s*ease:\s*\')power2\.out(\'\s*\},)\s*tSwap\);'
)

if pattern.search(content):
    content_new = pattern.sub(r'\g<1>none\g<2> tSwap);', content)
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content_new)
    print("Regex Replace OK")
else:
    print("Regex Target not found")
