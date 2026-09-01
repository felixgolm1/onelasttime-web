import re

file_path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\arbol.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_checkout = """        const Checkout = ({ globalData, progress, onBack }) => {
            const [loading, setLoading] = useState(false);
            const [outOfStock, setOutOfStock] = useState(false);
            const [paymentSuccess, setPaymentSuccess] = useState(false);
            const [emailLeft, setEmailLeft] = useState(false);
            
            const [clientSecret, setClientSecret] = useState('');
            const [stripeError, setStripeError] = useState('');
            const stripeElementsRef = useRef(null);
            const [isStripeReady, setIsStripeReady] = useState(false);

            const isDigital = globalData.formatId?.includes('digital');
            const price = isDigital ? '5,00€' : '35,00€';
            const formatName = isDigital ? 'Edición Digital' : 'Edición Física';

            const audNode = dbAudience.find(a => a.id === globalData.audienceId);
            const audLabel = audNode ? (audNode.label || audNode.nombre_visible) : 'Mesa Sensibles';

            useEffect(() => {
                fetch('http://localhost:8000/create-payment-intent', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ deliveryMode: isDigital ? 'digital' : 'fisico' })
                })
                .then(r => r.json())
                .then(data => {
                    if(data.clientSecret) {
                        setClientSecret(data.clientSecret);
                    } else if (data.error) {
                        setStripeError('Error al conectar con la pasarela.');
                    }
                })
                .catch(err => {
                    console.error("Error creating intent:", err);
                    setStripeError('Error de red al inicializar pago.');
                });
            }, [isDigital]);

            useEffect(() => {
                if (clientSecret && window.Stripe && !stripeElementsRef.current) {
                    const stripe = window.Stripe('pk_test_51U4dAmCV2A1IisxkBGbtiiurJ622x2EKPGkTuwhvDB3w65h4WO2PXafJpZA2Dtq7GY5ycOTZGQPlxe80nl308oD000rKsSQeOZ');
                    const elements = stripe.elements({ 
                        clientSecret, 
                        appearance: { 
                            theme: 'night', 
                            variables: { 
                                colorPrimary: '#ccff00', 
                                colorBackground: '#1a1a1a',
                                colorText: '#ffffff',
                                colorDanger: '#ff4444',
                                fontFamily: 'ui-sans-serif, system-ui, sans-serif'
                            } 
                        } 
                    });
                    const paymentElement = elements.create('payment');
                    paymentElement.mount('#payment-element');
                    paymentElement.on('ready', () => setIsStripeReady(true));
                    stripeElementsRef.current = { stripe, elements };
                }
            }, [clientSecret]);

            const handlePayment = async (e) => {
                if (e) e.preventDefault();
                setLoading(true);
                setStripeError('');

                if (!stripeElementsRef.current) {
                    setStripeError("Stripe no está inicializado");
                    setLoading(false);
                    return;
                }

                const { stripe, elements } = stripeElementsRef.current;
                
                const { error, paymentIntent } = await stripe.confirmPayment({
                    elements,
                    confirmParams: {
                        return_url: window.location.href,
                    },
                    redirect: 'if_required'
                });

                if (error) {
                    setStripeError(error.message);
                    setLoading(false);
                    return;
                }
                
                if (paymentIntent && paymentIntent.status === 'succeeded') {
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
                        _subject: "🔥 ¡Nuevo mazo personalizado pagado en Sensibles!"
                    };

                    const fallbackTimer = setTimeout(() => {
                        setLoading(false);
                        setPaymentSuccess(true);
                    }, 3200);

                    fetch(`https://script.google.com/macros/s/AKfycbzoQs8TtvApq_3EG1IWNv6oboIzdELMdvQsXk8Xuv8h9IRzg0nG1fBKT64IcEUkP8M/exec`, {
                        method: "POST",
                        headers: { 
                            'Content-Type': 'text/plain;charset=utf-8'
                        },
                        body: JSON.stringify(payload)
                    })
                    .then(response => response.json())
                    .then(data => {
                        clearTimeout(fallbackTimer);
                        setLoading(false);
                        setPaymentSuccess(true);
                    })
                    .catch(err => {
                        clearTimeout(fallbackTimer);
                        console.error("Error enviando datos:", err);
                        setLoading(false);
                        setPaymentSuccess(true);
                    });
                }
            };

            if (paymentSuccess) {
                return (
                    <div className="flex-1 flex items-center justify-center p-6 fade-in relative">
                        <div className="text-center max-w-md bg-[#111] p-10 rounded-[2.5rem] shadow-[0_20px_60px_rgba(0,0,0,0.4)] border border-[#222] mt-12">
                            <div className="w-20 h-20 bg-green-50 text-green-500 rounded-full flex items-center justify-center mx-auto mb-8">
                                <svg className="w-10 h-10" fill="none" stroke="currentColor" strokeWidth="2" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7"></path></svg>
                            </div>
                            <h2 className="text-3xl md:text-4xl font-semibold tracking-tight text-white mb-4">¡Nos ponemos a trabajar!</h2>
                            <p className="text-gray-500 mb-6 leading-relaxed">
                                Nos ponemos a trabajar para hacer de tu cena una de las más auténticas que hayas vivido hasta ahora.
                            </p>
                            <p className="text-xl font-medium text-white mb-8">Hasta muy pronto</p>
                            <button onClick={() => window.location.href = '3d-test.html'} className="text-xs font-bold text-gray-400 uppercase tracking-[0.2em] hover:text-black transition-colors">Volver al inicio</button>
                        </div>
                    </div>
                );
            }

            if (outOfStock) {
                return (
                    <div className="flex-1 flex items-center justify-center p-6 fade-in relative">
                        <div className="text-center max-w-md bg-[#111] p-10 rounded-[2.5rem] shadow-[0_20px_60px_rgba(0,0,0,0.4)] border border-[#222] mt-12">
                            <div className="w-20 h-20 bg-amber-50 text-amber-500 rounded-full flex items-center justify-center mx-auto mb-8">
                                <svg className="w-10 h-10" fill="none" stroke="currentColor" strokeWidth="2" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                            </div>
                            <h2 className="text-3xl md:text-4xl font-semibold tracking-tight text-white mb-4">Stock agotado en tu zona</h2>
                            <p className="text-gray-500 mb-4 leading-relaxed">
                                Lo sentimos, acabamos de recibir un volumen inusual de pedidos en los últimos minutos y hemos agotado las cajas físicas para tu ubicación.
                            </p>
                            <div className="bg-gray-50 p-4 rounded-2xl mb-8 border border-dashed border-gray-200">
                                <p className="text-xs font-semibold text-gray-600 uppercase tracking-widest mb-1">Aviso importante</p>
                                <p className="text-sm text-gray-400">Tu tarjeta NO ha sido cargada. La operación ha sido cancelada automáticamente.</p>
                            </div>
                            
                            {!emailLeft ? (
                                <div className="space-y-4">
                                    <p className="text-sm font-medium text-gray-700">¿Quieres que te avisemos en cuanto repongamos stock (24-48h)?</p>
                                    <div className="flex gap-2">
                                        <input type="email" placeholder="Tu email" className="pay-input !py-3 !text-sm" />
                                        <button onClick={() => setEmailLeft(true)} className="bg-black text-white px-6 rounded-xl text-sm font-bold">Avisadme</button>
                                    </div>
                                </div>
                            ) : (
                                <p className="text-green-600 font-bold text-sm animate-bounce">✨ ¡Te avisaremos pronto!</p>
                            )}
                            
                            <button onClick={() => window.location.href = 'index.html'} className="mt-10 text-xs font-bold text-gray-300 uppercase tracking-[0.2em] hover:text-black transition-colors">Volver al inicio</button>
                        </div>
                    </div>
                );
            }

            return (
                <div className="flex-1 py-12 px-6 flex flex-col items-center relative fade-in">
                    <div className="max-w-4xl w-full grid grid-cols-1 md:grid-cols-2 gap-12 mt-16">
                        <div className="space-y-8">
                            <div>
                                <h1 className="text-3xl font-semibold tracking-tight mb-4">Tus cartas personalizadas</h1>
                                <p className="text-gray-500">Hemos diseñado esta experiencia exclusivamente para tu cena basada en tus respuestas.</p>
                            </div>

                            <div className="summary-card text-black space-y-4">
                                <div className="flex justify-between items-center pb-4 border-b border-gray-200">
                                    <div className="flex items-center gap-3">
                                        <div className="w-12 h-12 bg-black rounded-lg flex items-center justify-center p-2.5">
                                            <img src="assets/img/logo one last time.png" alt="One Last Time" className="w-full h-full object-contain" style={{ filter: 'brightness(0) invert(1)' }} />
                                        </div>
                                        <div>
                                            <p className="font-semibold text-sm">Sensibles: {formatName}</p>
                                            <p className="text-xs text-gray-400 italic">Personalizado para: {audLabel}</p>
                                        </div>
                                    </div>
                                    <p className="font-bold text-gray-900">{price}</p>
                                </div>
                                
                                <div className="space-y-2">
                                    <div className="flex justify-between text-sm text-gray-500">
                                        <span>{isDigital ? 'Envío Inmediato (Email/Web)' : `Envío a ${globalData.logistics?.ciudad || 'tu zona'}`}</span>
                                        <span className="text-green-600 font-medium">Gratis</span>
                                    </div>
                                    <div className="flex justify-between text-lg font-bold pt-2 border-t border-gray-200">
                                        <span>Total</span>
                                        <span>{price}</span>
                                    </div>
                                </div>
                            </div>

                            <div className="flex items-center gap-4 text-xs text-gray-400 font-medium uppercase tracking-wider">
                                <div className="flex items-center gap-1">🔒 100% Seguro</div>
                            </div>
                        </div>

                        <div className="bg-[#111] rounded-[2rem] p-8 shadow-[0_20px_50px_rgba(0,0,0,0.4)] border border-[#222] flex flex-col justify-between">
                            <div>
                                <h3 className="text-lg font-semibold mb-6">Información de Pago</h3>
                                
                                <div id="payment-element" className="min-h-[150px] mb-4">
                                    {!clientSecret && !stripeError && (
                                        <div className="flex flex-col items-center justify-center py-10 text-gray-500">
                                            <div className="spinner mb-4 border-gray-500"></div>
                                            <span className="text-sm">Conectando con pasarela segura...</span>
                                        </div>
                                    )}
                                </div>
                                
                                {stripeError && (
                                    <div className="text-red-500 text-sm mb-4 text-center p-3 bg-red-500/10 rounded-lg">{stripeError}</div>
                                )}
                            </div>

                            <div className="pt-4 mt-auto">
                                <button 
                                    onClick={handlePayment}
                                    disabled={loading || !isStripeReady}
                                    className={`btn-pay shadow-lg ${!isStripeReady ? 'opacity-50 cursor-not-allowed' : ''}`}
                                >
                                    {loading ? (
                                        <div className="spinner"></div>
                                    ) : (
                                        <>Confirmar y pagar {price}</>
                                    )}
                                </button>
                                <p className="text-[10px] text-gray-500 text-center px-4 leading-relaxed mt-4">
                                    Pagos procesados de forma segura por Stripe.
                                </p>
                            </div>
                        </div>
                    </div>

                    <div className="mt-12 flex gap-8 grayscale opacity-30">
                         <div className="font-bold text-sm tracking-tighter">VISA</div>
                         <div className="font-bold text-sm tracking-tighter">Mastercard</div>
                         <div className="font-bold text-sm tracking-tighter">Stripe</div>
                         <div className="font-bold text-sm tracking-tighter">SSL Secure</div>
                    </div>
                </div>
            );
        };"""

# Use regex to find and replace the Checkout component
pattern = re.compile(r"const Checkout = \(\{ globalData, progress, onBack \}\) => \{.*?(?=\n\s*// ==========================================)", re.DOTALL)
new_content = pattern.sub(new_checkout, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
