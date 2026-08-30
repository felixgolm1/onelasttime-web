import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Restore the blur mask height to 130px instead of 180px
text = re.sub(r'\.top-blur-mask \{\s*position: fixed;\s*top: 0;\s*left: 0;\s*width: 100%;\s*height: 180px;', 
              r'.top-blur-mask {\n            position: fixed;\n            top: 0;\n            left: 0;\n            width: 100%;\n            height: 130px;', text)

# 2. Remove z-[38] from Checkout container
text = text.replace('<div className="flex-1 py-12 px-6 flex flex-col items-center relative fade-in z-[38]">', 
                    '<div className="flex-1 py-12 px-6 flex flex-col items-center relative fade-in">')

# 3. Restore the React ResizeObserver for the right box height (safest way to get dynamic height)
target_useeffect = """                const handleScroll = () => {
                    const container = el.parentElement;
                    if (!container) return;
                    
                    const containerRect = container.getBoundingClientRect();
                    const elHeight = el.offsetHeight;
                    const viewportHeight = window.innerHeight;
                    
                    // We want the element to stick such that its bottom is 32px from the viewport bottom
                    // Target Y relative to viewport: viewportHeight - elHeight - 32
                    // But it shouldn't go higher than its initial position (which is 152px from viewport top when container is at 104px margin)
                    
                    // Calculate how far the container has scrolled up
                    // When container top is at 152px (initial), offset should be 0
                    const initialContainerTop = 152; 
                    const scrollY = initialContainerTop - containerRect.top;
                    
                    if (scrollY > 0) {
                        // The container has scrolled up by `scrollY` pixels
                        // We want to translate the element down by `scrollY` to keep it sticky at the top
                        // BUT we want to delay the stickiness so it scrolls up a bit first!
                        // Let's let it scroll up until its bottom hits the bottom of the viewport
                        
                        const elementBottomInViewport = containerRect.top + elHeight;
                        const targetBottom = viewportHeight - 32;
                        
                        if (elementBottomInViewport < targetBottom) {
                            // Element needs to be pushed down to keep its bottom at targetBottom
                            let pushDown = targetBottom - elementBottomInViewport;
                            
                            // Don't push down more than the container's available height
                            const maxPush = containerRect.height - elHeight;
                            pushDown = Math.min(pushDown, maxPush);
                            pushDown = Math.max(0, pushDown);
                            
                            el.style.transform = `translateY(${pushDown}px)`;
                        } else {
                            el.style.transform = `translateY(0px)`;
                        }
                    } else {
                        el.style.transform = `translateY(0px)`;
                    }
                };
                
                window.addEventListener('scroll', handleScroll, { passive: true });
                window.addEventListener('resize', handleScroll);
                handleScroll();
                
                return () => {
                    window.removeEventListener('scroll', handleScroll);
                    window.removeEventListener('resize', handleScroll);
                };"""

replacement_useeffect = """                const updateHeight = () => {
                    document.documentElement.style.setProperty("--box-height", `${el.offsetHeight}px`);
                };
                
                updateHeight();
                
                const observer = new ResizeObserver(() => {
                    updateHeight();
                });
                observer.observe(el);
                
                return () => {
                    observer.disconnect();
                };"""
text = text.replace(target_useeffect, replacement_useeffect)

# 4. Restore the CSS sticky min() logic
target_col = """                        <div 
                            ref={rightColRef}
                            className="space-y-8 bg-white rounded-[2rem] p-6 md:p-8 border border-gray-200 shadow-[0_20px_50px_rgba(0,0,0,0.05)] h-fit self-start relative z-40"
                            style={{ willChange: 'transform' }}
                        >"""
replacement_col = """                        <div 
                            ref={rightColRef}
                            className="space-y-8 bg-white rounded-[2rem] p-6 md:p-8 border border-gray-200 shadow-[0_20px_50px_rgba(0,0,0,0.05)] h-fit md:sticky self-start relative z-40 transition-all duration-300"
                            style={{ top: 'min(152px, calc(100vh - var(--box-height, 0px) - 32px))' }}
                        >"""
text = text.replace(target_col, replacement_col)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Implemented final perfect solution")
