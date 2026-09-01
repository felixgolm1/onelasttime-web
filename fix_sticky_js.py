import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                        {/* COLUMNA DERECHA: RESUMEN */}
                        <div className="space-y-8 bg-white rounded-[2rem] p-6 md:p-8 border border-gray-200 shadow-[0_20px_50px_rgba(0,0,0,0.05)] h-fit md:sticky md:top-[152px] self-start relative z-40">"""

replacement = """                        {/* COLUMNA DERECHA: RESUMEN */}
                        <div 
                            ref={rightColRef}
                            className="space-y-8 bg-white rounded-[2rem] p-6 md:p-8 border border-gray-200 shadow-[0_20px_50px_rgba(0,0,0,0.05)] h-fit md:sticky self-start relative z-40 transition-all duration-300"
                            style={{ top: 'min(152px, calc(100vh - var(--box-height, 0px) - 32px))' }}
                        >"""

target_ref = """        const Checkout = ({ globalData, setGlobalData, progress, onBack }) => {
            useEffect(() => { window.scrollTo(0, 0); }, []);"""

replacement_ref = """        const Checkout = ({ globalData, setGlobalData, progress, onBack }) => {
            useEffect(() => { window.scrollTo(0, 0); }, []);
            const rightColRef = React.useRef(null);
            React.useEffect(() => {
                if (rightColRef.current) {
                    const updateHeight = () => {
                        rightColRef.current.style.setProperty("--box-height", `${rightColRef.current.offsetHeight}px`);
                    };
                    updateHeight();
                    window.addEventListener("resize", updateHeight);
                    return () => window.removeEventListener("resize", updateHeight);
                }
            }, [globalData]);"""

text = text.replace(target, replacement)
text = text.replace(target_ref, replacement_ref)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Implemented JS height tracker for perfect sticky bottom!")

