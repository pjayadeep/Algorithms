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

	def removeLinear(self):
		eps = 0.01
		points = []
		for x,y,z in combinations(self.city(),3):
			dist = []
			for c1,c2 in combinations([x,y,z],2):
				dist.append (self.dist(c1,c2))
			if dist[0]+ dist[1] - dist[2]  < eps or \
			dist[1] + dist[2] - dist[0] < eps \
			or dist[0]+dist[2] - dist[1] < eps:
				#print 'llinear', self.city()[x],self.city()[y],self.city()[z]
				points.append(y)
		size = len(self.cities)
		for y in set(points):
			self.city().pop(y)
		self.cities = dict([x for x in enumerate(self.city().values(), start=1)])
		print self.cities
		size = len(self.cities)
		self.bits = xrange(2,2**size+1,2) # subset without the 1

	def city(self):
		return self.cities

	def setsf(self,n):
		setx =  self.cities.keys()
		if n != 1:
			setx.remove(1)
		return list(combinations(setx,n-1))

	def setsb(self,n):
		setx =  self.cities.keys()

	def bitmap(self,s):
		x = 0
		for i in s:
			x |= 1 << i-1
		return x

	def unmap(self, i):
		for count in range(1,len(self.cities)+1):
			if i & (1 << count-1) > 0:
				yield count

	def dist(self,i,j):
		#print i,j
		ix,iy = self.cities[i]
		jx,jy = self.cities[j]
		return sqrt((ix-jx)*(ix-jx) + (iy-jy)*(iy-jy))

	def sets(self,n):
		setx =  self.cities.keys()
		return frozenset([self.bitmap(it) for it in combinations(setx,n)])

	def count1(self,n):
		count = 0
		while n:
			count += n & 1
			n >>= 1
		return count

	def comb(self,n):
		return (val for val in self.bits if bin(val).count('1') == n)

	def find(self,n):
		A = defaultdict(lambda:float('inf'))
		#A = [[0 for dummy_col in range(n+1)] for dummy_row in range(2**n-1)] 

		A[(0b1,1)] = 0
		for m in range(2,n+1):
			start = timer()
			for s in self.comb(m-1):
				sx = s|0b01
				for j in self.unmap(s):
					smj = sx & ~(1<<j-1)
					A[(sx,j)]= min(A[(smj,k)] + self.dist(k,j) 
							for k in self.unmap(sx) if k!= j)
			end=timer()
			print m, 'time=', end-start
		return min(A[(sx,j)] + self.dist(j,1)  for j in range(2,n+1))


	def findxx(self,n):
		A = defaultdict(int)
		#A = [[0 for dummy_col in range(n+1)] for dummy_row in range(2**n)] 

		for m in range(1,n+1):
			start = timer()
			for s in self.comb(m):
				if not s & 0b01:
					continue
				if s == 0b01:
					A[(s,1)] = 0
				else:
					A[(s,1)] = float('inf')
			end=timer()
			print m, 'time=', end-start
		print 'Init array done'
		print

		for m in range(2,n+1):
			start = timer()
			B = defaultdict(int)
			for s in self.comb(m):
				if not (s & 0b01):
					continue
				for j in self.unmap(s & ~(0b01)):
					smj = s & ~(1<<j-1)
					A[(s,j)]= min(A[(smj,k)] + self.dist(k,j) 
							for k in self.unmap(s) if k!= j)
			#A=B
			end=timer()
			print m, 'time=', end-start
		return min(A[(s,j)] + self.dist(j,1)  for j in range(2,n+1))

	def findx(self,n):
		#A = defaultdict(defaultdict)
		A = [[0 for dummy_col in range(n+1)] for dummy_row in range(2**n)] 
		#combD = defaultdict(tuple)
		#print 'init array'

		for m in range(1,n+1):
			start = timer()
			for s in self.comb(m):
				if not s & 0b01:
					continue
				if s == 0b01:
					A[s][1] = 0
				else:
					A[s][1] = float('inf')
			end=timer()
			print m, 'time=', end-start
		print 'Init array done'

		for m in range(2,n+1):
			start = timer()
			for s in self.comb(m):
				for j in self.unmap(s & ~(0b01)):
					if not (s & 0b01):
						continue
					smj = s & ~(1<<j-1)
					A[s][j]= min(A[smj][k] + self.dist(k,j) 
							for k in self.unmap(s) if k!= j)
			end=timer()
			print m, 'time=', end-start
		return min(A[s][j] + self.dist(j,1)  for j in range(2,n+1))

	def findf(self,n):
		A = defaultdict(defaultdict)
		for m in range(1,n+1):
			for s in self.setsf(m):
				sx = (1,) +s
				if sx == (1,):
					A[sx][1] = 0
				else:
					A[sx][1] = float('inf')

				#A[s][j] = float('inf')

		for m in range(2,n+2):
			start = timer()
			for s in self.setsf(m):
				sx = (1,)+s
				for j in s:
					smj = list(sx)
					smj.remove(j)
					smj = tuple(smj)
					A[sx][j]= min(A[smj][k] + self.dist(k,j) 
							for k in sx if k!= j)
			end=timer()
			#print m, 'time=', end-start
		return min(A[sx][j] + self.dist(j,1)  for j in range(2,n+1))


if __name__ == '__main__':
	t = tsp('tsp-1.txt')
	#t = tsp('tsp.txt')
	#t.removeLinear()

	start = timer()
	print t.find(len(t.city()))
	end=timer()
	print 'tsp find time:',  end-start

	exit()

	start = timer()
	for m in range(2,len(t.city())+1):
		start1 = timer()
		for s in t.comb(m-1):
			for k in t.unmap(s):
				x = m,s
		end1=timer()
		print m, 'loop time:',  end1-start1

	for i in t.subset_bit(set(range(24))):
		y = [x for x in i]
	end=timer()
	print 'subset time:',  end-start
	exit()

	for i in range(25):
		start = timer()
		#t.subsets(25,i)
		for s in t.comb(i):
			pass
		end=timer()
		print i, ' time:',  end-start
	exit()
