'''
This program reads a source code file and determines the estimated algorithmic runtime of 
its constituent functions. TODO: Should also detect algorithmic space costs as a bonus.


Challenges:
-We won't ever be able to truly tell the user the true O nature of some particular statement, like for-loop, for example.
The reason is that for loops depend on the number of iterations or size of some variable, like list.length or some range().
Perhaps the lowest-cost solution would be to detect for-loops and then look to see if there are any nested ones. If so, then
we flag that as potentially be O(n^2) or O(ab). The whole point is to capture the user's attention to focus on these areas.
How would I detect the end of a python for-loop? 


NEXT TO-DO: Now that we have successfully developed a way to detect the beginning and end of a for-loop, we should focus on detecting inner for-loops.
'''



'''
'''
def check_for(line):
	if "for" in line:
		print "It's a for loop!\n"
		w


# def check_nested_loops:
# 	pass


file = './test_source.py'

num_of_for_loops = 0
# num_of_nested_for_loops = 0

with open(file) as fp:
	line_count = 1

	'''
	Loop through each line and detect for loops.
		-If a "for"
		-If the next line is NOT empty and does NOT contain the same number of tabs, then it's considered the end of that for-loop statement
	'''
	num_loops_detected = 0
	num_of_nested_for_loops = 0
	num_tabs = 0
	for_loop_inner_indent_level = 0


	for line in fp:

		if line in ['\n', '\r\n']:
			print "LINE: ", line_count, " is empty!\n"
		else:
			num_tabs = line.count('\t')
			# print "LINE: ", line_count, ": ", line


		if num_loops_detected >= 1:
			if line.count('\t') != for_loop_inner_indent_level:
				print "LINE: ", line_count, ": EOL Detected on line ", line_count, ". Its indent level is ", line.count('\t')
				print "LINE: ", line_count, ": The for loop ended on line ", (line_count - 1),'\n'
			# End of for-loop detector
			# if '\t' in line and (line in ['\n', '\r\n']):
				# print "EOL Detected on line ", line_count, "\n"


				# Reset
				for_loop_inner_indent_level = 0
				num_loops_detected = 0


		# FOR-LOOP DETECTION! It's a for loop! Now keep checking...
		if "for" in line and "in" in line:

			for_loop_inner_indent_level = line.count('\t') + 1
			num_loops_detected += 1

			print "LINE: ", line_count, ": For-loop found! Level of its inner elements' indent:\t", for_loop_inner_indent_level

			# print "For-loop found! Now checking for nested loops\n"


		line_count += 1



