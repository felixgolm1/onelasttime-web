import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                        rightColRef.current.style.setProperty("--box-height", `${rightColRef.current.offsetHeight}px`);"""
replacement = """                        document.documentElement.style.setProperty("--box-height", `${rightColRef.current.offsetHeight}px`);"""
text = text.replace(target, replacement)

# We also need to fix the useEffect dependencies so it re-runs if it needs to, but ResizeObserver is better.
# Let's add a ResizeObserver to be absolutely bulletproof.
target_useeffect = """            React.useEffect(() => {
                if (rightColRef.current) {
                    const updateHeight = () => {
                        document.documentElement.style.setProperty("--box-height", `${rightColRef.current.offsetHeight}px`);
                    };
                    updateHeight();
                    window.addEventListener("resize", updateHeight);
                    return () => window.removeEventListener("resize", updateHeight);
                }
            }, [globalData]);"""

replacement_useeffect = """            React.useEffect(() => {
                const el = rightColRef.current;
                if (!el) return;
                
                const updateHeight = () => {
                    document.documentElement.style.setProperty("--box-height", `${el.offsetHeight}px`);
                };
                
                updateHeight();
                
                const observer = new ResizeObserver(() => {
                    updateHeight();
                });
                observer.observe(el);
                
                return () => {
                    observer.disconnect();
                };
            }, []);"""
text = text.replace(target_useeffect, replacement_useeffect)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated to use ResizeObserver and document.documentElement")
