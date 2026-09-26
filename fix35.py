import sys
import re

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Modify localP definition to delay the entire carousel
    old_localP = "         let localP_raw = p - 21.1;\n         let localP = localP_raw;"
    new_localP = """         let localP_raw = p - 21.1;
         if (window.innerWidth <= 768 || window._cIsMobile) {
             localP_raw = p - 21.58; // Sincroniza el carrusel completo para que arranque exactamente en p=24.08
         }
         let localP = localP_raw;"""
    content = content.replace(old_localP, new_localP)

    # 2. Remove the previous ec1_peek overrides since localP delay handles everything natively
    old_peek_block = """           let ec1_peek = mapRange(localP, 2.5, 3.0, 0, 1);
           let ec2_peek = mapRange(localP, 4.22, 4.72, 0, 1);
           let ec3_peek = mapRange(localP, 6.02, 6.52, 0, 1);
           let ec4_peek = mapRange(localP, 7.82, 8.32, 0, 1);
           if (window.innerWidth <= 768 || window._cIsMobile) {
               ec1_peek = mapRange(localP, 2.28, 2.78, 0, 1);
               ec2_peek = mapRange(localP, 4.00, 4.50, 0, 1);
               ec3_peek = mapRange(localP, 5.80, 6.30, 0, 1);
               ec4_peek = mapRange(localP, 7.60, 8.10, 0, 1);
           }"""
    new_peek_block = """           let ec1_peek = mapRange(localP, 2.5, 3.0, 0, 1);
           let ec2_peek = mapRange(localP, 4.22, 4.72, 0, 1);
           let ec3_peek = mapRange(localP, 6.02, 6.52, 0, 1);
           let ec4_peek = mapRange(localP, 7.82, 8.32, 0, 1);"""
    
    # regex since spacing might differ
    content = re.sub(
        r'let ec1_peek = mapRange\(localP, 2\.5, 3\.0, 0, 1\);.*if \(window\.innerWidth <= 768 \|\| window\._cIsMobile\) \{[^}]+}',
        new_peek_block,
        content,
        flags=re.DOTALL
    )

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
