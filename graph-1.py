"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports
import urllib2
import time
import numpy as np
import matplotlib.pyplot as plt
import random

# Set timeout for CodeSkulptor if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)


###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

EX_GRAPH0 = {0:set([1,2]),1:set([]),2:set([])} 
EX_GRAPH1 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3]), 
		4:set([1]), 5:set([2]), 3:set([0]),  6:set([])}
EX_GRAPH2 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3,7]), 3:set([7]), 4:set([1]), 5:set([2]), 
		6:set([]),7:set([3]), 8:set([1,2]), 9:set([4,5,6,7])}


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
    total = 0
    for line in graph_lines:
        neighbors = [int(x) for x in line.split()]
	total += len(neighbors)-1
        node = neighbors[0]
        answer_graph[node] = set([])
        [answer_graph[node].add(neighbor) for neighbor in neighbors[1:]]
    return answer_graph

def in_degree_distribution(digraph):
	""" docstring"""
	indegree = {}
	edges = sum([len(digraph[node]) for node in digraph.keys()]) 
	per_node_degree =  edges*1.0/len(digraph)
	print edges,per_node_degree

	degree = compute_in_degrees(digraph)
	for val in degree.values():
		try:
			indegree[val] += 1
		except KeyError:
			indegree[val] = 1.0
	for node in indegree:
		indegree[node] = indegree[node]*1.0/ (edges*1.0)
	return indegree


def compute_in_degrees(digraph):
	""" docstring"""
	indegree = {}
	for node in digraph.keys():
		indegree[node] = 0
	for node in digraph.keys():
		for head in digraph[node]:
			try:
				indegree[head]  += 1
			except KeyError:
				indegree[head]  = 1
    	print "max indegree", max(indegree.values())
	return indegree

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
			if random.random() < p and i != j :
				try:
					graph[j].add(i) 
				except KeyError:
					graph[j] = set([i])
	print("--- Total %s seconds ---generate_ER" % (time.time() - start_time))
	return graph

class DPATrial:
	"""
	Simple class to encapsulate optimized trials for DPA algorithm
	Maintains a list of node numbers with multiple instances of each number.
	The number of instances of each node number are
	in the same proportion as the desired probabilities
	Uses random.choice() to select a node number from this list for each trial.
	"""

	def __init__(self, m,n):
		"""
		Initialize a DPATrial object corresponding to a 
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
		#start_time = time.time()
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

	def DPA(self,m,n):
		start_time = time.time()
		m = self._m
		n = self._n
		for index in range(m,n):
			self.graph[index] = self.run_trial(m) 
		print("--- Total %s seconds ---" % (time.time() - start_time))
		return self.graph



def test_DPA():
	dpa = DPATrial(13,30000)
	full_graph = dpa.DPA(13,30000)

	plot_graph = in_degree_distribution(full_graph)
	x = plot_graph.keys()
	y = plot_graph.values()
	plot(x,y,'node number', 'noramlized in-degrees', 'DPA Graph')
	return

	dpa = DPATrial(10,5)
	print len(dpa._node_numbers)
	print dpa.run_trial(10)
	print len(dpa._node_numbers)
	print dpa.run_trial(10)
	print len(dpa._node_numbers)

def test_indegree():
	start_time = time.time()
	citation_graph = load_graph(CITATION_URL)
	print len(citation_graph)
	print("--- Total %s seconds ---" % (time.time() - start_time))
	start_time = time.time()
	plot_graph = in_degree_distribution(citation_graph)
	print("--- Total %s seconds ---" % (time.time() - start_time))

	x = plot_graph.keys()
	y = plot_graph.values() 

	plot(x,y,'node number', 'noramlized in-degrees', 'Citation Graph Question 1 ')
	#plot(logx,logy,'log(node number)', 'log(noramlized in-degrees)', 'Application Question 2 ')
	return

def plot(x,y,xlabel,ylabel,title):
	plt.title(title)
	plt.ylabel("log " + ylabel)
	plt.xlabel("log " + xlabel)
	plt.loglog(x,y,'ro')
	plt.show()

	plt.ylabel(ylabel)
	plt.xlabel(xlabel)
	plt.plot(x,y,'ro')
	plt.show()

def test_ER():
	plot_graph = in_degree_distribution(generate_ER(10000,.005))
	#plot_graph = compute_in_degrees(generate_ER(10,1.0))
	#print generate_ER(10,1.0)
	x = plot_graph.keys()
	y = plot_graph.values()
	plot(x,y,'node number', 'noramlized in-degrees', 'Application Question 2 ')

if __name__ == '__main__':
	test_indegree()
	test_DPA()
	test_ER()
