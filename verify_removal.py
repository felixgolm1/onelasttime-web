with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

checks = {
    'concept-1-section HTML gone': 'id="concept-1-section"' not in text,
    'concept-2-section HTML gone': 'id="concept-2-section"' not in text,
    'initConcept1 call gone': 'initConcept1()' not in text and 'setTimeout(initConcept1' not in text,
    'initConcept2 call gone': 'initConcept2()' not in text,
    'initNeuralCanvas call gone': 'initNeuralCanvas()' not in text,
    'CSS concept-2 gone': '/* --- CONCEPT 2 SECTION --- */' not in text,
    'CSS concept-1 gone': '/* --- CONCEPT 1 SECTION --- */' not in text,
    # Critical things that must still be present
    'concept-3-section still present': 'concept-3-section' in text,
    'animReady still present': 'animReady = true' in text,
    '_runIntroAnim still present': '_runIntroAnim' in text,
}

all_ok = True
for k, v in checks.items():
    status = 'OK' if v else 'FAIL'
    if not v: all_ok = False
    print(f'[{status}] {k}')
print()
print('All OK!' if all_ok else 'SOME CHECKS FAILED')
