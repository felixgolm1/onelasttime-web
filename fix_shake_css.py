import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add CSS rules
css_target = ".vip-anim-2 { animation: vipLoad 1.8s cubic-bezier(0.16, 1, 0.3, 1) forwards; opacity: 0; animation-delay: 0.7s; }"
css_replacement = css_target + "\n    .vip-shake { animation: vipShakeAnim 0.5s cubic-bezier(0.36, 0.07, 0.19, 0.97) both; }\n    @keyframes vipShakeAnim { 0%, 100% { transform: translateX(0); } 15%, 45%, 75% { transform: translateX(-6px); } 30%, 60% { transform: translateX(6px); } }"

if css_target in content:
    content = content.replace(css_target, css_replacement)
    print("Added CSS to 3d-test.html")

# Replace JS
js_search = """        var shakeKeys = [
            { transform: 'translateX(0)', offset: 0 },
            { transform: 'translateX(-8px)', offset: 0.2 },
            { transform: 'translateX(8px)', offset: 0.4 },
            { transform: 'translateX(-8px)', offset: 0.6 },
            { transform: 'translateX(8px)', offset: 0.8 },
            { transform: 'translateX(0)', offset: 1.0 }
        ];
        var shakeOpts = { duration: 400, easing: 'ease-in-out' };
        err.animate(shakeKeys, shakeOpts);
        input.animate(shakeKeys, Object.assign({}, shakeOpts, { composite: 'add' }));"""

js_replacement = """        err.classList.remove('vip-shake');
        input.classList.remove('vip-shake');
        void err.offsetWidth; // trigger reflow
        err.classList.add('vip-shake');
        input.classList.add('vip-shake');"""

if js_search in content:
    content = content.replace(js_search, js_replacement)
    print("Replaced JS in 3d-test.html")

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

if css_target in content:
    content = content.replace(css_target, css_replacement)
    print("Added CSS to index.html")
if js_search in content:
    content = content.replace(js_search, js_replacement)
    print("Replaced JS in index.html")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
