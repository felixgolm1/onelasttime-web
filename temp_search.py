import re
with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()
match = re.search(r'(<div[^>]+id="magazine-scene".*?)<script', text, re.DOTALL)
if match:
    print(match.group(1)[1500:3500])
else:
    print("Not found")
