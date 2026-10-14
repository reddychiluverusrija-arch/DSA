def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=[10,50,20,30]
target=20
result=linear_search(arr,target)
print("Element found at index:",result)