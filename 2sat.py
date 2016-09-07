from sccObj import Graph
from collections import defaultdict
from timeit import default_timer as timer
from math import log
import random
class sat2:
	def __init__(self,file):
		self.file = file
	def readF(self):
		self.var = {}
		with open(self.file) as fd:
			self.n= int(fd.readline())
			print self.n
			self.sats = [ tuple( int(x) for x in line.split()) 
					for line in fd]
			#self.setGraph()
			print self.setSccGraph()
		return self.sats

	def setGraph(self):
		for x,y in self.sats:	
			self.var[x] = random.choice([True,False])
			self.var[y] = random.choice([True,False])

	def setSccGraph(self):
		G = Graph()
		assert len(self.sats) == self.n
		for u,v in self.sats:
			G.addE(-v,u)
			G.addE(-u,v)
		start = timer()
		for scc in G.sccLenR():
			if len(scc) > 1:
				for i in scc:
					if -i in scc:
						print i, scc
						return False
		end=timer()
		#print '\t2sat scc time:',  end-start
		return True

	def eval(self):
		result = True

		for x,y in self.sats:
			if -x in self.var and x < 0:
				self.var[x] = not self.var[-x]
			if -y in self.var and y < 0:
				self.var[y] = not self.var[-y]

			boolean = self.var[x] or self.var[y]
			result = result and boolean
			if not result :
				return result,(x,y)
		return result,(x,y)

	def papedeuo(self):
		n = self.n
		for i in range(int(log(n))):
			start = timer()
			#m = 2*n*n
			m = 2*n
			while  m > 0:
				result, (x,y) = self.eval()
				if result :
					return True
				else:
					flipvar = random.choice((x,y))
					self.var[flipvar] =  not self.var[flipvar]
				m -= 1
			end=timer()
			print '\t2sat loop time:',i, end-start
		return False				

	def scc(self):
		pass


if __name__ == '__main__':
	files2 = ['2sat1.txt', '2sat2.txt', '2sat3.txt', '2sat4.txt', '2sat5.txt', '2sat6.txt']
	files1 = ['2sat-3.txt', '2sat-1.txt', '2sat-2.txt']

	for f in files1 + files2 :
		print f,
		start = timer()
		s = sat2(f)
		s.readF()
		#print s.papedeuo()
		end=timer()
		print '2sat eval time:', f,  end-start
		print

	#t.removeLinear()

