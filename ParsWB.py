import requests
import json
import os


def get_advert_to_json(url):
    count = 0
    while True:
        name = input(" Input Search Name: ")
        r = requests.get(f'{url}{name}')
        j = r.json()["adverts"]
        if j:
            try:
                path_exist = os.path.exists('json_library')
                if not path_exist:
                    os.makedirs('json_library')
                with open(f'json_library/{name}.json', 'x') as f:
                    json.dump(j, f, sort_keys=True, indent=4)
                    print(f'Файл добавлен {name}.json')
                    count += 1
            except FileExistsError:
                with open(f'json_library/{name}.json', 'w+') as f:
                    json.dump(j, f, sort_keys=True, indent=4)
                    print("Файл был перезаписан")
                    continue
        if j is None:
            print("По вашему запросу ничего не найдено")
            continue
        print(f'Кол-во записанных файлов "{count}"')


if __name__ == '__main__':
    base_url = "https://catalog-ads.wildberries.ru/api/v5/search?keyword="
    get_advert_to_json(base_url)
