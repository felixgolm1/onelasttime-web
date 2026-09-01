import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Extract the whole <li> block from Detalles del pedido
start_li = '                                        <li>\n                                            <strong className="text-gray-800 block mb-2">'
end_li = '                                                </div>\n                                            </div>\n                                        </li>'

idx_start = text.find(start_li)
idx_end = text.find(end_li, idx_start) + len(end_li)

li_block = text[idx_start:idx_end]

# 2. Remove it from Detalles del pedido
text = text.replace(li_block, "")

# 3. Modify the extracted block to remove <li> and make it a pure div
editable_block = li_block.replace('                                        <li>', '                                    <div className="mb-6">')
editable_block = editable_block.replace('                                        </li>', '                                    </div>')

# 4. Insert it into Detalles del envio, right after the flex row (mb-6 -> mb-4 in flex row)
old_flex_row = '                                    <div className="flex justify-between items-start text-sm text-gray-500 mb-6">\n                                        <span className="pr-4">{shipping.title}</span>\n                                        <div className="text-right">\n                                            <span className={`text-lg font-bold whitespace-nowrap leading-none block ${shipping.costColor}`}>{shipping.costText}</span>\n                                            {shipping.cost > 0 && <p className="text-[10px] text-gray-400 mt-0.5 whitespace-nowrap leading-none">IVA incluido</p>}\n                                        </div>\n                                    </div>'

new_flex_row = old_flex_row.replace('mb-6', 'mb-4') + '\n' + editable_block

text = text.replace(old_flex_row, new_flex_row)

# 5. Modify shipping.title for digital to remove the hardcoded whatsapp/email
old_digital_title = """                        title: (
                            <>
                                Envío de enlace al:<br/>
                                WhatsApp: {phone}<br/>
                                Email: {email}
                            </>
                        ),"""

new_digital_title = """                        title: "Envío de enlace digital", """

text = text.replace(old_digital_title, new_digital_title)


with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Moved editable block to Shipping details!")

