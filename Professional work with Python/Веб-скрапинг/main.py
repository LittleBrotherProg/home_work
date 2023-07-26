import requests      # Для запросов по API
import json          # Для обработки полученных результатов
import time          # Для задержки между запросами
from progress.bar import IncrementalBar
from progress.spinner import MoonSpinner

class hh:

    def __init__(self, url, text, area, additional_words, country):
        self.url = url
        self.text = text
        self.area = area.split(',')
        self.additional_words = additional_words.split(',')
        self.country = country

    def search_id_area(self):
        all_country = requests.get(url + '/areas/countries').json()
        for country in all_country:
            if country['name'] == self.country:
                id_country = country['id']
                break
        all_areas = requests.get(url + '/areas/' + id_country).json()
        id_areas = []
        for input_area in self.area:
            input_area = input_area.replace(' ', '')
            for area in all_areas['areas']:
                if area['name'] == input_area:
                    id_areas.append(area['id'])
        return id_areas

    def find(self):
        all_vacancies = []
        for id_area in Vacancies.search_id_area():
            params = {
                    'per_page': '100',
                    'text': self.text,
                    'area': id_area,

            }
            find_vacancies = requests.get(url + '/vacancies', params={**params}).json()
            progress_find_vacancies = IncrementalBar('Сохранения результатов поиска вакансий', max= find_vacancies['pages'])
            for page in range(find_vacancies['pages']):
                params['page'] = str(page)
                next_page = requests.get(url + '/vacancies', params={**params}).json()
                all_vacancies.append(next_page['items'])
                progress_find_vacancies.next()
            progress_find_vacancies.finish()
            print('Все найденые вакансии сохранены в список all_vacancies')
        return all_vacancies
    
    def processing(self, all_vacancies):
        selected_vacancies = []
        for aw in self.additional_words:
            aw = aw.replace(' ', '')
            progress_all_vacancies = MoonSpinner(f'Поиск вакансий с упоминанием {aw}')
            for index in range(len(all_vacancies)):
                progress_all_vacancies.next()
                time.sleep(1)
                for processing in all_vacancies[index]:
                    vacancies_url = processing["alternate_url"]
                    if processing["salary"] == None:
                        salary = 'Не указана'
                    else:
                        salary= processing["salary"]['from']
                    employer = processing["employer"]['name']
                    area = processing["area"]['name']
                    vacancy = [{
                        'vacancies_url': vacancies_url,
                        'salary': salary,
                        'department': employer,
                        'area': area
                    }]
                    snippet = processing['snippet']
                    if snippet != None:
                        if snippet['responsibility'] != None:
                            if snippet['responsibility'].count(aw) > 0:
                                selected_vacancies.append(vacancy)
            progress_all_vacancies.finish()
        return selected_vacancies
    
    def writing_to_json(self, selected_vacancies):
        with open('test.json', 'w', encoding='UTF-8') as file:
            json.dump(selected_vacancies, 
                      file, sort_keys=False,
                      indent=4,
                      ensure_ascii=False,
                      separators=(',', ': ')
                      )
        print('Completed successfully. The sorted vacancies were recorded in a file .json')

if __name__ == '__main__' :
    url = 'https://api.hh.ru'
    country = input('Введите страну в которой будет вестись поиск вакансий' '\n').capitalize()
    area = input('Введите города через запятую по которым будет ввестись поиск вакансий' '\n')
    text = input('Введите слово по которому программа будет искать вакансию' '\n').capitalize()
    additional_words = input('Введите слово или слова через запятую которые должны будут присутствовать в описании к вакансии \n')
    Vacancies = hh(url, text, area, additional_words, country)
    all_vacancies = Vacancies.find()
    selected_vacancies = Vacancies.processing(all_vacancies)
    writing = Vacancies.writing_to_json(selected_vacancies)





