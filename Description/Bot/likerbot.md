# Description
Bot that can like a certain amount of posts from one user.

Methods/Functions:
+ Constructor
+ like_posts
+ liking
+ post_result_of
+ post_case_dictionary
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
			<td colspan="2">It builds a liker bot invoking super</td>
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

## *like_posts*
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="2">Input</th>
			<td>str</td>
			<td>User</td>
		</tr>
		<tr>
			<td>int</td>
			<td>Number of posts to like</td>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">It likes the posts of a user and returns a summary</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
			<td>str</td>
			<td>Summary of whats has happened</td>
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
					<li>liking</li>
					<li>post_result_of</li>
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

Invoke liking with: user, number of posts. You get the case.
Invoke and return get post result of with: case, users, number of posts.
## *liking*
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="2">Input</th>
			<td>str</td>
			<td>User</td>
		</tr>
		<tr>
			<td>int</td>
			<td>number of posts to like</td>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">It likes a certain amount of posts from one user</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
			<td>str</td>
			<td>case occurred (an error, or everything fine for example)</td>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>like_posts</li>
					<li>post_result_of</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>Calls</th>			
			<td colspan="2">
				<ul>
					<li>bot.go_to_page</li>
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

Defines some functions internally:
+ are_there_posts: returns true if the user has posts, otherwise returns false
+ like_post: likes a post if it is not already liked. If it actually liked the post, returns True, otherwise returns False.
+ is_there_another_post: return True if there is another post after the one that is active, otherwise False.

Go to the user page with simpleBot.go_to_page.
If there are no posts, it returns the appropriate case.
Otherwise, like the post with like_post and store the returned value.
For _ in number of post minus 1, check if there is another post with is_there_another_post and if also the returned value from like_post is true. In the True scenario, it goes to the next post and invoke like_post (the returned value is stored to be checked in the loop).
All of this in a try and then except Element not found and a generic Exception.
## *post_result_of*
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="3">Input</th>
			<td>str</td>
			<td>Case to explicit into a string</td>
		</tr>
		<tr>
			<td>str</td>
			<td>User</td>
		</tr>
		<tr>
			<td>int</td>
			<td>Number of posts</td>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">Given the case occurred, if an error has occurred, it tries to like the posts again and returns the case occurred</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
			<td>str</td>
			<td>Description of what happened</td>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>like_posts</li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>Calls</th>
			<td colspan="2">
				<ul>
					<li>post_case_dictionary</li>
					<li>liking</li>
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

It takes the dictionary that describes the relationship between the case, the string that describes it and a function to be invoked.
Invoke the function associated with the case, given the result that is a case, it returns the string linked in the dictionary. 
## *post_case_dictionary*
<table>
	<thead></thead>
	<tbody>
		<tr>
			<th rowspan="1">Input</th>
		</tr>
		<tr>
			<th>Description</th>
			<td colspan="2">It defines a dictionary the describes the relationship between a case, the string that summarizes it and a function to be called</td>
		</tr>
		<tr>
			<th rowspan="1">Output</th>
			<td>dic</td>
			<td>Dictionary defined in this function</td>
		</tr>
		<tr>
			<th>Called by</th>
			<td colspan="2">
				<ul>
					<li>post_result_of</li>
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

Link a case to a dictionary that link a description and a function. For the error cases, the function is liking, for the other None (or a lambda that returns a case).

