import time
from sets import Set

class Graph:
	def __init__(self):
		self.adjList = {}
		self.radjList = {}
		self.status = {}
		self.rstatus = {}
		self.Tm = 0
		self.T = {}
		self.nodes = Set()

	def addE(self,v1, v2):
		try:
			self.adjList[v1].append(v2) 
		except:
			self.adjList[v1] = [v2]
		self.status[v1] = self.status[v2] = False
		self.nodes.add(v1)
		self.nodes.add(v2)

	def loadGFile(self,file):
		self.__init__()
		fd = open(file,"rU")
		for line in fd:
			s,d = [ int(x.strip()) for x in line.split()]
			self.addE(s,d)

	def reverse(self):
		R = Graph()
		for k in self.adjList:
			for d in self.adjList[k]:
				R.addE(d,k)
		return R

	def len(self):
		return len(self.adjList)

	def dfs(self,g):
		count = 1
		if self.status[g] == True:
			return 0
		else:
			self.status[g] = True
		try:
			for n in self.adjList[g]:
				count += self.dfs(n)
		except:
			pass
		self.Tm += 1
		self.T[self.Tm] = g
		return count

	def finTimes(self):
		return self.T

	def Nodes(self):
		return list(self.nodes)


	def sccLen(self):
		R = self.reverse()
		#R.dfs_loop(R.Nodes())
		R.dfs_loop(self.adjList)
		finT = R.finTimes()
		finOrder = [finT[n] for n in sorted(finT.keys())[::-1]]
		return self.dfs_loop(finOrder)

	def dfs_loop(self,Nodes):
		S = []
		for node in Nodes:
			if  not self.status[node] :
				S.append(self.dfs(node))
		return S

dFiles = ['SCCs-1.txt', 'SCCs-2.txt', 'SCCs-3.txt', 'SCCs-4.txt', 'SCCs-5.txt', 'SCCs-6.txt','SCCs-7.txt', 'xx.txt', 'SCC.txt']
#dFiles = ['xx.txt']
for file in dFiles:
	start_time = time.time()
	G = Graph()
	G.loadGFile(file)
	scc = G.sccLen()
	print file, sorted(scc)[::-1][:5]
	#print sorted(G.sccLen())[::-1][:5]
	print("--- %s seconds ---" % (time.time() - start_time))

