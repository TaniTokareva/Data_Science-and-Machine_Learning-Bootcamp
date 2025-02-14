#!/usr/bin/env python3
import timeit
import random
from collections import Counter

random_values = [random.randint(0, 100) for _ in range (1000000)]

def count_freq_manual(values):
    freq_dict = {}
    for num in values:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    return freq_dict


def count_freq_counter(values):
    return Counter(values)

def top_10_manual(values):
    freq_dict = count_freq_manual(values)
    return sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)[:10]

def top_10_counter(values):
    return Counter(values).most_common(10)

def benchmark():
    my_count_time = timeit.timeit(lambda: count_freq_manual(random_values), number =1 )
    print(f"my function: {my_count_time: .7f}")

    counter_count_time = timeit.timeit(lambda: count_freq_counter(random_values), number=1)
    print(f"Counter: {counter_count_time: .7f}")

    my_top_time = timeit.timeit(lambda: top_10_manual(random_values), number=1)
    print(f"my top: {my_top_time: .7f}")

    counter_top_time = timeit.timeit(lambda: top_10_counter(random_values), number=1)
    print(f"Counter's top: {counter_top_time: .7f}")

if __name__ == "__main__":
    benchmark()