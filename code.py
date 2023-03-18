for _ in range(int(input())):
	n = int(input())
	s = input()
	if "I" in s:
		print("INDIAN")
	elif "Y" in s and "N" in s:
		print("NOT INDIAN")
	else:
		print("NOT SURE")




# def minimumSubarrays(ar, n) :
#     se = []
 
#     cnt = 1;
 
#     for i in range(n) :
         
#         # Checking if an element already exist in
#         # the current sub-array
#         if se.count(ar[i]) == 0 :
             
#             # inserting the current element
#             se.append(ar[i])
#         else :
#             cnt += 1
             
#             # clear set for new possible value
#             # of subarrays
#             se.clear()
             
#             # inserting the current element
#             se.append(ar[i])
#     print(cnt)
#     return cnt
 
# # Driver Code
# print("Enter array")
# ar = [ 3,1,2,1 ]
# n = len(ar)
# print(minimumSubarrays(ar, n))


















# # i = 1
# # j = 2
# # lit = 4

# # for i 
# testString = 'Neptuneworld'
# revString = []
# for i in range(len(testString)-1,-1,-1):
# 	revString.append(testString[i])

# print(''.join(revString))

# # def reverse(testString):
# # 	if len(testString) == 0:
# # 		return testString
# # 	else:
# # 		return reverse(testString[1:]) + testString[0]
# # print(reverse("NeptuneWorld"))