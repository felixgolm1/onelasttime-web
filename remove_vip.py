import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Borrar el overlay vip que hayamos inyectado mal, o dejar el que está y sobreescribir su script
start_idx = content.find('<style>\n    .vip-pill {')
if start_idx != -1:
    print("Found VIP style, let's remove the whole block.")
    # El final del overlay suele ser <!-- END VIP OVERLAY -->, o el </script> final
    end_idx = content.find('<!-- END VIP OVERLAY -->', start_idx)
    if end_idx == -1:
        # try to find the end script tag manually
        end_idx = content.find('document.getElementById(\'vip-code\').focus();\n    }, 500);\n</script>', start_idx)
        if end_idx != -1:
             end_idx += len('document.getElementById(\'vip-code\').focus();\n    }, 500);\n</script>')

    if end_idx != -1:
        content = content[:start_idx] + content[end_idx:]
        with open('3d-test.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Removed existing VIP block")
    else:
        print("Could not find end of VIP block")
else:
    print("VIP block not found in 3d-test.html")
