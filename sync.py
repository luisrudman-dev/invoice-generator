import re

with open('wix-invoice-embed.html', 'r', encoding='utf-8') as f:
    content = f.read()

style_match = re.search(r'<style>([\s\S]*?)</style>', content)
script_match = re.search(r'<script.*?>([\s\S]*?)</script>', content, re.DOTALL)

if style_match and script_match:
    with open('index.css', 'w', encoding='utf-8') as f:
        f.write(style_match.group(1).strip())
    
    with open('index.js', 'w', encoding='utf-8') as f:
        f.write(script_match.group(1).strip())
        
    new_html = content[:style_match.start()] + '<link rel="stylesheet" href="index.css">' + content[style_match.end():script_match.start()] + '<script src="index.js"></script>' + content[script_match.end():]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
