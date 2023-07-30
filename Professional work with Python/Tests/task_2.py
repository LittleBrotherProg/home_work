import requests
import pytest
import os

class API_YA:

    def __init__(self, name):
        self.name_folder = name
        self.base_url = 'https://cloud-api.yandex.net/v1/disk/'
        self.token = os.getenv('YAME')
        # self.authorization = {'Authorization': self.token}
        self.headers = {
                        'Content-Type': 'application/json', 
                        'Authorization': self.token
                        }
        self.params = 'disk:/'
    

    def status_code(self, *args):
        return  args[1](args[0], headers=self.headers, params = args[2]).status_code
        

    def create_folder(self):
        status = self.status_code(self.base_url, 
                                  requests.get, 
                                  self.params
                                  )
        
        if status == 200:
            print(self.status_code(self.base_url + 'resources', 
                                   requests.put, 
                                   'disk:/' + self.name_folder
                                   ))
             



if __name__ == '__main__':
    ya = API_YA("test")
    ya.create_folder()