class InsertionSort(object):
	"""docstring for InsertionSort"""
	def __init__(self, arg):
		super(InsertionSort, self).__init__()
		self.arr = arg
		
	def insertion_sort(self):

		
		for j in range(1,len(self.arr)):
			x = self.arr[j]
			i=j-1
			while i>=0 and x < self.arr[i]:
				self.arr[i+1] = self.arr[i]
				i-=1

			self.arr[i+1] = x
		
		return self.arr

if __name__== "__main__":

	arr=[1,4,5,6,2,5,7,3,6]

	obj = InsertionSort(arr)
	print(obj.insertion_sort())