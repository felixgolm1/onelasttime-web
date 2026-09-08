import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the VIP shake CSS with the EXACT shakeAnim
search_css = ".vip-shake { animation: vipShakeAnim 0.5s cubic-bezier(0.36, 0.07, 0.19, 0.97) both; }\n    @keyframes vipShakeAnim { 0%, 100% { transform: translateX(0); } 15%, 45%, 75% { transform: translateX(-6px); } 30%, 60% { transform: translateX(6px); } }"
replace_css = ".vip-shake { animation: shakeAnim 0.4s ease-in-out; }\n    @keyframes shakeAnim { 0%, 100% { transform: translateX(0); } 20%, 60% { transform: translateX(-8px); } 40%, 80% { transform: translateX(8px); } }"

if search_css in content:
    content = content.replace(search_css, replace_css)
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed CSS in 3d-test.html")

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
if search_css in content:
    content = content.replace(search_css, replace_css)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed CSS in index.html")
