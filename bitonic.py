def bitonic_max(array):
    if len(array)==1:
        return array[0]
    else:
        if array[len(array)//2-1]<array[len(array)//2]:
            return bitonic_max(array[len(array)//2:])
        else:
            return bitonic_max(array[:len(array)//2])

assert bitonic_max([1,5,4,3,2]) == 5


def binary_search(nums,key,__cmp__= lambda x,y: x < y):
	#assert(nums != [])
	if not nums: return False
	size = len(nums)
	if size%2 == 0:
		middle = len(nums)//2-1
	else:
		middle = len(nums)//2

	#print "binary ", size,nums,middle

	if key == nums[middle]:
		return True
	else:
		if len(nums) == 1 :
			return False
	if __cmp__(nums[middle] , key):
		return binary_search(nums[middle+1:],key,__cmp__)
	else:
		return binary_search(nums[:middle],key, __cmp__)


def bitonic_search(nums, v):
	if not nums: return False
	size = len(nums)
	if size%2 == 0:
		middle = len(nums)//2-1
	else:
		middle = len(nums)//2
	#print "bitonic: ",size,nums,middle

	if v == nums[middle]:
	   return True
   	else:
		if size == 1:
			return False
	#split at the maximum value and binary search the lists
	if nums[middle-1] < nums[middle] > nums[middle+1]:
		if binary_search(nums[:middle],v):
			return True
		else : return binary_search(nums[middle+1:],v,lambda x,y:x>y)

	# v is in the bitonic part of the array
   	if nums[middle] < v :
		if nums[middle+1] < nums[middle]:
			return bitonic_search (nums[:middle],v)
		else:
			return bitonic_search(nums[middle+1:],v)

	# v is in head or tail part of the arrays: binary search first,
	# if not found,  continue as usual 
	if nums[middle] > v:
		if nums[middle+1] > nums[middle]:
			if binary_search(nums[:middle],v):
				return True
			else:
				return bitonic_search(nums[middle+1:],v)
		else:
			if binary_search(nums[middle+1:],v,lambda x,y:x>y):
				return True
			else:
				return bitonic_search(nums[:middle],v)

def test_bitsearch():
	assert bitonic_search([1,3,2], 2) 
	assert not bitonic_search([1,3,5,4,2,0], -1) 
	assert bitonic_search([1,3,5,4,2,0], 4) 
	left = range(1,100,2)
	right = range(100,0,-2)
	l = left + right
	assert not bitonic_search(l, -23) 
	assert not bitonic_search(l, 123) 
	for i in l:
		assert bitonic_search(l, i) 
	assert not bitonic_search(l, 0) 
	print "OK"

def test_bsearch():
	l = range(1,100)
	for i in l:
		assert binary_search(l,i)
	assert binary_search([50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2] , 35,lambda x,y:x>y) == False
	assert binary_search([50, 48] , 48,lambda x,y:x>y) == True
	assert binary_search([4,5],7) == False
	assert binary_search([4,5,6],6) == True
	assert binary_search([4,5,6],1) == False
	assert binary_search([4,5,6],8) == False
	assert binary_search([4],4) == True
	assert binary_search([4],5) == False
	assert binary_search([4,5],5) == True
	assert binary_search([4,5,7,8],5) == True
	assert binary_search([4,5,7,8],10) == False
	assert binary_search([4,2,0],4,lambda x,y:x>y) == True
	assert binary_search( [25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47],35) == True
	print "OK"


if __name__ == "__main__":
	test_bsearch()
	test_bitsearch()
