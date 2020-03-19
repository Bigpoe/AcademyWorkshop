class HeaderObj:

    def __init__(self, driver):
        self.driver = driver
        self.products_header = driver.find_element_by_css_selector('.product_label')
        self.menu_wrap_button = driver.find_element_by_css_selector('div.bm-burger-button button')
        self.logout_button = driver.find_element_by_css_selector('#logout_sidebar_link')

    def logout_process(self):
        self.menu_wrap_button.click()
        self.logout_button.click()
