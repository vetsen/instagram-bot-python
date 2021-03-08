# Description
It defines different utility functions.

Functions:
+ wait
+ write_log

## *wait*
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="1">Input</th>
			<td>number</td>
			<td>hours to sleep</td>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">It waits the number of hours specified, it's used if you don't want the script to start immediately</td>
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

## *write_log*
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="1">Input</th>
			<td>Indefinite input</td>
			<td>args</td>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">It writes into a log file the information passed</td>
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

It appends on a file with the name given by today the arguments passed as input.
