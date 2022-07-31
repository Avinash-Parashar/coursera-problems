def search(arr,query):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==query:
            return mid
        elif arr[mid]<query:
            start=mid+1
        else:
            end=mid-1
    return start-1
print(search([1,2,3,4,6,7],10))
