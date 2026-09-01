import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# I will find the block:
# `<div className="mb-6">\n                                        <strong className="text-gray-800 block mb-2">\n                                            ¿Quieres que tengamos algo en cuenta para la entrega?`
# And wrap it in `{globalData.logistics?.direccion && (` ... `)}`

block_start = '<div className="mb-6">\n                                        <strong className="text-gray-800 block mb-2">\n                                            ¿Quieres que tengamos algo en cuenta para la entrega?'

idx = text.find(block_start)
end_idx = text.find('                                    <div className="mb-6">\n                                            <strong className="text-gray-800 block mb-2">\n                                                {isDigital ? \'Información de contacto', idx)

if idx == -1 or end_idx == -1:
    print("Could not find the block.")
else:
    block = text[idx:end_idx]
    wrapped_block = "{globalData.logistics?.direccion && (\n                                    " + block.strip() + "\n                                    )}\n"
    text = text[:idx] + wrapped_block + text[end_idx:]
    with open("arbol.html", "w", encoding="utf-8") as f:
        f.write(text)
    print("Wrapped the notes block in condition!")

