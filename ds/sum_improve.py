import time

def sumOfN2(n):
	start = time.time()

	summ = (n*(n+1))/2

	end = time.time()

	return summ, end-start
	pass


for i in range(5):
	print("Sum is %d required %10.7f seconds" %sumOfN2(11150000))

for i in range(5):
	print("Sum is %d required %10.7f seconds" %sumOfN2(111555550))