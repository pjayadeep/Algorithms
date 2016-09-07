from UnionFind import UnionFind
import time

class hamClusters :
	def __init__(self,file):
		self.file = file
		self.hamm=[0]*300
		self.hamcode()
		self.points = [0]*pow(2,24)
		self.clusters = 0
		self.index = {}
		self.uf = UnionFind()
		self.process_data()

	def spacing(self):
		for node in  self.index.keys():
			self.cluster_neighbors(node)
		return self.clusters

	def process_data(self):
		with open(self.file) as f:
		    next(f)
		    cluster=1
		    for line in f:
			curindex=int(line.replace(' ',''), base = 2)
			self.points[curindex] = cluster
			self.index[curindex] = True
			cluster += 1
		self.clusters = len(self.index)
		print 'size=', self.clusters, len(self.points)

	def hamcode(self):
		#computing simple numbers
		k=0
		for i in range(24):
		    for j in range(i,24):
			mask=1 << i
			mask2 = 1 << j
			self.hamm[k]=mask|mask2
			k=k+1
	
	def cluster_neighbors(self,node):
	    	for i in self.hamm:
			if self.points[node^i] !=0:
				s1 = self.uf[node]
				s2 = self.uf[node^i]
				if s1 != s2:
					self.uf.union(s1,s2)
					self.clusters -= 1


if __name__ == "__main__":
	from timeit import default_timer as timer

	start=timer()
	graph = hamClusters('clustering_big.txt')
	read_end=timer()
	print("read time", read_end-start)

	loopstart=timer()
	print graph.spacing()
	end=timer()

	print("process time", end-loopstart)
	print("total time", end-start)
	exit()

