from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from utils.data_test import *
from pages.login import LoginPageObj
import time

def test_invalid_login():
    global driver
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
    driver.get(data_test['url'])

    login_page = LoginPageObj(driver)
    error_message = login_page.invalid_login(data_test['username'], data_test['invalid_password'])

    assert error_message == 'Epic sadface: Username and password do not match any user in this service'

    tear_down()

def tear_down():
    time.sleep(2)
    driver.quit()
