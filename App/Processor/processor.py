from math import floor
import time
import concurrent.futures

import sys
sys.path.append("../Bot/")
import bot


def tasks(number_of_accounts, number_of_processes, accounts, username, password, rest_time, driver_name, driver_string, number_of_posts, function):
    number_of_accounts_per_bot = floor(number_of_accounts / number_of_processes)
    for i in range(number_of_processes):
        number_of_accounts_remained = number_of_accounts - (i * number_of_accounts_per_bot)
        yield {
            "username": username,
            "password": password,
            "rest time": rest_time,
            "driver name": driver_name,
            "driver string": driver_string,
            "number of posts to like": number_of_posts,
            "group": group_of_users(accounts, number_of_accounts_per_bot, number_of_accounts_remained),
            "function": function
        }


def group_of_users(accounts, minimum_number_of_accounts_per_group, number_of_remained_accounts):
    if number_of_remained_accounts - minimum_number_of_accounts_per_group <= minimum_number_of_accounts_per_group:
        n = number_of_remained_accounts
    else:
        n = minimum_number_of_accounts_per_group
    group = []
    for _ in range(n):
        group.append(next(accounts))
    return tuple(group)


def stories_and_posts_all(users, number_of_processes, number_of_accounts, username, password, rest_time, driver_name, driver_string, number_of_posts, function):
    start = time.perf_counter()
    tasks_collection = tasks(number_of_accounts, number_of_processes, users, username, password, rest_time, driver_name, driver_string, number_of_posts, function)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(stories_and_posts_group, tasks_collection)
    end = time.perf_counter()
    elapsed_time = round((end - start)/60, 1)
    function(f"Time passed: {elapsed_time}")


def stories_and_posts_group(task):
    robot = bot.Bot(task["username"], task["password"], task["rest time"], task["driver name"](executable_path=task["driver string"]), task["number of posts to like"], task["group"], task["function"])
    robot.watch_and_like_all()
