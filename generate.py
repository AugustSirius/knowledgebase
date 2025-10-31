#!/usr/bin/env python3
import os, re, json

# 扫描所有.md文件
files = []
for root, dirs, filenames in os.walk('.'):
    for f in filenames:
        if f.endswith('.md'):
            path = os.path.join(root, f)[2:]  # 去掉 ./
            name = f[:-3]  # 去掉 .md
            files.append({'path': path.replace('\\', '/'), 'name': name})

# 生成JS数组
js = 'const files = ' + json.dumps(files, ensure_ascii=False, indent=12).replace('\n', '\n        ') + ';'

# 更新index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'const files = \[.*?\];', js, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'✅ 找到 {len(files)} 个文件，已更新 index.html')