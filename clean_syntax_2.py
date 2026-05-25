with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1

for i in range(len(lines)):
    # Find my injected block's end
    if "if (brainUI) brainUI.style.opacity = '0';" in lines[i]:
        # Next line is "        }"
        if "}" in lines[i+1]:
            # Now we look for the next "      } else {" that has "if (magazineScene) {" after it
            for j in range(i+2, i+30):
                if "} else {" in lines[j] and "if (magazineScene) {" in lines[j+1]:
                    start_idx = i + 2
                    end_idx = j
                    break
        if start_idx != -1:
            break

if start_idx != -1 and end_idx != -1:
    print(f"Deleting lines {start_idx} to {end_idx - 1}")
    del lines[start_idx:end_idx]
    
    with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Syntax cleaned completely!")
else:
    print("Could not find the bounds to delete.")
