import requests      # Для запросов по API
import json          # Для обработки полученных результатов
import time          # Для задержки между запросами


def vacancies():
    url = 'https://api.hh.ru/vacancies/'
    params = {
             'per_page': '100',
             'text': 'python',
             'area': '1',

    }
    find_vacancies = requests.get(url, params={**params}).json()
    all_vacancies = []
    form_vacancies = []
    for page in range(find_vacancies['pages']):
        params['page'] = str(page)
        next_page = requests.get(url, params={**params}).json()
        all_vacancies.append(next_page['items'])
    for index in range(len(all_vacancies)):
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
            if processing['snippet'] != None:
                if processing['snippet']['responsibility'] != None:
                    if processing['snippet']['responsibility'].count('Django') > 0  or processing['snippet']['responsibility'].count('Flask') > 0 :
                        form_vacancies.append(vacancy)
    with open('test.json', 'w', encoding='UTF-8') as g:
        json.dump(form_vacancies, g, sort_keys=False,
            indent=4,
            ensure_ascii=False,
            separators=(',', ': '))

areas = vacancies()
print(areas)