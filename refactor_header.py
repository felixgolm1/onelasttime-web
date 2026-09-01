import re

file_path = "arbol.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove all <GlobalHeader ... /> from everywhere EXCEPT we will add it to App
content = re.sub(r'<GlobalHeader[^>]*/>', '', content)

# 2. Add backRef to TreeEngine
content = content.replace(
    "const TreeEngine = ({ initialTitle, data, onComplete, onProgressUpdate, treeKey, treeStates, setTreeStates }) => {",
    "const TreeEngine = ({ initialTitle, data, onComplete, onProgressUpdate, treeKey, treeStates, setTreeStates, backRef }) => {"
)
# Add useEffect for backRef
content = content.replace(
    "const handleBack = () => {",
    "React.useEffect(() => { if (backRef) backRef.current = handleBack; return () => { if (backRef) backRef.current = null; }; }, [history.length, currentParent]);\n            const handleBack = () => {"
)

# 3. Add backRef to LogisticsForm
content = content.replace(
    "const LogisticsForm = ({ contextId, initialData, onComplete, progress, onBack, onSwitchToDigital }) => {",
    "const LogisticsForm = ({ contextId, initialData, onComplete, onBack, onSwitchToDigital, backRef }) => {"
)
content = content.replace(
    "const handleBack = () => {",
    "React.useEffect(() => { if (backRef) backRef.current = handleBack; return () => { if (backRef) backRef.current = null; }; }, [stepIndex, subStep]);\n            const handleBack = () => {"
)

# 4. Add backRef to CustomizationN4
content = content.replace(
    "const CustomizationN4 = ({ onComplete, onBack, globalData, progress }) => {",
    "const CustomizationN4 = ({ onComplete, onBack, globalData, backRef }) => {"
)
content = content.replace(
    "const handlePrevSubStep = () => {",
    "React.useEffect(() => { if (backRef) backRef.current = handlePrevSubStep; return () => { if (backRef) backRef.current = null; }; }, [subStep]);\n            const handlePrevSubStep = () => {"
)

# 5. In App, insert globalBackRef and calculateGlobalSubtitle
app_state_injection = """            const globalBackRef = React.useRef(null);
            const calculateGlobalSubtitle = () => {
                if (phase === 'format') {
                    if (!treeStates.format.currentParent && treeStates.format.history.length === 0) return '';
                    const rootSelection = treeStates.format.history[0] || treeStates.format.currentParent;
                    if (rootSelection?.includes('cartas_digitales')) return 'Versión digital';
                    else if (rootSelection?.includes('cartas_fisicas')) return 'Versión física';
                }
                return undefined;
            };
            """
content = content.replace(
    "const [treeStates, setTreeStates] = useState(() => JSON.parse(sessionStorage.getItem('dev_treeStates')) || {",
    app_state_injection + "const [treeStates, setTreeStates] = useState(() => JSON.parse(sessionStorage.getItem('dev_treeStates')) || {"
)

# 6. In App return, insert GlobalHeader
app_header_injection = """
                    {phase !== 'intro' && (
                        <GlobalHeader 
                            progress={getProgress()} 
                            onBack={() => { if (globalBackRef.current) globalBackRef.current(); else goBackPhase(); }} 
                            animateIn={phase === 'format' && treeStates.format.history.length === 0} 
                            overrideSubtitle={calculateGlobalSubtitle()} 
                        />
                    )}
"""
content = content.replace(
    "{/* HACK: preload bg */}",
    "{/* HACK: preload bg */}" + app_header_injection
)

# 7. Add backRef prop to TreeEngine, LogisticsForm, CustomizationN4 in App render
content = content.replace(
    "setTreeStates={setTreeStates}",
    "setTreeStates={setTreeStates} backRef={globalBackRef}"
)
content = content.replace(
    "<LogisticsForm key={globalData.formatId}",
    "<LogisticsForm backRef={globalBackRef} key={globalData.formatId}"
)
content = content.replace(
    "<CustomizationN4 globalData={globalData}",
    "<CustomizationN4 backRef={globalBackRef} globalData={globalData}"
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Refactor complete.")
