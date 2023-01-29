class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self):
        import requests
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = {
            'Content-Type': 'application/json', 
            'Authorization': 'OAuth {}'.format(self.token)
            }
        result = requests.get(url, headers = headers)
        return result.json()



if __name__ == '__main__':
    with open('token.txt') as token:
        token = token.read()
    uploader = YaUploader(token)
    print(uploader.upload())
