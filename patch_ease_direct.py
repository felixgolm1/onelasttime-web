import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1
content = content.replace("ease: 'power1.in' }, t3);", "ease: 'none' }, t3);")
# 2
content = content.replace("ease: 'power2.out'\n      }, tSwap);", "ease: 'none'\n      }, tSwap);")
content = content.replace("ease: 'power2.out'\r\n      }, tSwap);", "ease: 'none'\r\n      }, tSwap);")
# 3
content = content.replace("ease: 'power2.out' },\n        tSwap", "ease: 'none' },\n        tSwap")
content = content.replace("ease: 'power2.out' },\r\n        tSwap", "ease: 'none' },\r\n        tSwap")

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Replace OK")
