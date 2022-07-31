def countWays(A, B, C):
    # Write your code here.
    count=0
    if len(C)==0:
        count = count+1
        return count
    elif len(A)==0 and len(B)<len(C):
        return 0
   	##elif len(B)==0 and len(A)<len(C):
    ##   return 0
    elif len(B)==0 and len(A)<len(C):
        return 0
    elif len(A)==0:
        if B[0]==C[0]:
            return countWays(A,B[1:],C[1:])+countWays(A,B[1:],C)
        else:
            return countWays(A,B[1:],C)
    elif len(B)==0:
        if A[0]==C[0]:
            return countWays(A[1:],B,C[1:])+countWays(A[1:],B,C)
        else:
            return countWays(A[1:],B,C)
    else:
        if A[0]!=C[0] and B[0]!=C[0]:
            temp = countWays(A[1:],B[1:],C)
            if temp>0:
                return countWays(A[1:],B,C)+countWays(A,B[1:],C)+temp-1
            else:
                return countWays(A[1:],B,C)+countWays(A,B[1:],C)+temp
        elif A[0]==C[0] and B[0]!=C[0]:
            return countWays(A[1:],B,C[1:])+countWays(A[1:],B,C)
        elif A[0]!=C[0] and B[0]==C[0]:
            return countWays(A,B[1:],C[1:])+countWays(A,B[1:],C)
        temp1=countWays(A[1:],B[1:],C)
        temp2 = countWays(A[1:],B[1:],C[1:])
        if temp1*temp2!=0:
            return countWays(A[1:],B,C[1:])+countWays(A,B[1:],C[1:])+temp1+temp2-2
        else:
            if temp1+temp2>0:

                return countWays(A[1:],B,C[1:])+countWays(A,B[1:],C[1:])+temp1+temp2-1
            else:
                return countWays(A[1:],B,C[1:])+countWays(A,B[1:],C[1:])+temp1+temp2
print(countWays("abcd","bcda","ac"))