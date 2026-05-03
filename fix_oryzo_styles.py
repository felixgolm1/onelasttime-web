import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update font-family for review-text-col
content = content.replace("font-family: 'Poppins', sans-serif;", "font-family: 'Inter', sans-serif;")

# 2. Update font-size for review-quote
old_quote_css = '''    .review-quote {
      font-size: clamp(1.5rem, 3vw, 2.5rem);
      font-weight: 600;
      line-height: 1.3;
      margin-bottom: 2rem;
      letter-spacing: -0.02em;
    }'''
new_quote_css = '''    .review-quote {
      font-size: clamp(1.1rem, 2vw, 1.6rem);
      font-weight: 700;
      line-height: 1.35;
      margin-bottom: 2rem;
      letter-spacing: -0.02em;
    }'''
content = content.replace(old_quote_css, new_quote_css)

# 3. Update review-img-col img CSS
old_img_css = '''    .review-img-col img {
      width: 100%;
      max-width: 400px;
      aspect-ratio: 4/3;
      object-fit: cover;
      border-radius: 20px;
    }'''
new_img_css = '''    .review-img-col img {
      width: 100%;
      max-width: 280px;
      aspect-ratio: 1/1;
      object-fit: cover;
      border-radius: 0px;
    }'''
content = content.replace(old_img_css, new_img_css)

# 4. Update the highlight color to orange (Oryzo style)
content = content.replace("color: #ccff00; /* Verde/Amarillo marca */", "color: #d35400; /* Naranja Oryzo */")

# 5. Update HTML text '5 ESTRELLAS' to '★★★★★ [ 5/5 ]'
content = content.replace('<div class="osr-stars-small">5 ESTRELLAS</div>', '<div class="osr-stars-small" style="font-family:\'Inter\', sans-serif;">★★★★★ <span style="opacity: 0.5; margin-left: 8px; font-weight: 400;">[ 5/5 ]</span></div>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated styling to match Oryzo perfectly.")
