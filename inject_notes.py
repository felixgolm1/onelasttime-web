import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                                        </div>
                                    </div>"""

new_block = """                                        </div>
                                    </div>
                                    
                                    <div className="mb-6">
                                        <strong className="text-gray-800 block mb-2">
                                            ¿Quieres que tengamos algo en cuenta para la entrega?
                                        </strong>
                                        <div className="mt-1 flex flex-col gap-1">
                                            <div className={`flex items-center transition-all duration-300 ease-out ${editingContactField === 'notas' ? 'h-[36px]' : 'h-[24px]'}`}>
                                                <div className="relative flex-1 h-full">
                                                    <div className={`absolute left-0 top-0 h-full flex items-center gap-2 transition-all duration-300 ease-out w-full ${editingContactField === 'notas' ? 'opacity-100 translate-x-0 z-10' : 'opacity-0 -translate-x-4 pointer-events-none -z-10'}`}>
                                                        <div className={`flex items-center bg-white rounded-full border border-[#CCFF00] p-1 w-full shadow-sm transition-colors duration-200`}>
                                                            <input type="text" value={editContactData.notas_entrega} onChange={e => { setEditContactData({...editContactData, notas_entrega: e.target.value}); }} onKeyDown={e => { if (e.key === 'Enter') { handleSaveContact(); } if (e.key === 'Escape') { setEditingContactField(null); } }} id="edit-notas-input" className="bg-transparent outline-none text-sm px-2 w-full text-black placeholder-gray-300" placeholder="Escribe aquí..." tabIndex={editingContactField === 'notas' ? 0 : -1} />
                                                            <button onClick={() => { setEditingContactField(null); }} className="text-black hover:text-gray-700 px-1 text-lg leading-none mr-1" title="Cancelar" tabIndex={editingContactField === 'notas' ? 0 : -1}>&times;</button>
                                                            <button onClick={handleSaveContact} className={`rounded-full px-3 py-1 text-xs font-bold whitespace-nowrap transition-all duration-150 bg-[#CCFF00] text-black hover:bg-[#b3e600]`} tabIndex={editingContactField === 'notas' ? 0 : -1}>OK</button>
                                                        </div>
                                                    </div>
                                                    <div className={`absolute left-0 top-0 h-full flex items-center gap-2 group cursor-pointer transition-all duration-300 ease-out ${editingContactField !== 'notas' ? 'opacity-100 translate-x-0 z-10' : 'opacity-0 translate-x-4 pointer-events-none -z-10'}`} onClick={(e) => { setEditingContactField('notas'); setEditContactData({...editContactData, notas_entrega: derivedNotas}); setTimeout(() => document.getElementById('edit-notas-input')?.focus(), 50); }}>
                                                        <p className={`${derivedNotas ? 'text-gray-900 font-medium' : 'text-gray-400 font-medium underline decoration-gray-300 underline-offset-4'}`}>{derivedNotas || 'Añadir nota'}</p>
                                                        <svg className="w-3.5 h-3.5 text-gray-400 group-hover:text-gray-600 transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"></path></svg>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>"""

# Ensure we only replace the FIRST occurrence in Checkout component which is exactly after shipping details
# Wait, "border-t-[1.5px] border-gray-200" is at line 4058. We want the closing div of the flex row at line 4066.

checkout_idx = text.find('h3 className="font-bold text-lg text-gray-900 mb-4">Detalles del envío')
insert_idx = text.find('</div>\n                                    </div>', checkout_idx) + 52

text = text[:insert_idx] + new_block.replace(target, '') + text[insert_idx:]

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Injected notes block!")

