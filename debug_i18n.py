"""Direct test - manually scan extension dirs"""
import os, json

EXTENSIONS_BASE = r'C:\tubecreate-vue\zhiying\zhiying\extensions'
lang = 'zh'
merged = {}

for ext_name in os.listdir(EXTENSIONS_BASE):
    ext_dir = os.path.join(EXTENSIONS_BASE, ext_name)
    if not os.path.isdir(ext_dir):
        continue
    locales_dir = os.path.join(ext_dir, 'locales')
    if not os.path.isdir(locales_dir):
        continue
    
    locale_path = os.path.join(locales_dir, f'{lang}.json')
    if os.path.isfile(locale_path):
        with open(locale_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        merged.update(data)
        print(f"  {ext_name}: {len(data)} keys")

print(f"\nTotal merged keys: {len(merged)}")
print(f"market.title = {merged.get('market.title', 'MISSING')}")
print(f"nav.dashboard = {merged.get('nav.dashboard', 'MISSING')}")
