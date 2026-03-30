import os, json

lang = "zh"
merged = {}

def _load_locales_from_dir(base_dir):
    print(f"Scanning: {base_dir}")
    if not os.path.isdir(base_dir):
        print("  -> Not a directory")
        return
    for entry in os.listdir(base_dir):
        ext_dir = os.path.join(base_dir, entry)
        if not os.path.isdir(ext_dir):
            continue
        locales_dir = os.path.join(ext_dir, "locales")
        if not os.path.isdir(locales_dir):
            print(f"  [{entry}] NO locales dir")
            continue
        print(f"  [{entry}] Found locales dir!")
        for try_lang in [lang, "en"]:
            locale_path = os.path.join(locales_dir, f"{try_lang}.json")
            if os.path.isfile(locale_path):
                print(f"    -> Found {try_lang}.json")
                try:
                    with open(locale_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    merged.update(data)
                    print(f"    -> Loaded {len(data)} keys")
                except Exception as e:
                    print(f"    -> ERROR parsing JSON: {e}")
                break

builtin_ext_dir = os.path.join(r"C:\tubecreate-vue\zhiying\zhiying", "extensions")
_load_locales_from_dir(builtin_ext_dir)

from zhiying.config import EXTENSIONS_EXTERNAL_DIR
_load_locales_from_dir(str(EXTENSIONS_EXTERNAL_DIR))

print(f"\nTotal merged keys: {len(merged)}")
