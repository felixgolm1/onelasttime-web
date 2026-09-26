import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the current .osr-body grid rule
pattern_grid = r'\.osr-body \{\s*display: grid !important;\s*grid-template-columns: 75px 1fr !important;\s*grid-template-rows: auto auto 75px auto !important;\s*grid-template-areas:\s*\"topline topline\"\s*\"stars stars\"\s*\"image quote\"\s*\"author quote\" !important;\s*gap: 0 1rem !important;\s*align-items: start !important;\s*\}'

replacement_grid = '''.oryzo-review-panel .osr-body {
            display: grid !important;
            grid-template-columns: 75px 1fr !important;
            grid-template-rows: auto auto 75px auto !important;
            grid-template-areas:
              "topline topline"
              "stars stars"
              "image quote"
              "author quote" !important;
            gap: 0 1rem !important;
            align-items: start !important;
            background: rgba(255, 255, 255, 0.04) !important;
            backdrop-filter: blur(24px) !important;
            -webkit-backdrop-filter: blur(24px) !important;
            border: 1px solid rgba(255, 255, 255, 0.15) !important;
            border-radius: 12px !important;
            padding: 24px 20px !important;
            width: 90vw !important;
            margin: 0 auto !important;
            height: auto !important;
          }'''

if re.search(pattern_grid, content):
    content = re.sub(pattern_grid, replacement_grid, content)
    print("Replaced grid rule")
else:
    print("Grid rule not found")

# Remove the conflicting #end-reviews-container .osr-body
pattern_conflict = r'#end-reviews-container \.osr-body \{\s*gap: 2\.5rem !important;\s*flex-direction: column !important;\s*\}'
if re.search(pattern_conflict, content):
    content = re.sub(pattern_conflict, '', content)
    print("Removed conflicting rule")
else:
    print("Conflicting rule not found")

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
