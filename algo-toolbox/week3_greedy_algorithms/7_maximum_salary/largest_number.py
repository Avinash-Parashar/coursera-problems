#Uses python3

import sys
def isBetter(a,b):
    if int(a+b) >= int(b+a):
        return True
    else:
        return False
def largest_number(a):
    #write your code here
    res = ""
    while len(a)>0:
        max_num=a[0]
        for char in a:
            if isBetter(char,max_num):
                max_num = char
        res+=max_num
        a.remove(max_num)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a =data[1:]
    print(largest_number(a))
    
