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
Usual Runtime Performance:	O(branched_calls^depth)
Usual Space Complexity:		O(n)

Look for the following for recursion:

-Num of internal calls = For example, a recursive function that calls itself twice 
for four iterations on each call will incur O(2^4) runtime or O(2^n), where n is the 
depth of the call tree. 

-The num of iterations will be a runtime of O(1)

-The base case

-The recursive case

'''
def check_recursion(code_segment):
	# (0) Make sure it's a function first. Look for 'def' and '()' and ':'
	# (1) Get the name of the function
	# (2) check how many explicity calls inside the body. This gets us the 'branched_calls'
	# name_of_func = get_function_name(code_segment)

	# if if_valid_function(code_segment):
		# print "VALID FUNCTION:\n"
	base_case = ''
	recursive_case = ''
	num_recursive_calls = 0
	name_of_func = ''

	for line in code_segment:
		# print line
		if 'def' in line and ':' in line:
			print line,'\n\n'
			# Parse the name of the function from the string.
			name_of_func = get_function_name(line) 
		else:
			if name_of_func in line:
				num_recursive_calls  = line.count(name_of_func)

	print "NAME OF FUNC:\t", name_of_func
	print "NUM OF RECURSIVE CALLS:\t", num_recursive_calls
	print "POTENTIAL RUNTIME COMPLEXITY: O(", num_recursive_calls, "^n)"
	print "POTENTIAL SPACE COMPLEXITY: O(n)"


def if_valid_function(segment):
	print segment
	return ('def' in segment) and (':' in segment) and ('(' in segment and ')' in segment)


'''
Checks if this input is actually a function; if so, then return its name.
'''
def get_function_name(line):
	# Use this as the string separator
	separate = '('
	# Get the function string after the 'def' part and discard everything after the '(' char is encountered.
	name_of_func = line.split()[1].split(separate,1)[0]
	print name_of_func
	return name_of_func


'''
Grabs all of a function's arguments
'''
def get_function_args(function_signature):
	pass


'''
Checks for the existence of for-loops in this file and estimates their Big O cost in runtime.
'''
def check_for_loops(code_segment):
	print file
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



	for line in code_segment:

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
			current_index = code_segment.index(line)
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

	for index, match in enumerate(file):

		if "@ALGO_START" in match:
			# Get the starting index of the starting point of the code segment to be checked
			first_line_index = index


		elif "@ALGO_END" in match:
			# End of code segment-to-be-checked is reached. Cleave it off.
			last_line_index = index

			code_segments_to_analyze.append(file[first_line_index:last_line_index+1])
			# Reset
			last_line_index = -1
			first_line_index = -1

		else:
			continue


	# print code_segments_to_analyze

	return code_segments_to_analyze


'''
Guesstimates the length of the input variable to for loops, recursive functions, etc. Would greatly
determine the accuracy of the algorithmic performance
'''
def check_size_of_input(array):
	pass


################################################################################################################################
################################################################################################################################

with open(file) as fp:
	# Find the algorithm segment(s) first.
	algo_segment_list = find_algo_segments(fp)

	num_code_segements = len(algo_segment_list)

	check_recursion(algo_segment_list[1])

	# Go through each marked code segment and estimate its algorithmic runtime performance.
	for i in range(0,num_code_segements):
		print "SEGMENT:\n", algo_segment_list[i],'\n\n'
		# check_for_loops(algo_segment_list[i])
		# check_recursion(algo_segment_list[i])

