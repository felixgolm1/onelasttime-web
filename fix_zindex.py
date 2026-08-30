import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """<div className="flex-1 py-12 px-6 flex flex-col items-center relative fade-in">"""
replacement = """<div className="flex-1 py-12 px-6 flex flex-col items-center relative fade-in z-[38]">"""
text = text.replace(target, replacement)

# And revert the right column back to just top-[152px] and remove the JS complexity
target_col = """                        <div 
                            ref={rightColRef}
                            className="space-y-8 bg-white rounded-[2rem] p-6 md:p-8 border border-gray-200 shadow-[0_20px_50px_rgba(0,0,0,0.05)] h-fit md:sticky self-start relative z-40 transition-all duration-300"
                            style={{ top: 'min(152px, calc(100vh - var(--box-height, 0px) - 32px))' }}
                        >"""
replacement_col = """                        <div className="space-y-8 bg-white rounded-[2rem] p-6 md:p-8 border border-gray-200 shadow-[0_20px_50px_rgba(0,0,0,0.05)] h-fit md:sticky md:top-[152px] self-start relative z-40 transition-all duration-300">"""
text = text.replace(target_col, replacement_col)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated Checkout z-index and reverted to simple sticky top-152px")
