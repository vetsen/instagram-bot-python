from selenium.webdriver.common.keys import Keys
import time


class SimpleBot:
    def __init__(self, username, password, rest_time, driver):
        self.username = username
        self.password = password
        self.rest_time = rest_time
        self.driver = driver

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(self.rest_time)

        # It clicks the pop-up window
        try:
            self.driver.find_element_by_class_name("mt3GC").find_element_by_css_selector("button.aOOlW:nth-child(1)").click()
        except:
            pass

        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        time.sleep(self.rest_time)

        self.driver.find_element_by_name('password').send_keys("" + Keys.RETURN)
        time.sleep(self.rest_time)

    def go_to_page(self, user):
        self.driver.get('https://www.instagram.com/' + user + '/')
        time.sleep(self.rest_time)

    def close(self):
        self.driver.close()
