# Uses python3
import sys

def get_majority_element(a, left, right):
    dic={}
    for i in range(left,right):
        if a[i] in dic:
            dic[a[i]]+=1
        else:
            dic[a[i]]=1
    max_count = 0
    for key in dic.keys():
        max_count = max(max_count,dic[key])
    if max_count >n/2:
        return max_count
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
