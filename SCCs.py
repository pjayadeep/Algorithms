import sys 
from sets import Set
#import resource
 
#set rescursion limit and stack size limit
sys.setrecursionlimit(10 ** 6)
#resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))

# Read in the cyclic graph, reverse it!
import time

def loadGraph(file):
	S = Set()
	Edges = []
	rEdges = []

	fd = open(file,"rU")
	for line in fd:
		s,d = [ int(x) for x in line.split()]
		Edges.append([s,d])
		#rEdges.append([d,s])
		S.add(s)
		S.add(d)
	return Edges,rEdges,list(S),

def readG(file):
	G = {}
	B = {}
	fd = open(file,"rU")

	for line in fd:
		s,d = [ int(x) for x in line.split()]
		try :
			G[s].append(d)
		except :
			G[s] = [d]
		B[s] = B[d] = False
	return G,B

# Pathetically slow this one:
def revGD(G,B):
	R = {}
	for k in G:
		for d in G[k]:
			try:
				R[d].append(k)
			except :
				R[d] = [k]
			B[d] = B[k] = False
	return R,B


def adjList(Edges):
	B = {}
	adjL = [None]*(len(Edges)+2)
	for edge in Edges:
		s,d = edge
		if adjL[s]:
			adjL[s] = adjL[s] + [d]
		else:
			adjL[s] = [d]
		B[s] = False
		B[d] = False
	return adjL,B

def revAdjList(Nodes, adjList):
	revAdjL = [None]*(max(Nodes)+2)

	for node in Nodes:
		if adjList[node]:
			for rev in adjList[node]:
				if revAdjL[rev]:
					revAdjL[rev] = revAdjL[rev] + [node]
				else:
					revAdjL[rev] = [node]
	return revAdjL

"""
Depth First Search(DPS): Additionally it calculates which finishing
time of nodes it visits. Both are used for calculating the SCCs in 
the graph. Recursion hits the ceiling for Python, for large data, 
needs to up it and even the memory.
"""

Tm = 0
def dfs(G,B,g):
	count = 1
	global Tm,T
	if B[g] == True:
		return 0
	else:
		B[g] = True

	try:
		for n in G[g]:
			count += dfs(G,B,n)
	except:
		pass

	Tm+= 1
	T[Tm] = g
	return count

def dfs_loop(G,B,Nodes):
	for node in Nodes:
		if  not B[node] :
			S.append(dfs(G,B,node))
	return S

#if __main__:

dFiles = ['SCCs-1.txt', 'SCCs-2.txt', 'SCCs-3.txt', 'SCCs-4.txt', 'SCCs-5.txt', 'SCCs-6.txt','SCCs-7.txt', 'xx.txt']
#dFiles = ['xx.txt',]
S = []
T= {}
def dictGraphTest():
	global T, S,Tm
	for file in dFiles:
		print "Reading.. file:", file
		start_time = time.time()
		G,B = readG(file)
		print("--- %s seconds ---" % (time.time() - start_time))
		print "Reversing Graph.."
		start_time = time.time()
		GR,BR = revGD(G,B.copy())
		print("--- %s seconds ---" % (time.time() - start_time))

		T= {}
		S = [] 
		Tm = 0
		print "First DFS loop.."
		dfs_loop(GR,B.copy(),GR.keys())
		print "Second DFS loop.."
		start_time = time.time()
		S = [] 
		dfs_loop(G,B.copy(), T.values()[::-1])
		print (file, sorted(S)[::-1][:5])
		print("--- %s seconds ---" % (time.time() - start_time))
		print

def listGraphTest():
	for file in dFiles:
		print ("Reading.. file", file)
		start_time = time.time()
		st = start_time
		Edges,rEdges,N = loadGraph(file)
		print("--- %s seconds ---" % (time.time() - start_time))

		print ("Creating Adjacency list.. ")
		start_time = time.time()
		G,B = adjList(Edges)
		print("--- %s seconds ---" % (time.time() - start_time))

		print ("Reversing Graph..")
		start_time = time.time()
		R = revAdjList(N,G)
		print("--- %s seconds ---" % (time.time() - start_time))


#	R,B = adjList(rEdges)
#	print ("First DFS loop..")
#	start_time = time.time()

		S = [] 
		Tm = 0
		dfs_loop(R,B.copy(),range(1,len(N)+1))
		print("--- %s seconds ---" % (time.time() - start_time))

		print ("Second DFS loop..")
		start_time = time.time()
		S = [] 
		S = dfs_loop(G,B.copy(), T.values()[::-1])
		print file, (sorted(S)[::-1][:5]), 
		print("--- %s seconds ---" % (time.time() - start_time))
		print(" Total %s seconds ---" % (time.time() - st))

dictGraphTest()
#listGraphTest()
