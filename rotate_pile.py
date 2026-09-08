import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

old_func = """  function buildAllCards() {
    const cardPos = [
      {x: 0.15, z: 0.1,  rY:  0.08,  rZ:  0.03,  yOffset: 0.000},  // base
      {x: 0.15, z: 0.1,  rY:  0.04,  rZ: -0.015,  yOffset: 0.034},  // encima
      {x: 0.15, z: 0.1,  rY: -0.06,  rZ:  0.025,  yOffset: 0.068},  // encima
      {x: 0.15, z: 0.1,  rY: -0.02,  rZ: -0.01,   yOffset: 0.102},  // tope
    ];"""

new_func = """  function buildAllCards() {
    const isMobile = window.innerWidth <= 768;
    const mobRYOffset = isMobile ? -Math.PI / 2 : 0;
    const cardPos = [
      {x: 0.15, z: 0.1,  rY:  0.08 + mobRYOffset,  rZ:  0.03,  yOffset: 0.000},  // base
      {x: 0.15, z: 0.1,  rY:  0.04 + mobRYOffset,  rZ: -0.015,  yOffset: 0.034},  // encima
      {x: 0.15, z: 0.1,  rY: -0.06 + mobRYOffset,  rZ:  0.025,  yOffset: 0.068},  // encima
      {x: 0.15, z: 0.1,  rY: -0.02 + mobRYOffset,  rZ: -0.01,   yOffset: 0.102},  // tope
    ];"""

if old_func in content:
    content = content.replace(old_func, new_func)
    print("Replaced buildAllCards successfully")
else:
    print("Failed to replace buildAllCards")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
