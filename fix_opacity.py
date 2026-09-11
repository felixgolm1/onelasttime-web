import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

bad1 = """          gsap.to('.flt-in', {
              y: '0%', duration: 1.0, ease: 'power3.out', stagger: 0.05, delay: 0.6
            });"""
good1 = """          gsap.to('.flt-in', {
              y: '0%', opacity: 1, duration: 1.0, ease: 'power3.out', stagger: 0.05, delay: 0.6
            });"""

bad2 = """          gsap.to('.flt-in-up', {
              y: '0%', duration: 1.0, ease: 'power3.out', stagger: 0.05, delay: 0.8
            });"""
good2 = """          gsap.to('.flt-in-up', {
              y: '0%', opacity: 1, duration: 1.0, ease: 'power3.out', stagger: 0.05, delay: 0.8
            });"""

content = content.replace(bad1, good1).replace(bad2, good2)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("done")
