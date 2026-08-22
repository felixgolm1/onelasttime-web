import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

start_idx = text.find("<span className=\"text-gray-500 mr-2\">WhatsApp:</span>")
start_div = text.rfind("<div className=\"flex items-center min-h-[32px]\">", 0, start_idx)
email_idx = text.find("<span className=\"text-gray-500 mr-1\">Email:</span>", start_div)
end_str = "</div>\n                                            </div>\n                                        </li>"
end_div = text.find(end_str, email_idx)

if start_div != -1 and end_div != -1:
    old_block = text[start_div:end_div]
    print("Found block, length:", len(old_block))
    
    new_block = """<div className="flex items-center min-h-[36px]">
                                                    <span className="text-gray-500 mr-2">WhatsApp:</span>
                                                    <div className="relative flex-1 h-[36px]">
                                                        {/* Pill (Edit Mode) */}
                                                        <div className={`absolute left-0 top-0 h-full flex items-center gap-2 transition-all duration-300 ease-out ${editingContactField === 'phone' ? 'opacity-100 translate-x-0 z-10' : 'opacity-0 -translate-x-4 pointer-events-none -z-10'}`}>
                                                            <div className={`flex items-center bg-white rounded-full border p-1 w-full max-w-[220px] shadow-sm transition-colors duration-200 ${!phoneValid ? 'border-red-500' : 'border-[#CCFF00]'} ${shakeContact && !phoneValid ? 'shake' : ''}`}>
                                                                <input type="tel" value={editContactData.phone} onChange={e => { setEditContactData({...editContactData, phone: e.target.value}); setContactErrorMsg(null); }} onKeyDown={e => { if (e.key === 'Enter') handleSaveContact(); if (e.key === 'Escape') { setEditingContactField(null); setContactErrorMsg(null); } }} className="bg-transparent outline-none text-sm px-2 w-full text-black placeholder-gray-300" placeholder="Ej: +34 600..." tabIndex={editingContactField === 'phone' ? 0 : -1} />
                                                                <button onClick={() => { setEditingContactField(null); setContactErrorMsg(null); }} className="text-black hover:text-gray-700 px-1 text-lg leading-none mr-1" title="Cancelar" tabIndex={editingContactField === 'phone' ? 0 : -1}>&times;</button>
                                                                <button onClick={handleSaveContact} className={`rounded-full px-3 py-1 text-xs font-bold whitespace-nowrap transition-colors duration-200 ${!phoneValid ? 'bg-red-500 text-white' : 'bg-[#CCFF00] text-black hover:bg-[#b3e600]'}`} tabIndex={editingContactField === 'phone' ? 0 : -1}>OK</button>
                                                            </div>
                                                            <span className={`text-red-500 text-[10px] sm:text-xs leading-tight whitespace-nowrap transition-opacity duration-200 ${contactErrorMsg && !phoneValid ? 'opacity-100' : 'opacity-0'}`}>{contactErrorMsg}</span>
                                                        </div>
                                                        {/* Text (View Mode) */}
                                                        <div className={`absolute left-0 top-0 h-full flex items-center gap-2 group cursor-pointer transition-all duration-300 ease-out ${editingContactField !== 'phone' ? 'opacity-100 translate-x-0 z-10' : 'opacity-0 translate-x-4 pointer-events-none -z-10'}`} onClick={(e) => { setEditingContactField('phone'); setEditContactData({...editContactData, phone: globalData.contact?.phone || ''}); setContactErrorMsg(null); setTimeout(() => e.currentTarget.parentElement.querySelector('input[type="tel"]')?.focus(), 50); }}>
                                                            <p className="text-gray-900 font-medium">{globalData.contact?.phone || 'No indicado'}</p>
                                                            <svg className="w-3.5 h-3.5 text-gray-400 group-hover:text-gray-600 transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"></path></svg>
                                                        </div>
                                                    </div>
                                                </div>

                                                <div className="flex items-center min-h-[36px]">
                                                    <span className="text-gray-500 mr-2">Email:</span>
                                                    <div className="relative flex-1 h-[36px]">
                                                        {/* Pill (Edit Mode) */}
                                                        <div className={`absolute left-0 top-0 h-full flex items-center gap-2 transition-all duration-300 ease-out ${editingContactField === 'email' ? 'opacity-100 translate-x-0 z-10' : 'opacity-0 -translate-x-4 pointer-events-none -z-10'}`}>
                                                            <div className={`flex items-center bg-white rounded-full border p-1 w-full max-w-[220px] shadow-sm transition-colors duration-200 ${!emailValid ? 'border-red-500' : 'border-[#CCFF00]'} ${shakeContact && !emailValid ? 'shake' : ''}`}>
                                                                <input type="email" value={editContactData.email} onChange={e => { setEditContactData({...editContactData, email: e.target.value}); setContactErrorMsg(null); }} onKeyDown={e => { if (e.key === 'Enter') handleSaveContact(); if (e.key === 'Escape') { setEditingContactField(null); setContactErrorMsg(null); } }} className="bg-transparent outline-none text-sm px-2 w-full text-black placeholder-gray-300" placeholder="tu@email.com" tabIndex={editingContactField === 'email' ? 0 : -1} />
                                                                <button onClick={() => { setEditingContactField(null); setContactErrorMsg(null); }} className="text-black hover:text-gray-700 px-1 text-lg leading-none mr-1" title="Cancelar" tabIndex={editingContactField === 'email' ? 0 : -1}>&times;</button>
                                                                <button onClick={handleSaveContact} className={`rounded-full px-3 py-1 text-xs font-bold whitespace-nowrap transition-colors duration-200 ${!emailValid ? 'bg-red-500 text-white' : 'bg-[#CCFF00] text-black hover:bg-[#b3e600]'}`} tabIndex={editingContactField === 'email' ? 0 : -1}>OK</button>
                                                            </div>
                                                            <span className={`text-red-500 text-[10px] sm:text-xs leading-tight whitespace-nowrap transition-opacity duration-200 ${contactErrorMsg && !emailValid ? 'opacity-100' : 'opacity-0'}`}>{contactErrorMsg}</span>
                                                        </div>
                                                        {/* Text (View Mode) */}
                                                        <div className={`absolute left-0 top-0 h-full flex items-center gap-2 group cursor-pointer transition-all duration-300 ease-out ${editingContactField !== 'email' ? 'opacity-100 translate-x-0 z-10' : 'opacity-0 translate-x-4 pointer-events-none -z-10'}`} onClick={(e) => { setEditingContactField('email'); setEditContactData({...editContactData, email: globalData.contact?.email || ''}); setContactErrorMsg(null); setTimeout(() => e.currentTarget.parentElement.querySelector('input[type="email"]')?.focus(), 50); }}>
                                                            <p className="text-gray-900 font-medium">{globalData.contact?.email || 'No indicado'}</p>
                                                            <svg className="w-3.5 h-3.5 text-gray-400 group-hover:text-gray-600 transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"></path></svg>
                                                        </div>
                                                    </div>
                                                </div>"""

    new_text = text[:start_div] + new_block + "\n" + text[end_div:]
    
    with open("arbol.html", "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Replaced!")
else:
    print("Could not find bounds")
