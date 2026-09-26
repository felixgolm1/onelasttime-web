import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = r"      const scrollTl = gsap.timeline\(\{ paused: true \}\);"
replacement = """      const scrollTl = gsap.timeline({ paused: true });
      // DEBUG: Imprimir duracion total
      setTimeout(() => {
          console.log("BRAIN DURATION", scrollTl.duration());
      }, 1000);"""

content = re.sub(target, replacement, content)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Injected duration logger")
