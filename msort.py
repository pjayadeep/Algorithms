# Merge Sort - 7th July 2015:
#
# Poor programming skills indeed - could not lay out a simple loop for the 
# merge - had to look elsewhere for ideas :( Can't claim myself to be a
# programmer :(:( But interesting thing to do anyway with the collaboation of 
#internet. But after 25 years in the game, looks like my sell by date is over
# for sure!
#

def msort(arr):

	inv = 0
	size = len(arr)
	if size == 1:
		return arr,0

	toparr,tinv = msort(arr[:size//2])
	bottarr,binv = msort(arr[size//2:])
	inv = tinv+binv
	sortArray,minv = merge(toparr,bottarr)
	inv += minv
	return sortArray,inv

def merge(top,bot):
	merged = []
	inv = 0
	tidx = bidx = 0

	while tidx < len(top) and bidx < len(bot) :
		if top[tidx] < bot[bidx] :
			merged.append(top[tidx])
			tidx += 1
		else:
			merged.append(bot[bidx])
			inv += len(top) - tidx
			bidx += 1

	# append the rest
	merged += top[tidx:]
	merged += bot[bidx:]

	return merged,inv

if __name__ == '__main__':

	arr1 = [3,1,11, 14, 5, 34,6]
	arr2 = [3,1,11, 14, 5, 34]
	arr3 = [4,11,3,1]

	print merge([4,5],[11,23,35])
	print merge([4,5,15],[11,12,13])
	print merge([415],[35])
	print msort(arr1)
	print msort(arr2)
	print msort(arr3)

	x,inv = msort([ 4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54 ])
	assert inv==2372
	x,inv = msort( [ 37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45 ])
	assert (inv == 590)

	lines = [ int(x.strip())  for x in open("_IntegerArray.txt", 'rU').readlines()]

	srtd ,inv =  msort(lines)
	print 'inversions=', inv
	assert( inv == 2407905288)

	#pmsort = lines.sort()

	#fd = open('output.txt','w')
	#for lst in srtd:
	#	fd.write(str(lst) + "\n")
	#fd.close()
