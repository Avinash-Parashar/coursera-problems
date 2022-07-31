# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    arr = [0,0,1,1]
    j=4
    while j<=n:
        if j%3==0 and j%2==0:
            arr.append(min(1+arr[j-1],1+arr[j//2],1+arr[j//3]))
        elif j%3==0:
            arr.append(min(1+arr[j-1],1+arr[j//3]))
        elif j%2==0:
            arr.append(min(1+arr[j-1],1+arr[j//2]))
        else:
            arr.append(1+arr[j-1])
        j+=1

    while n >= 1:
        sequence.append(n)
        if n%3==0 and n%2==0:
            if arr[n//3]<=arr[n//2] and arr[n//3]<=arr[n-1]:
                n=n//3
            elif arr[n//2]<=arr[n//3] and arr[n//2]<=arr[n-1]:
                n=n//2
            else:
                n=n-1

        elif n%3==0:
            if arr[n//3]<=arr[n-1]:
                n=n//3
            else:
                n=n-1
        elif n%2==0:
            if arr[n//2]<=arr[n-1]:
                n=n//2
            else:
                n=n-1
        else:
            n-=1
    
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
