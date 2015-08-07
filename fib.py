import time
def fib1(n):
	if n == 0:
		return 0
	if n == 1:
		return 1 
	return(fib1(n-1) + fib1(n-2))


def fib2(n):
	fib = {}
	fib[0] = 0
	fib[1] = 1

	for i in range(2,n+1):
		fib[i] = fib[i-1] + fib[i-2]
	return fib[n]

if __name__ == '__main__':
	start_time = time.time()
	print fib2(30)
	print("--- %s seconds ---" % (time.time() - start_time))
	start_time = time.time()
	print fib1(30)
	print("--- %s seconds ---" % (time.time() - start_time))
