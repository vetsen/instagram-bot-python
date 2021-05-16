from selenium.webdriver.common.keys import Keys
import time


class SimpleBot:
    def __init__(self, username, password, rest_time, driver):
        self.username = username
        self.password = password
        self.rest_time = rest_time
        self.driver = driver

    def login(self, count = 0):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(self.rest_time)

        # It clicks the pop-up window
        try:
            self.driver.find_element_by_css_selector("button.aOOlW:nth-child(2)").click()
        except:
            pass

        time.sleep(self.rest_time)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        time.sleep(self.rest_time)

        self.driver.find_element_by_name('password').send_keys("" + Keys.RETURN)
        time.sleep(self.rest_time)

        self.check_login(count)

    def check_login(self, count):
        self.driver.get('https://www.instagram.com/000nopage/')
        time.sleep(self.rest_time)

        scenarios = {
            "Try to login again": {
                "condition": count < 3,
                "function": lambda: self.login(count+1)
            },
            "Tried to login too many times": {
                "condition": count >= 3,
                "function": lambda: 1+1
            }
        }

        functions = [scenarios[x]["function"] for x in scenarios if scenarios[x]["condition"]]

        try:
            self.driver.find_element_by_css_selector("a.tdiEy:nth-child(1)>button:nth-child(1)")
            for function in functions:
                function()
        except:
            pass

    def go_to_page(self, user):
        self.driver.get('https://www.instagram.com/' + user + '/')
        time.sleep(self.rest_time)

    def close(self):
        self.driver.close()
