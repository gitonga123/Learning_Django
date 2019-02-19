import time

from random import randrange

# O(n2)
def find_min(alist):
	min_num = alist[0]
	for i in alist:
		for j in alist:
			if min_num >= j:
				min_num = j

	return min_num

# Linear option
# O(1)
def findMin(alist):
	min_num = alist[0]
	for i in alist:
		if i < min_num:
			min_num = i

	return min_num
# print(find_min([5, 4,2, 1, 9, 0]))
# print(find_min([0, 5, 4,2, 1, 9, 10]))
for listSize in range(10000, 100001, 10000):
	alist = [randrange(10000009) for x in range(listSize)]
	start = time.time()
	print(findMin(alist))
	end = time.time()
	#max size took =  647 took 0.000707 mins
	print("Size : %d time: %f" % (listSize, end-start))

for listSize in range(10000, 100001, 10000):
	alist = [randrange(10000009) for x in range(listSize)]
	start = time.time()
	print(find_min(alist))
	end = time.time()
	#max size took =  647 took 43.902707 mins
	print("Size : %d time: %f" % (listSize, end-start))