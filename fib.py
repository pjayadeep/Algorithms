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

def fib3(n):
	x,y = 0,1
	for num in range(n):
		x,y = y,x+y
	return x

if __name__ == '__main__':
	val = 100

	start_time = time.time()
	print val , '! =',  fib3(val)
	print("--- %s seconds ---" % (time.time() - start_time))
	start_time = time.time()
	print val , '! =',  fib2(val)
	print("--- %s seconds ---" % (time.time() - start_time))
	start_time = time.time()
	print val , '! =',  fib1(val)
	print("--- %s seconds ---" % (time.time() - start_time))
