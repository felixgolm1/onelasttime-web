import codecs

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

old_style = "position: fixed; top: 50%; left: 6vw; transform: translateY(-50%); width: 25vw; background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 35px 30px; opacity: 0; pointer-events: none; z-index: 10005; visibility: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.2);"

new_style = "position: fixed; top: 50%; left: 0; transform: translateY(-50%); width: 28vw; background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.1); border-left: none; border-radius: 0 24px 24px 0; padding: 35px 30px 35px 5vw; opacity: 0; pointer-events: none; z-index: 10005; visibility: hidden; box-shadow: 5px 10px 30px rgba(0,0,0,0.15);"

content = content.replace(old_style, new_style)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
