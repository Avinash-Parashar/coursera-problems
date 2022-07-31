ext_ans=[]
def targetSum(target,arr,ans):

    if target==0:
        ext_ans.append(ans)
        return
    if target<0 or len(arr)==0:
        return
    targetSum(target-arr[0],arr[1:],ans+[arr[0]])
    targetSum(target,arr[1:],ans)
arr=[x for x in range(1,4)]
targetSum(3,arr,[])
print(ext_ans)