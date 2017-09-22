import random

def main():
	A = [3,4,2,6,1,5,8,7,9]
	quick_sort(A,0,len(A)-1)
	print A

def quick_sort(A,r,q):
	if r<q:
		index = partition(A,r,q)
		if r<index-1:
			quick_sort(A,r,index-1)
		if index+1<q:
			quick_sort(A,index+1,q)
	

def partition(A,r,q):
	x = A[q]
	i=r-1
	for j in range(r,q):
		if A[j]<=x:
			i+=1
			swap = A[i]
			A[i] = A[j]
			A[j] = swap
	swap = A[i+1]
	A[i+1] = A[q]
	A[q] = swap
	return i+1
		
	
	
	
	
if __name__ == "__main__":
	main()