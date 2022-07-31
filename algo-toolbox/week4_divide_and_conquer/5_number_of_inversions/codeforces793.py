test_case=int(input())
for i in range(test_case):
    n,x,y=[int(m) for m in input().split()]
    su_m=(n*(n+1))//2
    k=su_m/(x+y)
    if k==int(k):
        ka=int(k*x)
        count=0
        arr=[]
        for j in range(1,n+1):
            count+=j
            arr.append(j)
            if count==ka:
                break
            if count>ka:
                arr.pop(count-ka-1)
                break
        
                
        print(f'''Case #{i+1}: POSSIBLE''')
        print(len(arr))
        for j in arr:
            print(j,end=" ")
        print()
    else:
        print(f'''Case #{i+1}: IMPOSSIBLE''')
