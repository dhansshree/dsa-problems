def findThirdMaxInArrayV2(arr):
	firstmax = 0
	secondmax = 0
	thirdmax = 0
	for x in arr:
		if(x > firstmax):
		  thirdmax = secondmax
		  secondmax = firstmax
		  firstmax = x
		elif(x > secondmax):
			thirdmax = secondmax
			secondmax = x
		elif(x > thirdmax):
			thirdmax  = x

	if(firstmax == secondmax or secondmax == thirdmax):
		return "No 3rd Largest Element"
	else:
		return thirdmax
		

def findThirdMaxInArrayV1(arr):
	arr.sort(reverse = True)
	
	length = len(arr) 
	i = 1
	count = 1
	
	# Iterating using while loop 
	while i < length:
		if(arr[i] != arr[i-1]):
			count = count+1
		if(count == 3):
			return(arr[i])
		i += 1
	
	return "No 3rd Largest Element"
		
		
	