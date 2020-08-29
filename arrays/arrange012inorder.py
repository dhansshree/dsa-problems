def sort012inorderV1(arr):
	arr.sort()
	return arr
		
def sort012inorderV2(arr):
	count0 = 0
	count1 = 0
	count2 = 0
	index = 0
	for x in arr:
		if(x == 0):
			count0 = count0 + 1
		if(x == 1):
			count1 = count1 + 1
		if(x == 2):
			count2 = count2 + 1
	
	while(index < len(arr) - 1):
		
		while(count0 > 0):
			arr[index] = 0
			count0 = count0 - 1
			index = index + 1
		
		while(count1 > 0):
			arr[index] = 1
			count1 = count1 - 1
			index = index + 1
		
		while(count2 > 0):
			arr[index] = 2
			count2 = count2 - 1
			index = index + 1
		
	return arr
	

def sort012inorderV3(arr):
	low = 0
	mid = 0
	high = len(arr) - 1
	
	
	
	while(mid <= high):
		
		if(arr[mid] == 1):
			mid = mid + 1
		elif(arr[mid] == 0):
			swap(arr,mid,low)
			mid = mid + 1
			low = low + 1
		elif(arr[mid] == 2):
			swap(arr,high,mid)
			high = high - 1
			
		
	return arr
	


def swap(arr,element1Index,element2Index):
	temp = arr[element2Index] #temp = 2
	arr[element2Index] = arr[element1Index] #arr[2]= 2
	arr[element1Index] = temp
	
#https://www.geeksforgeeks.org/find-the-element-before-which-all-the-elements-are-smaller-than-it-and-after-which-all-are-greater-than-it/	
#https://www.geeksforgeeks.org/find-a-partition-point-in-array/
		
		
	