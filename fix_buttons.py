import re

for file in ['terminos.html', 'privacidad.html']:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Fix the CSS media query
    text = text.replace('.cta-text-span { padding-right: 20px !important; transform: translateX(-18px) !important; }', 
                        '@media (max-width: 768px) { .cta-text-span { padding-right: 20px !important; transform: translateX(-18px) !important; } }')
    
    # Fix top CTA HTML
    new_top_cta = '''<a href="3d-test.html" class="btn btn-blue" style="padding: 0.8rem 1.6rem; font-size: 0.85rem; height: auto;">
            <span class="cta-text-span" style="position:relative; z-index:2; text-align:center; display: inline-block; padding-right: 44px;">VOLVER A ONE LAST TIME</span>
            <div class="cta-arrow-pill" style="right: 6px; width: 38px; height: 24px;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="5" y1="12" x2="19" y2="12"></line>
                    <polyline points="12 5 19 12 12 19"></polyline>
                </svg>
            </div>
        </a>'''
    text = re.sub(r'<a href="3d-test\.html" class="btn btn-blue".*?</svg>\s*</div>\s*</div>\s*</a>', new_top_cta, text, flags=re.DOTALL)
    
    # Fix bottom CTA HTML
    new_bottom_cta = '''<div style="display: flex; justify-content: center; margin-top: 80px; margin-bottom: 40px; width: 100%;">
        <a href="3d-test.html" class="btn btn-blue btn-full" style="position:relative; z-index:99999; margin-top:0; text-decoration:none; padding: 1.8rem 0 !important; height: auto; width:70vw; max-width:900px; box-sizing:border-box; font-size: 1.875rem !important;">
            <span class="cta-text-span" style="position:relative; z-index:2; text-align:center; display: inline-block; padding-right: 94px;">VOLVER A ONE LAST TIME</span>
            <div class="cta-arrow-pill" style="right: 14px; width: 80px; height: 48px;">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="5" y1="12" x2="19" y2="12"></line>
                    <polyline points="12 5 19 12 12 19"></polyline>
                </svg>
            </div>
        </a>
    </div>'''
    text = re.sub(r'<div style="display: flex; justify-content: center; margin-top: 80px; margin-bottom: 40px;.*?>.*?</svg>\s*</div>\s*</div>\s*</a>\s*</div>', new_bottom_cta, text, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(text)
