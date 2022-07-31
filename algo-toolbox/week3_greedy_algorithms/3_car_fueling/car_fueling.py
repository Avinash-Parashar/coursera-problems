# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    count = 0
    stops.append(distance)
    current_position = 0
    next_position = 0
    while current_position<distance:
        #finding next position index
        

        while next_position<len(stops) and stops[next_position] - current_position<= tank:
            next_position +=1
        if stops[next_position-1] == current_position:
            return -1
        if next_position != len(stops):
            count+=1
            current_position = stops[next_position-1]
        else:
            return count
        
        

    return count

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d,m,stops))
