from simplebot import SimpleBot
from selenium import common
import time

class LikerBot(SimpleBot):
    def __init__(self, username, password, rest_time, driver):
        super().__init__(username, password, rest_time, driver)

    def like_posts(self, user, number_of_posts):
        case = self.liking(user, number_of_posts)
        return self.post_result_of(case, user, number_of_posts)

    def liking(self, user, number_of_posts):
        def there_are_posts():
            try:
                self.driver.find_element_by_class_name('v1Nh3')
                return True
            except common.exceptions.NoSuchElementException:
                return False

        def like_post():
            if self.driver.find_element_by_class_name('fr66n').find_element_by_class_name('_8-yf5 ').get_attribute('aria-label') == 'Like':
                self.driver.find_element_by_class_name('fr66n').click()
                return False
            else:
                return True

        def there_is_another_post():
            try:
                self.driver.find_element_by_class_name('coreSpriteRightPaginationArrow')
                return True
            except common.exceptions.NoSuchElementException:
                return False

        def click_last_post():
            self.driver.find_element_by_class_name('v1Nh3').click()

        def next_post():
            self.driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()

        self.go_to_page(user)
        time.sleep(self.rest_time)
        try:
            if there_are_posts():
                click_last_post()
                time.sleep(self.rest_time)
                already_liked = like_post()
                time.sleep(self.rest_time)
                for _ in range(number_of_posts-1):
                    if there_is_another_post() and not already_liked:
                        next_post()
                        time.sleep(self.rest_time)
                        already_liked = like_post()
                        time.sleep(self.rest_time)
                return "liked posts"
            else:
                return "no posts"
        except common.exceptions.NoSuchElementException:
            return "posts error"

    def post_result_of(self, case, user, number_of_posts):
        cases = self.post_case_dictionary()
        new_case = cases[case].get("function", lambda u, n, c=case: c)(user, number_of_posts)
        return cases[new_case].get("description", "No description: ")

    def post_case_dictionary(self):
        cases = {
            "liked posts": {
                "description": "liked the posts"
            },
            "no posts": {
                "description": "no posts to like"
            },
            "posts error": {
                "description": "there has been an error for the posts",
                "function": self.liking
            }
        }

        return cases
