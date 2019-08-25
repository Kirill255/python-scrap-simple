import requests
from pprint import pprint

BASE_URL = "https://api.github.com/users/AlwxSin"

r = requests.get(BASE_URL)

parsed_json = r.json()

pprint(parsed_json)

name = parsed_json["name"]
avatar_url = parsed_json["avatar_url"]

print(name)
print(avatar_url)

repos_url = requests.get(parsed_json["repos_url"])
pprint(repos_url.json())
