import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Add state variable
state_line = "            const [hasSelectedPaymentMethod, setHasSelectedPaymentMethod] = useState(false);\n            const [showOrderDetails, setShowOrderDetails] = useState(false);"
text = text.replace("            const [hasSelectedPaymentMethod, setHasSelectedPaymentMethod] = useState(false);", state_line)


# 2. Replace the HTML block
old_block = """                                <div className="rounded-xl bg-gray-50/50 py-4">
                                    <h3 className="text-lg font-bold text-black mb-4">Detalles del pedido</h3>
                                    <ul className="space-y-3 text-sm text-gray-600">"""

new_block = """                                <div className="rounded-xl bg-gray-50/50">
                                    <button 
                                        onClick={() => setShowOrderDetails(!showOrderDetails)} 
                                        className="w-full flex justify-between items-center py-4 px-4 outline-none hover:bg-gray-100/50 rounded-xl transition-colors"
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
                                        <div className="px-4 pb-4">
                                            <ul className="space-y-3 text-sm text-gray-600">"""

if old_block in text:
    text = text.replace(old_block, new_block)
    
    # We also need to close the extra div for the content wrapper!
    # Let's find where the </ul> is closed for this block
    # It ends with:
    #                                         </li>
    #                                     </ul>
    #                                 </div>
    
    end_block = """                                        </li>
                                    </ul>
                                </div>"""
    
    new_end = """                                        </li>
                                    </ul>
                                        </div>
                                    </div>
                                </div>"""
                                
    text = text.replace(end_block, new_end)
    
    with open("arbol.html", "w", encoding="utf-8") as f:
        f.write(text)
    print("Updated accordion!")
else:
    print("Old block not found")

