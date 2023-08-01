import requests
import pytest
import os

class API_YA:

    def __init__(self):
        self.base_url = 'https://cloud-api.yandex.net/v1/disk/'
        self.token = os.getenv('YAME')
        self.headers = {
                        'Authorization': self.token
                        }
        self.params = {"path":'disk:/'}
    

    def status_code(self, *args):
        return  args[1](args[0], headers=self.headers, params = args[2]).status_code
        

    def create_folder(self, name):
        status = self.status_code(self.base_url, 
                                  requests.get, 
                                  self.params
                                  )

        if status == 200:
            self.status_code(self.base_url + 'resources', 
                             requests.put,
                             {"path": self.params["path"] + self.name_folder}
                                )
             



# if __name__ == '__main__':
#     ya = API_YA(name_folder = "test")
#     ya.create_folder()

@pytest.fixture
def preparation():
    ya = API_YA()
    ya.create_folder(name_folder = "test")

def test_yandex_disk_access():
    ya = API_YA()
    assert 200 == ya.status_code('https://cloud-api.yandex.net/v1/disk/', 
                                  requests.get, 
                                  {"path":'disk:/'})
    print("Доступ к яндекс диску есть")
    assert 400 != ya.status_code('https://cloud-api.yandex.net/v1/disk/', 
                                  requests.get, 
                                  {"path":'disk:/'})
    
def test_yandex_disk_name_folder():
    ya = API_YA()
    assert 200 == ya.status_code('https://cloud-api.yandex.net/v1/disk/resources', 
                                  requests.get, 
                                  {"path":'disk:/test'})
    print("Папка существует на яндекс диске")
    
    assert 400 != ya.status_code('https://cloud-api.yandex.net/v1/disk/resources', 
                                  requests.get, 
                                  {"path":'disk:/test'})

    assert 401 != ya.status_code('https://cloud-api.yandex.net/v1/disk/resources', 
                                  requests.get, 
                                  {"path":'disk:/test'})


    assert 404 != ya.status_code('https://cloud-api.yandex.net/v1/disk/resources', 
                                  requests.get, 
                                  {"path":'disk:/test'})