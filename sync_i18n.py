"""
ZhiYing ↔ TubeCLI Sync Script
Syncs locales folders and static files between zhiying (dev) and tubecli (prod).
"""
import os
import shutil

ZHIYING_BASE = r"C:\tubecreate-vue\zhiying\zhiying"
TUBECLI_BASE = r"C:\tubecreate-vue\tubecli\tubecli"

ZHIYING_STATIC = os.path.join(ZHIYING_BASE, "extensions", "webui", "static")
TUBECLI_STATIC = os.path.join(TUBECLI_BASE, "extensions", "webui", "static")

def sync_file(src, dst):
    """Copy a single file, creating parent dirs as needed."""
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        print(f"  ✓ {os.path.basename(dst)}")

def sync_locales(ext_name):
    """Sync locales/ folder for a core extension."""
    src_dir = os.path.join(ZHIYING_BASE, "extensions", ext_name, "locales")
    dst_dir = os.path.join(TUBECLI_BASE, "extensions", ext_name, "locales")
    if os.path.isdir(src_dir):
        shutil.rmtree(dst_dir, ignore_errors=True)
        os.makedirs(dst_dir, exist_ok=True)
        for fname in os.listdir(src_dir):
            if fname.endswith(".json"):
                shutil.copy2(os.path.join(src_dir, fname), os.path.join(dst_dir, fname))
        print(f"  ✓ {ext_name}/locales/ ({len(os.listdir(dst_dir))} files)")


# ── 1. Sync WebUI static files ──────────────────────────────────────
print("📁 Syncing WebUI static files...")
for filename in [
    "i18n.js", "app.js", "market.html", "market.js", "market.css", "index.html", "style.css",
    "story.html", "story_player.js", "story_editor.js", "story_bubbles.js",
    "studio.html", "teams3d.js", "furniture3d.js"
]:
    sync_file(
        os.path.join(ZHIYING_STATIC, filename),
        os.path.join(TUBECLI_STATIC, filename),
    )

# Remove old static/i18n/ folder from tubecli if it exists
old_i18n = os.path.join(TUBECLI_STATIC, "i18n")
if os.path.isdir(old_i18n):
    shutil.rmtree(old_i18n)
    print("  ✓ Removed old static/i18n/ folder")


# ── 2. Sync locales/ for all core extensions ────────────────────────
print("\n🌐 Syncing extension locales...")
CORE_EXTENSIONS = [
    "webui", "market", "browser", "cloud_api",
    "ollama_manager", "multi_agents", "downloader",
    "studio3d", "auth_manager",
]
for ext_name in CORE_EXTENSIONS:
    sync_locales(ext_name)


# ── 3. Sync server.py (API) ─────────────────────────────────────────
print("\n🔧 Syncing API server...")
sync_file(
    os.path.join(ZHIYING_BASE, "api", "server.py"),
    os.path.join(TUBECLI_BASE, "api", "server.py"),
)


# ── 4. Sync video_editor external extension ─────────────────────────
print("\n📦 Syncing external extensions...")
zhiying_editor = r"C:\tubecreate-vue\zhiying\data\extensions_external\video_editor\static"
tubecli_editor = r"C:\tubecreate-vue\tubecli\data\extensions_external\video_editor\static"
if os.path.exists(zhiying_editor) and os.path.exists(tubecli_editor):
    sync_file(os.path.join(zhiying_editor, "editor.html"), os.path.join(tubecli_editor, "editor.html"))
    sync_file(os.path.join(zhiying_editor, "editor.js"), os.path.join(tubecli_editor, "editor.js"))


print("\n✅ All synced successfully!")
