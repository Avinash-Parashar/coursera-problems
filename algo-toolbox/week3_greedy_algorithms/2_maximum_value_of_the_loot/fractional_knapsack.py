# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    perWeight = {}
    for i in range(len(weights)):
        if values[i]/weights[i] in perWeight:
            perWeight[values[i]/weights[i]] += weights[i]
        else:
            perWeight[values[i]/weights[i]] = weights[i]
    keys = [key for key in perWeight.keys()]
    keys.sort(reverse = True)
    for key in keys:
        if capacity==0:
            return value
        else:
            tempWeight = perWeight[key]
            if tempWeight<= capacity:
                value += tempWeight*key
                capacity -= tempWeight
            else:
                value += capacity*key 
                capacity = 0
    
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values =data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
