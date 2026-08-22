import os
import re
import urllib.request
import urllib.parse
from pathlib import Path

content_file = r'C:\Users\M\.gemini\antigravity-ide\brain\b9a15039-2520-4ef8-8fa4-bcce8cda1311\.system_generated\steps\282\content.md'
out_dir = Path('src/assets/images/scraped')
out_dir.mkdir(parents=True, exist_ok=True)

with open(content_file, 'r', encoding='utf-8') as f:
    text = f.read()

# Find all href and src that look like images
img_urls = re.findall(r'(?:src|href)="([^"]+\.(?:jpg|png|jpeg|svg|webp)[^"]*|https://images.unsplash.com/[^"]+)"', text)
# Add some manually from the scraped text if needed, but the regex should catch unsplash ones
img_urls = [u.replace('&amp;', '&') for u in img_urls]
# filter unique
img_urls = list(set(img_urls))

for i, url in enumerate(img_urls):
    if not url.startswith('http'):
        if url.startswith('/'):
            url = 'https://internationalestimating.com' + url
        else:
            url = 'https://internationalestimating.com/' + url
    
    # Try to extract a meaningful name or use index
    if 'unsplash' in url:
        name = url.split('/')[-1].split('?')[0] + '.jpg'
    else:
        name = url.split('/')[-1].split('?')[0]
        if not name.endswith(('.jpg', '.png', '.svg', '.jpeg')):
            name += '.png'
            
    print(f"Downloading {url} to {name}")
    try:
        urllib.request.urlretrieve(url, out_dir / name)
    except Exception as e:
        print(f"Failed to download {url}: {e}")

print("Done downloading images.")
