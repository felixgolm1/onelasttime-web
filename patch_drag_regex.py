import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'let scrollPercent = newY / maxMove;\s*targetProg = scrollPercent \* maxProg;')

replacement = """let scrollPercent = newY / maxMove;
          let fakeMax = maxProg - 7.42;
          let fakeProg = scrollPercent * fakeMax;
          targetProg = fakeProg > 2.2 ? fakeProg + 7.42 : fakeProg;"""

if pattern.search(content):
    content = pattern.sub(replacement, content)
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Reemplazo regex exitoso.")
else:
    print("NO SE ENCONTRO EL PATRON CON REGEX")
