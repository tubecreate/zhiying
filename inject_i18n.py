import codecs
with codecs.open(r"c:\tubecreate-vue\zhiying\zhiying\extensions\webui\static\studio.html", "r", "utf-8") as f:
    text = f.read()

text = text.replace('<script src="/static/furniture3d.js?v=20260327"></script>', '<script src="/static/i18n.js"></script>\n    <script src="/static/furniture3d.js?v=20260327"></script>')
text = text.replace('async function init() {\n    await Promise.all', 'async function init() {\n    await loadI18nFromApi();\n    await Promise.all')

with codecs.open(r"c:\tubecreate-vue\zhiying\zhiying\extensions\webui\static\studio.html", "w", "utf-8") as f:
    f.write(text)
print("Injected successfully!")
