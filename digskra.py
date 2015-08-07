import time
from sets import Set
import heap
import Queue as Q

class Graph:
	def __init__(self):
		self.nodes = Set()
		self.G = {}
		self.D = []

	def loadGFile(self,file):
		self.__init__()
		fd = open(file,"rU")
		for line in fd:
			lineData = [ x.strip() for x in line.split()]
			headNode = int(lineData[0])
			self.nodes.add(headNode)
			distD = {}
			for dist in lineData[1:]:
				node, nodeDist =  [ int(i) for i in dist.split(',')]
				distD[node] = nodeDist
				try :
					self.G[headNode].append(distD)
				except :
					self.G[headNode] = distD
				self.nodes.add(node)
		self.D = [100000] * (len(self.nodes)+1)

	def l(self,node1, node2):
		return self.G[node1][node2]

	def tails(self,node):
		try:
			return self.G[node].keys()
		except:
			return []

	def D(self,node):
		return self.D[node]

	def Nodes(self):
		return list(self.nodes)

	def dijkstra(self, node1):
		S = []
		N = self.Nodes()
		self.D[node1] = 0
		S.append(node1)

		while N:
			node = self.pickNext(S)
			if node == 0: # No more reachable nodes from node1
				return self.D
			S.append(node)
			N.remove(node)
		return self.D

	def pickNext(self,S):
		node = 0
		nodeKey = 1000000
		for head in S:
			for tail in  self.tails(head):
				if tail not in S:
					val = self.l(head,tail) + self.D[head]
					if val < nodeKey:
						nodeKey = val
						node = tail
		self.D[node] = nodeKey
		return node

	def compareD(self,n1,n2):
		try :
			return self.D[n1] < self.D[n2]
		except:
			if n1 == 100000:
				return False
			else :
				return True

	def dijkstraH(self,node1,node2=-1): 
		X = []
		path = []
		first = node1
		self.D[first] = 0
		N = self.Nodes()

		H = heap.heap(len(N))
		H.setCmpF(self.compareD)
		H.heapify(N)

		while not H.empty():
			nextN =  H.extractMin()
			if nextN == node2:
				return self.D[nextN] #, X
			if nextN in X:
				print H.l()
				raise NameError("duplicate node in X")

			for tail in self.tails(nextN): 
				greedy = self.D[nextN] + self.l(nextN,tail)
				if tail not in X and self.D[tail]  > greedy:
					self.D[tail] = greedy
					H.updateVal(H.find(tail), tail)
			X.append(nextN)
		return self.D

	def dijkstraQ(self,node1,node2=-1): 
		X = []
		path = []
		self.D[node1] = 0
		q = Q.PriorityQueue()
		q.put((0, node1))

		while not q.empty():
			d,nextN =  q.get()

			if nextN in X:
				continue

			if nextN == node2:
				return d

			for tail in self.tails(nextN): 
				greedy = self.D[nextN] + self.l(nextN,tail)
				if tail not in X and self.D[tail]  > greedy:
					self.D[tail] = greedy
					q.put((greedy,tail))
			X.append(nextN)
		return self.D

	def setDijkstra(self, D):
		self.digkstra = D


def testdigs():
	dFiles = ['digs.txt']
	r = []
	G = Graph()
	start_time = time.time()
	G.loadGFile(dFiles[0])
	dist =  G.dijkstraQ(1)  #6878
	tails = [1,2,3,4,5,6,7,8,9,10]
	for t in tails:
		r.append(dist[t])
	assert r == [0, 104, 60, 84, 40, 150, 67, 61, 80, 116]

if __name__ == '__main__':

	testdigs()

	G = Graph()
	G.loadGFile('dij1.txt')
	assert G.dijkstraQ(1)[1:] == [0,3,3,5]  

	G = Graph()
	G.loadGFile('dij2.txt')
	assert 26 ==  G.dijkstraQ(13,5)  #6878

	G = Graph()
	G.loadGFile('dig3.txt')
	assert 9 ==  G.dijkstraQ(28,6)  #6878

	dFiles = ['dijkstraData.txt']

	#PE5 values and results
	tails = [7,37,59,82,99,115,133,165,188,197]
	ans  = [2599,2610,2947,2052,2367,2399,2029,2442,2505,3068]
	r = []

	for file in dFiles:
		start_time = time.time()
		G = Graph()
		start_time = time.time()
		G.loadGFile(file)
		print("--- %s seconds ---" % (time.time() - start_time))
		start_time = time.time()
		dist =  G.dijkstraQ(1)  #6878
		print("--- %s seconds ---" % (time.time() - start_time))
		for t in tails:
			r.append(dist[t])
		assert r == ans

		start_time = time.time()
		dist =  G.dijkstraQ(199)  #6878
		print("--- %s seconds ---" % (time.time() - start_time))
		assert dist[65] == 11
		assert dist[199] == 0
		assert dist[76]  == 3220
		assert G.dijkstraH(1,7) == 2599

