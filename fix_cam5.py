import re

def main():
    with open('3d-test.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # aggressively remove the loops
    # Look for Array.from(document.body.children).forEach(child => { ... })
    pattern = re.compile(r'Array\.from\(document\.body\.children\)\.forEach\(child => \{.*?\}\);', re.DOTALL)
    html = pattern.sub('', html)
    
    # Wait, there's another loop starting at 6415? Let's check if there are multiple variations of the loop.
    # It might not end with "});" immediately. It might have nested blocks.
    
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    main()
