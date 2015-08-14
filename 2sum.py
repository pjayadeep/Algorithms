import time
from sets import Set
fd = open('algo1-programming_prob-2sum.txt', 'rU')
#fd = open('med1.txt', 'rU')
hashTable = {}
bucketSize = 10**4
tRange = 10000

start_time = time.time()
st = start_time
for i in fd:
	val = long(i)
	key = val/bucketSize if val >= 0 else -(-val/bucketSize) 
	try:
		hashTable[key].append(val)
	except:
		hashTable[key] = [val]

S = Set()
print("--- %s seconds ---" % (time.time() - start_time))
print "reading done, size = ", len(hashTable)

start_time = time.time()
for key1 in hashTable:
	if key1 > 0: # sufficient to handle the -ve and 0 buckets.
		continue
	for x in hashTable[key1]:
		for p in [-key1, -key1-1, -key1+1]: 
			try:
				for y in hashTable[p]:
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
