import time
from sets import Set
import random

class Graph:
	def __init__(self):
		self.adjList = {}
		self.visited = {}
		self.order = []
		self.TD = []
		self.T = {}
		self.Tm = 0

	def addE(self,v1, v2):
		try:
			self.adjList[v1].append(v2) 
		except:
			self.adjList[v1] = [v2]
		self.visited[v1] = self.visited[v2] = False

	def loadGFile(self,file):
		self.__init__()
		fd = open(file,"rU")
		for line in fd:
			s,d = [ int(x.strip()) for x in line.split()]
			self.addE(s,d)
		return self.adjList

	def reverse(self):
		R = Graph()
		for k in self.adjList:
			for d in self.adjList[k]:
				R.addE(d,k)
		return R

	def __len__(self):
		return len(self.adjList)

	def dfs(self,root):
		TD = []
		stack = [root]
		while stack:
			node = stack.pop()
			if not self.visited[node] :
				self.visited[node] = True
				TD.append(node) 
				if node in self.adjList:
					stack += self.adjList[node]
		self.order += list(reversed(TD))
		return TD
	def dfsxxx(self,root):
		count = 0
		TD = []
		stack = [root]
		while stack:
			node = stack.pop()
			if not self.visited[node] :
				stack.append(node)
				count += 1
				self.visited[node] = True
				TD.append(node) 
				if node in self.adjList:
					for child in self.adjList[node]:
						if not self.visited[child] :
							stack.append(child)
			else:
				if node not in self.T.values():
					self.Tm += 1
					self.T[self.Tm] = node
		return TD

	def dfsR(self,g):
		count = 1
		self.TD = []
		#self.T = {}
		if self.visited[g]:
			return []
		self.TD.append(g)
		self.visited[g] = True
		try:
			for n in self.adjList[g]:
				self.TD += self.dfsR(n)
		except KeyError:
			pass

		self.Tm += 1
		self.T[self.Tm] = g
		return self.TD


	def sccLenR(self):
		self.T = {}
		self.Tm = 0
		R = self.reverse()
		R.dfs_loopR(R.adjList)
		finOrder = list(reversed(R.T.values()))
		#print finOrder
		return  self.dfs_loopR(finOrder)

	def dfs_loopR(self,Nodes):
		S = []
		for node in Nodes:
			if  not self.visited[node] :
				nodeCount = self.dfsR(node)
				#S.append(len(nodeCount))
				S.append(nodeCount)
		return S

	def sccLen(self):
		R = self.reverse()
		R.dfs_loop(R.adjList)
		finOrder = list(reversed(R.T.values()))
		#print 'finorder',finOrder
		return  self.dfs_loop(finOrder)

	def dfs_loop(self,Nodes):
		S = []
		for node in Nodes:
			if  not self.visited[node] :
				dfsNodes = self.dfs(node)
				S.append(len(dfsNodes))
				#S.append(dfsNodes)
		self.T = dict(enumerate(self.order,start=1))
		return S

if __name__ == '__main__':
	dFiles = ['SCCs-1.txt', 'SCCs-2.txt', 'SCCs-3.txt', 'SCCs-4.txt', 'SCCs-5.txt', 'SCCs-6.txt','SCCs-7.txt', 'xx.txt' , 'SCC.txt']
	results = [[3, 3, 2],  [3, 3, 1,1], [7, 1] , [6, 3, 2, 1], [3, 3, 2],[30, 11, 11, 1, 1], [3, 3, 3],[5] , [434821, 968, 459, 313, 211]]
	data_results = zip(dFiles,results)

	dataDict = dict(zip(dFiles,results))
	#print dataDict

	#dataDict = {'SCCs-5.txt': [3,3,2]}

	for file,result in dataDict.items():
		start_time = time.time()
		G = Graph()
		print file
		G.loadGFile(file)
		scc = G.sccLen()
		print sorted(scc)[::-1][:5] , result
		assert sorted(scc)[::-1][:5] == result
		print("--- %s seconds ---" % (time.time() - start_time))
		print

