class ProductDetailsObj:

    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button = driver.find_element_by_css_selector('.btn_primary')
