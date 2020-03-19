from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from utils.data_test import *
from pages.login import LoginPageObj
from pages.header import HeaderObj
import time

def test_valid_login():
    global driver
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
    driver.get(data_test['url'])

    login_page = LoginPageObj(driver)
    login_page.login_process(data_test['username'], data_test['valid_password'])

    header = HeaderObj(driver)

    assert header.products_header.is_displayed()

    tear_down()

def tear_down():
    time.sleep(2)
    driver.quit()
