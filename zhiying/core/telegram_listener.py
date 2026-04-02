import asyncio
import httpx
import traceback
import datetime
from typing import Dict, Any

from zhiying.core.agent import agent_manager
from zhiying.core.brain import AgentBrain

# Try to find global settings file
from zhiying.config import DATA_DIR
import os
import json

SETTINGS_FILE = DATA_DIR / "global_settings.json"

class TelegramListener:
    def __init__(self):
        self.running = False
        self.polling_tasks: Dict[str, asyncio.Task] = {}
        self.offsets: Dict[str, int] = {}
        self._sync_task = None
        self.client = httpx.AsyncClient(timeout=40)

    def get_configured_tokens(self) -> Dict[str, Dict[str, Any]]:
        """Finds all configured tokens and associated context (agent or global)"""
        tokens = {}
        
        # 1. Global Token (Orchestrator bot mapping)
        global_token = None
        if os.path.exists(SETTINGS_FILE):
            try:
                with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    global_token = data.get("telegram_bot_token")
            except Exception:
                pass
        
        if global_token:
            global_token = global_token.strip()
            # If global token is set, it might route to "global" or a default agent
            # We will use it just as a generic "System AI" wrapper or if there's a primary orchestrator agent
            tokens[global_token] = {"type": "global"}
            
        # 2. Agent-specific Tokens
        agents = agent_manager.get_all()
        for a in agents:
            if a.telegram_token:
                tok = a.telegram_token.strip()
                if tok:
                    tokens[tok] = {"type": "agent", "agent_id": a.id, "agent_name": a.name}
                    
        return tokens

    async def _poll_for_token(self, token: str, context: Dict[str, Any]):
        """Long-polling loop for a specific telegram bot token"""
        bot_name = context.get('agent_name', 'Global')
        print(f"[TelegramListener] Starting polling for {bot_name} Bot...")
        
        # CRITICAL: Delete any existing webhook first, otherwise getUpdates returns 409
        try:
            del_resp = await self.client.get(
                f"https://api.telegram.org/bot{token}/deleteWebhook",
                params={"drop_pending_updates": "false"},
                timeout=10
            )
            del_data = del_resp.json()
            if del_data.get("ok"):
                print(f"[TelegramListener] Webhook cleared for {bot_name} Bot")
            else:
                print(f"[TelegramListener] Webhook clear warning: {del_data}")
        except Exception as e:
            print(f"[TelegramListener] Webhook clear error: {e}")

        url = f"https://api.telegram.org/bot{token}/getUpdates"
        send_url = f"https://api.telegram.org/bot{token}/sendMessage"
        
        while self.running:
            try:
                offset = self.offsets.get(token, 0)
                # Long polling: timeout 30s
                resp = await self.client.get(url, params={"offset": offset, "timeout": 30})
                
                if resp.status_code != 200:
                    if resp.status_code == 401:
                        print(f"[TelegramListener] Invalid token for {context.get('agent_name', 'Global')} Bot")
                        break # stop polling this invalid token
                    await asyncio.sleep(5)
                    continue

                data = resp.json()
                if not data.get("ok"):
                    await asyncio.sleep(5)
                    continue

                updates = data.get("result", [])
                for update in updates:
                    update_id = update["update_id"]
                    self.offsets[token] = update_id + 1
                    
                    message = update.get("message")
                    if not message or "text" not in message:
                        continue
                        
                    chat_id = message["chat"]["id"]
                    text = message["text"]
                    
                    print(f"💬 [Telegram -> {context.get('agent_name', 'Global')}] {chat_id}: {text}")
                    
                    # --- Process with Brain ---
                    reply_text = await self._process_message(text, context)
                    
                    # Send response back
                    if reply_text:
                        await self.client.post(send_url, json={
                            "chat_id": chat_id,
                            "text": reply_text
                        })
                        
            except asyncio.CancelledError:
                break
            except Exception as e:
                print(f"[TelegramListener] Polling error for {context.get('agent_name', 'Global')}: {e}")
                await asyncio.sleep(5)

    def _build_extension_capabilities(self) -> str:
        """Build a description of available system capabilities for the AI."""
        return """### SYSTEM CAPABILITIES (bạn có thể gọi các chức năng này):

1. **Tạo Team AI** — Tạo đội nhóm AI agents phối hợp
   - Template: dev_team (💻 Dev Team), imperial_court (🏯 Triều Đình), company (🏢 Company), military (🎖️ Military)
   - Nếu user muốn tạo team, trả lời JSON: {"action": "create_team", "template": "dev_team", "name": "Tên team", "member_count": 4}

2. **3D Studio** — Tạo/quản lý studio 3D cho team
   - Nếu user muốn thiết kế studio: {"action": "open_studio", "team_name": "..."}

3. **Download Video** — Tải video từ YouTube, TikTok, etc.
   - {"action": "download_video", "url": "..."}

4. **Browser Automation** — Tự động hóa trình duyệt
   - {"action": "run_browser", "task": "..."}

5. **Workflow Builder** — Tạo và chạy workflow tự động
   - {"action": "create_workflow", "description": "..."}

6. **Market** — Mua/bán extensions và skills
   - {"action": "open_market"}

7. **Sheets Manager** — Quản lý Google Sheets
   - {"action": "sheets_manager", "task": "..."}

8. **Livestream** — Quản lý livestream
   - {"action": "start_livestream", "platform": "..."}

### QUY TẮC KHI NHẬN LỆNH TỪ TELEGRAM:
- Nếu user yêu cầu tạo team/nhóm → dùng action create_team
- Nếu user hỏi chuyện bình thường → trả lời bình thường, thân thiện
- Nếu user yêu cầu download → dùng action download_video
- Nếu user yêu cầu mở browser → dùng action run_browser
- Nếu nhận diện được ý định gọi chức năng hệ thống: trả lời JSON action block
- Nếu là trò chuyện thông thường: trả lời text tự nhiên

### THÔNG TIN VỀ CHỦ NHÂN:
- Chủ nhân giao tiếp qua Telegram
- Hệ thống là ZhiYing AI — nền tảng AI Agent đa năng
- Bạn là AI Tổng (Orchestrator) — quản lý toàn bộ sub-agents và extensions
"""

    def _get_cloud_model_config(self) -> Dict[str, Any]:
        """Read cloud API model from global settings."""
        try:
            if os.path.exists(SETTINGS_FILE):
                with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                model = data.get("default_model", "")
                if model and model != "qwen:latest":
                    return {"model": model}
        except Exception:
            pass
        return {}

    async def _process_message(self, text: str, context: Dict[str, Any]) -> str:
        """Route message to Brain and return reply"""
        from zhiying.core.skill import skill_manager

        agent_id = context.get("agent_id")

        if not agent_id:
            agents = agent_manager.get_all()
            if not agents:
                return "Tôi chưa được cấu hình Agent nào trong hệ thống."
            main_agent = next(
                (a for a in agents if "tổng" in a.name.lower() or "orchestra" in a.name.lower()),
                agents[0]
            )
            agent_id = main_agent.id

        agent = agent_manager.get(agent_id)
        if not agent:
            return "Lỗi: Không tìm thấy Agent cấu hình."

        agent_dict = agent.to_dict()

        # Override model with global settings if agent uses default/None
        cloud_cfg = self._get_cloud_model_config()
        if cloud_cfg.get("model") and (not agent_dict.get("model") or agent_dict["model"] == "qwen:latest"):
            agent_dict["model"] = cloud_cfg["model"]

        # Read cloud API keys from cloud_api_keys.json (Cloud API extension)
        try:
            from zhiying.extensions.cloud_api.extension import key_manager
            cloud_keys = {}
            for provider in ["gemini", "openai", "claude", "deepseek"]:
                key = key_manager.get_active_key(provider)
                if key:
                    cloud_keys[provider] = key
            if cloud_keys:
                agent_dict["cloud_api_keys"] = {**agent_dict.get("cloud_api_keys", {}), **cloud_keys}
        except Exception:
            pass

        # Inject extension capabilities into system prompt
        ext_capabilities = self._build_extension_capabilities()
        original_prompt = agent_dict.get("system_prompt", "You are a helpful assistant.")
        agent_dict["system_prompt"] = f"{original_prompt}\n\n{ext_capabilities}"

        # Get allowed skills
        all_skills = skill_manager.get_all()
        if agent.allowed_skills:
            skills = [s.to_dict() for s in all_skills if s.id in agent.allowed_skills]
        else:
            skills = [s.to_dict() for s in all_skills]

        history = agent.history_log or []

        # Run Brain chat
        brain_result = AgentBrain.chat(
            message=text,
            agent=agent_dict,
            skills=skills,
            history=history,
        )

        reply = brain_result.get("reply", "...")
        action = brain_result.get("action")
        skill_used = None

        # If skill needed
        if action == "run_skill" and brain_result.get("skill_id"):
            skill_id = brain_result["skill_id"]
            skill = skill_manager.get(skill_id)
            if skill:
                skill_used = skill.name
                skill_input = brain_result.get("skill_input", text)
                try:
                    reply = await AgentBrain.autonomous_run(
                        message=skill_input,
                        agent=agent_dict,
                        skill=skill.to_dict()
                    )
                    skill_manager.update(skill_id, last_run=datetime.datetime.now().isoformat())
                except Exception as e:
                    reply = f"[Skill Error] {e}"

        elif action == "create_skill":
            name = brain_result.get("skill_name", "New Skill")
            desc = brain_result.get("skill_desc", "")
            instructions = brain_result.get("skill_instructions", [])
            sop_text = "\n".join([f"{i+1}. {instr}" for i, instr in enumerate(instructions)])
            try:
                skill_manager.create(
                    name=name, description=desc, skill_type="AI Self-Created",
                    workflow_data={"sop": sop_text, "nodes": [{"type": "text", "data": {"text": sop_text}}]},
                    commands=[name.lower()]
                )
                skill_used = f"Created: {name}"
            except Exception as e:
                reply = f"[Create Skill Error] {e}"

        # --- Handle Extension Actions from AI response ---
        reply = await self._handle_extension_action(reply, agent_dict)

        # Save History
        history.append({"role": "user", "content": text, "timestamp": datetime.datetime.now().isoformat()})
        history.append({"role": "assistant", "content": reply, "timestamp": datetime.datetime.now().isoformat(), "skill_used": skill_used})
        if len(history) > 50:
            history = history[-50:]

        # Non-blocking memory update
        async def _bg_mem():
            try:
                AgentBrain.post_chat_memory_update(agent_id, agent_dict, history)
                agent_manager.update(agent_id, history_log=history)
            except Exception as e:
                print(f"[TelegramListener] Memory err: {e}")
        asyncio.create_task(_bg_mem())

        # Save immediate context
        agent_manager.update(agent_id, history_log=history)

        return reply

    async def _handle_extension_action(self, reply: str, agent_dict: Dict) -> str:
        """Parse AI reply for JSON action blocks and execute extension logic."""
        import re

        # Try to extract JSON action from the reply
        action_match = re.search(r'\{["\']action["\']\s*:\s*["\'](\w+)["\'].*?\}', reply, re.DOTALL)
        if not action_match:
            return reply

        try:
            # Extract full JSON
            json_match = re.search(r'(\{.*?"action".*?\})', reply, re.DOTALL)
            if not json_match:
                return reply
            action_data = json.loads(json_match.group(1))
        except (json.JSONDecodeError, Exception):
            return reply

        action_type = action_data.get("action", "")
        print(f"🔧 [TelegramListener] Extension action detected: {action_type}")

        if action_type == "create_team":
            return await self._exec_create_team(action_data)
        elif action_type == "download_video":
            return f"📥 Đang tải video: {action_data.get('url', '...')}. Vui lòng mở Dashboard để xem tiến trình."
        elif action_type in ("open_studio", "open_market", "start_livestream"):
            return f"✅ Đã ghi nhận yêu cầu '{action_type}'. Vui lòng mở Dashboard để thao tác trực quan."
        else:
            return reply

    async def _exec_create_team(self, action_data: Dict) -> str:
        """Execute create_team action via the multi-agents extension."""
        try:
            import httpx
            template = action_data.get("template", "dev_team")
            name = action_data.get("name", "New Team")

            async with httpx.AsyncClient(timeout=15) as client:
                resp = await client.post(
                    "http://localhost:5295/api/v1/multi-agents/teams/from-template",
                    json={"template_id": template, "name": name}
                )
                if resp.status_code == 200:
                    data = resp.json()
                    team = data.get("team", {})
                    node_count = len(team.get("nodes", []))
                    return (
                        f"✅ Đã tạo team '{team.get('name', name)}' thành công!\n"
                        f"📋 Template: {template}\n"
                        f"👥 Số lượng roles: {node_count}\n"
                        f"🆔 Team ID: {team.get('id', 'N/A')}\n\n"
                        f"Mở Dashboard → Teams để xem chi tiết và gán agent."
                    )
                else:
                    return f"❌ Tạo team thất bại: {resp.text[:200]}"
        except Exception as e:
            return f"❌ Lỗi tạo team: {e}"

    async def _sync_loop(self):
        """Periodically syncs polling tasks with configured tokens"""
        while self.running:
            configured_tokens = self.get_configured_tokens()
            
            # Start new ones
            for token, ctx in configured_tokens.items():
                if token not in self.polling_tasks:
                    self.polling_tasks[token] = asyncio.create_task(self._poll_for_token(token, ctx))
                    
            # Stop removed ones
            to_stop = []
            for token in self.polling_tasks.keys():
                if token not in configured_tokens:
                    to_stop.append(token)
                    
            for token in to_stop:
                self.polling_tasks[token].cancel()
                del self.polling_tasks[token]
                print(f"[TelegramListener] Stopped polling for removed token")
                
            await asyncio.sleep(10) # check for new bots every 10 seconds

    def start(self):
        if self.running:
            return
        self.running = True
        self._sync_task = asyncio.create_task(self._sync_loop())
        print("🤖 [TelegramListener] Background service started")

    async def stop(self):
        self.running = False
        if self._sync_task:
            self._sync_task.cancel()
        for tk, task in self.polling_tasks.items():
            task.cancel()
        self.polling_tasks.clear()
        await self.client.aclose()
        print("🤖 [TelegramListener] Background service stopped")

telegram_listener = TelegramListener()
