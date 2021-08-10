from pprint import pprint
import requests
import os

API_BASE_URL = "https://cloud-api.yandex.net/"

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать

        headers = {
            'accept': 'application/json',
            'authorization': f'OAuth {self.token}'
        }

        files_list_dir = os.listdir(file_path)

        for file_name_item in files_list_dir:

            r = requests.get(API_BASE_URL + "v1/disk/resources/upload", params={'path': file_name_item}, headers=headers)
            pprint(r.status_code)
            pprint(r.json())

            upload_url = r.json()["href"]
            r = requests.put(upload_url, files={'file': open(file_path+'/'+file_name_item, 'rb')})


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = str(input('Укажите путь: '))
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
