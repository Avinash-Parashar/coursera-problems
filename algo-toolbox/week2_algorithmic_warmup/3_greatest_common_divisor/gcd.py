# Uses python3
import sys

def gcd_naive(a, b):
    if a<b:
        a,b = b,a
    def rec(a,b):
        if b==0:
            return a
        return rec(b, a%b)
    return rec(a, b)
    

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
