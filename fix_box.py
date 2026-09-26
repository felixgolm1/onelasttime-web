import re

file_path = "3d-test.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Change box-3d-wrapper from 46vh to 52vh
target = r"\.box-3d-wrapper \{ top: 46vh !important; \}"
replacement = r".box-3d-wrapper { top: 52vh !important; }"
content = re.sub(target, replacement, content)

# 2. Change targetVH from 50 to 56 for scBoard in updateBoxState
target = r"targetVH = mapRange\(prog, 0, 0\.40, 65, 50\);"
replacement = r"targetVH = mapRange(prog, 0, 0.40, 71, 56);"
content = re.sub(target, replacement, content)

target = r"let targetVH = 50;"
replacement = r"let targetVH = 56;"
content = re.sub(target, replacement, content)

# 3. Change the mobile initial top for scBoard in updateFaceSwap
target = r"scBoard\.style\.setProperty\('top', '50vh', 'important'\);"
replacement = r"scBoard.style.setProperty('top', '56vh', 'important');"
content = re.sub(target, replacement, content)

# 4. Change initial y for scIntro from -45 to -22 so it doesn't jump as much
target = r"gsap\.set\(scIntro, \{ xPercent: -50, yPercent: -50, x: 0, y: window\._cIsMobile \? -45 : 0,"
replacement = r"gsap.set(scIntro, { xPercent: -50, yPercent: -50, x: 0, y: window._cIsMobile ? -22 : 0,"
content = re.sub(target, replacement, content)

# 5. Change final y for scIntro from -22 to 0
target = r"scrollTl\.to\(\[scIntro, scIntroBack\], \{ y: -22, duration: PAN, ease: 'power2\.inOut' \}, t\);"
replacement = r"scrollTl.to([scIntro, scIntroBack], { y: 0, duration: PAN, ease: 'power2.inOut' }, t);"
content = re.sub(target, replacement, content)

# 6. Change made-by-humans y translation from -23dvh to -30dvh to make space
target = r"y: window\._cIsMobile \? '-23dvh' : 0, x: '92vw'"
replacement = r"y: window._cIsMobile ? '-30dvh' : 0, x: '92vw'"
content = re.sub(target, replacement, content)

# 7. Change made-by-ai y translation from 23dvh to 20dvh to prevent it falling off screen
target = r"y: window\._cIsMobile \? '23dvh' : 0, x: '-92vw'"
replacement = r"y: window._cIsMobile ? '20dvh' : 0, x: '-92vw'"
content = re.sub(target, replacement, content)


with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done.")
