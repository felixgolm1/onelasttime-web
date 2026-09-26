import sys
import re

def apply_fixes():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the localP_raw math for 24.10
    content = content.replace(
        'localP_raw = p - 21.58; // Sincroniza el carrusel completo para que arranque exactamente en p=24.08',
        'localP_raw = p - 21.60; // Sincroniza el carrusel completo para que arranque exactamente en p=24.10'
    )

    # 2. Delete the override block using a robust regex
    pattern = r'\s*if\s*\(\s*window\.innerWidth\s*<=\s*768\s*\|\|\s*window\._cIsMobile\s*\)\s*\{\s*ec1_peek\s*=\s*mapRange\(localP,\s*2\.28,\s*2\.78,\s*0,\s*1\);\s*ec2_peek\s*=\s*mapRange\(localP,\s*4\.00,\s*4\.50,\s*0,\s*1\);\s*ec3_peek\s*=\s*mapRange\(localP,\s*5\.80,\s*6\.30,\s*0,\s*1\);\s*ec4_peek\s*=\s*mapRange\(localP,\s*7\.60,\s*8\.10,\s*0,\s*1\);\s*\}'
    
    content = re.sub(pattern, '', content)

    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)

apply_fixes()
