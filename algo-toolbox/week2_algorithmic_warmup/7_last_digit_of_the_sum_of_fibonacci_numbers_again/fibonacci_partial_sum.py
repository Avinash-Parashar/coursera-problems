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

# getting sum with help of last function
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

def fibonacci_partial_sum_naive(from_, to):
    if from_==0:
        if to==0:
            return 0
        else:
            return fibonacci_sum_naive(to)
    else:
        pre_sum = fibonacci_sum_naive(from_-1)
        _sum = fibonacci_sum_naive(to)
        if _sum>=pre_sum:
            return (_sum - pre_sum)%10
        else:
            return 10 - ((pre_sum-_sum)%10)



if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
