import os
import re

def get_chapter_title(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            # Remove markdown header markers
            return first_line.replace('# ', '').replace('`', '').strip()
    except:
        return os.path.basename(filepath)

def sort_key(filename):
    # Extract number from filename chXXX
    match = re.search(r'ch(\d+)', filename)
    if match:
        return int(match.group(1))
    return 9999

drafts_dir = '/workspaces/WenDao-Legend/drafts'
output_file = '/workspaces/WenDao-Legend/FINAL_TOC.md'

toc = ["# 《文道传说》- 全书目录\n"]
toc.append("> **万世开太平**\n")

volumes = {
    'volume_01': '第一卷：潜龙勿用',
    'volume_02': '第二卷：江湖远',
    'volume_03': '第三卷：绝地天通',
    'volume_04': '第四卷：万世开太平'
}

for vol_dir in sorted(volumes.keys()):
    full_vol_dir = os.path.join(drafts_dir, vol_dir)
    if not os.path.exists(full_vol_dir):
        continue
    
    vol_name = volumes.get(vol_dir, vol_dir)
    toc.append(f"## {vol_name}\n")
    
    files = [f for f in os.listdir(full_vol_dir) if f.startswith('ch') and f.endswith('.md')]
    files.sort(key=sort_key)
    
    for file in files:
        if 'outline' in file: continue
        path = os.path.join(full_vol_dir, file)
        title = get_chapter_title(path)
        # Link format: [Title](path)
        rel_path = f"drafts/{vol_dir}/{file}"
        toc.append(f"- [{title}]({rel_path})")
    
    toc.append("\n")

with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(toc))

print("TOC Generated Successfully")
