import os
import glob
import re

def count_chars(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 移除 Markdown 标记的一些简单处理，避免标题等占用过多字数
    # 去掉所有 # (标题)
    content = re.sub(r'#+\s*', '', content)
    # 去掉 ** (加粗)
    content = re.sub(r'\*\*', '', content)
    # 去掉链接
    content = re.sub(r'\[.*?\]\(.*?\)', '', content)
    
    # 统计中文、英文、数字
    # 这个正则匹配所有非空白字符，但我们主要关心实际阅读字数
    # 简单统计：中文算1，英文单词算1（或者简单算字符）
    # 为了保险起见，我们统计所有可见字符，但通常网文统计是汉字数+标点
    
    # 移除空白字符
    clean_content = re.sub(r'\s', '', content)
    return len(clean_content)

directory = '/workspaces/WenDao-Legend/drafts/volume_03'
files = glob.glob(os.path.join(directory, 'ch*.md'))
files.sort()

under_limit = []

print(f"{'File Name':<40} | {'Count':<10}")
print("-" * 55)

for file_path in files:
    filename = os.path.basename(file_path)
    count = count_chars(file_path)
    print(f"{filename:<40} | {count:<10}")
    if count < 2000:
        under_limit.append((file_path, count))

print("-" * 55)
print(f"Total files under 2000 chars: {len(under_limit)}")
if len(under_limit) > 0:
    print("Files to expand:")
    for f, c in under_limit:
        print(f"{os.path.basename(f)}: {c}")
