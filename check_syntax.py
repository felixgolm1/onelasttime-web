import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

script_start = text.find('<script>') + 8
script_end = text.rfind('</script>')
code = text[script_start:script_end]

state = 'CODE'
clean_code = []
i = 0
while i < len(code):
    char = code[i]
    if state == 'CODE':
        if char == '/' and i+1 < len(code) and code[i+1] == '/':
            state = 'LINE_COMMENT'
            i += 1
        elif char == '/' and i+1 < len(code) and code[i+1] == '*':
            state = 'BLOCK_COMMENT'
            i += 1
        elif char in '\"\'\':
            state = 'STRING_' + char
        else:
            clean_code.append(char)
    elif state == 'LINE_COMMENT':
        if char == '\n':
            state = 'CODE'
            clean_code.append('\n')
    elif state == 'BLOCK_COMMENT':
        if char == '*' and i+1 < len(code) and code[i+1] == '/':
            state = 'CODE'
            i += 1
        elif char == '\n':
            clean_code.append('\n')
    elif state.startswith('STRING_'):
        quote = state[-1]
        if char == '\\\\':
            i += 1 
        elif char == quote:
            state = 'CODE'
        elif char == '\n': 
            clean_code.append('\n')
    i += 1

clean_code_str = ''.join(clean_code)

stack = []
for i, char in enumerate(clean_code_str):
    if char in '{[(':
        stack.append((char, i))
    elif char in '}])':
        if len(stack) == 0:
            line_num = clean_code_str[:i].count('\n') + text[:script_start].count('\n') + 2
            print(f'Extra {char} found around line {line_num}')
            break
        last_char, last_i = stack.pop()
        if (char == '}' and last_char != '{') or (char == ']' and last_char != '[') or (char == ')' and last_char != '('):
            line_num = clean_code_str[:i].count('\n') + text[:script_start].count('\n') + 2
            print(f'Mismatched {char} for {last_char} found around line {line_num}')
            break

if len(stack) > 0:
    for char, idx in stack:
        line_num = clean_code_str[:idx].count('\n') + text[:script_start].count('\n') + 2
        print(f'Unclosed {char} found around line {line_num}')
