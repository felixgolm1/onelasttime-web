import xml.etree.ElementTree as ET
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.target_path = None

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        self.stack.append((tag, attrs_dict.get('id', '')))
        if attrs_dict.get('id') == 'made-by-ai':
            self.target_path = list(self.stack)

    def handle_endtag(self, tag):
        if self.stack:
            self.stack.pop()

parser = MyHTMLParser()
with open(r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html', 'r', encoding='utf-8') as f:
    parser.feed(f.read())

print("Path to #made-by-ai:")
for tag, id_val in parser.target_path:
    print(f"<{tag} id='{id_val}'>")
