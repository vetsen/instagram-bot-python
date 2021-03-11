import preferences
import sys
from ..Utility import utility
from ..Processor import processor


pref = preferences.Preferences()
try:
    pref.check_preferences()
    utility.wait(pref.hours_of_sleep)
    processor.stories_and_posts_all(pref.accounts, pref.number_of_processes, pref.number_of_accounts, pref.username, pref.password, pref.rest_time, pref.driver_function, pref.driver_string, pref.number_of_posts, utility.write_log)
except Exception as e:
    utility.write_log("Error! " + e)
