import re

css_replacement = '''
        .btn { position: relative; display: inline-flex; align-items: center; justify-content: center; border-radius: 100px; text-decoration: none; cursor: pointer; font-family: 'Inter', sans-serif; font-weight: 700; overflow: hidden; white-space: nowrap; pointer-events: auto; -webkit-font-smoothing: antialiased; }
        .btn-full { width: 100%; }
        .btn-blue { background: rgba(204, 255, 0, 0.08); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); color: rgba(204, 255, 0, 0.95); border: 1px solid rgba(204, 255, 0, 0.6); box-shadow: inset 0 0 20px rgba(204, 255, 0, 0.25); letter-spacing: 0.1em; text-transform: uppercase; transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1); }
        .btn-blue:hover { background: rgba(204, 255, 0, 0.15); border-color: rgba(204, 255, 0, 1); box-shadow: inset 0 0 45px rgba(204, 255, 0, 0.6); }
        .cta-content-wrapper { position: relative; z-index: 2; display: flex; align-items: center; justify-content: center; gap: 12px; width: 100%; height: 100%; pointer-events: none; }
        .cta-text-span { text-shadow: 0 2px 4px rgba(0,0,0,0.5); }
        .cta-arrow-pill { border-radius: 100px; display: flex; align-items: center; justify-content: center; background: #ccff00; box-shadow: 0 2px 8px rgba(0,0,0,0.4); color: #111; transition: transform 0.25s ease-out; flex-shrink: 0; }
        .btn-blue:hover .cta-arrow-pill { transform: scale(1.15); }
'''

top_cta = '''<div style="width: 280px;">
        <a href="3d-test.html" class="btn btn-blue btn-full" style="padding: 0.8rem 0; font-size: 0.85rem; height: auto;">
            <div class="cta-content-wrapper">
                <span class="cta-text-span">VOLVER A ONE LAST TIME</span>
                <div class="cta-arrow-pill" style="width: 32px; height: 22px;">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="5" y1="12" x2="19" y2="12"></line>
                        <polyline points="12 5 19 12 12 19"></polyline>
                    </svg>
                </div>
            </div>
        </a>
    </div>'''

bottom_cta = '''<div style="display: flex; justify-content: center; margin-top: 80px; margin-bottom: 40px; width: 100%;">
        <a href="3d-test.html" class="btn btn-blue btn-full" style="padding: 1.8rem 0; font-size: 1.4rem; height: auto; width: 80vw; max-width: 600px;">
            <div class="cta-content-wrapper" style="gap: 20px;">
                <span class="cta-text-span">VOLVER A ONE LAST TIME</span>
                <div class="cta-arrow-pill" style="width: 64px; height: 40px;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="5" y1="12" x2="19" y2="12"></line>
                        <polyline points="12 5 19 12 12 19"></polyline>
                    </svg>
                </div>
            </div>
        </a>
    </div>'''

for file in ['terminos.html', 'privacidad.html']:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Replace CSS safely
    start_idx = text.find('.btn {')
    end_idx = text.find('</style>')
    if start_idx != -1 and end_idx != -1:
        text = text[:start_idx] + css_replacement + text[end_idx:]
    
    # Replace Top CTA
    text = re.sub(r'<a href="3d-test\.html" class="btn btn-blue".*?</svg>\s*</div>\s*</div>\s*</a>', top_cta, text, flags=re.DOTALL)
    
    # Replace Bottom CTA
    text = re.sub(r'<div style="display: flex; justify-content: center; margin-top: 80px; margin-bottom: 40px;.*?>.*?</svg>\s*</div>\s*</div>\s*</a>\s*</div>', bottom_cta, text, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(text)
