import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                                <div className="rounded-xl bg-gray-50/50">
                                    <button 
                                        onClick={() => setShowOrderDetails(!showOrderDetails)} 
                                        className="w-full flex justify-between items-center py-4 outline-none transition-colors"
                                    >
                                        <h3 className="text-lg font-bold text-black m-0">Detalles del pedido</h3>
                                        <svg 
                                            className={`w-5 h-5 text-gray-500 transition-transform duration-300 ${showOrderDetails ? 'rotate-180' : ''}`} 
                                            fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                        >
                                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 9l-7 7-7-7"></path>
                                        </svg>
                                    </button>
                                    <div 
                                        className={`overflow-hidden transition-all duration-300 ease-in-out ${showOrderDetails ? 'max-h-[500px] opacity-100' : 'max-h-0 opacity-0'}`}
                                    >
                                        <div className="pb-4">
                                            <ul className="space-y-3 text-sm text-gray-600">
                                        <li><strong className="text-gray-800">Formato de la experiencia:</strong> Cartas en versión {isDigital ? 'digital' : 'física'}</li>
                                        {dondeLasUsaras && <li><strong className="text-gray-800">Lugar donde las vas a usar:</strong> {dondeLasUsaras}</li>}
                                        
                                        {globalData.logistics?.fecha && (
                                            <li>
                                                <strong className="text-gray-800">
                                                    {(globalData.formatId?.includes('restaurante') || globalData.formatId?.includes('reserva') || isDigital) ? 'Hora de la cena:' : 'Límite de entrega:'}
                                                </strong> {formatDate(globalData.logistics.fecha)}
                                            </li>
                                        )}


                                    </ul>
                                        </div>
                                    </div>
                                </div>"""

if target in text:
    text = text.replace(target, "")
    with open("arbol.html", "w", encoding="utf-8") as f:
        f.write(text)
    print("Removed Detalles del pedido block!")
else:
    print("Target not found.")

