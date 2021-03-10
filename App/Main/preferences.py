from selenium import webdriver


class Preferences:
    def __init__(self):
        self.hours_of_sleep = 0
        self.read_file_path = ""
        self.accounts_hard_coded = ("kurzgesagt", "nasa", "wikipedia")
        self.number_of_processes = 2
        self.number_of_posts = 3
        self.username = ""
        self.password = ""
        self.rest_time = 5
        self.driver_function = webdriver.Firefox
        self.driver_string = "./geckodriver"

    @property
    def accounts(self):
        if self.read_file_path == "":
            for user in self.accounts_hard_coded:
                yield user
        else:
            with open(self.read_file_path, "r") as file_cursor:
                for line in file_cursor.readlines():
                    account = line.replace("\n", "")
                    yield account

    @property
    def number_of_accounts(self):
        if self.read_file_path == "":
            return len(self.accounts_hard_coded)
        else:
            with open(self.read_file_path, "r") as file_cursor:
                count = 0
                for _ in file_cursor.readlines():
                    count += 1
                return count

    def check_preferences(self):
        if self.number_of_processes > self.number_of_accounts:
            self.number_of_processes = self.number_of_accounts
        bad_conditions = {
            "c1": {
                "condition": self.hours_of_sleep < 0,
                "message": "The hours of sleep must be 0 or more"
            },
            "c2": {
                "condition": self.number_of_processes < 1,
                "message": "The number of processes must be 1 or more"
            },
            "c3": {
                "condition": self.number_of_posts < 1,
                "message": "The number of posts must be 1 or more"
            },
            "c4": {
                "condition": self.username == "",
                "message": "Specify a username"
            },
            "c5": {
                "condition": self.password == "",
                "message": "Specify a password"
            },
            "c6": {
                "condition": self.rest_time < 0,
                "message": "The rest time of the bot must be positive"
            },
        }
        true_bad_conditions = [bad_conditions[x]["message"] for x in bad_conditions if bad_conditions[x]["condition"]]
        if len(true_bad_conditions) > 0:
            raise Exception(true_bad_conditions[0])
