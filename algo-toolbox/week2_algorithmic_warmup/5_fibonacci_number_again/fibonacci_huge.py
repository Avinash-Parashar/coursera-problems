# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    array = [0,1]
    for i in range(2,n+1):
        array.append(array[i-1]+array[i-2])
        if array[i]%m == 1:
            if array[i-1]%m==0:
                return array[n%(i-1)] %m
    return array[n]%m


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m =map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
