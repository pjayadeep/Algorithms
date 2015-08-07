# Pure copy from internet, while I had the idea, couldn't grasp some key aspects of 
# the algorithm - very poor indeed!

import random, copy
from sets import Set
from UnionFind import UnionFind

data = open("kargerMinCut.txt","r")
#data = open("pa1t.txt","r")
G = {}

def adj_list(data):
	for line in data:
	    lst = [int(s) for s in line.split()]
	    G[lst[0]] = lst[1:]
	return G

def createEdges(data):
	Edges = []
	Nodes = []
	for line in data:
		lst = [int(s) for s in line.split()]
		Nodes.append(lst[0])
		for node in lst[1:]	:
			if lst[0] < node:
				Edges.append((lst[0],node))
	return Edges,Nodes

"""
Idea borrowed from Internet, from a C++ implementation: copied a UnionFind
implementation(still haven't got a clue about its imp). Yet again struggled
to make this work - didn't copy the logic properly :( But this is fast, but 
nowhere near some of the speeds reported by folks elsewhere(yes, on Python).

The approach used is not straightforward, but clean one. The speed is comparable
to that of some of the folks though 10x slower still.
"""
def kerger_UF(Edges,n):
	cut = 0
	uf = UnionFind()
	random.shuffle(Edges)
	i = 0;
	# Populate the clusters of UF till there are 2 nodes left.
	while n > 2:
		e1,e2 = Edges[i]
		i += 1
		s1 = uf[e1]
		s2 = uf[e2]
		if s1 != s2:
			uf.union(s1,s2)
			n -= 1

	# Check for edges that cross the clusters, which are mincut edges
	for e in Edges:
		e1,e2 = e
		s1 = uf[e1]
		s2 = uf[e2]
		if s1 != s2:
			cut += 1
	return cut

def mincut_UF(n):
	mincut = 10000
	maxcut = 0
	Edges,Nodes = createEdges(data)
	nSize = len(Nodes)
	while n > 0:
		cut = kerger_UF(Edges,nSize)
		if cut < mincut:
			mincut = cut
		if cut > maxcut:
			maxcut = cut
		n -= 1
	return mincut,maxcut


def choose_random_key(G):
    v1 = random.choice(list(G.keys()))
    v2 = random.choice(list(G[v1]))
    return v1, v2

def karger(G):
    length = []
    while len(G) > 2:
        v1, v2 = choose_random_key(G)

        G[v1].extend(G[v2]) # v1 + v2

        for x in G[v2]:  # replace occurences of v2 with v1
            G[x].remove(v2)
            G[x].append(v1) 

        while v1 in G[v1]: # Remove loops
            G[v1].remove(v1)
        del G[v2] # contract v2

    # the degree of vertexes of the final 2 is the mincut!! Couldn't get 
    #this idea easily :(
    # which was the crux of the algo - so algo-dumb, didn't they find 
    # out in those interviews ??

    for key in G.keys():
        length.append(len(G[key]))
    return length[0]

def operation(n):
	G = adj_list(data)
	i = 0
	count = 10000   
	while i < n:
		dat = copy.deepcopy(G)
		min_cut = karger(dat)
		if min_cut < count:
			count = min_cut
		i = i + 1
	return count

def choose_random_edge(Edges):
	return random.choice(Edges)

def swap(a,b):
	a,b = b,a

""" Epic struggle to get this work :)) Time to hang your fucking software
boots - no hope I can see. Apparently, modifying the elements in a list in the
loop which is based on the iteration on the loop was fucking up the list 
calculations: figured that out finally!

But the implementation is really slow compared to the copied one which is
blazingly fast ! This uses sets for the edges - not sure if set operations are
causing it or the conversion from adjacent lists to edge lists.

But any way, the fucking program works!

"""
def karger_E(Edges,Nodes):
	i = 0
	while  len(Nodes) > 2  :
		edge = choose_random_edge(Edges)
		#print Edges,edge
		n1 = edge.pop()
		n2 = edge.pop()
		Edges.remove(edge)
		removeList = []
		appendList = []
		for ed in Edges:
			if n2 in ed:
				if ed == Set([n1,n2]):
					removeList.append(ed)
					continue
				t = ed.copy()
				removeList.append(ed)
				t.difference_update(Set([n1,n2]))
				n3 = t.pop()
				if n1 != n3:
					appendList.append(Set([n1,n3]))

		#print Edges,len(Edges)
		for it in appendList:
			Edges.append(it)
		for it in removeList:
			Edges.remove(it)
		Nodes.remove(n2)
	return len(Edges)


def mincut_Edges (n):
	i = 0
	mincut = 10000
	maxcut = 0
	Edges,nodes = createEdges(data)
	#print Edges,nodes
	while i < n:
		#print Edges
		dat = copy.deepcopy(Edges)
		node_c = copy.deepcopy(nodes)
		karger_E(dat,node_c)
		cut = len(dat)
		if cut < mincut:
			mincut = cut
		if cut > maxcut:
			maxcut = cut
		i +=1
		print cut, mincut, maxcut
	return mincut,maxcut

if __name__ == '__main__':

	import time
	start_time = time.time()
	print mincut_UF(100)
	#print mincut_Edges(10)
	#print(operation(100))
	print("--- %s seconds ---" % (time.time() - start_time))

