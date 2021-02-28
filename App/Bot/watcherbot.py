from selenium import common
from simplebot import SimpleBot
import time

class WatcherBot(SimpleBot):
    def __init__(self, username, password, rest_time, driver):
        super().__init__(username, password, rest_time, driver)

    def watch_stories(self, user):
        case = self.watching(user)
        return self.story_result_of(case, user)

    def watching(self, user):
        def there_are_stories():
            return self.driver.find_element_by_class_name('XjzKX').find_element_by_css_selector('div').get_attribute(
                'aria-disabled') == "false"

        def stories_are_active():
            try:
                self.driver.find_element_by_css_selector("._lz6s")
            except common.exceptions.NoSuchElementException:
                return True
            else:
                return False

        def click_stories():
            self.driver.find_element_by_class_name('XjzKX').find_element_by_css_selector('div').click()

        self.go_to_page(user)
        time.sleep(self.rest_time)
        try:
            if there_are_stories():
                click_stories()
                time.sleep(self.rest_time)
                while stories_are_active():
                    time.sleep(self.rest_time)
                return "watched stories"
            else:
                return "no stories"
        except common.exceptions.NoSuchElementException:
            return "stories error"

    def story_result_of(self, case, user):
        cases = self.story_case_dictionary()
        new_case = cases[case].get("function", lambda u=user, c=case: c)(user)
        return cases[new_case].get("description", "No description: ")

    def story_case_dictionary(self):
        cases = {
            "watched stories": {
                "description": "watched the stories"
            },
            "no stories": {
                "description": "no stories"
            },
            "stories error": {
                "description": "error in the stories",
                "function": self.watching
            }
        }

        return cases
