from sets import Set
import heap
from UnionFind import UnionFind
class MST :
	def __init__(self,file):
		self.Graph = {}
		self.sortedGraph = []
		self.file = file
		self.graph()

	def nodeinfo(self):
		return self.Graph

	def edges(self):
		with open(self.file) as fd:
			fd.readline()
			for line in fd:
				yield [int(num) for num in line.strip().split(' ')]

	def graph(self):
		# should index on node, but to make things easier for an old
		# fart, using weight as an index. But it doesn't hurt it seems??
		# update: changed that to index on nodes, in a desparate 
		# attempt to solve the problem. Old fart is getting upto
		# speed :)
		for node1, node2, weight in self.edges():

			l1 = {node1:weight}
			l2 = {node2:weight}

			if node1 not in self.Graph:
				self.Graph[node1] = l2
			else:
				self.Graph[node1].update(l2)

			if node2 not in self.Graph:
				self.Graph[node2] = l1
			else:
				self.Graph[node2].update(l1)

			self.sortedGraph.append((weight,node1,node2))
		self.sortedGraph = sorted(self.sortedGraph)

		#self.heapG()


	def heapG(self):
		h = heap.heap(501)
		h.setCmpF(self.cmpN)

		#h.heapify([ (min((cost,end) for (end,cost) in 
		#	self.Graph[node].items()) + (node,))
		#		for node in self.Graph.keys() ])

		h.heapify(self.Graph.keys())
		print h.extractMin()
		print h.extractMin()
		print h.extractMin()

	def cmpN(self,n1,n2):
		try: 
			return min(self.Graph[n1].values()) < min(self.Graph[n2].values())
		except :
			if n1 == float("inf"):
				return False
			else :
				return True


	def cheapest_edge(self, node,X):
		# use a heap ??
		curnode = self.Graph [node]
		targets =  [(cost,edge) 
				for (edge,cost) in curnode.items() 
				if edge not in X]
		if not targets:
			return [(),(),()]
		minval,end = min(targets)

		return minval,end,node
		
	def del_edge(self,node,pair):
		curnode = self.Graph[node]
		for end,weight in curnode.items():
			if end == pair:
				self.Graph[node].pop(end)
				break

	def primMST(self):
		cheapest_cost = 0
		S = Set(self.Graph.keys())
		X = Set([self.Graph.keys()[0] ])
		Tree = []
		# start prims with X
		while X != S:
			cheap_nodes =  [self.cheapest_edge(node,X) 
				for node in X if self.Graph[node] ]

			cost,target,source = min( (cost,target,source)
					for (cost,target,source) in cheap_nodes )

			cheapest_cost += cost
			X.update([target])
			Tree.append((source,target,cost))
			self.del_edge(target,source)
			self.del_edge(source,target)

		return cheapest_cost

	def kruskalsMST(self):
		edges = self.sortedGraph
		uf = UnionFind()
		T = []
		total_cost = 0
		for cost,source,target in edges:
			s1,s2 = uf[source],uf[target]
			if s1 != s2 :
				uf.union(s1,s2)
				T.append((source,target))
				total_cost += cost
		return total_cost

	def k_clustering(self):
		edges = self.sortedGraph
		uf = UnionFind()
		size = 500
		cluster_size = 4
		spacing = 0

		for spacing,source,target in edges:
			s1,s2 = uf[source],uf[target]
			# enough clusters, return the spacing
			if size <= cluster_size:
				if s1 != s2:
					return spacing
		# if in different clsuters, join them reducing one cluster
			if s1 != s2 :
				uf.union(s1,s2)
				size -= 1
		return spacing


if __name__ == '__main__':

	import time
	start_time = time.time()
	mst = MST('clustering1.txt')
	assert mst.k_clustering() == 106
	print("-Clustering1- %s seconds ---" % (time.time() - start_time))

	mst = MST('prims-t1.txt')
	assert -559 == mst.primMST()
	assert -559 == mst.kruskalsMST()

	mst = MST('prims-edges.txt')
	start_time = time.time()
	assert (-3612829 == mst.kruskalsMST())
	print("-kruskals- %s seconds ---" % (time.time() - start_time))

	start_time = time.time()
	assert (-3612829 == mst.primMST())
	print("-Prims- %s seconds ---" % (time.time() - start_time))
	exit()

	print gra[500] 
	mst.del_edge(478,193)
	print

	print gra[228] 
	print mst.cheapest_edge( 397)
	mst.del_edge(228,397)
	print gra[228] 
	print gra[397] 
	mst.del_edge(397,228)
	print gra[397] 

	#for key in gra.keys():

	print mst.cheapest_edge( 1)

	#assert gra[2][3] == gra[3][2]
	print gra[1] 
	print gra[397]
	#mst.del_edge(2)
	try:
		print gra[3]
		print gra[2] 
	except KeyError:
		pass

