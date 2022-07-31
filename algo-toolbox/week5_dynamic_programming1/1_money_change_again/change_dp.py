# Uses python3
import sys

def get_change(m):
    arr = [0,1,2,1,1]
    if m<=4:
        return arr[m]
    else:
        for i in range(5,m+1):
            arr.append(min(1+arr[i-1],1+arr[i-3],1+arr[i-4]))
        return arr[-1]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
