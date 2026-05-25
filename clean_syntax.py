with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Let's find the exact block to delete
# It starts after "if (brainUI) brainUI.style.opacity = '0';\n        }\n"
# And goes until "      } else {\n        if (magazineScene) {"

start_idx = -1
end_idx = -1

for i in range(len(lines)):
    if "if (brainUI) brainUI.style.opacity = '0';" in lines[i]:
        # The next line should be "        }"
        if "}" in lines[i+1]:
            start_idx = i + 2  # The line AFTER the closing brace of our logic
            break

for i in range(start_idx, len(lines)):
    if "} else {" in lines[i] and "if (magazineScene) {" in lines[i+1]:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    print(f"Deleting lines {start_idx} to {end_idx - 1}")
    del lines[start_idx:end_idx]
    
    with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Cleaned!")
else:
    print(f"Could not find indices: start={start_idx}, end={end_idx}")
