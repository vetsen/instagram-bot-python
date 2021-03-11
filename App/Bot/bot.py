from watcherbot import WatcherBot
from likerbot import LikerBot

class Bot(WatcherBot, LikerBot):
    def __init__(self, username, password, rest_time, driver, number_of_posts, users, function):
        super().__init__(username, password, rest_time, driver)
        self.number_of_posts = number_of_posts
        self.users = users
        self.function = function

    def watch_and_like_all(self):
        self.login()
        for user in self.users:
            self.watch_and_like(user)
        self.close()

    def watch_and_like(self, user):
        stories_result = self.watch_stories(user)
        posts_result = self.like_posts(user, self.number_of_posts)
        self.function(f"{user}: {stories_result}, {posts_result}\n")
