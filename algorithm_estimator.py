'''
This program reads a source code file and determines the estimated algorithmic runtime of 
its constituent functions. TODO: Should also detect algorithmic space costs as a bonus.


Challenges:
-We won't ever be able to truly tell the user the true O nature of some particular statement, like for-loop, for example.
The reason is that for loops depend on the number of iterations or size of some variable, like list.length or some range().
Perhaps the lowest-cost solution would be to detect for-loops and then look to see if there are any nested ones. If so, then
we flag that as potentially be O(n^2) or O(ab). The whole point is to capture the user's attention to focus on these areas.
How would I detect the end of a python for-loop? 

'''

from string import letters
# from random import choice


# Test file
file = './test_source.py'

'''
This function strips the newline and empty string elements from the file.
'''
def strip_file(file):
	# (1) Remove all newline-only elements as well as empty lines.
	new_stripped_file = [] 
	new_stripped_file = filter(lambda a: a != '', file)
	new_stripped_file = filter(lambda a: a != '\n', new_stripped_file)

	# print len(new_stripped_file)
	odd= 0
	for n in new_stripped_file:
		index = new_stripped_file.index(n)

		if index % 2 != 0:
			odd += 1
			new_stripped_file.insert(index, '---')

	# For some reason, a line needs to be added after the end of the for loop in order for the end-of-loop to be found.
	new_stripped_file.append('END')

	# print new_stripped_file,"\n\n"
	return new_stripped_file


'''
Checks for the existence of for-loops in this file and estimates their Big O cost in runtime.
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

	new_stripped_file = strip_file(file)

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


'''
Searches through the entire source code file and grabs all of the marked code segments and
returns them for analysis.
'''
def find_algo_segments(_source_code_file_):
	search_terms = ["ALGO_START", "ALGO_END"]
	code_segments_to_analyze = []

	first_line_index = -1
	last_line_index = -1

	file = strip_file(_source_code_file_)

	for line in file:
		if "@ALGO_START" in line:
			# Get the starting index of the starting point of the code segment to be checked
			first_line_index = file.index(line)

		elif "@ALGO_END" in line:
			# End of code segment-to-be-checked is reached. Cleave it off.
			last_line_index = file.index(line)

			# Append every string instance from the beginning to the end of the code segment.
			code_segments_to_analyze.append(file[first_line_index:last_line_index+1])

			last_line_index = -1
			first_line_index = -1

		else:
			continue

	# Open file
	# Go through each line and detect ALGO_START
	# Once detected, save all subsequent lines until ALGO_END. This will be saved as one segment.

	return code_segments_to_analyze


################################################################################################################################
################################################################################################################################

with open(file) as fp:
	# Find the algorithm segment(s) first.
	algo_segment_list = find_algo_segments(fp)

	for i in algo_segment_list:
		for j in i:
			print j

	# check_for_loops(fp)
