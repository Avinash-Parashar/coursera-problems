# Uses python3
import sys

def optimal_summands(n):
    summands = []
    index = None
    while n>0:
        if len(summands)==0:
            summands.append(1)
            index = 0
            n = n-1
        if n<=summands[index]:
            summands[index]+=n
            n=0
        else:
            num = summands[index]+1
            summands.append(num)
            n = n-num
            index +=1


    #write your code here
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
