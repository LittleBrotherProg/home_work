from selenium import webdriver
from selenium_driver_updater import DriverUpdater
from selenium.webdriver.common.by import By
from time import sleep
if __name__ == '__main__':
    url = 'https://hh.ru/'
    filename = DriverUpdater.install(driver_name=DriverUpdater.chromedriver)
    # options = webdriver.ChromeOptions()
    # options.add_argument("--start-maximized")
    # driver = webdriver.Chrome(option)
    driver = webdriver.Chrome(filename)
    driver.get(url)
    driver.maximize_window()
    element = driver.find_element(By.XPATH, '//*[@id="a11y-search-input"]')
    element.click()
    driver.find_element(By.XPATH, '//*[@id="a11y-search-input"]').send_keys('python')
    x = driver.find_element(By.XPATH,'//*[@id="a11y-search-input"]').is_displayed()
    element = driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div[1]/div/div/div[2]/div/form/div/div[2]/button')
    element.click()
    element = driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/aside/div[9]/fieldset/div[2]/div/button')
    element.click()
    element = driver.find_element(By.CLASS_NAME, 'serp-item__title')
    element.click()
    sleep(5)
    print(driver.find_element(By.XPATH, ("//span[contains(text(),\'Django')]")))
    # get_source = driver.page_source
    # search_text = 'Django'
    # print(search_text in get_source)

    print(x)
