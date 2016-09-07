# Johnson has the magic
import Queue as Q
from timeit import default_timer as timer
from collections import defaultdict

import dijkstra
import belmanford
from Graph import Graph

class johnson:
	def __init__(self, G, tails):
		self.n = len(G)
		self.G = G
		self.tails = tails

	def addDummyNode(self):
		self.n = self.n+1
		self.G[self.n] = {node:0 for node in self.G.keys()}
		for node in self.G:
			if node == self.n:
				continue
			self.tails[node].append(self.n)
		self.tails[self.n] = []
		#print self.G

	def setNodeWeight(self):
		self.weights = defaultdict(int)
		bf = belmanford.bellford(self.G, self.tails)
		dist =  bf.do_belman(self.n)
		for i in self.G:
			#self.weights[i] = dist[self.n][i]
			self.weights[i] = dist[i]
		#print min(w for w in self.weights)
		return self.weights

	def adjustDistance(self):
		for node in self.G:
			for tail in self.G[node]:
				self.G[node][tail] += (self.weights[node] 
				- self.weights[tail])
	def reAjdustDistance(self,data):
		for node in self.G:
			for tail in range(1,self.n+1):
				data[node][tail] -= (self.weights[node] 
				- self.weights[tail])


	def dijkstraQ(self,node1,node2=-1): 
		self.D = [float("inf")] * (len(self.G)+1)
		X = []
		path = []
		self.D[node1] = 0 # self.D has distances from node1
		q = Q.PriorityQueue()
		q.put((0, node1))

		while not q.empty():
			d,nextN =  q.get()  # least distant node from the heap
			if nextN in X:
				continue
			if nextN == node2:
				return d
			for head in self.G[nextN].keys(): 
				#calculate the distance of head->node1
				greedy = self.D[nextN] + self.G[nextN][head]
				if head not in X and  greedy < self.D[head]  :
					self.D[head] = greedy
					q.put((greedy,head))
			X.append(nextN)
		return self.D

	def allpairs_distance(self):
		dist_arr = {}
		for i in self.G:
			start=timer()
			self.dijkstraQ(i)
			end=timer()
			print 'Dijkstra time:',  end-start
			dist_arr[i] = self.D
		self.reAjdustDistance(dist_arr)
		#assert min(dist_arr[i][i] for i in self.G) == 0
		#assert max(dist_arr[i][i] for i in self.G) == 0
		return min(min(x) for x in dist_arr.values())


if __name__ == '__main__':

	files = [('bm-2.txt',-10003)]
	files = [('bm-1.txt',-10003),('bm-2.txt',-6) ]
	files = [('bm-1.txt',-10003),('bm-2.txt',-6) ,('g1.txt',-322),('g3.txt',-19),('g2.txt',-209)]
	#files = [('large.txt',-10003)]

	for file,ret in  files:
		start=timer()
		g,t = Graph(file).readF()
		j = johnson(g,t)
		#j.readF()
		j.addDummyNode()

		start1=timer()
		j.setNodeWeight()
		end=timer()
		print 'bellman-ford time:',  end-start1

		j.adjustDistance()
		assert j.allpairs_distance() == ret
		end=timer()
		print 'Total time:', file,  end-start
		print
		#print j.dijkstraQ(3)
		


