# Description
It calls:
+ utility.wait
+ preferences.check_preferences
+ preferences.accounts_from_file
+ preferences.number_of_accounts
+ processor.stories_and_posts_all

All the info are taken from preferences.
Invoke preferences.check_preferences that raises an exception if the preferences are set in a wrong way.
Invoke utility.wait with the number of hours

Invoke processor.stories_and_posts_all with: users, number of processes, number of accounts, number of posts, username, password, rest time, web driver function, web driver string, utility.write_log.
