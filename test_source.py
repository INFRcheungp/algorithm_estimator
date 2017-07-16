
l = [1,2,3]
m = [4,5,6,7,8,9,10]


for i in l:
	print i
	for j in range(0,10):
		print j
		for k in range(0,10):
			print k
		for l in range(0,10):
			print l
			for p in range(0,10):
				print p
				for o in range(0,10):
					print o


'''
'''
def test():
	for i in range(0,100):
		for k in range(0,100):
			print(i,k)
			for k in range(0,100):
				print "MALARKEY"
	for a in range(0,100):
		for b in range(0,100):
			print(i,j)
			for c in range(0,100):
				print "MALARKEY!"
