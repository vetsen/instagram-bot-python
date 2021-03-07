# Description
Given a collection of users and the preferences, invoke one or multiple processes in parallel to watch the stories and like the posts of the users.

Methods/Functions:
+ tasks
+ stories_and_posts_all
+ stories_and_posts_group
+ group_of_users
## *tasks*
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="10">Input</th>
			<td>int</td>
			<td>Number of accounts</td>
		</tr>
		<tr>
			<td>int</td>
			<td>Number of processes</td>
        </tr>
		<tr>
			<td>iterable</td>
			<td>Account to use to get the group of groups</td>
        </tr>
        <tr>
			<td>int</td>
			<td>Number of posts to like</td>
		</tr>
		<tr>
			<td>str</td>
			<td>Username</td>
		</tr>
		<tr>
			<td>str</td>
			<td>password</td>
		</tr>
		<tr>
			<td>int</td>
			<td>Time to rest</td>
		</tr>		
        <tr>
			<td>function</td>
			<td>function to get a driver, has an executable path argument</td>
		</tr>
        <tr>
			<td>str</td>
			<td>argument to pass in executable path of the driver function</td>
		</tr>
		<tr>
			<td>function</td>
			<td>What to do with the result got from the process</td>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">It divides all the accounts in different dictionary so each one is processed concurrently</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
			<td>Iterable</td>
			<td>Group that contains dictionary of tasks</td>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>stories_and_posts_all</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>Calls</th>
			<td colspan="2">
				<ul>
					<li>group_of_users</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>raise Exception (?)</th>
			<td colspan="2">No</td>
		</tr>
		<tr>
			<th>try (?)</th>
			<td colspan="2">No</td>
		</tr>
	</tbody>
</table>

Using the collection of all accounts, the number of processes, the number of all accounts, gets the number of accounts per bot (number of accounts / number of processes, using floor).
For i in number of processes, defines a dictionary that associates each element needed to create a bot from the parameters. For the group associated invoke group_of_users with: number of accounts per bot, number of accounts remained (number of accounts minus i * number of accounts per bot) and accounts. Yield the dictionary.
## *stories_and_posts_all*
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="10">Input</th>
			<td>Iterable</td>
			<td>Users</td>
		</tr>
		<tr>
			<td>int</td>
			<td>Number of processes</td>
		</tr>
		<tr>
			<td>int</td>
			<td>Number of accounts</td>
		</tr>
		<tr>
			<td>int</td>
			<td>Number of posts to like</td>
		</tr>
		<tr>
			<td>str</td>
			<td>Username</td>
		</tr>
		<tr>
			<td>str</td>
			<td>password</td>
		</tr>
		<tr>
			<td>int</td>
			<td>Time to rest</td>
		</tr>		
        <tr>
			<td>function</td>
			<td>function to get a driver, has an executable path argument</td>
		</tr>
        <tr>
			<td>str</td>
			<td>argument to pass in executable path of the driver function</td>
		<tr>
			<td>function</td>
			<td>What to do with the result got from the process</td>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">It invokes bot functions to watch the stories and like the posts of all user given, using the number of processes specified</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>Main.main</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>Calls</th>
			<td colspan="2">
				<ul>
					<li>stories_and_posts_group</li>
                    <li>tasks</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>raise Exception (?)</th>
			<td colspan="2">Yes</td>
		</tr>
		<tr>
			<th>try (?)</th>
			<td colspan="2">Yes</td>
		</tr>
	</tbody>
</table>

Get the start time. Get the tasks with: number of accounts, number of processes, accounts, username, password, rest time, number of posts to like, driver, function.
Using pool and map, invoke stories_and_posts_group with each task.
Get the finish time.
Measure the time passed. It processes it with the function given.
## *stories_and_posts_group*
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="1">Input</th>
			<td>dictionary</td>
			<td>task</td>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">It likes the post and watch the stories of the group</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>stories_and_posts_all</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>Calls</th>
			<td colspan="2">
				<ul>
					<li>Bot.constructor</li>
					<li>Bot.watch_and_like_all</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>raise Exception (?)</th>
			<td colspan="2">Yes</td>
		</tr>
		<tr>
			<th>try (?)</th>
			<td colspan="2">No</td>
		</tr>
	</tbody>
</table>

It creates a bot with the group associated, it takes the info from the task: username, password, rest time, driver, number of posts to like, users, function. Calls watch_and_like_all.
## *group_of_users*
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="3">Input</th>
			<td>Iterator</td>
			<td>Accounts</td>
		</tr>
		<tr>
			<td>int</td>
			<td>Minimum number of accounts per group</td>
		</tr>		
		<tr>
			<td>int</td>
			<td>Accounts remained to be added in a group</td>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">It returns a group of accounts</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
			<td>Iterator</td>
			<td>Group of accounts</td>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>tasks</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>Calls</th>
		</tr>
		<tr>
			<th>raise Exception (?)</th>
			<td colspan="2">No</td>
		</tr>
		<tr>
			<th>try (?)</th>
			<td colspan="2">No</td>
		</tr>
	</tbody>
</table>

Take the minimum number of accounts per group or the number of accounts remained. For _ in the range of that number yield next.


<!--
## Constructor
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="9">Input</th>
			<td>Iterable</td>
			<td>Users</td>
		</tr>
		<tr>
			<td>int</td>
			<td>Number of processes</td>
		</tr>
		<tr>
			<td>int</td>
			<td>Number of accounts</td>
		</tr>
		<tr>
			<td>int</td>
			<td>Number of posts to like</td>
		</tr>
		<tr>
			<td>str</td>
			<td>Username</td>
		</tr>
		<tr>
			<td>str</td>
			<td>password</td>
		</tr>
		<tr>
			<td>int</td>
			<td>Time to rest</td>
		</tr>		
        <tr>
			<td>driver object</td>
			<td>web driver</td>
		</tr>
		<tr>
			<td>function</td>
			<td>What to do with the result got from the process</td>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">It builds a processor to handle the task of watching stories and liking posts</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>Main.main</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>Calls</th>
		</tr>
		<tr>
			<th>raise Exception (?)</th>
			<td colspan="2">No</td>
		</tr>
		<tr>
			<th>try (?)</th>
			<td colspan="2">No</td>
		</tr>
	</tbody>
</table>

Each parameter becomes an instance variable.


## *start_bot*
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="1">Input</th>
			<td>Object</td>
			<td>bot</td>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">It starts the bot</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
			<td>Iterable</td>
			<td>Results</td>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>stories_and_posts_all</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>Calls</th>
			<td colspan="2">
				<ul>
					<li>bot.watch_and_like_all</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>raise Exception (?)</th>
			<td colspan="2">Yes</td>
		</tr>
		<tr>
			<th>try (?)</th>
			<td colspan="2">No</td>
		</tr>
	</tbody>
</table>

## bots
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="1">Input</th>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">It's a property that returns a collection of processes with a group of users associated with them</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
			<td>Iterable</td>
			<td>Collection of processes</td>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>stories_and_posts</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>Calls</th>
			<td colspan="2">
				<ul>
					<li>group_of_groups_of_users</li>
<li>Bot.constructor</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>raise Exception (?)</th>
			<td colspan="2">No</td>
		</tr>
		<tr>
			<th>try (?)</th>
			<td colspan="2">No</td>
		</tr>
	</tbody>
</table>

Using the group of groups, the number of posts to like, the username, the password, the rest time, the web driver and the function given, for each group it creates a bot and return the group of processes.

