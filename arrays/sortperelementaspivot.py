def sortAsOneElementAsPivotV1(arr,ele):
	arr.sort()
	return arr
		
def sortAsOneElementAsPivotV2(arr,ele):
	start = 0
	end = len(arr)-2
	
	count = 0
	for x in arr:
		if(x == ele):
			swap(arr,count,end + 1)
		count = count + 1
	
	while(start <= end):
		if(arr[start] < ele):
			start = start + 1
		elif(arr[start] > ele):
			swap(arr,start,end)
			end = end - 1
	swap(arr,start,len(arr)-1)
	return arr
	

def swap(arr,element1Index,element2Index):
	temp = arr[element2Index] #temp = 2
	arr[element2Index] = arr[element1Index] #arr[2]= 2
	arr[element1Index] = temp
	
#https://www.geeksforgeeks.org/find-the-element-before-which-all-the-elements-are-smaller-than-it-and-after-which-all-are-greater-than-it/	
#https://www.geeksforgeeks.org/find-a-partition-point-in-array/
		
		
	