import requests
from pprint import pprint

BASE_URL = "https://api.hh.ru"

vac_r = requests.get(BASE_URL + "/vacancies")

vacancies = vac_r.json()["items"]
first_vac = vacancies[0]  # тут краткое описание

full_vac = requests.get(BASE_URL + "/vacancies/" + first_vac["id"])  # тут уже расширенное

pprint(full_vac.json())

# или вот такой запрос например
py_vac_r = requests.get(BASE_URL + "/vacancies/?text=python")
pprint(py_vac_r.json())
