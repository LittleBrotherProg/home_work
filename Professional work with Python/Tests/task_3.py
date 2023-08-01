from selenium import webdriver, common
from selenium_driver_updater import DriverUpdater
from selenium.webdriver.common.by import By
import time


def test_сyrillic_login(login ='Ненадо_дядя'):
    filename =DriverUpdater.install(driver_name=DriverUpdater.chromedriver)
    url = "https://passport.yandex.ru/auth/"
    driver = webdriver.Chrome(filename)
    driver.get(url)
    xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[1]/div[1]/button'
    driver.find_element(By.XPATH,  xpath).click()
    time.sleep(1)
    driver.find_element(By.ID,  'passp-field-login').click()
    time.sleep(1)
    driver.find_element(By.ID,  'passp-field-login').send_keys(login)
    time.sleep(1)
    driver.find_element(By.ID,  'passp:sign-in').click()
    time.sleep(1)
    check = driver.find_element(By.ID, 'field:input-login:hint').text
    assert "Такой логин не подойдет" == check, 'Яндекс не распознал кириллицу в поле логин'

def test_not_сyrillic_login(login ='Ненадо_дядя'):
    filename =DriverUpdater.install(driver_name=DriverUpdater.chromedriver)
    url = "https://passport.yandex.ru/auth/"
    driver = webdriver.Chrome(filename)
    driver.get(url)
    xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[1]/div[1]/button'
    driver.find_element(By.XPATH,  xpath).click()
    time.sleep(1)
    driver.find_element(By.ID,  'passp-field-login').click()
    time.sleep(1)
    driver.find_element(By.ID,  'passp-field-login').send_keys(login)
    time.sleep(1)
    check = driver.find_element(By.ID,  'passp:sign-in').click()
    time.sleep(1)
    try:
        driver.find_element(By.CLASS_NAME, 'CurrentAccount-displayName').text
    except common.exceptions.NoSuchElementException:
        check = driver.find_element(By.ID, 'field:input-login:hint').text
        assert "Такой логин не подойдет" == check, 'Яндекс не распознал кириллицу в поле логин'

def test_bad_password(login ='apple', password ='Ненадо_дядя'):
    filename =DriverUpdater.install(driver_name=DriverUpdater.chromedriver)
    url = "https://passport.yandex.ru/auth/"
    driver = webdriver.Chrome(filename)
    driver.get(url)
    time.sleep(5)
    parent  =  driver.find_element(By.XPATH,  '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[1]/div[1]/button').click()
    driver.find_element(By.ID,  'passp-field-login').click()
    driver.find_element(By.ID,  'passp-field-login').send_keys(login)
    driver.find_element(By.ID,  'passp:sign-in').click()
    time.sleep(1)
    driver.find_element(By.ID,  'passp-field-passwd').click()
    time.sleep(1)
    driver.find_element(By.ID,  'passp-field-passwd').send_keys(password)
    time.sleep(1)
    driver.find_element(By.ID,  'passp:sign-in').click()
    time.sleep(1)
    assert driver.find_element(By.ID,  'field:input-passwd:hint').text == "Неверный пароль"

def test_bad_password(login ='apple', password ='Ненадо_дядя'):
    filename =DriverUpdater.install(driver_name=DriverUpdater.chromedriver)
    url = "https://passport.yandex.ru/auth/"
    driver = webdriver.Chrome(filename)
    driver.get(url)
    time.sleep(5)
    parent  =  driver.find_element(By.XPATH,  '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[1]/div[1]/button').click()
    driver.find_element(By.ID,  'passp-field-login').click()
    driver.find_element(By.ID,  'passp-field-login').send_keys(login)
    driver.find_element(By.ID,  'passp:sign-in').click()
    time.sleep(1)
    driver.find_element(By.ID,  'passp-field-passwd').click()
    time.sleep(1)
    driver.find_element(By.ID,  'passp-field-passwd').send_keys(password)
    time.sleep(1)
    driver.find_element(By.ID,  'passp:sign-in').click()
    time.sleep(1)
    assert driver.find_element(By.ID,  'field:input-passwd:hint').text == "Неверный пароль"


def test_good_password(login ='caplingrigory', password ='AaA2887233'):
    filename =DriverUpdater.install(driver_name=DriverUpdater.chromedriver)
    url = "https://passport.yandex.ru/auth/"
    driver = webdriver.Chrome(filename)
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.XPATH,  '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[1]/div[1]/button').click()
    driver.find_element(By.ID,  'passp-field-login').click()
    driver.find_element(By.ID,  'passp-field-login').send_keys(login)
    driver.find_element(By.ID,  'passp:sign-in').click()
    time.sleep(1)
    driver.find_element(By.ID,  'passp-field-passwd').click()
    time.sleep(1)
    driver.find_element(By.ID,  'passp-field-passwd').send_keys(password)
    time.sleep(1)
    driver.find_element(By.ID,  'passp:sign-in').click()
    time.sleep(5)
    assert bool(driver.find_element(By.CLASS_NAME,  "PasspAuthForm_withoutOffset")) == True
    