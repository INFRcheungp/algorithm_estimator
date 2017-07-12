'''
This program reads a source code file and determines the estimated algorithmic runtime of 
its constituent functions. TODO: Should also detect algorithmic space costs as a bonus.
'''

file = './test_source.py'

num_of_for_loops = 0
num_of_nested_for_loops = 0

with open(file) as fp:
    for line in fp:
        print line