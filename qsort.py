import random
""" 
This time I could make it work I think, but frustrating. Programming is
not my strength it appears :( But the ideas are there, but for a 25yr
experienced technical fart, you are NO good.

But still able to follow the Stanford Prof's
advanced topics!

"""
from collections import deque
def myPartition(arr,l,r):
	""" partition for quicksort. using pivot as the first element.
	""" 
	pivot = arr[l]

	res = deque()
	res.append(pivot)
	pidx = l

	i = l+1
	while i <= r:
		if arr[i] < pivot:
			res.appendleft(arr[i])
			pidx += 1
		else:
			res.append(arr[i])
		i += 1
	arr[l:r+1] = res
	return pidx


def pivotAtFirst(arr,l,r):
	""" Another partition using Prof's algorithm no additional arrays
	needed
	"""
	pivot = arr[l] # First element as the pivot
	idx = bdry = l+1
	while idx <= r:
		#print idx,bdry
		if arr[idx] < pivot:
			arr[idx],arr[bdry] = arr[bdry],arr[idx]
			bdry+=1
		idx += 1
	arr[l],arr[bdry-1] = arr[bdry-1],arr[l]
	return bdry-1


def randomPivot(arr,l,r):
	#pidx = random.randint(l,r)
	pidx = random.choice(range(l,r+1))
	arr[pidx],arr[l] = arr[l],arr[pidx]
	return pivotAtFirst(arr,l,r)

def pivotAtLast(arr,l,r):
#def partition(arr,l,r):
	arr[r],arr[l] = arr[l],arr[r]
	return pivotAtFirst(arr,l,r)


def _pivotAtLast(arr,l,r):
#def partition(arr,l,r):
	""" 
	"""
	pivot = arr[r] 
	idx = bdry = r-1
	while idx >= l:
		#print idx,bdry
		if arr[idx] > pivot:
			arr[idx],arr[bdry] = arr[bdry],arr[idx]
			bdry-=1
		idx -= 1
	arr[r],arr[bdry+1] = arr[bdry+1],arr[r]
	return bdry+1

def _qsort(nlist,l,r):
	#print l,r
	if l >= r :
		return nlist
	pindx = partition(nlist,l,r)

	nlist = _qsort(nlist,l,pindx-1)
	nlist = _qsort(nlist,pindx+1,r)

	return nlist

def qsortCompare(nlist,l,r):
	count = 0;
	if l >= r :
		return 0
	pivot = nlist[l]	# First element as the pivot; looks goofy
	pindx = partition(nlist,l,r)
	count += (r-l)
	count += qsortCompare(nlist,l,pindx-1)
	count += qsortCompare(nlist,pindx+1,r)

	return count

def Rselect(array,l,r,j):
	if l >= r:
		return array[l]
	pindx = randomPivot(array,l,r)
	if pindx == j-1:
		return array[pindx]
	if pindx > j-1:
		return Rselect(array,l,pindx-1,j)
	else:
		return Rselect(array,pindx+1, r,j)

rr = [1,7,2,3,9,5,4,0,6,10,8]
for i in range(1,12):
	assert Rselect(rr,0,len(rr)-1, i) == i-1


#def partition(arr,l,r):
def meanPivot(arr,l,r):

	size = r-l+1

	if size%2 == 0:
		m = size//2-1
	else:
		m = size/2

	pp = {arr[l]:l, arr[m]:m, arr[r]:r}
	pidx = pp[sorted(pp.keys())[1]]
	#print arr[l:r+1], arr[pidx]

	arr[pidx], arr[l] = arr[l],arr[pidx]
	return pivotAtFirst(arr,l,r)

partition = meanPivot
def qsortTest():
	assert _qsort([5,2],0,1) == [2,5]
	return
	assert _qsort([5,2,3,1,4,0,11,8],0,7) == [0,1,2,3,4,5,8,11]
	assert _qsort([0,1,2,3,4,5,8,11],0,7) == [0,1,2,3,4,5,8,11]
	assert partition([5,2],0,1)
	#assert _qsort([5],0,0) == [5]
	print partition([2,5,1],0,0) 
	assert partition([5,2,3, 8,7],3,4)
	assert partition([5,2,3, 8,7],2,3)

def testmeanPivot():
	partition = meanPivot
	rr = [5,2]
	print partition(rr,0,1)
	print rr
	print partition(rr,0,1)
	print rr

	rr = [1,2,3,5,4,0,11,8]
	print meanPivot(rr,0,7)
	print rr
	meanPivot([0,1,2,3,4,5,8,11],0,7)
	meanPivot([5,3,1,4,0,11,8,2],0,7)
	a = [5,2,3,1,4,0,11,8]
	meanPivot(a,0,7)
	meanPivot([2,3,1,5,0,11,8,4],0,7)
	meanPivot([5,2,3,1],0,3)
	meanPivot([5,2,3],0,2)
	#meanPivot([5,2,3,1],0,0)

Files = ["10.txt", "100.txt", "QuickSort.txt","IntegerArray.txt" ]
Partitions = [pivotAtFirst, pivotAtLast, meanPivot,randomPivot]
#Partitions = [randomPivot]
for file in  Files:
	for part in Partitions:
		partition = part
		print 'sorting ' + file + ' using ' + part.func_name
		lines = [ int(x.strip())  for x in open(file, 'rU').readlines()]
		print qsortCompare(lines,0,len(lines)-1) 
		assert lines == range(1,len(lines)+1)
		#print qsortCompare(lines,0,len(lines)-1) 

exit()


testmeanPivot()
qsortTest()
#exit()
print qsortCompare([3, 8, 2, 1, 4, 6, 7],0,6) 
print qsortCompare([3, 8, 2, 1, 4, 6, 7],0,6) 


assert _qsort([5,2],0,1) == [2,5]
ar=[5,2]
partition(ar,0,1) 
print ar


qsortTest()

a = [5,2]
partition(a,0,1)
print a

assert qsortCompare([5,2],0,1) == 1
assert qsortCompare([2,5],0,1) == 1
ar=[5,2,3,1,4,0,11,8]
partition(ar,0,7) 
print ar

partition(ar,0,7) 
print ar

#exit()
print _qsort(ar,0,7)
n1 = [ 4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54 ]

print 'sorting 100'
print qsortCompare(n1,0,len(n1)-1) 
assert n1 == range(0,100)
print 'sorting sorted 100'
print qsortCompare(n1,0,len(n1)-1) 
assert n1 == range(0,100)


print 'sorting 10000 from file'
lines = [ int(x.strip())  for x in open("QuickSort.txt", 'rU').readlines()]
print qsortCompare(lines,0,len(lines)-1) 
assert lines == range(1,10001)
#print qsortCompare(lines,0,len(lines)-1) 

print "done.."

print 'sorting 100000 from file'
lines = [ int(x.strip())  for x in open("IntegerArray.txt", 'rU').readlines()]
print qsortCompare(lines,0,len(lines)-1) 
assert lines == range(1,100001)

partition = randomPivot
print 'sorting sorted 100000 with random pivot'
print qsortCompare(lines,0,len(lines)-1) 
assert lines == range(1,100001)

#fd = open('output.txt','w')
#for lst in srtd:
#	fd.write(str(lst) + "\n")
#fd.close()
