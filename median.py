import heap
# Create 2 heaps, one min one, the other max one. Split the incoming 
# numbers equally into these heaps and pick either the min or max one
# as the median:

class median:

	def __init__(self,file):
		self.minHeap = heap.heap(10005)
		self.minHeap.setCmpF(lambda n1, n2:  n2 < n1)
		self.maxHeap = heap.heap(10000) 
		self.fd = open(file, "rU")
		self.medians = []

	def placeNo(self,no):

#		if self.minHeap.top() == float('inf') :
#			self.minHeap.insert(no)
#			print 'fxcx' , self.minHeap.top(), self.maxHeap.top(), no
#			return
#		if self.maxHeap.top() == float('inf') :
#			self.maxHeap.insert(no)
#			print 'fxcx' , self.minHeap.top(), self.maxHeap.top(), no
#			return
#			
		
		if no < self.minHeap.top():
			self.minHeap.insert(no)
		if no > self.maxHeap.top():
			self.maxHeap.insert(no)
		if no < self.maxHeap.top() and no >self.minHeap.top():
			self.minHeap.insert(no)

	def rebalance(self):

		if len(self.minHeap) - len(self.maxHeap)  > 1:
			self.maxHeap.insert(self.minHeap.extractMin())
		if len(self.maxHeap) - len(self.minHeap) > 1:
			self.minHeap.insert(self.maxHeap.extractMin())
		#print self.maxHeap.len(), self.minHeap.len()
		#assert len(self.maxHeap) == len(self.minHeap)

	def calcMedian(self):

		for line in self.fd:
			no = int(line)
			self.placeNo(no)
			self.rebalance()

			if self.maxHeap.top() == float('inf'):
				self.medians.append(self.minHeap.top())
				print 'ffffff', self.minHeap.top(), self.maxHeap.top()
				continue
			if self.minHeap.top() == float('inf'):
				self.medians.append(self.maxHeap.top())
				print 'sssssc', self.minHeap.top(), self.maxHeap.top()
				continue

			#print 'calc', self.minHeap.top(), self.maxHeap.top()
			if len(self.maxHeap) > len(self.minHeap):
				self.medians.append(self.maxHeap.top())
			else:
				self.medians.append(self.minHeap.top())
		return self.medians

if __name__ == '__main__':
	#med = median('Median.txt')
	med = median('_Median.txt')
	#med = median('med1.txt')
	tot=0
	print sum(med.calcMedian()) % 10000
	
