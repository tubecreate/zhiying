/**
 * ZhiYing Dashboard — Internationalization (i18n)
 * Loads language from API and provides T() for translations.
 */
let _lang = 'zh';
const _translations = {
    zh: {
        // Sidebar
        'nav.dashboard': '仪表盘',
        'nav.extensions': '扩展组件',
        'nav.api_manager': 'API 管理',
        'nav.settings': '设置',
        'sidebar.connected': 'API 已连接',
        'sidebar.offline': 'API 离线',

        // Dashboard
        'dash.title': '📊 仪表盘',
        'stat.agents': '智能体 (Agents)',
        'stat.profiles': '浏览器环境',
        'stat.skills': '技能 (Skills)',
        'stat.workflows': '工作流',
        'stat.extensions': '扩展组件',
        'stat.api_keys': 'API 密钥',
        'dash.system_status': '🟢 系统状态',
        'dash.quick_actions': '📌 快捷操作',
        'dash.manage_agents': '🤖 管理智能体',
        'dash.browser_profiles': '🌐 浏览器环境',
        'dash.workflow_builder': '🔄 工作流构建器',
        'dash.cloud_api_keys': '☁️ 云端 API 密钥',
        'status.online': '在线',
        'status.offline': '离线',
        'status.checking': '检查中...',
        'status.idle': '空闲',
        'status.running': '运行中',
        'status.models': '个模型',

        // Extensions
        'ext.title': '🧩 扩展组件',
        'ext.install_git': '+ 从 Git 安装',
        'ext.click_hint': '点击扩展组件以打开管理界面。',
        'ext.agents_desc': '创建、编辑并与 AI 智能体对话',
        'ext.browser_desc': '管理防关联浏览器独立环境 (Profiles)',
        'ext.workflows_desc': '可视化工作流节点编辑器',
        'ext.skills_desc': '管理和运行智能体技能',
        'ext.market_desc': '浏览和安装社区扩展',
        'ext.cloud_api_desc': '管理 Gemini, OpenAI, Claude, DeepSeek 等 API 密钥',
        'ext.ollama_desc': '通过 Ollama 管理本地 AI 模型',
        'ext.multi_agents_desc': '协调智能体团队与任务分配',
        'ext.back': '← 返回扩展',

        // Agents
        'agents.generate_ai': '⚡ AI 自动生成',
        'agents.create': '+ 创建智能体',
        'agents.no_agents': '暂无智能体。',
        'agents.skills_count': '个技能',
        'agents.chat': '💬 聊天',
        'agents.edit': '编辑',
        'agents.delete': '删除',
        'agents.delete_confirm': '确定删除该智能体？',

        // Agent Modal
        'agent_modal.create_title': '创建智能体',
        'agent_modal.edit_title': '编辑：',
        'agent_modal.identity': '👤 身份设定',
        'agent_modal.behavior': '🧠 行为模式',
        'agent_modal.browser': '🌐 浏览器环境',
        'agent_modal.schedule': '⏰ 定时任务',
        'agent_modal.history': '📜 历史记录',
        'agent_modal.skills': '⚡ 技能组合',
        'agent_modal.telegram': '✈️ Telegram',
        'agent_modal.messenger': '💬 Messenger',
        'agent_modal.identity_title': '身份与选项设定',
        'agent_modal.save': '保存智能体',
        'agent_modal.cancel': '取消',
        'agent_modal.name_required': '名称不能为空',

        // Browser
        'browser.new_profile': '+ 新建环境',
        'browser.no_profiles': '暂无环境。',
        'browser.create_profile': '创建环境',
        'browser.create_fetch': '创建并获取指纹',
        'browser.creating': '创建中...',
        'browser.delete_confirm': '删除',
        'browser.no_proxy': '无代理',

        // Skills
        'skills.no_skills': '未找到技能。',
        'skills.run': '▶ 运行',
        'skills.executed': '技能已执行，请检查 CLI 控制台。',

        // Cloud API
        'cloud_api.add_key': '+ 添加密钥',
        'cloud_api.stored_keys': '🔐 已保存的密钥',
        'cloud_api.no_keys': '暂无已保存的密钥。',
        'cloud_api.active': '✅ 激活',
        'cloud_api.no_key': '❌ 无密钥',
        'cloud_api.add': '+ 添加',
        'cloud_api.test': '🧪 测试',
        'cloud_api.remove_confirm': '确定要从 {provider} 删除 "{label}" 吗？',
        'cloud_api.provider': '服务商',
        'cloud_api.label': '标签',
        'cloud_api.key': '密钥 (API Key)',
        'cloud_api.status': '状态',
        'cloud_api.actions': '操作',

        // Ollama
        'ollama.models': '📦 模型列表',
        'ollama.loaded': '🔥 已加载',
        'ollama.not_running': 'Ollama 未运行。',
        'ollama.no_models': '暂无模型。请在下方拉取一个模型。',
        'ollama.pull': '📥 拉取模型',
        'ollama.enter_model': '输入模型名称。',
        'ollama.pulling': '正在拉取 "{name}"...',
        'ollama.done': '完成！',
        'ollama.failed': '失败：',
        'ollama.remove_confirm': '确定删除 "{name}"？',
        'ollama.model_col': '模型名称',
        'ollama.size_col': '大小',
        'ollama.modified_col': '更新时间',
        'ollama.status_col': '状态',
        'ollama.actions_col': '操作',

        // Multi-Agents
        'multi.create_team': '+ 创建团队',
        'multi.teams': '👥 团队列表',
        'multi.no_teams': '暂无团队。',
        'multi.delegation_log': '📋 委派日志',
        'multi.no_history': '暂无历史。',
        'multi.delete_confirm': '确定删除该团队？',
        'multi.team_name': '团队名称：',
        'multi.agent_ids': '智能体 IDs (用逗号分隔)：',
        'multi.strategy': '协作策略 (sequential/parallel/lead-delegate)：',
        'multi.created': '创建成功！',
        'multi.team_col': '团队名称',
        'multi.strategy_col': '协作策略',
        'multi.agents_col': '成员 (Agents)',
        'multi.time_col': '时间',
        'multi.task_col': '任务',

        // Settings
        'settings.title': '⚙️ 设置',
        'settings.version': '🔄 版本及更新',
        'settings.general': '⚙️ 通用设置',
        'settings.language': '🌐 语言',
        'settings.api_port': 'API 端口',
        'settings.ai_model': 'AI 模型',
        'settings.api_base': 'API Base URL',
        'settings.save': '保存设置',
        'settings.check_update': '🔍 检查更新',
        'settings.update_now': '⬆️ 立即更新',
        'settings.checking': '🔍 正在检查...',
        'settings.fetching': '正在从 GitHub 获取...',
        'settings.update_available': '🔔 发现新版本！{count} 个新提交',
        'settings.up_to_date': '✅ 您正在使用最新版本！',
        'settings.update_confirm': '确定将 ZhiYing 更新至最新版本？更新后 API 服务器需要重启。',
        'settings.updating': '⏳ 更新中...',
        'settings.pulling': '正在从 GitHub 拉取最新代码...',
        'settings.updated': '✅ 已更新至 v{version}！',
        'settings.restart_needed': '请重启 API 服务器。',
        'settings.restart_banner': '⚠️ 请重启 API 服务器以应用更新。请运行：',
        'settings.update_failed': '❌ 更新失败：',
        'settings.changelog': '📋 更新日志',
        'settings.lang_label': '界面语言',
        'settings.lang_saved': '✅ 保存成功！正在重新加载...',

        // Install Extension Modal
        'install_ext.title': '📦 从 Git 安装扩展',
        'install_ext.url_label': 'Git 仓库 URL',
        'install_ext.cancel': '取消',
        'install_ext.install': '🚀 安装',
        'install_ext.installing': '⏳ 安装中...',
        'install_ext.url_required': 'URL 不能为空。',
        'install_ext.installed': '安装成功！',
        'install_ext.failed': '安装失败：',

        // Chat
        'chat.title': '💬 与以下对象聊天',
        'chat.placeholder': '输入消息...',
        'chat.send': '发送',
        'chat.say_hello': '打个招呼吧！',
        'chat.typing': '正在输入...',
        'chat.loading': '加载中...',

        // Generate Agent
        'gen.title': '⚡ 通过 AI 自动生成智能体',
        'gen.name': '智能体名称',
        'gen.prefix': '标签前缀',
        'gen.desc': '描述信息',
        'gen.provider': 'AI 服务商',
        'gen.model': 'AI 模型',
        'gen.api_key': 'API 密钥',
        'gen.accounts': '🔑 Google 账号 (用制表符Tab分隔)',
        'gen.preview': '📄 预览',
        'gen.close': '关闭',
        'gen.generate': '⚡ 生成',
        'gen.apply': '🚀 应用',
        'gen.name_desc_required': '必须填写名称和描述！',
        'gen.calling': '🤖 正在调用 {provider}/{model}...',
        'gen.done': '✅ 完成！',
        'gen.failed': '❌ 失败',
        'gen.error': '❌ 错误',
        'gen.generating': '生成中...',

        // Add API Key Modal
        'add_key.title': '🔑 添加 API 密钥',
        'add_key.provider': '服务商',
        'add_key.key': 'API 密钥 (Key)',
        'add_key.label': '标签',
        'add_key.cancel': '取消',
        'add_key.save': '保存密钥',
        'add_key.required': '密钥不能为空。',
        'add_key.added': '添加成功！',
        'add_key.failed': '添加失败。',

        // API Manager
        'api.title': '🔌 API 管理中心',
        'api.desc': '系统 CLI REST API — ZhiYing API 服务端点 (Endpoints)',
        'api.status': '服务器状态：',
        'api.running': '正在运行',
        'api.base_url': 'Base URL:',
        'api.swagger': '打开 Swagger 文档',
        'api.redoc': '打开 ReDoc',
        'api.endpoints': '📡 可用服务端点',
        'api.method': '请求方法',
        'api.path': '路径',
        'api.description': '描述',
        'api.tags': '标签 (Tags)',
        'api.load_fail': '无法加载 API 规范文档。请检查服务器是否正在运行。',

        // Form labels
        'form.name': '名称',
        'form.proxy': '代理 (Proxy)',
        'form.os': '操作系统',
        'form.browser': '浏览器内核',

        // Market UI
        'market.search': '搜索',
        'market.search_placeholder': '通过名称、标签或描述搜索',
        'market.cat_all': '所有分类',
        'market.cat_extension': '🧩 扩展组件',
        'market.cat_node': '🔗 节点 (Nodes)',
        'market.cat_skill': '⚡ 技能 (Skills)',
        'market.cat_model3d': '🎨 3D 模型',
        'market.filter_all': '全部',
        'market.filter_free': '仅免费',
        'market.filter_paid': '仅付费',
        'market.sort_by': '排序依据',
        'market.sort_newest': '最新上传',
        'market.sort_popular': '下载最多',
        'market.sort_rating': '评分最高',
        'market.sort_price_asc': '价格升序 ↑',
        'market.sort_price_desc': '价格降序 ↓',
        'market.my_listings': '我的商品',
        'market.sell_item': '发布商品',
        'market.loading': '正在加载插件市场...',
        'market.no_items': '未找到相关项目',
        'market.results': '返回结果',

        // Sell on Market modal
        'sell.title': '发布到市场',
        'sell.step1': '选择项目',
        'sell.step2': '设置价格并发布',
        'sell.category': '分类',
        'sell.filter_placeholder': '🔍 筛选项目...',
        'sell.loading_items': '正在加载您的项目...',
        'sell.loading_listings': '正在加载您的发布记录...',
        'sell.display_name': '展示名称',
        'sell.display_name_hint': '在市场上显示的名称',
        'sell.price': '价格 (积分/Credits)',
        'sell.visibility': '可见性',
        'sell.vis_public': '🌐 公开',
        'sell.vis_private': '🔒 仅自己可见',
        'sell.version': '版本号',
        'sell.tags': '标签 (用逗号分隔)',
        'sell.deps': 'Python 依赖项',
        'sell.deps_hint': '(该扩展运行所需的 pip 库)',
        'sell.deps_note': '用逗号分隔。当用户安装您的扩展时，将自动安装这些库。',
        'sell.description': '说明描述',
        'sell.desc_placeholder': '说明该组件的具体功能...',
        'sell.back': '上一步',
        'sell.publish': '正式发布',
        'market.cat_skill_s': '技能',
        'market.cat_ext_s': '扩展',
        'market.cat_node_s': '节点',
        'market.cat_3d_s': '3D模型',

        // Detail modal
        'detail.other_items': '其他项目',
        'detail.downloads': '下载次数',
        'detail.reviews': '条评价',
        'detail.reviews_title': '用户评价',
        'detail.no_reviews': '暂无评价',
        'detail.install': '安装',
        'detail.installed': '已安装',
        'detail.uninstall': '卸载',
        'detail.buy_for': '购买，只需',
    },
    vi: {
        // Sidebar
        'nav.dashboard': 'Dashboard',
        'nav.extensions': 'Extensions',
        'nav.api_manager': 'API Manager',
        'nav.settings': 'Cài đặt',
        'sidebar.connected': 'API Đã kết nối',
        'sidebar.offline': 'API Ngoại tuyến',

        // Dashboard
        'dash.title': '📊 Dashboard',
        'stat.agents': 'Agents',
        'stat.profiles': 'Hồ sơ trình duyệt',
        'stat.skills': 'Kỹ năng',
        'stat.workflows': 'Workflows',
        'stat.extensions': 'Extensions',
        'stat.api_keys': 'API Keys',
        'dash.system_status': '🟢 Trạng thái hệ thống',
        'dash.quick_actions': '📌 Thao tác nhanh',
        'dash.manage_agents': '🤖 Quản lý Agents',
        'dash.browser_profiles': '🌐 Hồ sơ trình duyệt',
        'dash.workflow_builder': '🔄 Trình tạo Workflow',
        'dash.cloud_api_keys': '☁️ Cloud API Keys',
        'status.online': 'Trực tuyến',
        'status.offline': 'Ngoại tuyến',
        'status.checking': 'Đang kiểm tra...',
        'status.idle': 'Chờ',
        'status.running': 'đang chạy',
        'status.models': 'mô hình',

        // Extensions
        'ext.title': '🧩 Extensions',
        'ext.install_git': '+ Cài từ Git',
        'ext.click_hint': 'Nhấp vào extension để mở giao diện quản lý.',
        'ext.agents_desc': 'Tạo, chỉnh sửa và trò chuyện với AI agents',
        'ext.browser_desc': 'Quản lý hồ sơ trình duyệt ẩn danh',
        'ext.workflows_desc': 'Trình tạo workflow với node editor',
        'ext.skills_desc': 'Quản lý và chạy kỹ năng của agent',
        'ext.market_desc': 'Duyệt và cài đặt extension cộng đồng',
        'ext.cloud_api_desc': 'Quản lý API keys cho Gemini, OpenAI, Claude, DeepSeek, Grok',
        'ext.ollama_desc': 'Quản lý mô hình AI cục bộ qua Ollama',
        'ext.multi_agents_desc': 'Điều phối đội agent và phân công công việc',
        'ext.back': '← Quay lại Extensions',

        // Agents
        'agents.generate_ai': '⚡ Tạo bằng AI',
        'agents.create': '+ Tạo Agent',
        'agents.no_agents': 'Chưa có agent nào.',
        'agents.skills_count': 'kỹ năng',
        'agents.chat': '💬 Chat',
        'agents.edit': 'Sửa',
        'agents.delete': 'Xóa',
        'agents.delete_confirm': 'Xóa agent này?',

        // Agent Modal
        'agent_modal.create_title': 'Tạo Agent',
        'agent_modal.edit_title': 'Sửa:',
        'agent_modal.identity': '👤 Danh tính',
        'agent_modal.behavior': '🧠 Hành vi',
        'agent_modal.browser': '🌐 Trình duyệt',
        'agent_modal.schedule': '⏰ Lên lịch',
        'agent_modal.history': '📜 Lịch sử',
        'agent_modal.skills': '⚡ Kỹ năng',
        'agent_modal.telegram': '✈️ Telegram',
        'agent_modal.messenger': '💬 Messenger',
        'agent_modal.identity_title': 'Danh tính & Tùy chọn',
        'agent_modal.save': 'Lưu Agent',
        'agent_modal.cancel': 'Hủy',
        'agent_modal.name_required': 'Tên không được để trống',

        // Browser
        'browser.new_profile': '+ Hồ sơ mới',
        'browser.no_profiles': 'Chưa có hồ sơ nào.',
        'browser.create_profile': 'Tạo hồ sơ',
        'browser.create_fetch': 'Tạo & Lấy Fingerprint',
        'browser.creating': 'Đang tạo...',
        'browser.delete_confirm': 'Xóa',
        'browser.no_proxy': 'Không proxy',

        // Skills
        'skills.no_skills': 'Không tìm thấy kỹ năng.',
        'skills.run': '▶ Chạy',
        'skills.executed': 'Kỹ năng đã được thực thi. Kiểm tra CLI.',

        // Cloud API
        'cloud_api.add_key': '+ Thêm Key',
        'cloud_api.stored_keys': '🔐 Keys đã lưu',
        'cloud_api.no_keys': 'Chưa có keys nào.',
        'cloud_api.active': '✅ Hoạt động',
        'cloud_api.no_key': '❌ Chưa có Key',
        'cloud_api.add': '+ Thêm',
        'cloud_api.test': '🧪 Kiểm tra',
        'cloud_api.remove_confirm': 'Xóa "{label}" từ {provider}?',
        'cloud_api.provider': 'Provider',
        'cloud_api.label': 'Nhãn',
        'cloud_api.key': 'Key',
        'cloud_api.status': 'Trạng thái',
        'cloud_api.actions': 'Thao tác',

        // Ollama
        'ollama.models': '📦 Mô hình',
        'ollama.loaded': '🔥 Đã tải',
        'ollama.not_running': 'Ollama chưa chạy.',
        'ollama.no_models': 'Chưa có mô hình. Tải một mô hình bên dưới.',
        'ollama.pull': '📥 Tải',
        'ollama.enter_model': 'Nhập tên mô hình.',
        'ollama.pulling': 'Đang tải "{name}"...',
        'ollama.done': 'Xong!',
        'ollama.failed': 'Thất bại: ',
        'ollama.remove_confirm': 'Xóa "{name}"?',
        'ollama.model_col': 'Mô hình',
        'ollama.size_col': 'Dung lượng',
        'ollama.modified_col': 'Cập nhật',
        'ollama.status_col': 'Trạng thái',
        'ollama.actions_col': 'Thao tác',

        // Multi-Agents
        'multi.create_team': '+ Tạo nhóm',
        'multi.teams': '👥 Nhóm',
        'multi.no_teams': 'Chưa có nhóm.',
        'multi.delegation_log': '📋 Nhật ký phân công',
        'multi.no_history': 'Chưa có lịch sử.',
        'multi.delete_confirm': 'Xóa nhóm?',
        'multi.team_name': 'Tên nhóm:',
        'multi.agent_ids': 'ID Agents (phân cách bằng dấu phẩy):',
        'multi.strategy': 'Chiến lược (sequential/parallel/lead-delegate):',
        'multi.created': 'Đã tạo!',
        'multi.team_col': 'Nhóm',
        'multi.strategy_col': 'Chiến lược',
        'multi.agents_col': 'Agents',
        'multi.time_col': 'Thời gian',
        'multi.task_col': 'Nhiệm vụ',

        // Settings
        'settings.title': '⚙️ Cài đặt',
        'settings.version': '🔄 Phiên bản & Cập nhật',
        'settings.general': '⚙️ Tổng quan',
        'settings.language': '🌐 Ngôn ngữ',
        'settings.api_port': 'Cổng API',
        'settings.ai_model': 'Mô hình AI',
        'settings.api_base': 'API Base URL',
        'settings.save': 'Lưu cài đặt',
        'settings.check_update': '🔍 Kiểm tra cập nhật',
        'settings.update_now': '⬆️ Cập nhật ngay',
        'settings.checking': '🔍 Đang kiểm tra...',
        'settings.fetching': 'Đang lấy từ GitHub...',
        'settings.update_available': '🔔 Có bản cập nhật! {count} commit mới',
        'settings.up_to_date': '✅ Bạn đang dùng phiên bản mới nhất!',
        'settings.update_confirm': 'Cập nhật ZhiYing lên phiên bản mới nhất? API server cần khởi động lại.',
        'settings.updating': '⏳ Đang cập nhật...',
        'settings.pulling': 'Đang tải mã nguồn mới từ GitHub...',
        'settings.updated': '✅ Đã cập nhật lên v{version}!',
        'settings.restart_needed': 'Vui lòng khởi động lại API server.',
        'settings.restart_banner': '⚠️ Khởi động lại API server để áp dụng bản cập nhật. Chạy: ',
        'settings.update_failed': '❌ Cập nhật thất bại: ',
        'settings.changelog': '📋 Nhật ký thay đổi',
        'settings.lang_label': 'Ngôn ngữ giao diện',
        'settings.lang_saved': '✅ Đã lưu! Đang tải lại...',

        // Install Extension Modal
        'install_ext.title': '📦 Cài đặt Extension từ Git',
        'install_ext.url_label': 'Git Repository URL',
        'install_ext.cancel': 'Hủy',
        'install_ext.install': '🚀 Cài đặt',
        'install_ext.installing': '⏳ Đang cài đặt...',
        'install_ext.url_required': 'URL không được để trống.',
        'install_ext.installed': 'Đã cài đặt!',
        'install_ext.failed': 'Thất bại: ',

        // Chat
        'chat.title': '💬 Trò chuyện với',
        'chat.placeholder': 'Nhập tin nhắn...',
        'chat.send': 'Gửi',
        'chat.say_hello': 'Hãy nói xin chào!',
        'chat.typing': 'Đang gõ...',
        'chat.loading': 'Đang tải...',

        // Generate Agent
        'gen.title': '⚡ Tạo Agent bằng AI',
        'gen.name': 'Tên Agent',
        'gen.prefix': 'Tag Prefix',
        'gen.desc': 'Mô tả',
        'gen.provider': 'AI Provider',
        'gen.model': 'Mô hình',
        'gen.api_key': 'API Key',
        'gen.accounts': '🔑 Tài khoản Google (phân cách bằng tab)',
        'gen.preview': '📄 Xem trước',
        'gen.close': 'Đóng',
        'gen.generate': '⚡ Tạo',
        'gen.apply': '🚀 Áp dụng',
        'gen.name_desc_required': 'Cần có Tên & Mô tả!',
        'gen.calling': '🤖 Đang gọi {provider}/{model}...',
        'gen.done': '✅ Xong!',
        'gen.failed': '❌ Thất bại',
        'gen.error': '❌ Lỗi',
        'gen.generating': 'Đang tạo...',

        // Add API Key Modal
        'add_key.title': '🔑 Thêm API Key',
        'add_key.provider': 'Provider',
        'add_key.key': 'API Key',
        'add_key.label': 'Nhãn',
        'add_key.cancel': 'Hủy',
        'add_key.save': 'Lưu Key',
        'add_key.required': 'Key không được để trống.',
        'add_key.added': 'Đã thêm!',
        'add_key.failed': 'Thất bại.',

        // API Manager
        'api.title': '🔌 API Manager',
        'api.desc': 'System CLI REST API — ZhiYing API Server Endpoints',
        'api.status': 'Trạng thái Server:',
        'api.running': 'Đang chạy',
        'api.base_url': 'Base URL:',
        'api.swagger': 'Mở Swagger Docs',
        'api.redoc': 'Mở ReDoc',
        'api.endpoints': '📡 Endpoints có sẵn',
        'api.method': 'Phương thức',
        'api.path': 'Đường dẫn',
        'api.description': 'Mô tả',
        'api.tags': 'Tags',
        'api.load_fail': 'Không thể tải API spec. Kiểm tra server đang chạy.',

        // Form labels
        'form.name': 'Tên',
        'form.proxy': 'Proxy',
        'form.os': 'Hệ điều hành',
        'form.browser': 'Trình duyệt',

        // Market UI
        'market.search': 'Tìm kiếm',
        'market.search_placeholder': 'Tìm theo tên, tag hoặc mô tả',
        'market.cat_all': 'Tất cả danh mục',
        'market.cat_extension': '🧩 Extensions',
        'market.cat_node': '🔗 Nodes',
        'market.cat_skill': '⚡ Skills',
        'market.cat_model3d': '🎨 Mô hình 3D',
        'market.filter_all': 'Tất cả',
        'market.filter_free': 'Miễn phí',
        'market.filter_paid': 'Trả phí',
        'market.sort_by': 'Sắp xếp',
        'market.sort_newest': 'Mới nhất',
        'market.sort_popular': 'Tải nhiều nhất',
        'market.sort_rating': 'Đánh giá cao',
        'market.sort_price_asc': 'Giá tăng dần',
        'market.sort_price_desc': 'Giá giảm dần',
        'market.my_listings': 'Sản phẩm của tôi',
        'market.sell_item': 'Bán sản phẩm',
        'market.loading': 'Đang tải marketplace...',
        'market.no_items': 'Không tìm thấy sản phẩm',
        'market.results': 'Kết quả',

        // Sell on Market modal
        'sell.title': 'Bán trên Marketplace',
        'sell.step1': 'Chọn mục',
        'sell.step2': 'Giá & Đăng bán',
        'sell.category': 'Danh mục',
        'sell.filter_placeholder': '🔍 Lọc mục...',
        'sell.loading_items': 'Đang tải danh sách...',
        'sell.loading_listings': 'Đang tải sản phẩm...',
        'sell.display_name': 'Tên hiển thị',
        'sell.display_name_hint': 'Tên hiển thị trên Marketplace',
        'sell.price': 'Giá (credits)',
        'sell.visibility': 'Hiển thị',
        'sell.vis_public': '🌐 Công khai',
        'sell.vis_private': '🔒 Riêng tư',
        'sell.version': 'Phên bản',
        'sell.tags': 'Tags (phân cách bằng dấu phẩy)',
        'sell.deps': 'Thư viện Python',
        'sell.deps_hint': '(các gói pip cần cài)',
        'sell.deps_note': 'Phân cách bằng dấu phẩy. Sẽ tự động cài khi người dùng cài extension.',
        'sell.description': 'Mô tả',
        'sell.desc_placeholder': 'Mô tả chức năng của mục này...',
        'sell.back': 'Trở lại',
        'sell.publish': 'Đăng bán',
        'market.cat_skill_s': 'Skills',
        'market.cat_ext_s': 'Extensions',
        'market.cat_node_s': 'Nodes',
        'market.cat_3d_s': 'Mô hình 3D',

        // Detail modal
        'detail.other_items': 'sản phẩm khác',
        'detail.downloads': 'lượt tải',
        'detail.reviews': 'đánh giá',
        'detail.reviews_title': 'Đánh giá',
        'detail.no_reviews': 'Chưa có đánh giá',
        'detail.install': 'Cài đặt',
        'detail.installed': 'Đã cài',
        'detail.uninstall': 'Gỡ cài',
        'detail.buy_for': 'Mua với giá',
    },
    en: {
        // Sidebar
        'nav.dashboard': 'Dashboard',
        'nav.extensions': 'Extensions',
        'nav.api_manager': 'API Manager',
        'nav.settings': 'Settings',
        'sidebar.connected': 'API Connected',
        'sidebar.offline': 'API Offline',

        // Dashboard
        'dash.title': '📊 Dashboard',
        'stat.agents': 'Agents',
        'stat.profiles': 'Browser Profiles',
        'stat.skills': 'Skills',
        'stat.workflows': 'Workflows',
        'stat.extensions': 'Extensions',
        'stat.api_keys': 'API Keys',
        'dash.system_status': '🟢 System Status',
        'dash.quick_actions': '📌 Quick Actions',
        'dash.manage_agents': '🤖 Manage Agents',
        'dash.browser_profiles': '🌐 Browser Profiles',
        'dash.workflow_builder': '🔄 Workflow Builder',
        'dash.cloud_api_keys': '☁️ Cloud API Keys',
        'status.online': 'Online',
        'status.offline': 'Offline',
        'status.checking': 'Checking...',
        'status.idle': 'Idle',
        'status.running': 'running',
        'status.models': 'models',

        // Extensions
        'ext.title': '🧩 Extensions',
        'ext.install_git': '+ Install from Git',
        'ext.click_hint': 'Click on an extension to open its management interface.',
        'ext.agents_desc': 'Create, edit and chat with AI agents',
        'ext.browser_desc': 'Manage anti-detect browser profiles',
        'ext.workflows_desc': 'Visual workflow builder with node editor',
        'ext.skills_desc': 'Manage and run agent skills',
        'ext.market_desc': 'Browse and install community extensions',
        'ext.cloud_api_desc': 'Manage API keys for Gemini, OpenAI, Claude, DeepSeek, Grok',
        'ext.ollama_desc': 'Manage local AI models via Ollama',
        'ext.multi_agents_desc': 'Orchestrate agent teams and task delegation',
        'ext.back': '← Back to Extensions',

        // Agents
        'agents.generate_ai': '⚡ Generate with AI',
        'agents.create': '+ Create Agent',
        'agents.no_agents': 'No agents yet.',
        'agents.skills_count': 'skills',
        'agents.chat': '💬 Chat',
        'agents.edit': 'Edit',
        'agents.delete': 'Del',
        'agents.delete_confirm': 'Delete agent?',

        // Agent Modal
        'agent_modal.create_title': 'Create Agent',
        'agent_modal.edit_title': 'Edit:',
        'agent_modal.identity': '👤 Identity',
        'agent_modal.behavior': '🧠 Behavior',
        'agent_modal.browser': '🌐 Browser',
        'agent_modal.schedule': '⏰ Schedule',
        'agent_modal.history': '📜 History',
        'agent_modal.skills': '⚡ Skills',
        'agent_modal.telegram': '✈️ Telegram',
        'agent_modal.messenger': '💬 Messenger',
        'agent_modal.identity_title': 'Identity & Options',
        'agent_modal.save': 'Save Agent',
        'agent_modal.cancel': 'Cancel',
        'agent_modal.name_required': 'Name required',

        // Browser
        'browser.new_profile': '+ New Profile',
        'browser.no_profiles': 'No profiles yet.',
        'browser.create_profile': 'Create Profile',
        'browser.create_fetch': 'Create & Fetch Fingerprint',
        'browser.creating': 'Creating...',
        'browser.delete_confirm': 'Delete',
        'browser.no_proxy': 'No proxy',

        // Skills
        'skills.no_skills': 'No skills found.',
        'skills.run': '▶ Run',
        'skills.executed': 'Skill executed. Check CLI.',

        // Cloud API
        'cloud_api.add_key': '+ Add Key',
        'cloud_api.stored_keys': '🔐 Stored Keys',
        'cloud_api.no_keys': 'No keys stored.',
        'cloud_api.active': '✅ Active',
        'cloud_api.no_key': '❌ No Key',
        'cloud_api.add': '+ Add',
        'cloud_api.test': '🧪 Test',
        'cloud_api.remove_confirm': 'Remove "{label}" from {provider}?',
        'cloud_api.provider': 'Provider',
        'cloud_api.label': 'Label',
        'cloud_api.key': 'Key',
        'cloud_api.status': 'Status',
        'cloud_api.actions': 'Actions',

        // Ollama
        'ollama.models': '📦 Models',
        'ollama.loaded': '🔥 Loaded',
        'ollama.not_running': 'Ollama not running.',
        'ollama.no_models': 'No models. Pull one below.',
        'ollama.pull': '📥 Pull',
        'ollama.enter_model': 'Enter model name.',
        'ollama.pulling': 'Pulling "{name}"...',
        'ollama.done': 'Done!',
        'ollama.failed': 'Failed: ',
        'ollama.remove_confirm': 'Remove "{name}"?',
        'ollama.model_col': 'Model',
        'ollama.size_col': 'Size',
        'ollama.modified_col': 'Modified',
        'ollama.status_col': 'Status',
        'ollama.actions_col': 'Actions',

        // Multi-Agents
        'multi.create_team': '+ Create Team',
        'multi.teams': '👥 Teams',
        'multi.no_teams': 'No teams.',
        'multi.delegation_log': '📋 Delegation Log',
        'multi.no_history': 'No history.',
        'multi.delete_confirm': 'Delete team?',
        'multi.team_name': 'Team name:',
        'multi.agent_ids': 'Agent IDs (comma-separated):',
        'multi.strategy': 'Strategy (sequential/parallel/lead-delegate):',
        'multi.created': 'Created!',
        'multi.team_col': 'Team',
        'multi.strategy_col': 'Strategy',
        'multi.agents_col': 'Agents',
        'multi.time_col': 'Time',
        'multi.task_col': 'Task',

        // Settings
        'settings.title': '⚙️ Settings',
        'settings.version': '🔄 Version & Update',
        'settings.general': '⚙️ General',
        'settings.language': '🌐 Language',
        'settings.api_port': 'API Port',
        'settings.ai_model': 'AI Model',
        'settings.api_base': 'API Base URL',
        'settings.save': 'Save Settings',
        'settings.check_update': '🔍 Check for Update',
        'settings.update_now': '⬆️ Update Now',
        'settings.checking': '🔍 Checking...',
        'settings.fetching': 'Fetching from GitHub...',
        'settings.update_available': '🔔 Update available! {count} new commit(s)',
        'settings.up_to_date': '✅ You are up to date!',
        'settings.update_confirm': 'Update ZhiYing to latest version? The API server will need to restart after update.',
        'settings.updating': '⏳ Updating...',
        'settings.pulling': 'Pulling latest code from GitHub...',
        'settings.updated': '✅ Updated to v{version}!',
        'settings.restart_needed': 'Please restart the API server.',
        'settings.restart_banner': '⚠️ Restart the API server to apply the update. Run: ',
        'settings.update_failed': '❌ Update failed: ',
        'settings.changelog': '📋 Changelog',
        'settings.lang_label': 'UI Language',
        'settings.lang_saved': '✅ Saved! Reloading...',

        // Install Extension Modal
        'install_ext.title': '📦 Install Extension from Git',
        'install_ext.url_label': 'Git Repository URL',
        'install_ext.cancel': 'Cancel',
        'install_ext.install': '🚀 Install',
        'install_ext.installing': '⏳ Installing...',
        'install_ext.url_required': 'URL required.',
        'install_ext.installed': 'Installed!',
        'install_ext.failed': 'Failed: ',

        // Chat
        'chat.title': '💬 Chat with',
        'chat.placeholder': 'Type a message...',
        'chat.send': 'Send',
        'chat.say_hello': 'Say hello!',
        'chat.typing': 'Typing...',
        'chat.loading': 'Loading...',

        // Generate Agent
        'gen.title': '⚡ Generate Agent with AI',
        'gen.name': 'Agent Name',
        'gen.prefix': 'Tag Prefix',
        'gen.desc': 'Description',
        'gen.provider': 'AI Provider',
        'gen.model': 'Model',
        'gen.api_key': 'API Key',
        'gen.accounts': '🔑 Google Accounts (tab-separated)',
        'gen.preview': '📄 Preview',
        'gen.close': 'Close',
        'gen.generate': '⚡ Generate',
        'gen.apply': '🚀 Apply',
        'gen.name_desc_required': 'Name & Description required!',
        'gen.calling': '🤖 Calling {provider}/{model}...',
        'gen.done': '✅ Done!',
        'gen.failed': '❌ Failed',
        'gen.error': '❌ Error',
        'gen.generating': 'Generating...',

        // Add API Key Modal
        'add_key.title': '🔑 Add API Key',
        'add_key.provider': 'Provider',
        'add_key.key': 'API Key',
        'add_key.label': 'Label',
        'add_key.cancel': 'Cancel',
        'add_key.save': 'Save Key',
        'add_key.required': 'Key required.',
        'add_key.added': 'Added!',
        'add_key.failed': 'Failed.',

        // API Manager
        'api.title': '🔌 API Manager',
        'api.desc': 'System CLI REST API — ZhiYing API Server Endpoints',
        'api.status': 'Server Status:',
        'api.running': 'Running',
        'api.base_url': 'Base URL:',
        'api.swagger': 'Open Swagger Docs',
        'api.redoc': 'Open ReDoc',
        'api.endpoints': '📡 Available Endpoints',
        'api.method': 'Method',
        'api.path': 'Path',
        'api.description': 'Description',
        'api.tags': 'Tags',
        'api.load_fail': 'Cannot load API spec. Check if server is running.',

        // Form labels
        'form.name': 'Name',
        'form.proxy': 'Proxy',
        'form.os': 'OS',
        'form.browser': 'Browser',

        // Market UI
        'market.search': 'Search',
        'market.search_placeholder': 'Search by Name, Tag, or Description',
        'market.cat_all': 'All Categories',
        'market.cat_extension': '🧩 Extensions',
        'market.cat_node': '🔗 Nodes',
        'market.cat_skill': '⚡ Skills',
        'market.cat_model3d': '🎨 3D Models',
        'market.filter_all': 'All',
        'market.filter_free': 'Free Only',
        'market.filter_paid': 'Paid Only',
        'market.sort_by': 'Sort by',
        'market.sort_newest': 'Newest',
        'market.sort_popular': 'Most Downloaded',
        'market.sort_rating': 'Highest Rated',
        'market.sort_price_asc': 'Price ↑',
        'market.sort_price_desc': 'Price ↓',
        'market.my_listings': 'My Listings',
        'market.sell_item': 'Sell Item',
        'market.loading': 'Loading marketplace...',
        'market.no_items': 'No items found',
        'market.results': 'Results',

        // Sell on Market modal
        'sell.title': 'Sell on Market',
        'sell.step1': 'Select Item',
        'sell.step2': 'Set Price & Publish',
        'sell.category': 'Category',
        'sell.filter_placeholder': '🔍 Filter items...',
        'sell.loading_items': 'Loading your items...',
        'sell.loading_listings': 'Loading your listings...',
        'sell.display_name': 'Display Name',
        'sell.display_name_hint': 'Name shown on Market',
        'sell.price': 'Price (credits)',
        'sell.visibility': 'Visibility',
        'sell.vis_public': '🌐 Public',
        'sell.vis_private': '🔒 Private',
        'sell.version': 'Version',
        'sell.tags': 'Tags (comma separated)',
        'sell.deps': 'Python Dependencies',
        'sell.deps_hint': '(pip packages required by this extension)',
        'sell.deps_note': 'Comma separated. These will be auto-installed when users install your extension.',
        'sell.description': 'Description',
        'sell.desc_placeholder': 'Describe what this item does...',
        'sell.back': 'Back',
        'sell.publish': 'Publish to Market',
        'market.cat_skill_s': 'Skills',
        'market.cat_ext_s': 'Extensions',
        'market.cat_node_s': 'Nodes',
        'market.cat_3d_s': '3D Models',

        // Detail modal
        'detail.other_items': 'other items',
        'detail.downloads': 'downloads',
        'detail.reviews': 'reviews',
        'detail.reviews_title': 'Reviews',
        'detail.no_reviews': 'No reviews yet',
        'detail.install': 'Install',
        'detail.installed': 'Installed',
        'detail.uninstall': 'Uninstall',
        'detail.buy_for': 'Buy for',
    }
};

/**
 * Translate key, with optional replacements.
 * T('ollama.pulling', {name:'qwen'})  →  'Đang tải "qwen"...'
 */
function T(key, vars) {
    let s = (_translations[_lang] && _translations[_lang][key]) || (_translations['en'] && _translations['en'][key]) || key;
    if (vars) {
        Object.keys(vars).forEach(k => {
            s = s.replace(new RegExp('\\{' + k + '\\}', 'g'), vars[k]);
        });
    }
    return s;
}

/**
 * Apply translations to all elements with data-i18n attribute.
 */
function applyI18n() {
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        el.textContent = T(key);
    });
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
        el.placeholder = T(el.getAttribute('data-i18n-placeholder'));
    });
    // Update html lang attribute
    document.documentElement.lang = _lang;
}

/**
 * Fetch current language from API and apply.
 */
async function loadI18nFromApi() {
    try {
        const r = await fetch((localStorage.getItem('zhiying_api') || 'http://localhost:5295') + '/api/v1/settings/language');
        const d = await r.json();
        if (d && d.language) {
            _lang = d.language;
        }
    } catch (e) {
        // Default to en on failure
        _lang = localStorage.getItem('zhiying_lang') || 'en';
    }
    applyI18n();
}

/**
 * Save language to API and reload page.
 */
async function changeLanguage(lang) {
    _lang = lang;
    localStorage.setItem('zhiying_lang', lang);
    try {
        await fetch((localStorage.getItem('zhiying_api') || 'http://localhost:5295') + '/api/v1/settings/language', {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ language: lang })
        });
    } catch (e) { /* ignore */ }
    applyI18n();
    // Reload current tab content
    location.reload();
}
