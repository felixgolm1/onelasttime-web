import json
import re

paths = [
    r'c:\Users\Félix Gol\.gemini\antigravity\brain\69ca0832-5ae7-40fd-a8ae-abac65e873b0\.system_generated\logs\overview.txt',
    r'c:\Users\Félix Gol\.gemini\antigravity\brain\a2fbe4e1-b1eb-4f33-9257-8d838b3e1e5a\.system_generated\logs\overview.txt'
]

results = []
for p in paths:
    with open(p, 'r', encoding='utf-8') as f:
        for line in f:
            if 'replace_file_content' in line or 'multi_replace_file_content' in line:
                try:
                    data = json.loads(line)
                    if 'tool_calls' in data:
                        for call in data['tool_calls']:
                            if call['name'] in ['replace_file_content', 'multi_replace_file_content']:
                                args = call['args']
                                if '3d-test.html' in str(args.get('TargetFile', '')):
                                    if call['name'] == 'replace_file_content':
                                        content = args.get('ReplacementContent', '')
                                        if 'review-panel' in content or 'oryzo-review' in content or 'story' in content or 'elsa-scroll-video' in content:
                                            results.append(content)
                                    elif call['name'] == 'multi_replace_file_content':
                                        chunks_str = args.get('ReplacementChunks', '[]')
                                        chunks = json.loads(chunks_str)
                                        for chunk in chunks:
                                            content = chunk.get('ReplacementContent', '')
                                            if 'review-panel' in content or 'oryzo-review' in content or 'story' in content or 'elsa-scroll-video' in content:
                                                results.append(content)
                except Exception as e:
                    pass

with open('extracted_snippets.txt', 'w', encoding='utf-8') as f:
    for i, res in enumerate(results):
        f.write(f"=== SNIPPET {i} ===\n{res}\n\n")

print(f"Extracted {len(results)} snippets.")
