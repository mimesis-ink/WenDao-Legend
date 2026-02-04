import sys
import os

filename = sys.argv[1]
content = sys.stdin.read()

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully wrote to {filename}")
