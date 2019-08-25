import requests
from pprint import pprint

BASE_URL = "http://jsonplaceholder.typicode.com/photos"

r = requests.get(BASE_URL)

# print(r.content) # грубо говоря тут ещё строка
# print(r.json())  # тут уже json объект(список []) с которым можно работать

parsed_json = r.json()

print(parsed_json[0])
pprint(parsed_json[0])  # pprint(pretty print) более красивый вывод, это встроенная в python библиотека

last_photo = parsed_json[0]

photo_r = requests.get(last_photo["url"])

pprint(photo_r.content)
