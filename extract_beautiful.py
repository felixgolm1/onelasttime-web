import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# Buscamos la etiqueta <style> que empieza por .vip-pill
style_match = re.search(r'<style>\s*\.vip-pill\s*\{', idx)
if not style_match:
    print("Could not find <style> block")
    exit(1)

start_idx = style_match.start()

# Buscamos el final del script VIP
end_marker = "setTimeout(checkVipCode, 50); // slight delay to feel the click\n    }\n});\n</script>"
end_idx = idx.find(end_marker, start_idx)
if end_idx == -1:
    print("Could not find end of VIP block")
    exit(1)

end_idx += len(end_marker)

vip_code = idx[start_idx:end_idx]

# Replace localStorage with sessionStorage
vip_code = vip_code.replace('localStorage.getItem', 'sessionStorage.getItem')
vip_code = vip_code.replace('localStorage.setItem', 'sessionStorage.setItem')

print(f"Extracted {len(vip_code)} bytes of VIP code.")

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Quitamos el VIP overlay "fake" que inyectamos antes
start_fake = content.find('<!-- VIP OVERLAY START -->')
end_fake = content.find('<!-- VIP OVERLAY END -->')
if start_fake != -1 and end_fake != -1:
    end_fake += len('<!-- VIP OVERLAY END -->')
    content = content[:start_fake] + content[end_fake:]
    print("Removed fake VIP overlay")

# Lo inyectamos al final
if '</html>' in content:
    content = content.replace('</html>', vip_code + '\n</html>')
else:
    content += '\n' + vip_code

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Injected BEAUTIFUL VIP gateway into 3d-test.html")
