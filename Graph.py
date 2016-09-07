# Johnson has the magic
import Queue as Q
from timeit import default_timer as timer
from collections import defaultdict

class Graph:
	def __init__(self,file):
		self.file = file
		self.G = defaultdict(defaultdict)
		self.tails = defaultdict(list)
		self.D = []

	def readF(self):
		with open(self.file) as fd:
			self.n,self.m = [int(val) for val in fd.readline().split(' ')]
			for line in fd:
				h,t,l = [int(val) for val in line.split(' ')]
				self.G[h][t] = l
				if t not in self.G:
					self.G[t] = {}
				self.tails[t].append(h)
		return self.G, self.tails
