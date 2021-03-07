# Description
Class with global variables that contains the settings that will be followed by the app.

The variables are:
+ Hours of sleep
+ Path of the file to read
+ Accounts as an explicit collections
+ Number of processors
+ Number of posts to like
+ Username
+ Password
+ Rest time
+ web driver function, web driver string (and dictionary associated)

It also contains the methods:
+ accounts
+ number_of_accounts
+ check_preferences
## *accounts*
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="1">Input</th>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">It's a property function that returns the accounts to process</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
			<td>Iterable</td>
			<td>Accounts</td>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>main</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>Calls</th>
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

If the path file is not an empty string, reads the file and each line is a new user to process. It yields each user. Otherwise, it returns the explicit accounts.
## *number_of_accounts*
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="1">Input</th>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">It's a property function that returns the number of accounts to process</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
			<td>int</td>
			<td>Accounts</td>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>main</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>Calls</th>
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

If the path file is not an empty string, reads the file and for each row increments the counts; it returns the count. Otherwise, it returns the explicit accounts length.
## *check_preferences*
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="1">Input</th>
		<tr>
			<th>Description</th>
			<td colspan="2">It checks if there is any errors in the preferences</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>main</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>Calls</th>
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
