# Description
Bot that does the basic actions on the browser.

Functions/methods:
+ Constructor
+ login
+ go_to_page
+ close
## Constructor
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="4">Input</th>
			<td>str</td>
			<td>Username</td>
		</tr>
		<tr>
			<td>str</td>
			<td>Password</td>
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
			<th>Description</th>
			<td colspan="2">It builds a basic bot</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>Bot.Constructor</li>
					<li>likerBot.Constructor</li>
					<li>watcherBot.Constructor</li>
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

## *login*
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="1">Input</th>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">Log in with the username and password</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>Bot.watch_and_like_all</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>Calls</th>
		</tr>
		<tr>
			<th>raise Exception (?)</th>
			<td colspan="2">Yes, Instagram could add some pop-up and the bot would not be able to actually find elements in the page and write on it, for example.</td>
		</tr>
		<tr>
			<th>try (?)</th>
			<td colspan="2">No</td>
		</tr>
	</tbody>
</table>

## *go_to_page*
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="1">Input</th>
			<td>str</td>
			<td>User</td>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">Goes to the user page</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>likerbot.liking</li>
					<li>watcherbot.watching</li>
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

## *close*
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="1">Input</th>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">It closes the browser in which the bot is working</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>Bot.watch_and_like_all</li>
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

