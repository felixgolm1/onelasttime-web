import re

file_path = "arbol.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove the spacer from GlobalHeader
# <div className="w-full transition-all duration-500 ease-in-out flex-shrink-0 pointer-events-none" style={{ height: subtitle ? '22px' : '0px' }} />
content = re.sub(
    r'<div className="w-full transition-all duration-500 ease-in-out flex-shrink-0 pointer-events-none" style={{ height: subtitle \? \'22px\' : \'0px\' }} />',
    '',
    content
)

# 2. Modify App's wrapper to be a flex container and handle the spacer padding
app_wrapper_search = '<div className="w-full relative min-h-screen">'
app_wrapper_replace = """<div className="w-full relative min-h-[100dvh] flex flex-col bg-black">
                    <div className="flex-1 w-full flex flex-col relative transition-all duration-500 ease-in-out" style={{ paddingTop: calculateGlobalSubtitle() ? '22px' : '0px' }}>"""

content = content.replace(app_wrapper_search, app_wrapper_replace)

# Close the wrapper div at the end of App
# We need to find the end of App's return statement.
# App ends around line 2760:
#                     {phase === 'checkout' && <Checkout ... />}
#                 </div>
#             );
app_end_search = """                    {phase === 'checkout' && <Checkout globalData={globalData} progress={getProgress()} onBack={goBackPhase} onComplete={() => advanceTo('success')} />}
                </div>
            );"""
app_end_replace = """                    {phase === 'checkout' && <Checkout globalData={globalData} progress={getProgress()} onBack={goBackPhase} onComplete={() => advanceTo('success')} />}
                    </div>
                </div>
            );"""
content = content.replace(app_end_search, app_end_replace)

# 3. Replace `min-h-screen` and `min-h-[100dvh]` with `flex-1` in all child components
child_replacements = [
    ('className="scene flex-col justify-start pt-28 px-4 pb-16 relative bg-transparent min-h-screen"', 'className="scene flex-1 flex-col justify-start pt-28 px-4 pb-16 relative bg-transparent"'),
    ('className="min-h-screen flex flex-col items-center pt-28 p-6 relative"', 'className="flex-1 flex flex-col items-center pt-28 p-6 relative"'),
    ('className="scene flex-col justify-start pt-28 px-4 relative bg-transparent min-h-screen"', 'className="scene flex-1 flex-col justify-start pt-28 px-4 relative bg-transparent"'),
    ('className="min-h-[100dvh] flex flex-col items-center justify-center p-6 pt-24 fade-in relative"', 'className="flex-1 flex flex-col items-center justify-center p-6 pt-24 fade-in relative"'),
    ('className="w-full min-h-screen flex flex-col pb-[350px] fade-in relative overflow-hidden"', 'className="flex-1 w-full flex flex-col pb-[350px] fade-in relative overflow-hidden"'),
    ('className="min-h-screen flex flex-col items-center pt-28 p-4 relative fade-in"', 'className="flex-1 flex flex-col items-center pt-28 p-4 relative fade-in"'),
    ('className="min-h-screen flex items-center justify-center p-6 fade-in relative"', 'className="flex-1 flex items-center justify-center p-6 fade-in relative"'),
    ('className="min-h-screen py-12 px-6 flex flex-col items-center relative fade-in"', 'className="flex-1 py-12 px-6 flex flex-col items-center relative fade-in"')
]

for old, new in child_replacements:
    content = content.replace(old, new)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Refactor scroll complete.")
