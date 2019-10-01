# class for a quick_sort_ sort
class Quicksort:
    # constructer for initialization
	def __init__(self,arr):
		self.arr=arr
    
    # Function for patition the arr 
	def partition(self,l,h):
		x= self.arr[h]
		i=l-1
		for j in range(l,h):
			if self.arr[j] <= x:
				i+=1
				self.arr[i],self.arr[j] = self.arr[j],self.arr[i]
		self.arr[i+1],self.arr[h] = self.arr[h], self.arr[i+1]
		# print(i+1,"After",self.arr)
		return i+1

	# quick_sort_ sort function for a recursive call
	def quick_sort_(self,l,h):
		if l<h:
		    pi = obj.partition(l,h)
		    
		    obj.quick_sort_(l,pi-1)
		    obj.quick_sort_(pi+1,h)

		return self.arr

# Driver code
arr=[2,8,7,1,3,5,6,4]

# Create a object for a class
obj= Quicksort(arr)
print(obj.quick_sort_(0,7))