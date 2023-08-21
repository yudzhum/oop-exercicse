# Реализуйте функцию stringify(), которая принимает на вход тег и возвращает его текстовое представление.
# В структуре тега есть три специальных ключа:
# name — имя тега
# tag_type — тип тега, определяет его парность (pair) или одиночность (single)
# body — тело тега, используется для парных тегов. Если у парного тега нет содержимого, то body равно пустой строке ''.
# Всё остальное становится атрибутами тега и не зависит от того, парный он или нет.

hr_tag = {
  'name': 'hr',
  'class': 'px-3',
  'id': 'myid',
  'tag_type': 'single',
}
# html = stringify(hr_tag) ## <hr class="px-3" id="myid">
 
div_tag = {
  'name': 'div',
  'tag_type': 'pair',
  'body': 'text2',
  'id': 'wow',
}
# html = stringify(div_tag) ## <div id="wow">text2</div>
 
empty_div_tag = {
  'name': 'div',
  'tag_type': 'pair',
  'body': '',
  'id': 'empty',
}
# html = stringify(empty_div_tag) ## <div id="empty"></div>

exluded_attrs = ['name', 'tag_type', 'body']

def build_attrs(tag):
    acc = []
    for attr in tag:
        if attr not in exluded_attrs:
            acc.append(f' {attr}="{tag[attr]}"')
    return ''.join(acc)


stringify_type = {
    'pair': lambda tag: f'<{tag["name"]}{build_attrs(tag)}>{tag["body"]}</{tag["name"]}>',
    'single': lambda tag: f'<{tag["name"]}{build_attrs(tag)}>' 
}

def stringify(tag):
    build = stringify_type.get(tag['tag_type'])
    return build(tag)

print(stringify(div_tag))
print(stringify(hr_tag))
print(stringify(empty_div_tag))
