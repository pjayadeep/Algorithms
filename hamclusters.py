from UnionFind import UnionFind
import numpy as np
import time
import sys
#sys.setrecursionlimit(10 ** 4)

class hamClusters :
	def __init__(self,file):
		self.file = file

	def hamNodes(self):
		with open(self.file) as fd:
			next(fd)
			bits = [  bitStream for bitStream in 
					[''.join(line.strip().split(' ')) 
						for line in fd] ]
		#for bit in bits:
			#print bit, int(bit,2)
		return bits

	def hammingDistance(self,s1,s2):
		assert len(s1) == len(s2)
		return sum ( x != y for (x,y) in zip(s1,s2))

if __name__ == "__main__":
	from timeit import default_timer as timer
	
	#computing simple numbers
	hamm=[0]*300
	k=0
	for i in range(24):
	    #for j in range(i,24):
	    for j in range(i,24):
		mask=1 << i
		mask2 = 1 << j
		hamm[k]=mask|mask2
		k=k+1

	
	#function that computes neighbors for the given point
	cx = 0
	def cluster_neighbors(node,uf):
		global size
	    	for i in hamm:
			if points[node^i] !=0:
				s1 = uf[node]
				s2 = uf[node^i]
				if s1 != s2:
					uf.union(s1,s2)
					size -= 1
		return 

	#reading the data into arrays points and index
	loopstart=timer()
	points = [0]*pow(2,24)
	index = {}
	from timeit import default_timer as timer
	start=timer()
	
	#with open("cl_t.txt") as f:
	with open("clustering_big.txt") as f:
	    next(f)
	    cluster=1
	    for line in f:
		curindex=int(line.replace(' ',''), base = 2)
		points[curindex] = cluster
		index[curindex] = True
		cluster += 1

	size =len(index)
	uf = UnionFind()
	print 'size=', size, len(points)
	for node in  index.keys():
		cluster_neighbors(node,uf)
	end=timer()

	print("loop time", end-loopstart)
	print("total time", end-start)
	#print(len(names)-1)
	exit()

	hst = hamClusters('clustering_big.txt')
	bits = hst.hamNodes()
	first = bits[0]
	for first in bits:
		start_time = time.time()
		print [ hst.hammingDistance(first,bit) 
					for bit in bits if bit != first and hst.hammingDistance(first,bit) <4 ]
		print("--- %s seconds ---" % (time.time() - start_time))
					#for first in bits]


	assert hst.hammingDistance('000100001', '110000010') == 5
	assert hst.hammingDistance('000100001', '000100001') == 0
	assert hst.hammingDistance('100100001', '000100001') == 1
	assert hst.hammingDistance('000100001', '000100000') == 1

	def neighbors(vertex):
		ns = []
	    	for i in hamm:
			if points[vertex^i] !=0:
				ns.append(vertex^i)
		return ns

	def discover_cluster(vertex):
		reached[vertex] = True
		for v in neighbors(vertex):
			if not reached[v] :
				discover_cluster(v)
	def fss():
		reached = [False]*pow(2,24)
		nclusters = 0
		for vertex in index:
			if not reached[vertex]:
				nclusters += 1
				discover_cluster(vertex)
