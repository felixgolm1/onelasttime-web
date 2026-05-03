import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update card-table z-index
old_card_table = '#card-table { position: fixed; inset: 0; z-index: 20000; pointer-events: none; perspective: 1200px; transform-style: preserve-3d; }'
new_card_table = '#card-table { position: fixed; inset: 0; z-index: 10005; pointer-events: none; perspective: 1200px; transform-style: preserve-3d; }'
content = content.replace(old_card_table, new_card_table)

# Also update the comment warning about card-table
content = content.replace('cardTable (position:fixed inset:0 z-index:20000) NUNCA debe', 'cardTable (position:fixed inset:0 z-index:10005) NUNCA debe')

# 2. Update oryzo-reviews-container z-index
old_reviews = 'z-index: 10005; /* Encima del 3D (10004) pero debajo del menu (10010) */'
new_reviews = 'z-index: 10006; /* Encima de las cartas (10005) y 3D (10004), pero debajo del menu (10010) y CTAs (10008) */'
content = content.replace(old_reviews, new_reviews)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated Z-indexes correctly!")
