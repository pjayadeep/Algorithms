G1 = {1:[2], 2:[3,4], 3:[5], 5:[6] }
G2 = {1:[]}
def depth(adjList,g):
	depth = {}
	depth[g] = maxDepth = 1
	stack = [g] # stack the nodes to do a depth first search

	while stack:
		parent = stack.pop()
		if parent in adjList:
			for child in adjList[parent]:
				stack.append(child)
				# increment the height of each node by 1
				depth[child] = depth[parent]+1
				#pick the max among the children
				maxDepth = max(depth[child], maxDepth)
	return maxDepth

if __name__ == '__main__' :
	assert depth(G1,1) == 5
	assert depth(G2,1) == 1
