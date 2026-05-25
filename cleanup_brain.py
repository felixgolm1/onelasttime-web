with open('3d-test.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

total = len(lines)
print(f'Total lines before cleanup: {total}')

# All ranges to DELETE (0-indexed, inclusive)
# Working BOTTOM-UP to preserve line numbers as we delete
# Each range: (start_idx, end_idx)

# First, we need to check what's in the main loop lines 7599-7696
# We need to KEEP the core render/parallax/card stuff but REMOVE the brain parts
# Lines 7599-7696 contain the main animation loop. Let's see what we want to keep.

# The loop has these sections:
# 7599: (function loop()
# 7600: requestAnimationFrame(loop)
# 7601-7603: clock stuff
# 7604-7649: MAGAZINE TO BRAIN TRANSITION block (REMOVE)
# 7650: blank
# 7651-7657: BRAIN RENDER block (REMOVE)
# 7658: blank
# 7659-7688: Parallax + renderer.render + BRAIN RENDER again (KEEP parallax, KEEP renderer.render, REMOVE brain)
# 7689: blank
# 7690: cssRenderer.render
# 7691: blank
# 7692-7695: card renderer2
# 7696: })();

# So the cleanest approach:
# 1. Remove 7604-7657 (mag-to-brain transition + first brain render)
# 2. Remove 7679-7688 (second brain render in main loop)

# Let's build the deletions list (0-indexed ranges to remove, BOTTOM UP):
deletions = [
    (7759, 7804),  # brain-annotations HTML div + script (lines 7760-7805)
    (7747, 7758),  # brain-annotations CSS style block (lines 7748-7759)
    (7678, 7688),  # BRAIN RENDER second block in main loop (lines 7679-7689)
    (7603, 7657),  # MAGAZINE TO BRAIN TRANSITION + first BRAIN RENDER (lines 7604-7658)
    (7183, 7597),  # Brain globals + initBrainRenderer IIFE (lines 7184-7598)
    (5439, 5476),  # Third BRAIN PROGRESS LOGIC copy (lines 5440-5477)
    (5339, 5376),  # Second BRAIN PROGRESS LOGIC copy (lines 5340-5377)
    (5030, 5076),  # First BRAIN PROGRESS LOGIC copy (lines 5031-5077)
    (2628, 2628),  # CSS2DRenderer script tag (line 2629)
    (1515, 1533),  # brain-label CSS styles (lines 1516-1534)
]

# Apply deletions bottom-up
result = list(lines)
for start, end in deletions:
    print(f'Removing lines {start+1} to {end+1} (count: {end-start+1})')
    del result[start:end+1]

print(f'Total lines after cleanup: {len(result)}')

# Verify key things still exist
text = ''.join(result)
checks = [
    ('magazine-content', 'Magazine content HTML'),
    ('mag-breakout-overlay', 'Overlay div'),
    ('MAGAZINE EXPANSION', 'Magazine expansion JS'),
    ('(function loop()', 'Main animation loop'),
    ('renderer.render(scene', 'Main Three.js render'),
    ('cssRenderer.render', 'CSS renderer'),
    ('carousel-track', 'Carousel track'),
]
print()
print('Verification:')
for marker, name in checks:
    print(f'  {name}: {"OK" if marker in text else "MISSING!"}')

print()
bad = ['brain-label', 'initBrainRenderer', 'BRAIN PROGRESS LOGIC', 'bann-1', 'brain-annotations', 'CSS2DRenderer']
print('Should be REMOVED:')
for marker in bad:
    print(f'  {marker}: {"STILL PRESENT - CHECK!" if marker in text else "REMOVED OK"}')

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.writelines(result)
print()
print('Cleanup complete!')
