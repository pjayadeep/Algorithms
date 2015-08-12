import heap
# Create 2 heaps, one min one, the other max one. Split the incoming 
# numbers equally into these heaps and pick either the min or max one
# as the median:

def maxCmp(n1,n2):
	return n2 < n1

class median:

	def __init__(self,file):
		self.minHeap = heap.heap(10005)
		self.minHeap.setCmpF(lambda n1, n2:  n2 < n1)
		self.maxHeap = heap.heap(10000) 
		self.fd = open(file, "rU")
		self.medians = []

	def placeNo(self,no):
		if no < self.minHeap.top():
			self.minHeap.insert(no)
		if no > self.maxHeap.top():
			self.maxHeap.insert(no)
		if no < self.maxHeap.top() and no >self.minHeap.top():
			self.minHeap.insert(no)

	def rebalance(self):
		if self.minHeap.len() - self.maxHeap.len()  > 1:
			self.maxHeap.insert(self.minHeap.extractMin())
		if self.maxHeap.len() - self.minHeap.len() > 1:
			self.minHeap.insert(self.maxHeap.extractMin())
		#print self.maxHeap.len(), self.minHeap.len()

	def calcMedian(self):
		for line in self.fd:
			no = int(line)
			self.placeNo(no)
			self.rebalance()

			if self.maxHeap.len() ==  self.minHeap.len():
				self.medians.append(self.minHeap.top())
			elif self.maxHeap.len() > self.minHeap.len():
				self.medians.append(self.maxHeap.top())
			else:
				self.medians.append(self.minHeap.top())
		return self.medians

if __name__ == '__main__':
	med = median('med1.txt')
	med = median('Median.txt')
	print sum(med.calcMedian())%10000
	#sum(self.medians), sum(self.medians) % 10000
