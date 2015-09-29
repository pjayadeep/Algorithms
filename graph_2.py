"""Docstring"""
import urllib2
import time
import random
from collections import deque

class Graph:
	"""Docstring"""
	def __init__(self, graph):
		self._graph = graph
		self._state = {}
		for node in graph:
			self._state[node] = False 
	def bfs(self,node):
		"""Docstring"""
		#if not cluster: cluster = self._graph.keys()
		visited = set([node])
		#visited = [node]
		queue = deque()
		queue.append(node)
		while queue:
			node = queue.popleft()
			for head in self._graph[node]:
				if head not in visited :
					visited.add(head)
					#visited.append(head)
					queue.append(head)
		return visited

	def largest_cc_size(self):
		"""Docstring"""
		try:
			return max([len(x) for x in self.cc_visited()])
		except ValueError:
			return 0

	def cc_visited(self):
		"""Docstring"""
		nodes_left = self._graph.keys()
		connected_components = []

		while nodes_left:
			node = nodes_left[0]
			visited_nodes = self.bfs(node)
			connected_components.append(visited_nodes)
			for node in visited_nodes:
				if node in nodes_left:
					nodes_left.remove(node)
		return list(connected_components)


def compute_resilience_fucked(graph_attack,attack_order):
	graph = Graph(graph_attack)
	connected_components = graph.cc_visited()
	# Put all the conneced notes in a UnionFind datastructure, we'll
	# check if the deleted node is in any of these before doing the bfs

	from UnionFind import UnionFind
	uf = UnionFind()
	cluster = {}
	for set_ccs in connected_components:
		ccs = list(set_ccs)
		first_uf = uf[ccs[0]]
		[uf.union(first_uf,x) for x in ccs[:]]
		cluster[uf[ccs[-1]]] = ccs
	attacked_components = []
	print cluster

	cclen = []
	cclen.append( max(len(x) for x in connected_components))
	print connected_components
	for attacked in attack_order:
		if uf[attacked] in cluster.keys():
			attacked_ccs =  cluster[uf[attacked]]
			print attacked, attacked_ccs
			attacked_ccs.remove(attacked)
			print "att", attacked_ccs
			new_ccs = graph.cc_visited(attacked_ccs)
			print new_ccs
			for ccs in  new_ccs:
				attacked_components.append(ccs)

		else:
			print "not in uf"
			attacked_components.append(cluster[uf[attacked]])
		cclen.append( max(len(x) for x in attacked_components))
	return cclen

def compute_resilience_fucked(graph_attack,attack_order):
#def compute_resilience(graph_attack,attack_order):
	"""Docstring"""
	exclude_list = []
	resilience_list =[]
	resilience_list.append(Graph(graph_attack).largest_cc_size(exclude_list))

	graph = graph_attack.copy()
	for node in attack_order:
		start_time = time.time()
		exclude_list.append(node)
		graph_tmp = Graph(graph)
		resilience_list.append( graph_tmp.largest_cc_size(exclude_list))
		print("--- Total %s seconds ---" % (time.time() - start_time))

	return resilience_list

#def compute_resilience_working(graph_attack,attack_order):
def compute_resilience(graph_attack,attack_order):
	"""Docstring"""
	resilience_list =[]
	resilience_list.append(Graph(graph_attack).largest_cc_size())

	graph = graph_attack.copy()
	for node in attack_order:
		graph.pop(node)
		for heads in graph.values():
			if node in heads:
				heads.remove(node)
		graph_tmp = Graph(graph)
		resilience_list.append( graph_tmp.largest_cc_size())
	return resilience_list

EX_GRAPH0 = {0:set([1,2]),1:set([]),2:set([])} 
EX_GRAPH1 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3]), 
		4:set([1]), 5:set([2]), 3:set([0]),  6:set([])}
EX_GRAPH2 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3,7]), 3:set([7]), 4:set([1]), 5:set([2]), 
		6:set([]),7:set([3]), 8:set([1,2]), 9:set([4,5,6,7])}

def bfs_visited(graph_visited,node):
	"""Docstring"""
	graph = Graph(graph_visited)
	return graph.bfs(node)
	
def largest_cc_size(graph_size):
	"""Docstring"""
	graph = Graph(graph_size)
	return graph.largest_cc_size()
	

#print bfs_visited(EX_GRAPH0, 0)
#print bfs_visited(EX_GRAPH1, 0)
#print bfs_visited(EX_GRAPH2, 0)
#print bfs_visited(EX_GRAPH2, 8)
#print bfs_visited(EX_GRAPH2, 9)

def cc_visited(graph_use):
	"""Docstring"""
	graph = Graph(graph_use)
	return graph.cc_visited()

#cc_visited(EX_GRAPH2)
#compute_resilience(EX_GRAPH2,[4,5])
GRAPH0 = {0: set([1]),
          1: set([0, 2]),
          2: set([1, 3]),
          3: set([2])}
#print cc_visited(GRAPH0)

GRAPH2 = {1: set([2, 4, 6, 8]),
          2: set([1, 3, 5, 7]),
          3: set([2, 4, 6, 8]),
          4: set([1, 3, 5, 7]),
          5: set([2, 4, 6, 8]),
          6: set([1, 3, 5, 7]),
          7: set([2, 4, 6, 8]),
          8: set([1, 3, 5, 7])}

print compute_resilience(EX_GRAPH2,[4,5])
print
#print compute_resiliencex(EX_GRAPH2,[4,5])
#print compute_resilience(GRAPH2, [1, 3, 5, 7, 2, 4, 6, 8])

#from UnionFind import UnionFind
#uf = UnionFind()
#print len(uf)

import matplotlib.pyplot as plt

def legend_example():
    """
    Plot an example with two curves with legends
    """
    xvals = [1, 2, 3, 4, 5]
    yvals1 = [1, 2, 3, 4, 5]
    yvals2 = [1, 4, 9, 16, 25]

    plt.plot(xvals, yvals1, '-b', label='linear')
    plt.plot(xvals, yvals2, '-r', label='quadratic')
    plt.legend(loc='upper right')
    plt.show()

#legend_example()

NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"


def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph


def generate_ER(n,p):
	start_time = time.time()
	graph = {}
	for i in range(n):
		#graph[i] = set([])
		for j in range(i,n):
			if random.random() < p and i != j :
				try:
					graph[i].add(j) 
				except KeyError:
					graph[i] = set([j])
	print("--- Total %s seconds ---generate_ER" % (time.time() - start_time))
	return graph

class UPATrial:
	"""
	Simple class to encapsulate optimized trials for UPA algorithm
	Maintains a list of node numbers with multiple instances of each number.
	The number of instances of each node number are
	in the same proportion as the desired probabilities
	Uses random.choice() to select a node number from this list for each trial.
	"""

	def __init__(self, m,n):
		"""
		Initialize a UPATrial object corresponding to a 
		complete graph with num_nodes nodes

		Note the initial list of node numbers has num_nodes copies of
		each node number
		"""
		self._m = m
		self._n = n
		self.graph = generate_ER(m,1.0)
		self._node_numbers = [node for node in range(m) for dummy_idx in range(m)]


	def run_trial(self, num_nodes):
		"""
		Conduct num_node trials using by applying random.choice()
		to the list of node numbers

		Updates the list of node numbers so that the number of instances of
		each node number is in the same ratio as the desired probabilities

		Returns:
		Set of nodes
		"""
		start_time = time.time()
		# compute the neighbors for the newly-created node
		new_node_neighbors = set()
		for dummy_idx in range(num_nodes):
			new_node_neighbors.add(random.choice(self._node_numbers))
		# update the list of node numbers so that each node number 
		# appears in the correct ratio
		self._node_numbers.append(self._m)
		self._node_numbers.extend(list(new_node_neighbors))
		#update the number of nodes
		self._m += 1
		#print("--- Total %s seconds ---" % (time.time() - start_time))
		return new_node_neighbors

	def UPA(self,m,n):
		start_time = time.time()
		m = self._m
		n = self._n
		for index in range(m,n):
			self.graph[index] = self.run_trial(m) 
		print("--- Total %s seconds ---" % (time.time() - start_time))
		return self.graph



def test_UPA():
	dpa = UPATrial(13,30000)
	full_graph = dpa.UPA(13,30000)

#	plot_graph = in_degree_distribution(full_graph)
#	x = plot_graph.keys()
#	y = plot_graph.values()
#	plot(x,y,'node number', 'noramlized in-degrees', 'UPA Graph')
	return


#test_UPA()
start_time = time.time()
network_graph = load_graph(NETWORK_URL)
print len(network_graph), sum(len(x) for x in network_graph.values())
compute_resilience(network_graph,network_graph.keys())
print("--- Total %s seconds ---" % (time.time() - start_time))
exit()

ER1 = generate_ER(1239,0.0101)
print len(ER1), sum(len(x) for x in ER1.values())
