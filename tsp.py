from timeit import default_timer as timer
from itertools import combinations
from math import sqrt
from collections import defaultdict
#from sets import frozenset

class tspRead:
	def __init__(self,file):
		self.file = file
	def readF(self):
		with open(self.file) as fd:
			next(fd)
			cities = [ [float(x) for x in line.split()] 
					for line in fd]
			dfdict = defaultdict(dict)
			for i, c in enumerate(cities,start=1):
				dfdict[i] = c
		return dfdict
class tsp:
	def __init__(self,file):
		self.cities = tspRead(file).readF()	
		size = len(self.cities)
		self.bits = xrange(2,2**size+1,2) # subset without the 1

	def city(self):
		return self.cities

	def dist(self,i,j):
		ix,iy = self.cities[i]
		jx,jy = self.cities[j]
		return sqrt((ix-jx)*(ix-jx) + (iy-jy)*(iy-jy))

	def comb(self,n):
		return (val for val in self.bits if bin(val).count('1') == n)

	def unmap(self, i):
		for count in range(1,len(self.cities)+1):
			if i & (1 << count-1) > 0:
				yield count

	def removeLinear(self):
		eps = 0.00001
		points = []
		for x,y,z in combinations(self.city(),3):
			dist = []
			for c1,c2 in combinations([x,y,z],2):
				dist.append (self.dist(c1,c2))
			if dist[0]+ dist[1] - dist[2]  < eps or \
			dist[1] + dist[2] - dist[0] < eps \
			or dist[0]+dist[2] - dist[1] < eps:
				print 'llinear', self.city()[x],self.city()[y],self.city()[z]
				points.append(y)
		size = len(self.cities)
		for y in set(points):
			self.city().pop(y)
		self.cities = dict([x for x in enumerate(self.city().values(), start=1)])
		#print self.cities
		size = len(self.cities)
		self.bits = xrange(2,2**size+1,2) # subset without the 1

	def find(self,n):
		A = defaultdict(lambda:float('inf'))
		A[(0b1,1)] = 0
		for m in range(2,n+1):
			start = timer()
			for s in self.comb(m-1):
				sx = s|0b01
				for j in self.unmap(s):
					smj = sx & ~(1<<j-1)
					A[(sx,j)]= min(A[(smj,k)] + self.dist(k,j) 
							for k in self.unmap(sx) if k!= j)
			print len(A)
			end=timer()
			print m, 'time=', end-start
		return min(A[(sx,j)] + self.dist(j,1)  for j in range(2,n+1))

if __name__ == '__main__':
	t = tsp('tsp-1.txt')
	#t = tsp('tsp.txt')

	start = timer()
	t.removeLinear()
	print t.find(len(t.city()))
	end=timer()
	print 'tsp find time:',  end-start

