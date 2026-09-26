import re

file_path = "3d-test.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add the CSS rule to move the frame and video up on mobile
# We will inject it inside the existing @media (max-width: 768px) block near the bottom

target = r"/\* Show desktop-style scrollbar on mobile \*/"
replacement = r"""#magazine-border-svg, .carousel-viewport { transform: translateY(-1.7vh) !important; }
    /* Show desktop-style scrollbar on mobile */"""

content = re.sub(target, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done.")
