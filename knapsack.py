import numpy as np
import sys,resource
sys.setrecursionlimit(10 ** 6)
#resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))

# knapsack: fill the sack with highest value with as minimum weight as
# possible. A greedy alogrithm to solve this.

class knapsack:
	def __init__(self,file):
		self.file = file
		self.data = {}

	def readFile(self):
		with open(self.file) as fd:
			self.W,self.size = [int(val) for val in 
					fd.readline().split(' ')]
			rows = []
			for line in fd:
				rows.append(tuple([int(val) for val in 
					line.split(' ')]))
		self.data = dict( enumerate(rows))
		#print self.W, self.size
		return self.data

	def sack(self):
		self.readFile()
		# Initialize a 2D array
		arr = np.zeros([self.size,self.W], dtype=int)
		for i in range(self.size):
			for x in range(self.W):
				v_i,w_i = self.data[i]
				if x >= w_i :
					arr[i,x] = max(arr[i-1,x] , 
						arr[i-1,x-w_i] + v_i)
				else:
					arr[i,x] = arr[i-1,x]
		return arr[self.size-1,self.W-1]

	def sackX(self):
		self.readFile()
		print 'n=',self.size,'W=', self.W
		arr_im1 = arr_ix = 0
		xvalues = [0]*self.W
		xvalues_m1 = [0]*self.W
		for item in self.data.items():
			x,(v_i,w_i) = item
			for x in xrange(self.W):
				if x >= w_i:
					arr_ix = max(xvalues_m1[x], 
							xvalues_m1[x-w_i]+v_i)
				else:
					arr_ix = xvalues_m1[x]
				xvalues[x] = arr_ix
			xvalues_m1 = xvalues[:]
		return arr_ix

	def sackR(self):
		self.readFile()
		print 'n=',self.size,'W=', self.W

		# How to recurse ? Pick one item, check if it belongs and keep it aside
		# by recursing on the rest.
		nodes = []
		#print self.data
		cache = {}
		def ksack(i,x):
			if i <= 0:
				return 0
			v,w = self.data[i-1]
			try :
				return cache[(i,x)]
			except KeyError:
				if x < w:
					cache[(i,x)] = ksack(i-1,x)
				else:
					cache[(i,x)] =  max(ksack(i-1,x), 
							ksack(i-1,x-w)+v)
			return cache[(i,x)]
		return ksack(self.size,self.W)
		#print nodes
			
				
if __name__ == '__main__':
	from timeit import default_timer as timer

	data_results = [('1.txt', 4), ('knapsack_t1.txt',8), ('knapsack1.txt',2493893), 
			('knapsack_big.txt',4243395)]
#	data_results = [('1.txt', 4), ('knapsack_t1.txt',8), ('knapsack1.txt',2493893), ]

	for f,result in data_results:
		start=timer()
		assert knapsack(f).sackR() == result
		end1 = timer()
		print('total time for ' + f, end1-start)

