# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')
def intersection(segment1,segment2):
    if segment1.start <segment2.start:
        if segment1.end <segment2.start:
            return False,[segment1,segment2]
        else:
            if segment1.end <= segment2.end:
                return True,[Segment(segment2.start,segment1.end)]
            else:
                return True,[Segment(segment2.start,segment2.end)]
    else:
        if segment1.start > segment2.end:
            return False,[segment1,segment2]
        else:
            if segment2.end <= segment1.end:
                return True,[Segment(segment1.start,segment2.end)]
            else:
                return True,[Segment(segment1.start,segment1.end)]


def optimal_points(segments):
    points = []
    segment_arr = []
    #write your code here
    segments = sorted(segments, key=lambda x: x.end)
    for segment in segments:
        if len(segment_arr) == 0:
            segment_arr.append(segment)
        else:
            i = 0
            while i<len(segment_arr):
                if intersection(segment,segment_arr[i])[0]:
                    segment_arr[i] = intersection(segment,segment_arr[i])[1][0]
                    break
                else:
                    i+=1
            if i==len(segment_arr):
                segment_arr.append(segment)
    for segment in segment_arr:
        points.append(segment.end)

    
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
