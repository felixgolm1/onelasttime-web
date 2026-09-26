import sys

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    old_peek = """         let ec1_peek = mapRange(localP, 2.5, 3.0, 0, 1);
           let ec2_peek = mapRange(localP, 4.22, 4.72, 0, 1);
           let ec3_peek = mapRange(localP, 6.02, 6.52, 0, 1);
           let ec4_peek = mapRange(localP, 7.82, 8.32, 0, 1);"""
           
    new_peek = """         let ec1_peek = mapRange(localP, 2.5, 3.0, 0, 1);
           let ec2_peek = mapRange(localP, 4.22, 4.72, 0, 1);
           let ec3_peek = mapRange(localP, 6.02, 6.52, 0, 1);
           let ec4_peek = mapRange(localP, 7.82, 8.32, 0, 1);
           if (window.innerWidth <= 768 || window._cIsMobile) {
               ec1_peek = mapRange(localP, 2.28, 2.78, 0, 1); // empieza en 24.08 (24.08 - 21.8 = 2.28)
               ec2_peek = mapRange(localP, 4.00, 4.50, 0, 1);
               ec3_peek = mapRange(localP, 5.80, 6.30, 0, 1);
               ec4_peek = mapRange(localP, 7.60, 8.10, 0, 1);
           }"""

    content = content.replace(old_peek, new_peek)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
