# Princeton Class work - needs to be done in Java, trying
# this in Python.

import random
from UnionFind import UnionFind
import time
import scipy
import math

class Percolation:
	def __init__(self, N):
		self.uf = UnionFind()
		[self.uf[(n,m)] for n in range(N) for m in range(N)]
		self.grid = {(n,m):0 for n in range(N) for m in range(N)}
		self.N = N

		#setup virtual cells on top and bottom
		self.vtop = (-1,-1)
		self.grid[self.vtop] = 1
		self.vbot = (self.N,self.N)
		self.grid[self.vbot] = 1

	def __str__(self):
		"""
		Return a string representation of the grid for debugging.
		"""
		rows = [[self.grid[(i,j)] for j in range(self.N)] for i in range(self.N)]
		return '\n'.join([str(row) for row in rows])

	def open(self,i,j):
		self.grid[(i,j)] = 1

	def isOpen(self,i,j):
		return self.grid[(i,j)] == 1
		
	def isFull(self ):
		False if 0 in self.grid.values() else True

	def percentageFull(self):
		full = sum(self.grid.values())
		return full*1.0/(self.N*self.N)

	def neighbors(self,i,j):
		probables =  [(i+1,j) ,(i-1,j),(i,j+1), (i,j-1)]
		coords = [(x,y) for (x,y) in probables if 0<=x<self.N and 0<=y<self.N]
		# Add the virtual cells for top and bottom
		if i == 0: coords += [self.vtop]
		if i == self.N-1: coords += [self.vbot]
		return coords

	def percolates(self):
		return self.uf[self.vbot] == self.uf[self.vtop]

	def run(self):
		start_time = time.time()
		cells = self.grid.keys()

		for count in cells:
			coord = random.choice(cells)
			while self.isOpen(coord[0],coord[1]):
				coord = random.choice(cells)
			self.open(coord[0], coord[1])

			for cell in self.neighbors(coord[0],coord[1]):
				if self.isOpen(cell[0],cell[1]):
					self.uf.union(coord,cell)
			if self.percolates():
				break
		#print("--- %sX%s  %s seconds ---" % (self.N,self.N,time.time() - start_time))
		return self.percentageFull()

class PercolationStats:
	def __init__(self,N,T):
		self.N = N
		self.T = T
		start_time = time.time()
		self.ratio = []
		for i in range(T):
			self.ratio.append(Percolation(N).run())
		print
		self.elapsed = time.time() - start_time
		print("--- %sX%s(%s)  %s seconds ---" % (N,N,T,self.elapsed))

	def timeTaken(self):
		return self.elapsed

   	def mean(self):
	   return sum(self.ratio)/self.T
	   #return scipy.mean(self.ratio)

   	def stddev(self) :
		mean = self.mean()
	   	#return scipy.std(self.ratio)
		return math.sqrt(sum([(value-mean)**2 for value in self.ratio])/(self.T-1))
	def confidence(self):
		mean = self.mean()
		sigma = self.stddev()
		return mean - (1.96*sigma/math.sqrt(self.T)), mean + (1.96*sigma/math.sqrt(self.T))

if __name__ == "__main__":
	grid = Percolation(4)
	print grid
	print grid.run()
	print grid

	#stats = PercolationStats(5,1)
	timeStats = {}
	for count in [(2**i)*10 for i in range(6)]:
		stats = PercolationStats(count,50)
		timeStats[count] = stats.timeTaken()
		print "mean = ", stats.mean()
		print "stddev = ", stats.stddev()
		print "95% confidence interval = ", stats.confidence()
		print
	for i in sorted(timeStats.keys()):
		print i, timeStats[i]
