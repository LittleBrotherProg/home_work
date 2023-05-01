import requests      # Для запросов по API
import json          # Для обработки полученных результатов
import time          # Для задержки между запросами

# def getAreas():
#     Moscow = requests.get('https://api.hh.ru/areas/1')
#     Saint_Petersburg = requests.get('https://api.hh.ru/areas/2')

   


def vacancies():
    url = 'https://api.hh.ru/vacancies/'
    params = {
             'per_page': '100',
             'text': 'python',
             'area': '1',

    }
    find_vacancies = requests.get(url, params={**params}).json()
    form_vacancies = []
    for page in range(find_vacancies['pages']):
        next_page = requests.get(url, params={**params, 'page':str(page)}).json()
        for id in next_page['items']:
            id = id['id'] 
            params = {
                'vacancy_id': id
            }
            res = requests.get(url + id)
            vacancies_url = res.json()["alternate_url"]
            if res.json()["salary"] == None:
                salary = 'Не указана'
            else:
                salary= res.json()["salary"]['from']
            employer = res.json()["employer"]['name']
            area = res.json()["area"]['name'] 
            vacancy = [{
                'vacancies_url': vacancies_url,
                'salary': salary,
                'department': employer,
                'area': area
            }]
            form_vacancies.append(vacancy)
        with open('test.json', 'w', encoding='UTF-8') as g:
            json.dump(form_vacancies, g, sort_keys=False,
                indent=4,
                ensure_ascii=False,
                separators=(',', ': '))

    # return h
areas = vacancies()
print(areas)




















# from selenium import webdriver






# from selenium_driver_updater import DriverUpdater
# from selenium.webdriver.common.by import By
# from time import sleep
# import json
# if __name__ == '__main__':
#     url = 'https://hh.ru/'
#     filename = DriverUpdater.install(driver_name=DriverUpdater.chromedriver)
#     # options = webdriver.ChromeOptions()
#     # options.add_argument("--start-maximized")
#     # driver = webdriver.Chrome(option)
#     driver = webdriver.Chrome(filename)
#     driver.get(url)
#     driver.maximize_window()
#     element = driver.find_element(By.XPATH, '//*[@id="a11y-search-input"]')
#     element.click()
#     sleep(2)
#     driver.find_element(By.XPATH, '//*[@id="a11y-search-input"]').send_keys('python')
#     x = driver.find_element(By.XPATH,'//*[@id="a11y-search-input"]').is_displayed()
#     element = driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div[1]/div/div/div[2]/div/form/div/div[2]/button')
#     element.click()
#     element = driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/aside/div[9]/fieldset/div[2]/div/button')
#     element.click()

#     sleep(5)
#     input_text = driver.find_element(By.CLASS_NAME, "novafilters-search-areas")
#     input_text = input_text.find_element(By.CLASS_NAME, "bloko-input-text")
#     input_text.click()
#     input_text.send_keys('Москва')
#     find_chek_box_sity = driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/aside/div[9]')
#     lol = find_chek_box_sity.find_element(By.CLASS_NAME, "novafilters-list")
#     lol.find_element(By.CLASS_NAME, 'bloko-checkbox__input').click()

#     main_info = driver.find_element(By.CLASS_NAME, 'vacancy-serp-item-body__main-info')
#     Company_name = driver.find_element(By.CLASS_NAME, 'vacancy-serp-item__info').get_property('outerText').split('\n')[0]
#     salary = main_info.find_element(By.CLASS_NAME, 'bloko-header-section-3').get_property('innerText')
#     sity = main_info.find_element(By.CLASS_NAME, 'vacancy-serp-item__info').get_property('outerText').split('\n')[1].split(',')[0]
#     element = driver.find_element(By.CLASS_NAME, 'serp-item__title')
#     element.click()
#     sleep(5)
#     link =  driver.current_url
#     get_source = driver.page_source
#     search_text = "Django"
#     search_text in get_source
#     if search_text in get_source == True:
#         data = {}
#         data['vacansy'] = []
#         data['vacansy'].append({
#             'link': link,
#             'salary': salary,
#             'Company name': Company_name,
#             'sity': sity
#         })
#         with open('job_openings.json') as file:
#             json.dump(file,data)
#     else:
#         print('False')
            
            

#     # get_source = driver.page_source
#     # search_text = 'Django'
#     # print(search_text in get_source)
    

#     print(x)
