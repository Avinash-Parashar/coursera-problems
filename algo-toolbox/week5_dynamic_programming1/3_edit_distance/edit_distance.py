# Uses python3
def edit_distance(s, t):
    #write your code here
    arr = []
    for i in range(len(t)+1):
        temp = [0]*(len(s)+1)
        arr.append(temp)
    #filling last rows and columns
    temp=0
    for i in range(len(s),-1,-1):
        arr[len(t)][i]=temp
        temp+=1
    temp=0
    for i in range(len(t),-1,-1):
        arr[i][len(s)] = temp
        temp+=1
    
    #filling top parts
    for i in range(len(t)-1,-1,-1):
        for j in range(len(s)-1,-1,-1):
            if s[j]==t[i]:
                arr[i][j] = arr[i+1][j+1]
            else:
                arr[i][j] = 1+min(arr[i+1][j+1],arr[i+1][j],arr[i][j+1])

    


    return arr[0][0]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
    
