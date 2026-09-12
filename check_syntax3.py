import re

with open("3d-test.html", "r", encoding="utf-8") as f:
    lines = f.read().split("\n")
code = "\n".join(lines[6995:19973])
state, clean, i = "CODE", [], 0
while i < len(code):
    c = code[i]
    if state == "CODE":
        if c == "/" and i+1 < len(code) and code[i+1] == "/": state="L_COM"; i+=1
        elif c == "/" and i+1 < len(code) and code[i+1] == "*": state="B_COM"; i+=1
        elif c in "\"'`": state = "STR_" + c
        else: clean.append(c)
    elif state == "L_COM":
        if c == "\n": state="CODE"; clean.append("\n")
    elif state == "B_COM":
        if c == "*" and i+1 < len(code) and code[i+1] == "/": state="CODE"; i+=1
        elif c == "\n": clean.append("\n")
    elif state.startswith("STR_"):
        q = state[-1]
        if c == "\\": i+=1
        elif c == q: state="CODE"
        elif c == "\n": clean.append("\n")
    i += 1
cl = "".join(clean)
stack = []
for j, char in enumerate(cl):
    if char in "{[(": stack.append((char, j))
    elif char in "}])":
        if not stack: print(f"Extra {char} at line {cl[:j].count(chr(10))+6996}"); break
        lc, lj = stack.pop()
        if (char=="}" and lc!="{") or (char=="]" and lc!="[") or (char==")" and lc!="("):
            print(f"Mismatch {char} for {lc} at line {cl[:j].count(chr(10))+6996}"); break
if stack: print(f"Unclosed {stack[-1][0]} at line {cl[:stack[-1][1]].count(chr(10))+6996}")
