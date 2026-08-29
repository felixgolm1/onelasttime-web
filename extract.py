import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Let's extract the exact JSX of the editable block.
start_marker = '<div className="mt-1 flex flex-col gap-1">'
end_marker = '</div>\n                                        </li>'
idx_start = text.find(start_marker)
idx_end = text.find(end_marker, idx_start)

editable_block = text[idx_start:idx_end + 6] # including the closing </div>
# But wait, it's inside a <li>. I want just the div.
print(editable_block[:200])

