# Uses python3
def calc_fib(n):
    if n==0:
        return 0
    array = [0 for i in range(n+1)]
    array[0]  = 0
    array[1] = 1
    for i in range(2,n+1):
        array[i] = array[i-1] + array[i-2]
    return array[n]


n = int(input())
print(calc_fib(n))
