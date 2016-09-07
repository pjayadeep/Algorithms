from UnionFind import UnionFind

class MST :
	def __init__(self,file):
		self.Graph = {}
		self.file = file
		self.graph()

	def nodeinfo(self):
		return self.Graph

	def edges(self):
		with open(self.file) as fd:
			fd.readline()
			for line in fd:
				yield [int(num) for num in 
						line.strip().split(' ')]

	def graph(self):
		return sorted((cost,source,target) 
				for (source,target,cost) in self.edges())



	def kruskalsMST(self):
		edges = self.graph()
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

if __name__ == '__main__':
	
	mst = MST('prims-edges.txt')
	assert (-3612829 == mst.kruskalsMST())
	mst = MST('prims-t1.txt')
	assert -559 == mst.kruskalsMST()
