# Uses python3
import sys
# finding pisano period for 10 so that we can find remainder of numbers with 10
def pisano(m):
    array = [0,1]
    for i in range(2,m*m):
        array.append(array[i-1]+array[i-2])
        if array[i]%m == 1:
            if array[i-1]%m == 0:
                return i-1


def fibonacci_sum_naive(n):
    
    if n <= 1:
        return n
    pisanoOf10 = pisano(10)
    array = [0,1]

    for i in range(2,pisanoOf10):
        array.append(array[i-1]+array[i-2])
    times = n//pisanoOf10
    rem = n%pisanoOf10
    return (times*sum(array) + sum(array[:rem+1]))%10


if __name__ == '__main__':
    input = sys.stdin.read()
    n =int(input)
    print(fibonacci_sum_naive(n))
