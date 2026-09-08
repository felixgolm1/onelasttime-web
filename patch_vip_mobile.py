import os
import re

css_to_inject = """
<!-- MOBILE OPTIMIZATIONS FOR VIP OVERLAY -->
<style>
@media screen and (max-width: 768px) {
  /* Logo breathing room */
  #vip-overlay .vip-anim-1 {
    width: 100%;
    padding: 0 24px;
    box-sizing: border-box;
    margin-bottom: 24px !important; 
  }
  #vip-overlay .vip-anim-1 img:first-child {
    max-width: 88% !important; 
  }
  
  /* Typography and rhythm */
  #vip-title {
    font-size: 20px !important;
    line-height: 1.4 !important;
    margin-bottom: 24px !important;
    min-height: auto !important;
    padding: 0 30px !important;
  }
  
  #vip-form-container {
    min-height: auto !important;
  }

  /* Input and Button identical sizing */
  #vip-overlay .vip-pill {
    width: 88vw !important;
    max-width: 320px !important;
    height: 56px !important;
    box-sizing: border-box !important;
    margin: 0 auto !important;
  }
  
  #vip-code {
    padding: 0 24px !important;
    margin-bottom: 12px !important;
  }
  
  /* Fix button internal alignment */
  #vip-submit-btn {
    padding: 0 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
  }
  #vip-submit-btn span {
    padding-right: 0 !important; 
    margin-right: 32px !important; 
    line-height: 1 !important;
  }
  #vip-submit-btn .cta-arrow-pill {
    top: 50% !important;
    transform: translateY(-50%) !important;
    right: 8px !important;
  }
  
  /* Error msg */
  #vip-error {
    margin-top: 16px !important;
  }

  /* Bottom Waitlist text */
  #vip-form-container > div:last-child {
    margin-top: 24px !important;
  }
  #vip-toggle-prefix, #vip-toggle-mode {
    font-size: 15px !important;
  }
}
</style>
"""

files = ['3d-test.html', 'index.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<!-- MOBILE OPTIMIZATIONS FOR VIP OVERLAY -->' in content:
        content = re.sub(r'<!-- MOBILE OPTIMIZATIONS FOR VIP OVERLAY -->.*?</style>', css_to_inject.strip(), content, flags=re.DOTALL)
    else:
        content = content.replace('</head>', css_to_inject + '\n</head>')
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Patched successfully.")
