import time
from sets import Set
fd = open('algo1-programming_prob-2sum.txt', 'rU')
#fd = open('med1.txt', 'rU')
arr = {}
bucketSize = 10**4
tRange = 10000

start_time = time.time()
st = start_time
for i in fd:
	val = int(i)
	try:
		arr[val/bucketSize].append(val)
	except:
		arr[val/bucketSize] = [val]

S = Set()
print("--- %s seconds ---" % (time.time() - start_time))
print "reading done, size = ", len(arr)
#print len(arr), len(arr.values())

start_time = time.time()
for key1 in arr:
	if key1 > 0: # sufficient to handle the -ve and 0 buckets.
		continue
	yrange1 = tRange/bucketSize - key1
	yrange2 = -tRange/bucketSize - key1
	#print key1, range(yrange2-1,yrange1)

	for x in arr[key1]:
		for p in range(yrange2-1,yrange1):
		#for p in [-key1, -key1-1, -key1-2]: 
			try:
				for y in arr[p]:
					if y == x: continue
					t = x + y
					if abs(t) <= tRange :
						S.add(t)
			except :
				pass

print("--- all %s seconds ---" % (time.time() - start_time))
print("--- Total %s seconds ---" % (time.time() - st))
print len(S)
assert len(S) == 427
