#import numpy as np
from timeit import default_timer as timer
from collections import defaultdict
import sys
from Graph import  Graph

# Belman Ford algorithm for shortest path from each of the vertex
# Dynamic programming algorithm 

class bellford:
	def __init__(self,G,tails):
		self.n = len(G)
		self.G = G
		self.tails = tails

	def do_belman(self,s):
		self.n = len(self.G)
		#print 'size=' , self.n
        	self.arr = [0 for dummy_col in range(self.n+2)] 

		for x in self.G.keys():
			if x != s:
				self.arr[x] = float('inf')
		start=timer()
		for i in xrange(1,self.n+2):
			start1=timer()
			barr = [ 0 for i in range(self.n+2)]
			for v in self.G:
				tail = self.tails[v]
				if tail:
					minv = min( self.arr[w] +self.G[w][v]
							for w in tail)
				else:
					minv = float('inf')
				barr[v] = min(self.arr[v], minv)
			end1=timer()
			#print 'loop time:',  end1-start1
			self.arr = barr

		end=timer()
		#print 'loop time:',  end-start
		#return self.arr
		return min(self.arr)


	def do_belmanx(self,s):
		self.n = len(self.G)
		print 'size=' , self.n
        	self.arr = [[0 for dummy_col in range(self.n+2)] for dummy_row in range(self.n+2)] 
		self.arr[0][s] = 0
		for x in self.G.keys():
			if x != s:
				self.arr[0][x] = float('inf')
		start=timer()
		for i in xrange(1,self.n+2):
			start1=timer()
			for v in self.G:
				tail = self.tails[v]
				if tail:
					minv = min( self.arr[i-1][w] +self.G[w][v]
							for w in tail)
				else:
					minv = float('inf')
				self.arr[i][v] = min(self.arr[i-1][v], minv)
			end1=timer()
			#print 'loop time:',  end1-start1
			if self.arr[i] == self.arr[i-1]:
				break
		end=timer()
		print 'loop time:',  end-start
		#return min(min (x) for x in self.arr)
		return self.arr

	def run(self):
		return min (self.do_belman(i) for i in self.G)



if __name__ == '__main__':

	files = [('bm-3.txt',-10003)]
	files = [('bm-1.txt',-10003),('bm-2.txt',-6) ]
	files = [('bm-1.txt',-10003),('bm-2.txt',-6) ,('g2.txt',55),('g1.txt',66),('g2.txt',77)]

	for file,ret in  files:
		start=timer()
		g,t= Graph(file).readF()
		bf = bellford(g,t)
		value = bf.run() 
		assert value == ret
		end=timer()
		print(file, value, "time: ", end-start)
		print
