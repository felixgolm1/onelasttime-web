import os
from playwright.sync_api import sync_playwright

html = '''
<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  body {
    background: #222;
    color: #f4f2ea;
    font-family: 'Inter', sans-serif;
    font-size: 150px;
    font-weight: 700;
    letter-spacing: -0.05em;
    white-space: nowrap;
    padding: 200px;
  }
</style>
</head>
<body>
    <div id="made-by-ai">
      <span style="position: relative; display: inline-block;">
        <span style="position: absolute; right: 100%; top: 48%; transform: translateY(-50%) rotate(-90deg); margin-right: -0.08em; display: flex; justify-content: space-between; font-size: 0.18em; font-weight: 600; letter-spacing: 0; color: #f4f2ea; opacity: 0.9; width: 4.1em;">
          <span>u</span><span>l</span><span>t</span><span>r</span><span>a</span>
        </span>
        personalizado con 
      </span>
      <span style="color: #c1ff00; position: relative; display: inline-block;">
        IA
        <span style="position: absolute; left: 4%; top: 82%; display: flex; justify-content: space-between; font-size: 0.13em; font-weight: 700; letter-spacing: 0; width: 92%; white-space: nowrap; color: #c1ff00;">
          <span>M</span><span>o</span><span>d</span><span>e</span><span>l</span><span>o</span><span>&nbsp;</span><span>O</span><span>L</span><span>T</span><span>-</span><span>1</span>
        </span>
      </span>
    </div>
</body>
</html>
'''

with open('test_render_2.html', 'w', encoding='utf-8') as f:
    f.write(html)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('file://' + os.path.abspath('test_render_2.html'))
    page.screenshot(path='test_render_5.png')
    browser.close()
