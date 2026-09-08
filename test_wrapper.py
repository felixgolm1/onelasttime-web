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
        <span style="position: absolute; right: 100%; top: 41%; width: 0; height: 0;">
          <span style="position: absolute; right: 0.24em; top: 50%; transform: translateY(-50%) rotate(-90deg); display: flex; justify-content: space-between; font-size: 0.22em; font-weight: 600; letter-spacing: 0; color: #f4f2ea; opacity: 0.9; width: 3.35em; transform-origin: center right;">
            <span>u</span><span>l</span><span>t</span><span>r</span><span>a</span>
          </span>
        </span>
        personalizado con 
      </span>
    </div>
</body>
</html>
'''

with open('test_wrapper.html', 'w', encoding='utf-8') as f:
    f.write(html)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('file://' + os.path.abspath('test_wrapper.html'))
    page.screenshot(path='test_wrapper_bigger2.png')
    browser.close()
