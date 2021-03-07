# Description
Bot that has a collection of users to process (watching the stories e liking a certain amount of posts).

Subclass of:
+ simpleBot
+ likerBot
+ watcherBot

Methods/functions:
+ Constructor
+ watch_and_like_all
+ watch_and_like
## Constrcutor
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="7">Input</th>
			<td>String</td>
			<td>username</td>
		</tr>
		<tr>
			<td>String</td>
			<td>password</td>
		</tr>
		<tr>
			<td>int</td>
			<td>Seconds to rest</td>
		</tr>		
        <tr>
			<td>driver object</td>
			<td>web driver</td>
		</tr>
		<tr>
			<td>int</td>
			<td>Numbers of posts to like</td>
		</tr>
		<tr>
			<td>Iterable</td>
			<td>Users to process</td>
		</tr>
        <tr>
			<td>function</td>
			<td>what to do of the result of watching and liking a user</td>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">It constructs an instance of this bot</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>Processor.stories_and_posts_group</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>Calls</th>
			<td colspan="2">
				<ul>
					<li>super</li>
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
 
 Invoke the constructor of simpleBot with: username, password, time to rest.
 The iterable and the number of posts become instance variables.
 ## *watch_and_like_all*
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="1">Input</th>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">It watches the stories and like the posts of the users in the collection</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
			<td>Iterable of strings</td>
			<td>Result of processing the users</td>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>Processor.stories_and_posts_group</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>Calls</th>
			<td colspan="2">
				<ul>
					<li>simpleBot.login</li>
					<li>watch_and_like</li>
					<li>simpleBot.close</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>raise Exception (?)</th>
			<td colspan="2">Yes, from invoking login</td>
		</tr>
		<tr>
			<th>try (?)</th>
			<td colspan="2">No</td>
		</tr>
	</tbody>
</table>

Login.
For each element of the collection invoke watch_and_like with that element as an argument. It should be used map.
Close the bot.
Return the result.
## *watch_and_like*
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="1">Input</th>
			<td>String</td>
			<td>User</td>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">It watches the stories and like the posts of the user</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
			<td>String</td>
			<td>Summary of the result of each process</td>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>watch_and_like_all</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>Calls</th>
			<td colspan="2">
				<ul>
					<li>watcherBot.watch_stories</li>
					<li>likerBot.like_posts</li>
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

Invoke watch_stories with: user. It takes the string returned.
Invoke like_posts with: user, number of post. It takes the string returned.
Invoke the function given in the constructor for: the user plus the two strings returned before.
