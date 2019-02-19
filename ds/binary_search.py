import time

from random import randrange

def binary_search(listing, left, right, item):
    if right >= left:
        mid = left + ((right - left)//2)

        if listing[mid] == item:
            return mid

        if listing[mid] > item:
            return binary_search(listing, left, right-1, item)
        
        return binary_search(listing, mid+1, right, item)
    else:
    	return False;


for listSize in range(10000, 100001, 10000):
	alist = [randrange(10000009) for x in range(listSize)]
	start = time.time()
	print(binary_search(alist, 0, (len(alist)-1), 10000009))
	end = time.time()
	#max size took =  647 took 43.902707 mins
	print("Size : %d time: %f" % (listSize, end-start))



    