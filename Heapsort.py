class HeapSort:

	def __init__(self,arr):
		self.arr = arr

	
	def heapify(self,n , i):
		large = i 
		l = 2*i + 1
		r = 2*i + 2

		if l<n and self.arr[i] < self.arr[l]:
			large = l 

		if r < n and self.arr[large] < self.arr[r]:
			large = r 

		if large!=i:
			self.arr[i],self.arr[large] = self.arr[large],self.arr[i]

			self.heapify(n, large)


	def heap_sort(self):
		n=len(self.arr)

		for i in range(n, -1, -1):
			self.heapify(n, i)

		for i in range(n-1, 0, -1):
			self.arr[i], self.arr[0] =self.arr[0], self.arr[i]
			self.heapify(i, 0)


# Main function
def main():
	arr=[10,30,80,30,5,55,90,100]
	obj = HeapSort(arr)
	obj.heap_sort()
	print(arr)

if __name__=="__main__":
	main()
