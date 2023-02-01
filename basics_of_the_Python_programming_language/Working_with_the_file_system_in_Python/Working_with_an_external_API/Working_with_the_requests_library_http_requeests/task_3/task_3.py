import requests
import datetime
class apiSW():
    def __init__(self, tags, date):
        self.tags = tags
        self.date_ = date

    def count_date(self):
        max_date = datetime.datetime.today().date()
        min_date = str(max_date - datetime.timedelta(days=self.date_))
        return [min_date, str(max_date)]

    def tag(self):
        data = self.count_date()
        for index in range(1, 25):
            api_url = 'https://api.stackexchange.com'
            url = f'{api_url}/2.3/questions?page={index}&pagesize=100&fromdate={data[0]}&todate={data[1]}&order=desc&sort=creation&tagged={self.tags}&site=stackoverflow'
            request = requests.get(f'{url}')
            json = request.json()
            items = json.get('items')
            if len(items) != 0 or items is not None:
                for item in items:
                    print(item.get('title'), str(datetime.datetime.fromtimestamp(item.get('creation_date')).date()))
            else:
                return        
                    
                    

date_input = int(input('Введите за какое колчисевтво дней вы хотите посомтреть запросы'))
tags = input('Введите язык программирования по которому хотите отсортировать запросы').lower()
result = apiSW(tags, date_input)
result.tag()



