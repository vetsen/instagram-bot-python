import time
from datetime import date


def wait(hours):
    time.sleep(60*60*hours)


def write_log(*args):
    with open(str(date.today()), "a") as cursor_file:
        for a in args:
            cursor_file.write(str(a) + "\n")
