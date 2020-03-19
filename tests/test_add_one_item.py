from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from utils.data_test import *
from pages.login import LoginPageObj
from pages.products_list import ProductsListObj
import time

def test_add_one_item():
    global driver
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
    driver.implicitly_wait(5)
    driver.get(data_test['url'])

    login_page = LoginPageObj(driver)
    login_page.login_process(data_test['username'], data_test['valid_password'])

    products_list_page = ProductsListObj(driver)
    products_list_page.add_one_item_to_cart_from_product_list()

    assert products_list_page.sauce_lab_bagpack_add_button.text == 'REMOVE'
## assert is missing

def test_tear_down():
    time.sleep(2)
    driver.quit()

test_add_one_item()
test_tear_down()
