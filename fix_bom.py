import codecs

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

with codecs.open('3d-test.html', 'w', 'utf-8') as f:
    f.write(content)
