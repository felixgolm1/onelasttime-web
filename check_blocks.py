import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("--- 4047 block ---")
for i in range(4044, 4055):
    print(lines[i].strip())

print("\n--- 5200 block ---")
for i in range(5197, 5208):
    print(lines[i].strip())
