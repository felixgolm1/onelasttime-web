import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                                        {isDigital ? (
                                            <>
                                                {globalData.logistics?.fecha && <li><strong className="text-gray-800">Día y hora de la cena:</strong> {formatDate(globalData.logistics.fecha)}</li>}
                                                <li><strong className="text-gray-800">Entrega:</strong> Entrega con enlace por WhatsApp y email justo al inicio de la cena o cuando quieras a partir de 10 minutos con un solo click. Por si os adelantáis</li>
                                            </>
                                        ) : (
                                            <>
                                                {globalData.logistics?.fecha && <li><strong className="text-gray-800">{globalData.formatId?.includes('restaurante') ? 'Día y hora de la cena:' : 'Límite de entrega:'}</strong> {formatDate(globalData.logistics.fecha)}</li>}
                                                <li><strong className="text-gray-800">Entrega:</strong> {globalData.formatId?.includes('restaurante') ? `Las cartas te estarán esperando en tu mesa del ${globalData.logistics?.restaurante || 'restaurante'} reservada a nombre de ${globalData.logistics?.reserva || 'tu reserva'}.` : globalData.formatId?.includes('mi_casa') || globalData.formatId?.includes('otro') ? `${globalData.logistics?.direccion || ''}${globalData.logistics?.info_adicional_direccion ? ', ' + globalData.logistics.info_adicional_direccion : ''}, ${globalData.logistics?.ciudad_entrega || globalData.logistics?.ciudad_restaurante || ''}` : globalData.logistics?.punto_recogida ? `En el punto de recogida ${globalData.logistics.punto_recogida}` : 'Dirección de envío'}</li>
                                            </>
                                        )}"""

replacement = """                                        {globalData.logistics?.fecha && (
                                            <li>
                                                <strong className="text-gray-800">
                                                    {(globalData.formatId?.includes('restaurante') || globalData.formatId?.includes('reserva') || isDigital) ? 'Hora de la cena:' : 'Límite de entrega:'}
                                                </strong> {formatDate(globalData.logistics.fecha)}
                                            </li>
                                        )}"""

if target in text:
    text = text.replace(target, replacement)
    with open("arbol.html", "w", encoding="utf-8") as f:
        f.write(text)
    print("Replaced delivery details block!")
else:
    print("Target block not found. Trying regex.")

