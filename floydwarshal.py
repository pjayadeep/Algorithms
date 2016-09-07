#import numpy as np
import sys
from timeit import default_timer as timer
from Graph import Graph

# Floyd Warshal shortest path pairs in the graph: O(n^3) in time and space
# can't run on laptop, poor space.

class floydWarshal:
	def __init__(self,G,tails):
		self.G = G
		self.n = len(G)
		self.tails = tails

	def do_fw(self):

		print '|v|=', self.n
        	self.arr = [[[float('inf') for dummy_col in range(self.n+1)] for dummy_row in range(self.n+1)] for dummy_height in range(self.n+1)] 
		#self.arr = np.full([self.n+1, self.n+1, self.n+1], 99999999999, dtype=int)
		print 'initialized the 3-D array'

		n = self.n+1
		A = self.arr

		start=timer()
		for i in xrange(1,n):
			for j in xrange(1,n):
				if i == j :
					A[i][j][0] = 0
				if i in self.G:
					if j in self.G[i]:
						A[i][j][0] = self.G[i][j]
					else:
						A[i][j][0] =float('inf')
				else:
					A[i][j][0] =float('inf')

		for k  in xrange(1,n):
			for i in xrange(1,n):
				for j in xrange(1,n):
					A[i][j][k] = min(A[i][j][k-1],
						A[i][k][k-1] + A[k][j][k-1])
		end=timer()
		print 'loop time:',  end-start
		mins = []
		for xx in self.arr:
			for x in xx:
				mins.append(min(x))
		#print min(min(x) for x in  [y for y in self.arr])
		return min(mins)
		#return np.min(self.arr)


if __name__ == '__main__':

	files = [('bm-1.txt',-10003),('bm-2.txt',-6) ]
	files = [('bm-1.txt',-10003),('bm-2.txt',-6) ,('g2.txt',55),('g1.txt',66),('g2.txt',77)]

	for file,ret in  files:
		start=timer()
		g,t = Graph(file).readF()
		bf = floydWarshal(g,t)
		print 'read done'
		print bf.do_fw() 
		#assert bf.run() == ret
		end=timer()
		print(file, "time: ", end-start)
		print
