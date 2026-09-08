import os
from playwright.sync_api import sync_playwright

html_template = '''
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
    padding: 100px;
  }
</style>
</head>
<body>
    <div id="made-by-ai">
      <span style="position: relative; display: inline-block;">
        <span style="position: absolute; right: 100%; top: 48%; transform: translateY(-50%) rotate(-90deg); margin-right: {margin}; display: flex; justify-content: space-between; font-size: 0.18em; font-weight: 600; letter-spacing: 0; color: #f4f2ea; opacity: 0.9; width: 4.1em;">
          <span>u</span><span>l</span><span>t</span><span>r</span><span>a</span>
        </span>
        personalizado con 
      </span>
    </div>
</body>
</html>
'''

margins = ["-1.5em", "-1.8em", "-2.1em", "-2.4em"]
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    for i, m in enumerate(margins):
        html = html_template.replace('{margin}', m)
        with open(f'test_gap_{i}.html', 'w', encoding='utf-8') as f:
            f.write(html)
        page.goto('file://' + os.path.abspath(f'test_gap_{i}.html'))
        page.screenshot(path=f'test_gap_{i}.png')
        
    browser.close()
