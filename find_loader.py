import xml.etree.ElementTree as ET
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.loader_end_line = -1

    def handle_starttag(self, tag, attrs):
        if tag in ['meta', 'link', 'img', 'br', 'hr', 'input']:
            return
        attrs_dict = dict(attrs)
        self.stack.append((tag, attrs_dict.get('id', '')))

    def handle_endtag(self, tag):
        if tag in ['meta', 'link', 'img', 'br', 'hr', 'input']:
            return
        if self.stack:
            popped_tag, popped_id = self.stack.pop()
            if popped_id == 'loader':
                self.loader_end_line = self.getpos()[0]

parser = MyHTMLParser()
with open(r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html', 'r', encoding='utf-8') as f:
    parser.feed(f.read())

print(f"loader ends at line: {parser.loader_end_line}")
