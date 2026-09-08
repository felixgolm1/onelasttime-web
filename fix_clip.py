import codecs

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

old_code = '''                let inner = document.createElement('div');
                inner.className = 'glass-mask-line';'''

new_code = '''                let inner = document.createElement('div');
                inner.className = 'glass-mask-line';
                inner.style.paddingRight = '5px'; // Evitar que overflow:hidden corte las cursivas que se inclinan hacia la derecha'''

content = content.replace(old_code, new_code)

with codecs.open('3d-test.html', 'w', 'utf-8') as f:
    f.write(content)
