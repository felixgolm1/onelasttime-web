import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# Emojis are hard to match if there are encoding issues, so let's match the exact context strings.
# Replace button padlock
# Old: <>🔒 Pagar {price} de forma segura</>
text = re.sub(
    r'<>. Pagar \{price\} de forma segura</>',
    '<><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="2.5" stroke="currentColor" className="w-5 h-5 mr-1.5 inline-block -mt-1"><path strokeLinecap="round" strokeLinejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" /></svg> Pagar {price} de forma segura</>',
    text
)

# Replace text padlock
# Old: <span className="font-semibold text-gray-800">🔒 Pago 100% Seguro.</span>
text = re.sub(
    r'<span className="font-semibold text-gray-800">. Pago 100% Seguro.</span>',
    '<span className="font-semibold text-gray-800 flex items-center justify-center mb-1"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="2.5" stroke="currentColor" className="w-3.5 h-3.5 mr-1 inline-block"><path strokeLinecap="round" strokeLinejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" /></svg>Pago 100% Seguro.</span>',
    text
)


with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated icons!")

