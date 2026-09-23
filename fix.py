with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find the start of sc-board
start_match = re.search(r'<div class=.sc-board. id=.sc-board.>', text)
if not start_match:
    print('Start not found')
    exit()

end_idx = text.find('<!--  SCENE 3 : 3D CAROUSEL  -->')

if end_idx == -1:
    print('End not found')
    exit()

html_chunk = text[start_match.end():end_idx]
last_div_idx = html_chunk.rfind('</div>')

if last_div_idx == -1:
    print('Last div not found')
    exit()

new_chunk = '\n<div id="sc-pan-wrapper" style="width:0; height:0; position:absolute; top:0; left:0;">\n' + html_chunk[:last_div_idx] + '\n</div>\n' + html_chunk[last_div_idx:]

new_text = text[:start_match.end()] + new_chunk + text[end_idx:]

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print('Wrapper injected successfully!')
