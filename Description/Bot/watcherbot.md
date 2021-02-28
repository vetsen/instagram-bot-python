# Description
Bot that watches the stories of a user.

Functions/methods:
+ Constructor
+ watch_stories
+ watching
+ story_result_of
+ story_case_dictionary
## Constructor
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="4">Input</th>
			<td>String</td>
			<td>Username</td>
		</tr>
		<tr>
			<td>String</td>
			<td>Password</td>
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
			<th>Description</th>
			<td colspan="2">It builds a watcher bot invoking super</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>Bot.constructor</li>
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

## *watch_stories*
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
			<td colspan="2">It watches the stories of a user and returns a summary</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
			<td>str</td>
			<td>Description of what happened (error, everything fine,...)</td>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>Bot.watch_and_like</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>Calls</th>
			<td colspan="2">
				<ul>
					<li>watching</li>
					<li>story_result_of</li>
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

Invoke watching with: user. It stored the case returned.
Invoke and return story_result_of with: case, user.
## *watching*
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
			<td colspan="2">It watches the stories of a user</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
			<td>str</td>
			<td>Case that summarizes what happened</td>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>watch_stories</li>
					<li>story_result_of</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>Calls</th>
			<td colspan="2">
				<ul>
					<li>simpleBot.go_to_page</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>raise Exception (?)</th>
			<td colspan="2">No, it has a general except</td>
		</tr>
		<tr>
			<th>try (?)</th>
			<td colspan="2">No</td>
		</tr>
	</tbody>
</table>

It defines some functions:
+ are_there_stories: returns True if there are stories, otherwise returns False.
+ are_stories_ended: returns True if the stories are ended, otherwise returns False.

Invoke go to page.
If there are stories, it clicks on it and waits in a while loop until stories are ended.
Except all errors.
## *story_result_of*
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="2">Input</th>
			<td>str</td>
			<td>Case occurred</td>
		</tr>
		<tr>
			<td>str</td>
			<td>User</td>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">If the case is an error, it retries to watch the stories</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
			<td>str</td>
			<td>Description of what has happened</td>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>watch_stories</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>Calls</th>
			<td colspan="2">
				<ul>
					<li>story_case_dictionary</li>
					<li>watching</li>
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

It takes the dictionary that describes the relationship between the case, the description and a function using story_case_dictionary.
Invoke the function linked in the dictionary to the case. From the case that has been returned, get the description and return it. 
## *story_case_dictionary*
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="1">Input</th>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">It defines and returns the dictionary that links together case, description, function to call</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
			<td>dic</td>
			<td>Dictionary as described in Description</td>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>story_result_of</li>
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

Each case has a description and a function. The error cases has watching as a function, while the non-error cases has no function or a lambda that returns the same case linked.


