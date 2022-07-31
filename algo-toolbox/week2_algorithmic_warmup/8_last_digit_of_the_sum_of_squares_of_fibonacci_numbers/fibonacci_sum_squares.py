# Uses python3
from sys import stdin

# finding pisano period for 10 so that we can find remainder of numbers with 10
def pisanoSquared(m):
    array = [0,1]
    for i in range(2,(m**4)):
        array.append(array[i-1]+array[i-2])
        if (array[i]**2)%m == 1:
            if (array[i-1]**2)%m == 0:
                return i-1

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n
    pisanoOf10 = pisanoSquared(10)
    array = [0,1]
    array_sum = [0,1]
    _sum = 1

    for i in range(2,pisanoOf10):
        array.append(array[i-1]+array[i-2])
        _sum += (array[i]**2)
        array_sum.append(_sum)
    times = n//pisanoOf10
    rem = n%pisanoOf10
    return (times*array_sum[-1] + array_sum[rem])%10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
    
