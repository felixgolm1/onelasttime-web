import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove yellow border + white inset from magazine-content
content = content.replace(
    'border: 12px solid #f9cc10; justify-content: flex-start; padding: 10px; position: relative; box-shadow: inset 0 0 0 2px #fff;',
    'border: none; justify-content: flex-start; padding: 10px; position: relative;',
    1
)

# 2. Update the breakout overlay - also no border initially
content = content.replace(
    'border:12px solid #f9cc10;box-shadow:inset 0 0 0 2px #fff;',
    'border:none;',
    1
)

# 3. In the JS - the borderW calculation is now irrelevant but harmless; 
#    let's also zero it out for cleanliness by making borderW always 0
# (optional, the overlay border was already being set to 0 as it expands)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done. Yellow border removed.')
