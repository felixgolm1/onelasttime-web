import re

with open('arbol.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update App state initialization
app_start_code_old = """            const urlParams = new URLSearchParams(window.location.search);
            const forceSkip = urlParams.get('skipIntro') === 'true';
            
            
            if (forceSkip && !sessionStorage.getItem('forceSkipApplied')) {"""
app_start_code_new = """            const urlParams = new URLSearchParams(window.location.search);
            const redirectStatus = urlParams.get('redirect_status');
            const forceSkip = urlParams.get('skipIntro') === 'true';
            
            if (forceSkip && !redirectStatus && !sessionStorage.getItem('forceSkipApplied')) {"""

content = content.replace(app_start_code_old, app_start_code_new)

phase_old = """            const [phase, setPhase] = useState(() => {
                if (forceSkip && !sessionStorage.getItem('forceSkipApplied')) {
                    return 'format';
                }
                return sessionStorage.getItem('dev_phase') || 'intro';
            });"""
phase_new = """            const [phase, setPhase] = useState(() => {
                if (redirectStatus) return 'checkout';
                if (forceSkip && !sessionStorage.getItem('forceSkipApplied')) {
                    return 'format';
                }
                return sessionStorage.getItem('dev_phase') || 'intro';
            });"""

content = content.replace(phase_old, phase_new)

# 2. Update Checkout
checkout_start = content.find("const Checkout = ({ globalData, progress, onBack }) => {")
handle_payment_idx = content.find("const handlePayment =", checkout_start)

checkout_vars_end = content.find("const audLabel =", checkout_start)
checkout_vars_end = content.find("\n", checkout_vars_end) + 1

# Insert processSuccessfulPayment and useEffect after variables
process_logic = """
            const processSuccessfulPayment = () => {
                let selectedTones = (globalData.tones || []).map(tId => {
                    for (const cat of dbTones) {
                        const t = cat.subtones.find(s => s.id === tId);
                        if (t) return t.text;
                    }
                    return tId;
                }).join(', ');

                const participantesText = (globalData.participants || []).map(p => 
                    `Nombre: ${p.name}`
                ).join('\\n');

                const payload = {
                    Edicion: isDigital ? 'Digital' : 'Física',
                    Tipo_Relacion: audLabel,
                    Tonos_Elegidos: selectedTones,
                    Ciudad: globalData.logistics?.ciudad || 'N/A',
                    Fecha_Cena: globalData.logistics?.fecha || 'N/A',
                    Participantes: participantesText || 'Ninguno',
                    Objetivo_Cena: globalData.objective || 'N/A',
                    Notas_Extra: globalData.n4?.extraDetails || 'Ninguna',
                    _subject: "✨ ¡Nuevo mazo personalizado pagado en Sensibles!"
                };

                const fallbackTimer = setTimeout(() => {
                    setLoading(false);
                    setPaymentSuccess(true);
                }, 3200);

                fetch(`https://script.google.com/macros/s/AKfycbzoQs8TtvApq_3EG1IWNv6oboIzdELMdvQsXk8Xuv8h9IRzg0nG1fBKT64IcEUkP8M/exec`, {
                    method: "POST",
                    headers: { 'Content-Type': 'text/plain;charset=utf-8' },
                    body: JSON.stringify(payload)
                }).then(() => {
                    clearTimeout(fallbackTimer);
                    setPaymentSuccess(true);
                    setLoading(false);
                    sessionStorage.clear();
                }).catch(e => {
                    console.error("Error saving to sheets", e);
                });
            };

            useEffect(() => {
                const urlParams = new URLSearchParams(window.location.search);
                const redirectStatus = urlParams.get('redirect_status');
                const clientSecretParam = urlParams.get('payment_intent_client_secret');

                if (redirectStatus === 'succeeded' && clientSecretParam) {
                    setLoading(true);
                    const checkStripe = () => {
                        if (window.Stripe) {
                            const stripe = window.Stripe('pk_test_51U4dAmCV2A1IisxkBGbtiiurJ622x2EKPGkTuwhvDB3w65h4WO2PXafJpZA2Dtq7GY5ycOTZGQPlxe80nl308oD000rKsSQeOZ');
                            stripe.retrievePaymentIntent(clientSecretParam).then(({ paymentIntent }) => {
                                if (paymentIntent && paymentIntent.status === 'succeeded') {
                                    processSuccessfulPayment();
                                } else {
                                    setStripeError('No se pudo verificar el pago tras la redirección.');
                                    setLoading(false);
                                }
                            });
                        } else {
                            setTimeout(checkStripe, 500);
                        }
                    };
                    checkStripe();
                } else if (redirectStatus === 'failed') {
                    setStripeError('El pago falló. Por favor, intenta de nuevo.');
                }
            }, []);
"""

content = content[:checkout_vars_end] + process_logic + content[checkout_vars_end:]

# Now replace the inner logic of handlePayment
handle_payment_old_regex = re.compile(r"if \(paymentIntent && paymentIntent\.status === 'succeeded'\) \{.*?\};?\s*\}\s*\}", re.DOTALL)
content = handle_payment_old_regex.sub("""if (paymentIntent && paymentIntent.status === 'succeeded') {
                    processSuccessfulPayment();
                }""", content, count=1)


with open('arbol.html', 'w', encoding='utf-8') as f:
    f.write(content)
