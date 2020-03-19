from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from utils.data_test import *
from pages.login import LoginPageObj
from pages.header import HeaderObj
import time

def test_logout():
    global driver
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
    driver.implicitly_wait(5)
    driver.get(data_test['url'])

    login_page = LoginPageObj(driver)
    login_page.login_process(data_test['username'], data_test['valid_password'])

    header = HeaderObj(driver)
    header.logout_process()

    login_page = LoginPageObj(driver)
    assert login_page.bot_image.is_displayed()

def test_tear_down():
    time.sleep(2)
    driver.quit()

# test_logout()
# test_tear_down()
