# Implement Binary Search
# function defination

def BinarySearch(arr,low,high,target):
    # condition checking
    if high > low:
        mid= (high + low)//2
        # if the target is mid element returning the mid element
        if arr[mid]==target:
            return mid
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid]>target:
            return BinarySearch(arr,low,mid-1,target)
        else:
            arr[mid]<target
            return BinarySearch(arr,mid+1,high,target)
    else:
        return -1
# array declearation
arr = [1,2,3,4,5,6,7]
# taking input from the user
target = int(input())
# function calling
result = BinarySearch(arr,0,len(arr)-1,target)
if result != -1:
    print("element is present at the index ",str(result))
else:
    print("the result is not found ")
        

