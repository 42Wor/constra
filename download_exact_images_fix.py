import os
import re
import urllib.request
import urllib.parse
from pathlib import Path

content_file = r'C:\Users\M\.gemini\antigravity-ide\brain\b9a15039-2520-4ef8-8fa4-bcce8cda1311\.system_generated\steps\285\content.md'
out_dir = Path('src/assets/images/scraped')
out_dir.mkdir(parents=True, exist_ok=True)

with open(content_file, 'r', encoding='utf-8') as f:
    text = f.read()

img_urls = re.findall(r'(?:src|href)="([^"]+\.(?:jpg|png|jpeg|svg|webp)[^"]*)"', text)
img_urls = [u.replace('&amp;', '&') for u in img_urls]
img_urls = list(set(img_urls))

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

for i, url in enumerate(img_urls):
    if not url.startswith('http'):
        if url.startswith('/'):
            url = 'https://exactestimation.com' + url
        else:
            url = 'https://exactestimation.com/' + url
    
    name = url.split('/')[-1].split('?')[0]
    if not name.endswith(('.jpg', '.png', '.svg', '.jpeg')):
        name += '.png'
            
    print(f"Downloading {url} to {name}")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(out_dir / name, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
    except Exception as e:
        print(f"Failed to download {url}: {e}")

print("Done downloading Exact Estimation images.")
