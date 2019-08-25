import requests
from bs4 import BeautifulSoup

BASE_URL = "http://forum.eve-ru.com/index.php?showtopic=111891"

r = requests.get(BASE_URL)

# передаём текстовые данные, а не r.content, потому что content это бинарные данные, а bs4 работает с текстом
soup = BeautifulSoup(r.text, "html.parser")  # смотреть в доке возможные парсеры

print(soup.title)  # title страницы

"""
select принимает обычный css-селектор, поэтому смотрим на странице где у нас лежат сообщения и достаём селектор
<div class="post entry-content">...</div>
"""
msgs = soup.select("div.post.entry-content")

# print(len(msgs))  # всего сообщений
# print(msgs[-1])  # выводим последнее, сейчас сообщения выводятся с кучей тегов, прям как в html структуре сайта

parsed_msgs = []

for msg in msgs:
    txt = msg.get_text().strip()  # get_text() это метод bs4, strip() это метода python
    parsed_msgs.append(txt)

print(len(parsed_msgs))
print(parsed_msgs[-1])  # сейчас здесь только текст сообщения
