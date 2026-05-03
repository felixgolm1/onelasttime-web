import sys
from bs4 import BeautifulSoup

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

from html.parser import HTMLParser

class FindReview(HTMLParser):
    def __init__(self):
        super().__init__()
        self.found = False
        self.html = ""
        self.depth = 0

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if attrs_dict.get('id') == 'oryzo-review':
            self.found = True
        if self.found:
            self.html += f"<{tag}"
            for k, v in attrs:
                self.html += f" {k}='{v}'"
            self.html += ">"
            if tag not in ['meta', 'link', 'img', 'br', 'hr', 'input', 'source']:
                self.depth += 1

    def handle_endtag(self, tag):
        if self.found:
            if tag not in ['meta', 'link', 'img', 'br', 'hr', 'input', 'source']:
                self.depth -= 1
            self.html += f"</{tag}>"
            if self.depth == 0:
                self.found = False

    def handle_data(self, data):
        if self.found:
            self.html += data

parser = FindReview()
parser.feed(content)
print(parser.html)
