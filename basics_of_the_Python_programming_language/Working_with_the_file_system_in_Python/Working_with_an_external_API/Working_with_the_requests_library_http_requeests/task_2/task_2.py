import requests
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, path_to_file: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
            'Content-Type': 'application/json', 
            'Authorization': self.token
            }
        params = {'path': path_to_file, 'overwrite': True}
        link = requests.get(url, headers = headers, params=params)
        upload = requests.put((link.json()).get('href'), data=open(r'.\\8112.jpg', 'rb'))
        return upload



if __name__ == '__main__':
    path_to_file = 'Загрузки/8112.jpg'
    token = (input('Введите свой токен от яндекс диска'))
    uploader = YaUploader(token)
    print(uploader.upload(path_to_file))
