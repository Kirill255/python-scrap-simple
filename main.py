from pathlib import Path
import requests

BASE_URL = "http://forum.eve-ru.com/index.php?showtopic=111891&page={page_num}"
BASE_SAVE_PATH = Path("./result")

for i in range(1, 4):
    r = requests.get(BASE_URL.format(page_num=i))

    print(r.status_code)
    # print(r.content)

    # путь куда положить данные ./result/index_1.html
    html_file_path = BASE_SAVE_PATH / "index_{page_num}.html".format(page_num=i)

    # открыть на запись в бинарном виде
    with open(str(html_file_path.absolute()), "wb") as f:
        f.write(r.content)
