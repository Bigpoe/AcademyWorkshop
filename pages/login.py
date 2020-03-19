class LoginPageObj:

    def __init__(self, driver):
        self.driver = driver
        self.username = driver.find_element_by_css_selector('#user-name')
        self.password = driver.find_element_by_css_selector('#password')
        self.login_button = driver.find_element_by_css_selector('input.btn_action')
        self.bot_image = driver.find_element_by_css_selector('.bot_column')

    def login_process(self, username, password):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.login_button.click()

    def invalid_login(self, username, password):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.login_button.click()
        return self.driver.find_element_by_css_selector('h3[data-test="error"]').text
