import re
with open(r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

css = '''
    .oryzo-review-panel {
      position: absolute;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      display: flex;
      flex-direction: column;
      padding: 0 4vw;
      box-sizing: border-box;
      font-family: 'Inter', sans-serif;
      pointer-events: none;
      z-index: 5;
    }

    .osr-top-line {
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 100%;
      border-top: 1px dashed rgba(255,255,255,0.2);
      padding: 1.5rem 0;
      font-size: 0.75rem;
      font-weight: 600;
      letter-spacing: 0.05em;
      color: rgba(255,255,255,0.8);
      margin-top: auto; 
      margin-bottom: 3rem;
    }

    .osr-top-center .osr-stars { margin-left: 1rem; color: #ffffff; }

    .osr-body {
      display: flex;
      width: 100%;
      gap: 5vw;
      align-items: center;
      margin-bottom: auto; 
    }

    .review-text-col {
      flex: 1.2;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      color: #fff;
    }

    .review-img-col {
      flex: 1;
      display: flex;
      justify-content: flex-end;
    }

    .osr-stars-small {
      font-size: 0.8rem;
      color: rgba(255,255,255,0.6);
      margin-bottom: 1.5rem;
      letter-spacing: 0.1em;
    }

    .review-quote {
      position: relative;
      font-family: 'Inter', sans-serif;
      font-size: clamp(1.8rem, 2.5vw, 3rem);
      font-weight: 500;
      line-height: 1.2;
      margin-bottom: 3rem;
      letter-spacing: -0.02em;
    }

    .review-quote-bg {
      color: rgba(255,255,255,0.15); 
    }

    .review-quote-fg {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      color: #ffffff; 
      clip-path: inset(0% 0% 0% 100%); 
    }

    .review-highlight {
      color: #cc4400; 
    }

    .review-author {
      font-size: 0.75rem;
      font-weight: 600;
      color: rgba(255,255,255,0.5);
      letter-spacing: 0.05em;
    }

    .review-img-col img {
      width: 100%;
      max-width: 500px;
      aspect-ratio: 16/10;
      object-fit: cover;
      transform: scale(1.0);
      filter: brightness(0.3); 
      border-radius: 4px;
    }
'''

# Replace old CSS rules
text = re.sub(r'\.oryzo-review-panel\s*{.*?\.review-img-col img\s*{.*?}', css, text, flags=re.DOTALL)
# Wait, the regex might fail if the old CSS doesn't end with .review-img-col img.
# Let's be safe and just replace the whole style block from .oryzo-review-panel { to the next unrelated selector.
