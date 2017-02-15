import re

def gen():
    with open ("викинги.txt", "r", encoding="utf-8") as f:
        text=f.read()
        vikings='ви.?кинг((?:а(?:ми?|х)?)|и|о(?:в|м)|у|е)?([\s,.!-&\?:"\(\)\'»<])'
        Vikings='Ви.?кинг((?:а(?:ми?|х)?)|и|о(?:в|м)|у|е)?([\s,.!-&\?:"\(\)\'»<])'
        text_changed = re.sub(vikings,'бурундук\\1\\2', text)
        text_changed = re.sub(Vikings,'Бурундук\\1\\2', text_changed)
        with open('brand_new vikings.txt', 'w', encoding = 'utf-8') as new:
            new.write(text_changed)
gen()
