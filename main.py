from arrays.find3dmaxofanarray import *
from arrays.sortperelementaspivot import *

#arr = [70,100,60,60,70]
#print(findThirdMaxInArrayV1(arr))
#print(findThirdMaxInArrayV2(arr))

#arr = [2,3,1,9] #2,9,1,3 2,1,9,3
#ele = 3

arr = [2,3,1,4,8,5,9,7,10,6,11]
ele = 8
for x in sortAsOneElementAsPivotV2(arr,ele):
	print(x)

