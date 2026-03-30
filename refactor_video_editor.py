import os
import json
import re

html_path = r"C:\tubecreate-vue\zhiying\data\extensions_external\video_editor\static\editor.html"
i18n_dir = r"C:\tubecreate-vue\zhiying\data\extensions_external\video_editor\static\i18n"
os.makedirs(i18n_dir, exist_ok=True)

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# I18N maps
zh = {
    "nav.title": "视频编辑器",
    "nav.new": "新建",
    "nav.open": "打开",
    "nav.export": "导出",
    "status.checking": "检查 FFmpeg 中...",
    "tab.media": "媒体库",
    "tab.effects": "特效",
    "tab.text": "文本",
    "tab.audio": "音频",
    "media.upload": "上传媒体",
    "media.drop": "拖拽文件到此处<br><small>或点击浏览文件</small>",
    "effects.title": "视频特效",
    "text.title": "文本叠加",
    "text.content": "文本内容",
    "text.placeholder": "输入文字...",
    "text.size": "字体大小",
    "text.color": "文字颜色",
    "text.position": "位置",
    "text.add": "添加文字叠加",
    "audio.title": "音频",
    "audio.empty": "请先在“媒体库”选项卡上传音频文件。",
    "preview.placeholder": "上传视频开始创作",
    "props.title": "属性",
    "props.empty": "选择素材以查看属性",
    "modal.export.title": "📤 导出视频",
    "modal.export.source": "源文件",
    "modal.export.format": "导出格式",
    "modal.export.quality": "画质",
    "modal.export.res": "分辨率",
    "modal.export.fps": "帧率 (FPS)",
    "modal.export.start": "开始导出",
    "modal.export.cancel": "取消",
    "modal.projects.title": "📁 项目列表",
    "modal.projects.loading": "正在加载项目...",
    "modal.projects.close": "关闭"
}

en = {
    "nav.title": "Video Editor",
    "nav.new": "New",
    "nav.open": "Open",
    "nav.export": "Export",
    "status.checking": "Checking FFmpeg...",
    "tab.media": "Media",
    "tab.effects": "Effects",
    "tab.text": "Text",
    "tab.audio": "Audio",
    "media.upload": "Upload Media",
    "media.drop": "Drag & drop files here<br><small>or click to browse</small>",
    "effects.title": "Video Effects",
    "text.title": "Text Overlay",
    "text.content": "Text Content",
    "text.placeholder": "Enter text...",
    "text.size": "Font Size",
    "text.color": "Color",
    "text.position": "Position",
    "text.add": "Add Text Overlay",
    "audio.title": "Audio",
    "audio.empty": "Upload audio files from the Media tab to add them here.",
    "preview.placeholder": "Upload a video to get started",
    "props.title": "Properties",
    "props.empty": "Select a clip to view properties",
    "modal.export.title": "📤 Export Video",
    "modal.export.source": "Source File",
    "modal.export.format": "Format",
    "modal.export.quality": "Quality",
    "modal.export.res": "Resolution",
    "modal.export.fps": "FPS",
    "modal.export.start": "Start Export",
    "modal.export.cancel": "Cancel",
    "modal.projects.title": "📁 Projects",
    "modal.projects.loading": "Loading projects...",
    "modal.projects.close": "Close"
}

vi = {
    "nav.title": "Trình sửa Video",
    "nav.new": "Tạo mới",
    "nav.open": "Mở",
    "nav.export": "Xuất",
    "status.checking": "Đang kiểm tra FFmpeg...",
    "tab.media": "Thư viện Media",
    "tab.effects": "Hiệu ứng",
    "tab.text": "Văn bản",
    "tab.audio": "Âm thanh",
    "media.upload": "Tải lên Media",
    "media.drop": "Kéo thả file vào đây<br><small>hoặc click để chọn</small>",
    "effects.title": "Hiệu ứng Video",
    "text.title": "Chèn văn bản",
    "text.content": "Nội dung chữ",
    "text.placeholder": "Nhập văn bản...",
    "text.size": "Cỡ chữ",
    "text.color": "Màu sắc",
    "text.position": "Vị trí",
    "text.add": "Chèn văn bản",
    "audio.title": "Âm thanh",
    "audio.empty": "Upload file âm thanh ở tab Media trước.",
    "preview.placeholder": "Tải video lên để bắt đầu",
    "props.title": "Thuộc tính",
    "props.empty": "Chọn một clip để xem thuộc tính",
    "modal.export.title": "📤 Xuất Video",
    "modal.export.source": "Nguồn Video",
    "modal.export.format": "Định dạng",
    "modal.export.quality": "Chất lượng",
    "modal.export.res": "Độ phân giải",
    "modal.export.fps": "FPS",
    "modal.export.start": "Bắt đầu xuất",
    "modal.export.cancel": "Hủy",
    "modal.projects.title": "📁 Dự án",
    "modal.projects.loading": "Đang tải...",
    "modal.projects.close": "Đóng"
}

# Write JSONs
with open(os.path.join(i18n_dir, "zh.json"), "w", encoding="utf-8") as f:
    json.dump(zh, f, ensure_ascii=False, indent=2)
with open(os.path.join(i18n_dir, "en.json"), "w", encoding="utf-8") as f:
    json.dump(en, f, ensure_ascii=False, indent=2)
with open(os.path.join(i18n_dir, "vi.json"), "w", encoding="utf-8") as f:
    json.dump(vi, f, ensure_ascii=False, indent=2)

# Replacements in HTML
reps = [
    ('<span class="nav-title">Video Editor</span>', '<span class="nav-title" data-i18n="nav.title">Video Editor</span>'),
    ('New\n            </button>', '<span data-i18n="nav.new">New</span>\n            </button>'),
    ('Open\n            </button>', '<span data-i18n="nav.open">Open</span>\n            </button>'),
    ('Export\n            </button>', '<span data-i18n="nav.export">Export</span>\n            </button>'),
    ('<span class="status-text">Checking FFmpeg...</span>', '<span class="status-text" data-i18n="status.checking">Checking FFmpeg...</span>'),
    ('<span>Media</span>', '<span data-i18n="tab.media">Media</span>'),
    ('<span>Effects</span>', '<span data-i18n="tab.effects">Effects</span>'),
    ('<span>Text</span>', '<span data-i18n="tab.text">Text</span>'),
    ('<span>Audio</span>', '<span data-i18n="tab.audio">Audio</span>'),
    ('<h3 id="propsTitle">Properties</h3>', '<h3 id="propsTitle" data-i18n="props.title">Properties</h3>'),
    ('<h3>Media Library</h3>', '<h3 data-i18n="tab.media">Media Library</h3>'),
    ('<p>Drag & drop files here<br><small>or click to browse</small></p>', '<p data-i18n="media.drop">Drag & drop files here<br><small>or click to browse</small></p>'),
    ('<h3>Video Effects</h3>', '<h3 data-i18n="effects.title">Video Effects</h3>'),
    ('<h3>Text Overlay</h3>', '<h3 data-i18n="text.title">Text Overlay</h3>'),
    ('<label>Text Content</label>', '<label data-i18n="text.content">Text Content</label>'),
    ('placeholder="Enter text..."', 'data-i18n-placeholder="text.placeholder" placeholder="Enter text..."'),
    ('<label>Font Size</label>', '<label data-i18n="text.size">Font Size</label>'),
    ('<label>Color</label>', '<label data-i18n="text.color">Color</label>'),
    ('<label>Position</label>', '<label data-i18n="text.position">Position</label>'),
    ('btnAddText">Add Text Overlay', 'btnAddText" data-i18n="text.add">Add Text Overlay'),
    ('<h3>Audio</h3>', '<h3 data-i18n="audio.title">Audio</h3>'),
    ('<p class="empty-state">Upload audio files from the Media tab to add them here.</p>', '<p class="empty-state" data-i18n="audio.empty">Upload audio files from the Media tab to add them here.</p>'),
    ('<p>Upload a video to get started</p>', '<p data-i18n="preview.placeholder">Upload a video to get started</p>'),
    ('<p class="empty-state">Select a clip to view properties</p>', '<p class="empty-state" data-i18n="props.empty">Select a clip to view properties</p>'),
    ('<h2>📤 Export Video</h2>', '<h2>📤 <span data-i18n="modal.export.title">Export Video</span></h2>'),
    ('<label>Source File</label>', '<label data-i18n="modal.export.source">Source File</label>'),
    ('<label>Format</label>', '<label data-i18n="modal.export.format">Format</label>'),
    ('<label>Quality</label>', '<label data-i18n="modal.export.quality">Quality</label>'),
    ('<label>Resolution</label>', '<label data-i18n="modal.export.res">Resolution</label>'),
    ('<label>FPS</label>', '<label data-i18n="modal.export.fps">FPS</label>'),
    ('Start Export\n                </button>', '<span data-i18n="modal.export.start">Start Export</span>\n                </button>'),
    ('>Cancel</button>', ' data-i18n="modal.export.cancel">Cancel</button>'),
    ('<h2>📁 Projects</h2>', '<h2>📁 <span data-i18n="modal.projects.title">Projects</span></h2>'),
    ('<p class="empty-state">Loading projects...</p>', '<p class="empty-state" data-i18n="modal.projects.loading">Loading projects...</p>'),
    ('data-modal="projectsModal">Close</button>', 'data-modal="projectsModal" data-i18n="modal.projects.close">Close</button>'),
]

for old, new in reps:
    html = html.replace(old, new)

# inject script tag for i18n
import_tag = """
    <script>window.I18N_BASE_URL = '/video-editor-static/i18n';</script>
    <script src="/static/i18n.js?v=4"></script>
    <script src="/video-editor-static/editor.js"></script>
"""
html = html.replace('<script src="/video-editor-static/editor.js"></script>', import_tag)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Finished i18n migration for video_editor.")
