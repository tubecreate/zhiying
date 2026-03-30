import json
import os
import re

BUILTIN_ASSETS = [
    {"id":"desk_modern","name":"Bàn hiện đại"},
    {"id":"desk_wood","name":"Bàn gỗ cổ điển"},
    {"id":"chair_office","name":"Ghế xoay"},
    {"id":"sofa","name":"Sofa"},
    {"id":"bookshelf","name":"Tủ sách"},
    {"id":"table_round","name":"Bàn tròn"},
    {"id":"cabinet","name":"Tủ hồ sơ"},
    {"id":"plant_pot","name":"Chậu cây"},
    {"id":"plant_tall","name":"Cây cao"},
    {"id":"plant_cactus","name":"Xương rồng"},
    {"id":"aquarium_small","name":"Bể cá nhỏ"},
    {"id":"aquarium_large","name":"Bể cá lớn"},
    {"id":"terrarium","name":"Tiểu cảnh"},
    {"id":"rock_garden","name":"Hòn non bộ"},
    {"id":"lantern","name":"Đèn lồng"},
    {"id":"whiteboard","name":"Bảng trắng"},
    {"id":"monitor","name":"Màn hình"},
    {"id":"pillar_red","name":"Cột đỏ"},
    {"id":"wall_segment","name":"Tường"},
    {"id":"wall_partition_solid","name":"Vách ngăn 2m"},
    {"id":"wall_partition_glass","name":"Vách kính 2m"},
    {"id":"wall_partition_1m","name":"Vách ngăn 1m"},
    {"id":"wall_partition_glass_1m","name":"Vách kính 1m"},
    {"id":"floor_tile","name":"Ô sàn"},
    {"id":"door_frame","name":"Cửa ra vào"},
    {"id":"chair_classic","name":"Ghế cổ điển"},
    {"id":"chair_dining","name":"Ghế bàn ăn"},
    {"id":"fridge","name":"Tủ lạnh"},
    {"id":"washing_machine","name":"Máy giặt"},
    {"id":"bar_counter","name":"Bar nước"},
    {"id":"coffee_machine","name":"Máy pha cà phê"},
    {"id":"pool_table","name":"Bàn bida"},
    {"id":"conference_table_rect","name":"Bàn hội nghị dài"},
    {"id":"conference_table_oval","name":"Bàn tròn bầu hội nghị"},
    {"id":"meeting_table_small","name":"Bàn họp nhỏ (4 người)"},
    {"id":"meeting_table_large","name":"Bàn họp lớn (6 người)"},
    {"id":"workstation","name":"Bàn làm việc (trọn bộ)"},
]

translations = {
    "vi": { f"studio.item.{item['id']}": item['name'] for item in BUILTIN_ASSETS },
    "en": {
        "studio.item.desk_modern": "Modern Desk",
        "studio.item.desk_wood": "Classic Wood Desk",
        "studio.item.chair_office": "Office Chair",
        "studio.item.sofa": "Sofa",
        "studio.item.bookshelf": "Bookshelf",
        "studio.item.table_round": "Round Table",
        "studio.item.cabinet": "Filing Cabinet",
        "studio.item.plant_pot": "Potted Plant",
        "studio.item.plant_tall": "Tall Plant",
        "studio.item.plant_cactus": "Cactus",
        "studio.item.aquarium_small": "Small Aquarium",
        "studio.item.aquarium_large": "Large Aquarium",
        "studio.item.terrarium": "Terrarium",
        "studio.item.rock_garden": "Rock Garden",
        "studio.item.lantern": "Lantern",
        "studio.item.whiteboard": "Whiteboard",
        "studio.item.monitor": "Monitor",
        "studio.item.pillar_red": "Red Pillar",
        "studio.item.wall_segment": "Wall",
        "studio.item.wall_partition_solid": "Partition 2m",
        "studio.item.wall_partition_glass": "Glass Partition 2m",
        "studio.item.wall_partition_1m": "Partition 1m",
        "studio.item.wall_partition_glass_1m": "Glass Partition 1m",
        "studio.item.floor_tile": "Floor Tile",
        "studio.item.door_frame": "Door Frame",
        "studio.item.chair_classic": "Classic Chair",
        "studio.item.chair_dining": "Dining Chair",
        "studio.item.fridge": "Fridge",
        "studio.item.washing_machine": "Washing Machine",
        "studio.item.bar_counter": "Bar Counter",
        "studio.item.coffee_machine": "Coffee Machine",
        "studio.item.pool_table": "Pool Table",
        "studio.item.conference_table_rect": "Long Conference Table",
        "studio.item.conference_table_oval": "Oval Conference Table",
        "studio.item.meeting_table_small": "Small Meeting Table (4 persons)",
        "studio.item.meeting_table_large": "Large Meeting Table (6 persons)",
        "studio.item.workstation": "Workstation (Full set)"
    },
    "zh": {
        "studio.item.desk_modern": "现代办公桌",
        "studio.item.desk_wood": "经典木桌",
        "studio.item.chair_office": "办公椅",
        "studio.item.sofa": "沙发",
        "studio.item.bookshelf": "书柜",
        "studio.item.table_round": "圆桌",
        "studio.item.cabinet": "文件柜",
        "studio.item.plant_pot": "盆栽",
        "studio.item.plant_tall": "高大植物",
        "studio.item.plant_cactus": "仙人掌",
        "studio.item.aquarium_small": "小鱼缸",
        "studio.item.aquarium_large": "大鱼缸",
        "studio.item.terrarium": "微型景观",
        "studio.item.rock_garden": "假山",
        "studio.item.lantern": "灯笼",
        "studio.item.whiteboard": "白板",
        "studio.item.monitor": "显示器",
        "studio.item.pillar_red": "红柱子",
        "studio.item.wall_segment": "墙壁",
        "studio.item.wall_partition_solid": "2米隔断",
        "studio.item.wall_partition_glass": "2米玻璃隔断",
        "studio.item.wall_partition_1m": "1米隔断",
        "studio.item.wall_partition_glass_1m": "1米玻璃隔断",
        "studio.item.floor_tile": "地砖",
        "studio.item.door_frame": "门框",
        "studio.item.chair_classic": "经典椅子",
        "studio.item.chair_dining": "餐椅",
        "studio.item.fridge": "冰箱",
        "studio.item.washing_machine": "洗衣机",
        "studio.item.bar_counter": "吧台",
        "studio.item.coffee_machine": "咖啡机",
        "studio.item.pool_table": "台球桌",
        "studio.item.conference_table_rect": "长会议桌",
        "studio.item.conference_table_oval": "椭圆会议桌",
        "studio.item.meeting_table_small": "小会议桌 (4人)",
        "studio.item.meeting_table_large": "大会议桌 (6人)",
        "studio.item.workstation": "全套工作站"
    }
}

studio_dir = r"c:\tubecreate-vue\zhiying\zhiying\extensions\studio3d\locales"
for lang, klist in translations.items():
    fp = os.path.join(studio_dir, f"{lang}.json")
    if os.path.isfile(fp):
        with open(fp, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = {}
    data.update(klist)
    with open(fp, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# Patch HTML
html_file = r"c:\tubecreate-vue\zhiying\zhiying\extensions\webui\static\studio.html"
with open(html_file, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<span class="label">${a.name}</span>', '<span class="label" data-i18n="studio.item.${a.id}">${a.name}</span>')
text = text.replace('title="${a.name}"', 'title="${T(\'studio.item.\' + a.id) || a.name}"')
text = text.replace("T('studio.selected')}: ${assets.find(a => a.id === id)?.name}", "T('studio.selected')}: ${T('studio.item.' + id) || assets.find(a => a.id === id)?.name}")
text = text.replace('<span class="pi-name">${def ? def.name : p.asset_id}</span>', '<span class="pi-name">${T(\'studio.item.\' + p.asset_id) || (def ? def.name : p.asset_id)}</span>')
text = text.replace('<span class="pi-name">${def.name}</span>', '<span class="pi-name">${T(\'studio.item.\' + def.id) || def.name}</span>')

# For placed list, to be sure:
text = text.replace("document.getElementById('placed-list').innerHTML = list.map(p => {", "document.getElementById('placed-list').innerHTML = list.map(p => {")
# If applyI18n needs to be called, we can just inject it whenever renderAssetList is called
text = text.replace("    }).join('');", "    }).join('');\n    if (typeof applyI18n === 'function') setTimeout(applyI18n, 10);")
text = text.replace("    `).join('');\n}", "    `).join('');\n    if (typeof applyI18n === 'function') setTimeout(applyI18n, 10);\n}")

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(text)

print("Items localized.")
