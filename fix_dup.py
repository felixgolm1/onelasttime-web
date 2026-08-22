import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# I want to find the OLD WhatsApp block and remove it.
# Wait, let's just find the entire block from the old WhatsApp to the end of the new Email block and replace it correctly.
# The current HTML has:
# 1. Old WhatsApp block (min-h-[32px], mr-1)
# 2. New WhatsApp block (min-h-[36px], mr-2)
# 3. New Email block (min-h-[36px], mr-2)

old_whatsapp_start = text.find("<div className=\"flex items-center min-h-[32px]\">\n                                                    <span className=\"text-gray-500 mr-1\">WhatsApp:</span>")
if old_whatsapp_start != -1:
    print("Found old whatsapp block!")
    new_whatsapp_start = text.find("<div className=\"flex items-center min-h-[36px]\">\n                                                    <span className=\"text-gray-500 mr-2\">WhatsApp:</span>", old_whatsapp_start)
    if new_whatsapp_start != -1:
        print("Found new whatsapp block right after it!")
        
        # we want to delete from old_whatsapp_start to new_whatsapp_start
        new_text = text[:old_whatsapp_start] + text[new_whatsapp_start:]
        with open("arbol.html", "w", encoding="utf-8") as f:
            f.write(new_text)
        print("Deleted the duplicate old WhatsApp block!")
else:
    print("Not found old block")

