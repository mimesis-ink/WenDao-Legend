import os
import re

drafts_dir = 'drafts/volume_01'

files = sorted([f for f in os.listdir(drafts_dir) if f.endswith('.md')])

header_pattern = re.compile(r'^#\s+(.*)', re.MULTILINE)

print(f"{'Filename':<35} | {'Header Content'}")
print("-" * 80)

for filename in files:
    if 'outline' in filename or 'chapter_list' in filename or 'chapter_status' in filename:
        continue
        
    filepath = os.path.join(drafts_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    headers = header_pattern.findall(content)
    if headers:
        header_text = headers[0].strip()
        print(f"{filename:<35} | {header_text}")
        if len(headers) > 1:
             print(f"{' ':<35} | WARNING: {len(headers)} headers found!")
             for h in headers[1:]:
                 print(f"{' ':<35} |   {h.strip()}")
    else:
        print(f"{filename:<35} | NO HEADER")
