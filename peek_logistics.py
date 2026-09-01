with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find("const LogisticsForm =")
end_idx = text.find("const ErrorEntrega = ", idx)
print(text[idx:idx+1500])
print("\n--- JUMP ---\n")
print(text[end_idx-1500:end_idx])

