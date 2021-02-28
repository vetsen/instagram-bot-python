# Description
Given a collection of users and the preferences, invoke one or multiple bots in parallel to watch the stories and like the posts of the users.

Methods/Functions:
+ Constructor
+ group_of_groups_of_users
+ bots
+ stories_and_posts
+ start_bot
+ group_of_users
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
			<td>Number of bots</td>
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
## *group_of_groups_of_users*
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="1">Input</th>
		<tr>
			<th>Description</th>
			<td colspan="2">It's a property that divides all the accounts in different groups so each one is processed by a bot</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
			<td>Iterable</td>
			<td>Group that contains groups of users</td>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>bots</li>
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

Using the collection of all accounts, the number of bots, the number of all accounts, gets the number of accounts per bot (number of accounts / number of bots, using floor).
For i in number of bots, invoke group_of_users with: number of accounts per bot, number of accounts remained (number of accounts minus i * number of accounts per bot). Yield the returned value.
## bots
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="1">Input</th>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">It's a property that returns a collection of bots with a group of users associated with them</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
			<td>Iterable</td>
			<td>Collection of bots</td>
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

Using the group of groups, the number of posts to like, the username, the password, the rest time, the web driver and the function given, for each group it creates a bot and return the group of bots.
## *stories_and_posts*
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="1">Input</th>
			<td>int</td>
			<td>Number of processes</td>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">It invokes bot functions to watch the stories and like the posts of a group of user</td>
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
					<li>start_bot</li>
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

Get the start time.
Using pool and map, invoke start_bot with the group of bots.
Get the finish time.
Measure the time passed. It processes it with the function given.
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
					<li>stories_and_posts</li>
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
			<td>Maximum number of accounts per group</td>
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
					<li>group_of_groups_of_users</li>
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

Take the minimum between maximum number of accounts per group and number of accounts remained. For _ in the range of that number yield next.

