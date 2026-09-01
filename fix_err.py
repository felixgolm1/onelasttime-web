import codecs
content = codecs.open('3d-test.html', 'r', 'utf-8').read()

start = content.find("window.addEventListener('error', function(e) {")
if start != -1:
    end = content.find("});", start) + 3
    content = content[:start] + content[end:]
    with codecs.open('3d-test.html', 'w', 'utf-8') as f:
        f.write(content)
    print("Fixed")
else:
    print("Not found")
