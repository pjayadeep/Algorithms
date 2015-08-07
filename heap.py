import random
class heap:
	def __init__(self,n):
		self.inf = 100000
		self.N = [self.inf]*(n) # 2*i and 2*i + 1
		self.D = [self.inf]*(n) # Dijkstra distane
		self.size = n # size of the heap
		self.nxt = 0 # next slot empty
		self.cmpF = self.cmp

	def insert(self,val):
		self.N[self.nxt] = val
		self.bubbleUp(self.nxt)
		self.nxt += 1
		
	def l(self):
		return self.N[:self.nxt]

	def itemAt(self,slot):
		self.N[slot]

	def left(self,node):
		try:
			return self.N[2*node+1]
		except:
			return self.inf

	def right(self, node):
		try:
			return self.N[2*(node+1)]
		except:
			return self.inf

	def children(self, node):
		return self.right(node), self.left(node)

	def cmp(self, node1, node2):
		return node1 < node2

	def setCmpF(self,cmpF):
		self.cmpF = cmpF

	def bubbleUp(self, node):
		#print "entry", self.N
		pslot = (node-1)/2
		parent = self.N[pslot]
		cur = node
		while self.cmpF( self.N[cur] , self.N[pslot]) and cur != 0:
			self.N[pslot], self.N[cur] = self.N[cur], self.N[pslot]
			cur = pslot
			pslot = (pslot-1)/2
		return cur

	def bubbleDown(self,node=0):
		root = node
		while  self.right(root) != self.inf and self.left(root) != self.inf:
			if self.cmpF(self.N[2*root+1] , self.N[2*(root+1)]):
				minslot = 2*root + 1
			else:
				minslot = 2*(root+1)
			if self.cmpF(self.N[minslot], self.N[root]) :
				self.N[root],self.N[minslot] = self.N[minslot],self.N[root]
			else:
				break
			root = minslot
		return root
		#print minslot,root, self.l()

	def extractMin(self):
		top = self.N[0]
		self.N[0] = self.N[self.nxt-1]
		self.nxt -= 1
		self.bubbleDown()
		self.N[self.nxt] = self.inf
		return top

	def empty(self):
		if self.nxt == 0:
			return True
		else:
			return False

	def heapify(self,values ):
		for val in values:
			self.insert(val)

	def delete(self,node):
		self.N[node], self.N[self.nxt-1] = self.N[self.nxt-1], self.N[node] 
		self.nxt -= 1
		self.N[self.nxt] = self.inf
		if self.bubbleUp(node) == node:
			self.bubbleDown(node)

	def updateVal(self,node,val):
		self.N[node] = val
		self.N[node], self.N[self.nxt-1] = self.N[self.nxt-1], self.N[node] 
		if self.bubbleUp(node) == node:
			self.bubbleDown(node)

	def find(self,val):
		try:
			return self.N.index(val)
		except:
			return -1

	def parent(self,node): # i/2 for even, floor(i/2) for odd
		return self.N[(node-1)/2]


def heapTest():
	x = [10, 4, 2, 9, 5, 8, 1, 7, 3, 6]
	for i in range(1,100):
		random.shuffle(x)
		h = heap(10)
		for i in x:
			h.insert(i)
		assert h.left(10) == 100000 
		assert h.right(10) == 100000
		assert h.children(10) == (100000,100000)

		r = []
		for i in range(1,len(x)+1):
			r.append( h.extractMin())
		assert(r == sorted(x))

	x = range(1,100)
	hh = heap(len(x))
	random.shuffle(x)
	hh.heapify(x)
	r = []
	for i in range(1,len(x)+1):
		r.append( hh.extractMin())
	assert(r == sorted(x)) 


	x = [8,9,10]
	x = [5, 6, 2, 8, 3, 4, 10, 7, 9, 1]
	h = heap(10)
	h.heapify(x)

	r = []
	for i in range(1,len(x)+1):
		r.append( h.extractMin())
	assert(r == sorted(x))
	print "OK"


def heapUTest():
	x = [5, 6, 2, 8, 3, 4, 15, 7, 9, 1]
	h = heap(10)

	for i in range(0,10):
		for val in [100]:
			h.heapify(x)
			h.updateVal(i,val)
			#print h.l()
			r = []
			for i in range(1,len(x)+1):
				r.append( h.extractMin())
			assert r[9] == val
	print 'OK'

def heapIndexTest():
	x = [5, 6, 2, 8, 3, 4, 10, 7, 9, 1]
	h = heap(10)
	h.heapify(x)
	for val in range(1,11):
		assert h.find(val) == h.l().index(val)
	assert h.find(100) == -1
	print 'OK'

def delTest():
	x = [5, 6, 2, 8, 3, 4, 10, 7, 9, 1]
	h = heap(10)
	h.heapify(x)
	h.delete(0)
	assert h.find(0) == -1
	print 'OK'

def strTest():
	x = ['xdas', 'adasdsa', 'bfefs']
	h = heap(10)
	h.heapify(x)
	r = []
	while not h.empty():
		r.append( h.extractMin())
	assert r == sorted(x)
	print 'OK'

if __name__ == '__main__':

	heapTest()
	heapUTest()
	heapIndexTest()
	delTest()
	strTest()
