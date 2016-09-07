class sched :
	def __init__(self,file):
		self.file = file

	def read_jobs(self):
		with  open(self.file) as fd:
			next(f)
			for line in fd:
				yield [int(num) for num in line.strip().split(' ')]

	def sched(self,sched_func):
		sched_list = [ (sched_func(weight,length),weight,length)
				for weight,length in self.read_jobs()]
		sched_list = sorted(sched_list,reverse=True)

		runtime = wt_time = 0;
		for diff,weight,length in sched_list:
			runtime += length
			wt_time += runtime*weight

		return wt_time
				
if __name__ == '__main__':
	s = sched('jobs.txt')
	print s.sched(lambda x,y: x-y)
	print s.sched(lambda x,y: x*1.0/y)
