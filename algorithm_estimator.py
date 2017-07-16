'''
This program reads a source code file and determines the estimated algorithmic runtime of 
its constituent functions. TODO: Should also detect algorithmic space costs as a bonus.


Challenges:
-We won't ever be able to truly tell the user the true O nature of some particular statement, like for-loop, for example.
The reason is that for loops depend on the number of iterations or size of some variable, like list.length or some range().
Perhaps the lowest-cost solution would be to detect for-loops and then look to see if there are any nested ones. If so, then
we flag that as potentially be O(n^2) or O(ab). The whole point is to capture the user's attention to focus on these areas.
How would I detect the end of a python for-loop? 


NEXT TO-DO: Successfully detect inner loops. Now have to account for cases where we can have many non-nested for-loops
inside of another loop. 

The algorithm should be like this: IF for-loop detected, then continue searching until the next statement is 
truly the end of line for that for-loop statement.
'''

from string import letters
# from random import choice


# Test file
file = './test_source.py'

'''
Checks for the existence of for-loops in this file and estimates their Big O cost.
'''
def check_for_loops(file):
	line_count = 1
	'''
	Loop through each line and detect for loops.
		-If a "for"
		-If the next line is NOT empty and does NOT contain the same number of tabs, then it's considered the end of that for-loop statement
	'''
	num_loops_detected = 0
	num_nested_loops_detected = 0
	num_of_nested_for_loops = 0
	num_tabs = 0
	for_loop_inner_indent_level = 0
	for_loop_indent_level = 0
	for_loop_start_line = 0
	for_loop_detected_previously = False
	first_for_loop_detection = False

	# REMOVE all newline-only elements as well as empty lines.
	new_stripped_file = filter(lambda a: a != '', file)
	new_stripped_file = filter(lambda a: a != '\n', new_stripped_file)

	print len(new_stripped_file)
	odd= 0
	for n in new_stripped_file:
		index = new_stripped_file.index(n)
		# print index, n

		if index % 2 != 0:
			odd += 1
			# print index, n
			new_stripped_file.insert(index, '---')

	# For some reason, a line needs to be added after the end of the for loop in order for the end-of-loop to be found.
	new_stripped_file.append('END')

	print odd, "NUM ODDS"


			# new_stripped_file = list('-'.join(new_stripped_file))
			# new_stripped_file.insert(index, '---')

	print new_stripped_file,"\n\n"

	for line in new_stripped_file:

		if num_loops_detected >= 1:

			# END-OF-LINE DETECTION!
			if ("---" not in line) and (line.count('\t') <= for_loop_indent_level):
				terms = ''
				for i in range (0,num_nested_loops_detected+1):
					terms += letters[i].lower()

				print '\n\n'
				print "LINE: ", line_count, ": EOL Detected on line ", line_count, ". Its indent level is ", line.count('\t')
				print "LINE: ", line_count, ": The for loop ended on line ", (line_count - 1)
				print "LINE: ", line_count, ": TOTAL FOR-LOOP ", num_loops_detected
				print "LINE: ", line_count, ": TOTAL NESTED FOR-LOOP ", num_nested_loops_detected
				print "POTENTIAL RUNTIME COST: O(n^", len(terms), ") or O(", terms, ")\t"
				print '\n\n'

				# Reset
				for_loop_inner_indent_level = 0
				for_loop_indent_level = 0
				num_loops_detected = 0
				num_nested_loops_detected = 0
				for_loop_start_line = 0
				for_loop_detected_previously = False
				first_for_loop_detection = False


		# FOR-LOOP DETECTION! It's a for loop! Now keep checking...
		if "for" in line and "in" in line and "#" not in line:
			current_index = new_stripped_file.index(line)
			print "FOR LOOP FOUND ON LINE:\t", line_count, ": '", line.strip('\n'), "' INDEX:\t", current_index

			# Only applies to the first time a for loop is detected
			if first_for_loop_detection is False:
				first_for_loop_detection = True
				for_loop_indent_level = line.count('\t')


			if (for_loop_detected_previously and line.count('\t') > for_loop_indent_level):
				print "NESTED LOOP FOUND ON LINE:\t", line_count, line
				num_nested_loops_detected += 1

			# for_loop_indent_level = line.count('\t')
			for_loop_inner_indent_level = line.count('\t') + 1
			for_loop_detected_previously = True

			num_loops_detected += 1
			for_loop_start_line = line_count

			print "LINE: ", line_count, ": For-loop found! Level of its inner elements' indent:\t", for_loop_inner_indent_level


		line_count += 1


################################################################################################################################
################################################################################################################################

num_of_for_loops = 0
# num_of_nested_for_loops = 0

with open(file) as fp:


	check_for_loops(fp)
