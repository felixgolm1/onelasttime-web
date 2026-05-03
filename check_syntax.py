import re

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the main script
match = re.search(r'<script>(.*?)</script>', content[content.find('id_card_base64'):], re.DOTALL)
if match:
    script = match.group(1)
    
    # Strip comments
    script = re.sub(r'//.*', '', script)
    script = re.sub(r'/\*.*?\*/', '', script, flags=re.DOTALL)
    
    # Check string literal closures
    in_single = False
    in_double = False
    in_backtick = False
    
    for i, char in enumerate(script):
        if char == "'" and not in_double and not in_backtick:
            if i == 0 or script[i-1] != '\\':
                in_single = not in_single
        elif char == '"' and not in_single and not in_backtick:
            if i == 0 or script[i-1] != '\\':
                in_double = not in_double
        elif char == '' and not in_single and not in_double:
            if i == 0 or script[i-1] != '\\':
                in_backtick = not in_backtick
                
    print(f"Unclosed strings -> Single: {in_single}, Double: {in_double}, Backtick: {in_backtick}")
    
    braces = 0
    parens = 0
    for i, char in enumerate(script):
        if char == '{': braces += 1
        elif char == '}': braces -= 1
        elif char == '(': parens += 1
        elif char == ')': parens -= 1
    print(f"Unclosed Braces: {braces}, Parens: {parens}")
