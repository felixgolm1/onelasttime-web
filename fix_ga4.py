import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """            const [phase, setPhase] = useState(() => {"""

replacement = """            useEffect(() => {
                if (typeof window !== 'undefined' && typeof window.gtag === 'function') {
                    window.gtag('event', 'page_view', {
                        page_title: 'Fase ' + phase,
                        page_path: '/' + phase
                    });
                }
            }, [phase]);
            
            const [phase, setPhase] = useState(() => {"""

text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated App with GA4 tracking")
