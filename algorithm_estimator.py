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
	num_nested_loops_detected = 0
	num_of_nested_for_loops = 0
	num_tabs = 0
	for_loop_inner_indent_level = 0
	for_loop_indent_level = 0
	for_loop_start_line = 0

	# stripped_file = [line.rstrip('') for line in fp]
	# stripped_file = [line.rstrip('\n') for line in stripped_file]
	# stripped_file = [line.rstrip('') for line in stripped_file]
	# [stripped_file.remove(i) for i in stripped_file]
	# REMOVE all newline-only elements as well as empty lines.
	new_stripped_file = filter(lambda a: a != '', fp)
	new_stripped_file = filter(lambda a: a != '\n', new_stripped_file)

	# for i in stripped_file:
		# if i == '':
			# stripped_file.remove(i)

	print new_stripped_file



	for line in new_stripped_file:
		# print line

		# if line in ['\n', '\r\n'] and "#" not in line:
			# print "LINE: ", line_count, " is empty!\n"
		# else:
			# print "LINE: ", line_count, ": ", line
			# num_tabs = line.count('\t')
			# print "LINE: ", line_count, ": ", line


		if num_loops_detected >= 1:

			# END-OF-LINE DETECTION!
			if (line.count('\t') <= for_loop_inner_indent_level-1) and "for" not in line:
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
				num_loops_detected = 0
				num_nested_loops_detected = 0


		# FOR-LOOP DETECTION! It's a for loop! Now keep checking...
		if "for" in line and "in" in line and "#" not in line:
			print "\nFOR LOOP FOUND ON LINE:\t", line_count, ": '", line, "'"
			# Detect inner loop
			# if num_loops_detected >= 1:


			if (line.count('\t') != for_loop_indent_level):
				print "NESTED LOOP FOUND ON LINE:\t", line_count, line
				num_nested_loops_detected += 1

			for_loop_indent_level = line.count('\t')
			for_loop_inner_indent_level = line.count('\t') + 1

			num_loops_detected += 1
			for_loop_start_line = line_count

			print "LINE: ", line_count, ": For-loop found! Level of its inner elements' indent:\t", for_loop_inner_indent_level

			# print "For-loop found! Now checking for nested loops\n"


		line_count += 1



