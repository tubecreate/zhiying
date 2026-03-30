import os
import json
import codecs

def patch_file(path, reps):
    with codecs.open(path, 'r', 'utf-8') as f:
        content = f.read()
    for old, new in reps:
        if old not in content:
            print(f"WARN: Not found in {os.path.basename(path)}: {old[:30]}...")
        else:
            content = content.replace(old, new)
    with codecs.open(path, 'w', 'utf-8') as f:
        f.write(content)

story_reps = [
    ('<title>3D Story Engine — ZhiYing</title>', '<title data-i18n="story.title_doc">3D Story Engine — ZhiYing</title>'),
    ('<span class="story-logo">🎬 Story</span>', '<span class="story-logo" data-i18n="story.app_title">🎬 Story</span>'),
    ('placeholder="Tên kịch bản..."', 'data-i18n-placeholder="story.placeholder_name" placeholder="Tên kịch bản..."'),
    ('<option value="">-- Chọn Team --</option>', '<option value="" data-i18n="story.sel_team">-- Chọn Team --</option>'),
    ('>▶ Play</button>', ' data-i18n="story.btn_play">▶ Play</button>'),
    ('>⏸ Pause</button>', ' data-i18n="story.btn_pause">⏸ Pause</button>'),
    ('>■ Stop</button>', ' data-i18n="story.btn_stop">■ Stop</button>'),
    ('>＋ Mới</button>', ' data-i18n="story.btn_new">＋ Mới</button>'),
    ('>📂 Tải</button>', ' data-i18n="story.btn_load">📂 Tải</button>'),
    ('>💾 Lưu</button>', ' data-i18n="story.btn_save">💾 Lưu</button>'),
    ('>🤖 AI Generate</button>', ' data-i18n="story.btn_ai">🤖 AI Generate</button>'),
    ('<div class="sidebar-title">🏛️ Team đang dùng</div>', '<div class="sidebar-title" data-i18n="story.sidebar_team">🏛️ Team đang dùng</div>'),
    ('<div class="sidebar-title">👤 Nhân vật (từ team)</div>', '<div class="sidebar-title" data-i18n="story.sidebar_actors">👤 Nhân vật (từ team)</div>'),
    ('>Chọn Team ở trên để load nhân vật<', ' data-i18n="story.actors_empty">Chọn Team ở trên để load nhân vật<'),
    ('<div class="sidebar-title">📍 Vị trí</div>', '<div class="sidebar-title" data-i18n="story.sidebar_waypoints">📍 Vị trí</div>'),
    ('<div class="sidebar-title">📁 Kịch bản đã lưu</div>', '<div class="sidebar-title" data-i18n="story.sidebar_saved">📁 Kịch bản đã lưu</div>'),
    ('>Chưa có<', ' data-i18n="story.saved_empty">Chưa có<'),
    ('<span>⏱ Timeline</span>', '<span data-i18n="story.timeline_title">⏱ Timeline</span>'),
    ('title="Thu nhỏ"', 'data-i18n-title="story.zoom_out" title="Thu nhỏ"'),
    ('title="Phóng to"', 'data-i18n-title="story.zoom_in" title="Phóng to"'),
    ('>Click vào track để thêm event · Kéo event để đổi thời gian<', ' data-i18n="story.timeline_hint">Click vào track để thêm event · Kéo event để đổi thời gian<'),
    ('<label>🧠 Chọn AI Model:</label>', '<label data-i18n="story.ai_model">🧠 Chọn AI Model:</label>'),
    ('<label>Mô tả kịch bản:</label>', '<label data-i18n="story.ai_desc">Mô tả kịch bản:</label>'),
    ('VD: Buổi họp sáng thứ hai, team báo cáo công việc tuần, thảo luận kế hoạch...', 'VD: Buổi họp sáng thứ hai...'), # replaced below
    ('placeholder="VD: Buổi họp sáng thứ hai, team báo cáo công việc tuần, thảo luận kế hoạch..."', 'data-i18n-placeholder="story.ai_desc_placeholder" placeholder="VD: Buổi họp sáng thứ hai, team báo cáo công việc tuần, thảo luận kế hoạch..."'),
    ('>AI sẽ tạo timeline tự động dựa trên nhân vật và waypoints hiện tại.<', ' data-i18n="story.ai_hint">AI sẽ tạo timeline tự động dựa trên nhân vật và waypoints hiện tại.<'),
    ('<script src="/static/story_bubbles.js"></script>', '<script src="/static/i18n.js"></script>\n<script src="/static/story_bubbles.js"></script>'),
    ('async function initStoryPage() {', 'async function initStoryPage() {\n    await loadI18nFromApi();'),
]

update_story_js = [
    ('${assignedCount} agent được gán · ${(team.nodes||[]).length} vai trò', '${assignedCount} ${T(\'story.agent_assigned\')} · ${(team.nodes||[]).length} ${T(\'story.roles\')}'),
    ('showToast(`🏛️ Đã load team: ${team.name} · ${actors.length} nhân vật`, \'success\');', 'showToast(`${T(\'story.loaded_team\', {name: team.name, count: actors.length})}`, \'success\');'),
    ("showToast('⚠️ Chưa có kịch bản. Tạo mới hoặc tải kịch bản!', 'error');", "showToast(T('story.err_no_script'), 'error');"),
    ("showToast('✅ Kịch bản kết thúc!', 'success');", "showToast(T('story.script_finished'), 'success');"),
    ("if (!confirm('Tạo kịch bản mới? Dữ liệu chưa lưu sẽ mất.')) return;", "if (!confirm(T('story.confirm_new'))) return;"),
    ("titleEl.value = 'Kịch bản mới';", "titleEl.value = T('story.new_script_title');"),
    ("Chưa có kịch bản nào.", "Chưa có kịch bản nào."), # wait
    ('<p style="color:var(--muted);font-size:13px">Chưa có kịch bản nào.</p>', '<p style="color:var(--muted);font-size:13px">${T(\'story.no_saved_scripts\')}</p>'),
    ('${s.actor_count} nhân vật · ${s.event_count} events', '${s.actor_count} ${T(\'story.actors\')} · ${s.event_count} ${T(\'story.events\')}'),
    ("showModal('📂 Tải kịch bản'", "showModal('📂 ' + T('story.modal_load_title')"),
    ('<option value="">Không tìm thấy model nào</option>', '<option value="">${T(\'story.no_models\')}</option>'),
    ("showModal('🤖 AI Generate Kịch Bản'", "showModal('🤖 ' + T('story.modal_ai_title')"),
    ("showToast('⏳ Đang tạo kịch bản bằng AI... (có thể mất 30-60 giây)', 'info');", "showToast(T('story.ai_generating'), 'info');"),
    ("btnAI.textContent = '⏳ Đang tạo...';", "btnAI.textContent = T('story.ai_btn_generating');"),
    ("btnAI.textContent = '🤖 AI Generate';", "btnAI.textContent = T('story.btn_ai');"),
    ("showToast(`✅ Đã tạo kịch bản AI${note}${prov} · ${(s.timeline||[]).length} events`, 'success');", "showToast(T('story.ai_success', {note, prov, count: (s.timeline||[]).length}), 'success');"),
    ("showToast(`❌ Lỗi: ${data.error || 'Không thể tạo kịch bản'}`, 'error');", "showToast(T('story.ai_error', {err: data.error || T('story.err_cannot_gen')}), 'error');"),
    ("showToast(`❌ Lỗi kết nối: ${e.message}`, 'error');", "showToast(T('story.err_conn', {msg: e.message}), 'error');"),
]

studio_reps = [
    ('<title>3D Studio — ZhiYing</title>', '<title data-i18n="studio.title_doc">3D Studio — ZhiYing</title>'),
    ('<h2>🎨 3D Studio</h2>', '<h2 data-i18n="studio.title_main">🎨 3D Studio</h2>'),
    ('>← Quay lại Teams</a>', ' data-i18n="studio.back_teams">← Quay lại Teams</a>'),
    ('<label>Team đang chỉnh sửa</label>', '<label data-i18n="studio.team_edit">Team đang chỉnh sửa</label>'),
    ('<option value="">-- Chọn team --</option>', '<option value="" data-i18n="studio.sel_team">-- Chọn team --</option>'),
    ('title="Tạo team mới bằng AI"', 'data-i18n-title="studio.btn_new_ai" title="Tạo team mới bằng AI"'),
    ('<label>📐 Kích thước phòng</label>', '<label data-i18n="studio.room_size">📐 Kích thước phòng</label>'),
    ('>Rộng</span>', ' data-i18n="studio.width">Rộng</span>'),
    ('>Dài</span>', ' data-i18n="studio.depth">Dài</span>'),
    ('>Tất cả</button>', ' data-i18n="studio.tab_all">Tất cả</button>'),
    ('>🪑 Nội thất</button>', ' data-i18n="studio.tab_furn">🪑 Nội thất</button>'),
    ('>🌿 Trang trí</button>', ' data-i18n="studio.tab_deco">🌿 Trang trí</button>'),
    ('>🧱 Kiến trúc</button>', ' data-i18n="studio.tab_struct">🧱 Kiến trúc</button>'),
    ('<h4>📦 Đã đặt (<span id="placed-count">0</span>)</h4>', '<h4>📦 <span data-i18n="studio.placed">Đã đặt</span> (<span id="placed-count">0</span>)</h4>'),
    ('<span class="tb-label">Công cụ:</span>', '<span class="tb-label" data-i18n="studio.tools">Công cụ:</span>'),
    ('>📌 Đặt</button>', ' data-i18n="studio.tool_place">📌 Đặt</button>'),
    ('>✋ Di chuyển</button>', ' data-i18n="studio.tool_move">✋ Di chuyển</button>'),
    ('>🔄 Xoay</button>', ' data-i18n="studio.tool_rotate">🔄 Xoay</button>'),
    ('>🗑️ Xóa</button>', ' data-i18n="studio.tool_delete">🗑️ Xóa</button>'),
    ('>🪄 Tạo bằng AI</button>', ' data-i18n="studio.tool_ai">🪄 Tạo bằng AI</button>'),
    ('>🧹 Xóa hết</button>', ' data-i18n="studio.tool_clear">🧹 Xóa hết</button>'),
    ('>💾 Lưu</button>', ' data-i18n="studio.tool_save">💾 Lưu</button>'),
    ('>Sẵn sàng — chọn vật phẩm bên trái rồi bấm vào sàn để đặt</span>', ' data-i18n="studio.status_ready">Sẵn sàng — chọn vật phẩm bên trái rồi bấm vào sàn để đặt</span>'),
    ('<div class="desk-agent-popup-header">🤖 Gán agent cho bàn này</div>', '<div class="desk-agent-popup-header" data-i18n="studio.assign_agent">🤖 Gán agent cho bàn này</div>'),
    ('<h3>✨ Tạo Phòng làm việc bằng AI</h3>', '<h3 data-i18n="studio.ai_room_title">✨ Tạo Phòng làm việc bằng AI</h3>'),
    ('<label style="display:block; font-size:12px; color:var(--text2); margin-bottom:8px;">Nhập prompt mô tả phòng</label>', '<label style="display:block; font-size:12px; color:var(--text2); margin-bottom:8px;" data-i18n="studio.ai_prompt_lbl">Nhập prompt mô tả phòng</label>'),
    ('placeholder="Ví dụ: Tạo phòng làm việc hiện đại cho team này, xếp bàn thành hình chữ U, có nhiểu cây xanh và tủ sách..."', 'data-i18n-placeholder="studio.ai_room_prompt" placeholder="Ví dụ: Tạo phòng làm việc hiện đại..."'),
    ('>Đang phân tích team và thiết kế 3D...<', ' data-i18n="studio.ai_room_analyzing">Đang phân tích team và thiết kế 3D...<'),
    ('>Hủy</button>', ' data-i18n="studio.btn_cancel">Hủy</button>'),
    ('>🪄 Tạo tự động</button>', ' data-i18n="studio.btn_auto_create">🪄 Tạo tự động</button>'),
    ('<h3>⚡ Tạo Team nhanh bằng AI</h3>', '<h3 data-i18n="studio.ai_team_title">⚡ Tạo Team nhanh bằng AI</h3>'),
    ('<label style="display:block; font-size:12px; color:var(--text2); margin-bottom:8px;">Mô tả team bạn muốn tạo</label>', '<label style="display:block; font-size:12px; color:var(--text2); margin-bottom:8px;" data-i18n="studio.ai_team_lbl">Mô tả team bạn muốn tạo</label>'),
    ('placeholder="VD: Team developer gồm 4 người: 1 leader, 2 dev frontend/backend, 1 tester"', 'data-i18n-placeholder="studio.ai_team_prompt" placeholder="VD: Team..."'),
    ('>Đang phân tích và tạo team...<', ' data-i18n="studio.ai_team_analyzing">Đang phân tích và tạo team...<'),
    ('>⚡ Tạo Team</button>', ' data-i18n="studio.btn_team_create">⚡ Tạo Team</button>'),
    ('<script src="/static/furniture3d.js?v=20260327"></script>', '<script src="/static/i18n.js"></script>\n    <script src="/static/furniture3d.js?v=20260327"></script>'),
    ('async function init() {', 'async function init() {\n    await loadI18nFromApi();'),
]

studio_js = [
    ("toast('Lỗi lưu: ' + e.message, 'error');", "toast(T('studio.err_save') + ': ' + e.message, 'error');"),
    ("setStatus(`Đang chỉnh sửa: ${teams.find(t => t.id === currentTeamId)?.name || currentTeamId}`);", "setStatus(`${T('studio.editing_team')}: ${teams.find(t => t.id === currentTeamId)?.name || currentTeamId}`);"),
    ("setStatus(`📐 Phòng: ${roomW} × ${roomD}`);", "setStatus(`📐 ${T('studio.room_status')}: ${roomW} × ${roomD}`);"),
    ("toast('⚠️ Vui lòng chọn Team trước khi đặt vật phẩm!', 'error');", "toast('⚠️ ' + T('studio.err_sel_team_first'), 'error');"),
    ("setStatus(`Đã chọn: ${assets.find(a => a.id === id)?.name} — bấm vào sàn để đặt`);", "setStatus(`${T('studio.selected')}: ${assets.find(a => a.id === id)?.name} — ${T('studio.click_to_place')}`);"),
    ("toast(`🔄 Đã xoay`, 'success');", "toast(`🔄 ${T('studio.rotated')}`, 'success');"),
    ("toast(`🗑️ Đã xóa`, 'success');", "toast(`🗑️ ${T('studio.deleted')}`, 'success');"),
    ("toast(`📌 Đã đặt ${def.name}`, 'success');", "toast(`📌 ${T('studio.placed_success', {name: def.name})}`, 'success');"),
    ("toast('Chọn team trước khi lưu!', 'error');", "toast('⚠️ ' + T('studio.err_sel_team_save'), 'error');"),
    ("toast('💾 Đã lưu thành công!', 'success');", "toast('💾 ' + T('studio.saved_success'), 'success');"),
]


webui_dir = r'c:\tubecreate-vue\zhiying\zhiying\extensions\webui\static'

patch_file(os.path.join(webui_dir, 'story.html'), story_reps + update_story_js)
patch_file(os.path.join(webui_dir, 'studio.html'), studio_reps + studio_js)

print("HTML/JS PATCHED.")
