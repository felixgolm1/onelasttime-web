import re

with open('garantia.html', 'r', encoding='utf-8') as f:
    text = f.read()

body_html = '''        <h2>LA GARANTÍA ONE LAST TIME</h2>
        <p>En <em>One Last Time</em> estamos tan seguros de la calidad y del impacto de nuestra experiencia que hemos decidido asumir nosotros todo el riesgo.</p>
        
        <p>Si al vivir la experiencia sientes que no ha valido la pena o no estás satisfecho con lo vivido, haremos lo siguiente:</p>
        
        <ul>
            <li><strong>Te devolvemos el 100% del dinero</strong> que pagaste por la reserva. Sin rodeos y sin letra pequeña.</li>
            <li><strong>Te regalamos una experiencia adicional</strong> como disculpa por no haber cumplido tus expectativas.</li>
        </ul>
        
        <h2>CÓMO FUNCIONA Y QUÉ TIENES QUE HACER</h2>
        <p>Hacer uso de la garantía es extremadamente fácil y libre de fricciones:</p>
        <ul>
            <li>Solo tienes que decírnoslo durante las <strong>24 horas posteriores</strong> tras haber vivido la experiencia por email a <strong>hola@sensibles.co</strong>, por WhatsApp al <strong>+34 649 67 16 50</strong> o por Instagram a <strong>@sensibles.co</strong>.</li>
            <li><strong>No te preguntaremos nada.</strong> Procesaremos la devolución sin hacer preguntas incómodas (aunque, si te apetece, nos encantaría saber en qué fallamos para poder mejorar).</li>
        </ul>
        
        <h2>LA ÚNICA REGLA (PARA EVITAR ABUSOS)</h2>
        <p>Queremos ser transparentes: esta garantía está pensada para protegerte a ti si nuestro servicio no da la talla. Sin embargo, para evitar abusos fraudulentos, la dirección se reserva el derecho de revisión si se detecta mala fe evidente.</p>
        
        <p><strong>Aclaración importante sobre cancelaciones:</strong> Esta garantía aplica <em>exclusivamente</em> a las personas que asisten y viven la experiencia. Si cancelas antes de venir, cambias de planes o simplemente no te presentas (<em>no show</em>), no se aplica esta garantía y no hay devoluciones (al tratarse de un evento cerrado y exclusivo, tal y como marca la ley para actividades de esparcimiento con fecha cerrada).</p>
'''

start_idx = text.find('<h2>LA GARANTÍA ONE LAST TIME</h2>')
end_idx = text.find('<div style="display: flex; justify-content: center; margin-top: 80px; margin-bottom: 40px; width: 100%;">')

if start_idx != -1 and end_idx != -1:
    text = text[:start_idx] + body_html + '\n    ' + text[end_idx:]

with open('garantia.html', 'w', encoding='utf-8') as f:
    f.write(text)
    
print('Updated garantia.html content')
