#!/usr/bin/env python3
import timeit
import sys
from functools import reduce

def sum_of_squares_loop(n):
    result = 0
    for i in range(1, n + 1):
        result += i * i
    return result

def sum_of_squares_reduce(n):
    return reduce(lambda res, i: res + i*i, range(1, n + 1))

def benchmark(method, reps, n):
    if method == 'loop':
        time = timeit.timeit(lambda: sum_of_squares_loop(n), number=reps)
    elif method == 'reduce':
        time = timeit.timeit(lambda: sum_of_squares_reduce(n), number=reps)
    else: 
        raise ValueError("Incorrect method. Use 'loop' or 'reduce'")
    return time

if __name__ == "__main__":
    if len(sys.argv) == 4:
        method = sys.argv[1]
        try:
            reps = int(sys.argv[2])
            n = int(sys.argv[3])
        except ValueError:
            print("Error: reps and n must be an integer")    
            sys.exit(1)
        try:
            time = benchmark(method, reps, n)
            print(time)
        except ValueError as e:
            print(e)
            sys.exit(1)
    else:
        print("Error: Incorrect number of args")
        sys.exit(1)