import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'fake-bg-fade' in line:
        print(f"--- Occurrence at line {i+1} ---")
        start = max(0, i - 15)
        end = min(len(lines), i + 15)
        for j in range(start, end):
            print(f"{j+1}: {lines[j].strip()}")
