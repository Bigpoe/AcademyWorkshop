class ProductsListObj:

    def __init__(self, driver):
        self.driver = driver
        self.sauce_lab_bagpack = driver.find_element_by_css_selector('#item_4_title_link')
        self.sauce_lab_bagpack_add_button = driver.find_element_by_css_selector('.inventory_list div:nth-child(1) .pricebar button')
        self.sauce_labs_bike_light_add_button = driver.find_element_by_css_selector('.inventory_list div:nth-child(2) .pricebar button')

    def add_one_item_to_cart_from_product_list(self):
        self.sauce_lab_bagpack_add_button.click()

    def add_some_items_to_cart_from_product_list(self):
        self.sauce_lab_bagpack_add_button.click()
        self.sauce_labs_bike_light_add_button.click()